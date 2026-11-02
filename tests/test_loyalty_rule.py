"""
tests/test_loyalty_rule.py - Day 1 take-home, Part B.

New policy rule 1a: customers flagged 'loyalty' on the ORDER RECORD get a late-delivery
grace of 1 day instead of 3. These tests pin the rule, its boundaries, and the fact that
a customer merely CLAIMING loyalty in the ticket text changes nothing.
Run:  python -m unittest tests.test_loyalty_rule -v
"""
import unittest

from solutions.day1_ai_spectrum import dispute_tools as dt


def order(days_late: int, loyalty=None, amount: float = 38.0) -> dict:
    """A synthetic delivered order, `days_late` days after a 2026-10-10 promise, inside the 30-day window."""
    from datetime import date, timedelta
    delivered = date(2026, 10, 10) + timedelta(days=days_late)
    row = {"order_id": "ORD-9999", "customer_email": "test@example.com", "item": "Test item", "amount": amount,
           "status": "delivered", "ordered": "2026-10-01", "promised": "2026-10-10",
           "delivered": delivered.isoformat(), "condition_note": ""}
    if loyalty is not None:
        row["loyalty"] = loyalty
    return row


class LoyaltyGraceRule(unittest.TestCase):
    def decide(self, o):
        return dt.evaluate("test@example.com", o)

    # --- the rule passes ---------------------------------------------------------------
    def test_loyalty_two_days_late_is_refunded(self):
        d = self.decide(order(2, loyalty=True))
        self.assertEqual((d["decision"], d["reason_code"], d["amount"]), ("refund", "LATE_DELIVERY_LOYALTY", 38.0))

    def test_ticket_t09_from_data_is_refunded(self):
        desk = dt.DisputeDesk(write_logs=False)
        d = dt.evaluate(desk.tickets["T-09"]["customer_email"], desk.orders["ORD-1009"])
        self.assertEqual((d["decision"], d["reason_code"]), ("refund", "LATE_DELIVERY_LOYALTY"))

    # --- boundaries ----------------------------------------------------------------------
    def test_loyalty_exactly_one_day_late_is_not_late(self):
        """'MORE THAN 1 day' - exactly 1 day is still inside the grace period."""
        d = self.decide(order(1, loyalty=True))
        self.assertEqual((d["decision"], d["reason_code"]), ("escalate", "MANUAL_REVIEW"))

    def test_non_loyalty_two_days_late_is_not_late(self):
        """Same order, no flag: the normal 3-day grace still applies."""
        d = self.decide(order(2))
        self.assertEqual(d["reason_code"], "MANUAL_REVIEW")

    def test_non_loyalty_boundary_unchanged(self):
        self.assertEqual(self.decide(order(3))["reason_code"], "MANUAL_REVIEW")   # exactly 3 -> not late
        self.assertEqual(self.decide(order(4))["reason_code"], "LATE_DELIVERY")   # 4 -> late

    def test_loyalty_very_late_keeps_normal_reason_code(self):
        """Late under BOTH rules -> plain LATE_DELIVERY (rule 1a was not needed)."""
        self.assertEqual(self.decide(order(5, loyalty=True))["reason_code"], "LATE_DELIVERY")

    # --- safety --------------------------------------------------------------------------
    def test_only_boolean_true_counts(self):
        """A string like "yes" (e.g. copied from free text) must not switch the rule on."""
        self.assertEqual(self.decide(order(2, loyalty="yes"))["reason_code"], "MANUAL_REVIEW")
        self.assertEqual(self.decide(order(2, loyalty=False))["reason_code"], "MANUAL_REVIEW")

    def test_loyalty_refund_still_respects_auto_approval_limit(self):
        d = self.decide(order(2, loyalty=True, amount=150.0))
        self.assertTrue(d["needs_human"])

    def test_issue_refund_pays_t09_and_lookup_exposes_grace(self):
        desk = dt.DisputeDesk(write_logs=False)
        self.assertEqual(desk.lookup_order("ORD-1009", "T-09")["late_grace_days"], 1)
        self.assertEqual(desk.lookup_order("ORD-1001", "T-01")["late_grace_days"], 3)
        self.assertEqual(desk.issue_refund("T-09", "ORD-1009", 38.0, "late, loyalty")["status"], "refunded")


if __name__ == "__main__":
    unittest.main()
