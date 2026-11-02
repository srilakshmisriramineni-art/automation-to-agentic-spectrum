# Day 2 Take-Home Submission - Gowtham

**Code and output (readable, no PDF needed): [`../DAY2_CODE_AND_OUTPUT.md`](../DAY2_CODE_AND_OUTPUT.md)**

- Write-up (Parts A-E): `Day2_Take_Home_Submission_Gowtham.docx` / `.pdf`
- Tier reports + homework sheet + audit log: `reports/` (copies of outputs/, which git ignores)
- Raw console output of every run: `evidence/`
- Changed files only: `day2_changed_files.zip`
- Steps still to do by hand (consumer apps, real embedding model): `PartB_Your_Steps.txt`

## Files changed
| File | Change |
|---|---|
| solutions/day2_models_and_embeddings/verify_outputs.py | late_interest_percent_per_month (clause 4.2, 1.5%); decimal-matching fix; clause_coverage() completeness check |
| solutions/day2_models_and_embeddings/data/sentences.json | 8 sentences on new topic finance_expenses |
| solutions/day2_models_and_embeddings/embeddings_map.py | palette bug fix (5th topic was dropped from the map) |
| solutions/day2_models_and_embeddings/data/my_query_itdesk.txt | my synthetic Part B source text |
| tests/test_day2.py | 8 new tests |

Tests: 80 pass (1 skipped where the real embedding model is not installed).
No `.env`, API key, `.venv` or real data included.
