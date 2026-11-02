# Day 1 Take-Home Submission - Gowtham

Write-up (Parts A-D, tables, answers, scoreboards): `Day1_Take_Home_Submission_Gowtham.docx` (same content in `.pdf`).
Raw console output of every run: `evidence/` (before = original code, partB, partC_before, final).
Changed files only: `day1_changed_files.zip`.

## Files changed in the repo
| File | Change |
|---|---|
| solutions/day1_ai_spectrum/dispute_tools.py | Rule 1a loyalty grace (1 day); Part C control: ticket-scoped `lookup_order()` with redaction |
| solutions/day1_ai_spectrum/data/policy.md | Rule 1a in plain English |
| solutions/day1_ai_spectrum/data/orders.json, tickets.json | T-09 (loyalty case), T-10 and T-11 (new injection attacks) |
| tests/test_loyalty_rule.py | 9 tests incl. boundary cases |
| tests/test_injection_control.py | 8 tests for the new control |
| level3/4/5 scripts | ticket scope set by code; Level 4 token tally + schema fix; Level 5 `--max-tokens` fix |
| solutions/day1_ai_spectrum/approve_pending.py | Stretch 3: human approval step |

## Key results
- Unit tests: 55 passing before, 72 passing after (`python -m unittest discover -s tests`).
- Part B: Level 1 and 3 both refund T-09 after the rule (expected changed from escalated to refunded).
- Part C: all levels escalated T-10/T-11, but Level 3 obeyed the injected pointer and read another customer's order (ORD-1003); the new control now returns a redacted record.
- Part D (11 tickets): L3 --all 9/11, 83 s, 72,040/6,687 tokens; L4 8/11, 76 s, 45,811/7,974; L5 11/11, 31 s, 33,850/4,626.

No `.env`, API key, `.venv` or real data is included. All data is synthetic.
