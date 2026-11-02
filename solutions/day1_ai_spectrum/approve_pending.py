"""
Human-approval step (Day 1 take-home, stretch option 3)
=======================================================
Lists refunds that Level 5 queued as "pending_human_approval" and lets a PERSON approve or
reject each one. Every decision is appended to the same audit log, so the trail shows
agent request -> human decision.

Safety: before an approval is recorded the policy is re-checked in code (evaluate), so a
stale or tampered queue entry cannot be approved for the wrong amount or order.

Run (after level5_agentic_ai.py has written outputs/level5_audit.jsonl):
    python solutions/day1_ai_spectrum/approve_pending.py                     # interactive
    python solutions/day1_ai_spectrum/approve_pending.py --list              # just list
    python solutions/day1_ai_spectrum/approve_pending.py --decide T-03=approve --decide T-08=reject --approver "A. Lead"
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # run from any folder

from common import config  # noqa: E402
from solutions.day1_ai_spectrum import dispute_tools as dt  # noqa: E402

DECIDED = {"human_approved", "human_rejected"}


def read_audit(path: Path) -> list[dict]:
    if not path.exists():
        raise SystemExit(f"No audit log at {path}. Run level5_agentic_ai.py first.")
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def pending_items(records: list[dict]) -> list[dict]:
    """Queued refunds that do not yet have a human decision."""
    decided = {r["ticket_id"] for r in records if r["action"] in DECIDED}
    return [r for r in records if r["action"] == "refund_pending_human_approval" and r["ticket_id"] not in decided]


def decide(item: dict, choice: str, approver: str, note: str = "") -> dict:
    """Build the audit record for one human decision. Approvals are re-checked against the policy code."""
    desk = dt.DisputeDesk(write_logs=False)
    ticket, order = desk.tickets.get(item["ticket_id"]), desk.orders.get(item["order_id"])
    action = "human_rejected"
    if choice == "approve":
        verdict = dt.evaluate(ticket["customer_email"], order) if ticket and order else {"decision": "missing"}
        if verdict["decision"] == "refund" and order and abs(order["amount"] - float(item["amount"])) < 0.005:
            action = "human_approved"
        else:
            note = f"approval refused by policy re-check ({verdict.get('reason_code', verdict['decision'])}). {note}"
    return {"time": datetime.now(timezone.utc).isoformat(timespec="seconds"), "action": action,
            "ticket_id": item["ticket_id"], "order_id": item["order_id"], "amount": item["amount"],
            "approver": approver, "note": note.strip()}


def main() -> None:
    parser = argparse.ArgumentParser(description="Approve or reject refunds waiting for a human")
    parser.add_argument("--audit", default=str(config.output_dir() / "level5_audit.jsonl"))
    parser.add_argument("--list", action="store_true", help="only list pending items")
    parser.add_argument("--decide", action="append", default=[], help="TICKET=approve|reject (repeatable)")
    parser.add_argument("--approver", default="", help="name of the person deciding (required to decide)")
    args = parser.parse_args()

    path = Path(args.audit)
    items = pending_items(read_audit(path))
    print(f"Pending human approval: {len(items)}")
    for it in items:
        print(f"  {it['ticket_id']}  {it['order_id']}  {float(it['amount']):8.2f}  {it['reason_code']}  - {it.get('agent_reason', '')[:70]}")
    if args.list or not items:
        return

    approver = args.approver or input("Your name (approver): ").strip()
    if not approver:
        raise SystemExit("An approver name is required - decisions must be attributable.")

    preset = dict(d.split("=", 1) for d in args.decide)
    new_records = []
    for it in items:
        choice = preset.get(it["ticket_id"])
        if choice is None:
            if args.decide:
                continue  # non-interactive mode: only decide what was given
            choice = input(f"{it['ticket_id']} {it['order_id']} {float(it['amount']):.2f} - approve/reject/skip? ").strip().lower()
        if choice not in ("approve", "reject"):
            continue
        rec = decide(it, choice, approver)
        new_records.append(rec)
        print(f"  -> {rec['action']}: {rec['ticket_id']} {rec['note']}")

    if new_records:
        with path.open("a", encoding="utf-8") as fh:
            for rec in new_records:
                fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print(f"Wrote {len(new_records)} decision(s) to {path}")


if __name__ == "__main__":
    main()
