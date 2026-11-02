# Tier comparison - Q1: Contract clause analysis (reasoning + arithmetic + careful reading)

## Prompt
```
You are helping a procurement analyst. Using ONLY the clauses below, answer:
1. In one month availability was 98.6%. What service credit is owed in money? Show the calculation.
2. The Customer terminates after 8 months. What is the early-termination charge in money?
3. Can the Supplier process customer data in India without asking? Quote the clause.
Keep the answer under 150 words.

<clauses>
SERVICES AGREEMENT - EXTRACT (fictional, for training use)

4.1 Fees. The Customer shall pay the Supplier a fixed monthly fee of 12,400.00 for the
Managed Support Service, invoiced on the first business day of each month.

4.2 Late payment. Invoices unpaid after 30 days incur interest at 1.5% per month on the
overdue amount.

7.1 Service credits. If monthly availability falls below 99.5%, the Supplier shall credit
5% of that month's fee for each full 0.5 percentage points below 99.5%, up to a maximum
credit of 20% of the monthly fee.

9.2 Termination for convenience. Either party may terminate on 90 days' written notice.
If the Customer terminates in the first 12 months, an early-termination charge equal to
two months' fees applies.

11.4 Data location. Customer personal data shall be processed only within the European
Economic Area unless the Customer gives prior written consent.

</clauses>
```

## Reference answer (for the human judge)
- Q1: 99.5 - 98.6 = 0.9 points -> 1 full 0.5-point step -> 5% of 12,400.00 = 620.00
- Q2: two months' fees = 24,800.00 (terminated within first 12 months)
- Q3: No - clause 11.4 requires prior written consent for processing outside the EEA

## opus

*4.3s, cost $0.0314, tokens in/out 2/418, served by claude-haiku-5-5, claude-opus-5-5*

**1. Service credit:** 620.00
- Shortfall: 99.5% − 98.6% = 0.9 percentage points
- Full 0.5-point steps: 1 (the remaining 0.4 doesn't count, since only *full* steps earn a credit)
- Credit: 1 × 5% = 5%, well under the 20% cap
- 5% × 12,400.00 = **620.00**

**2. Early-termination charge:** 24,800.00
- 8 months falls within the first 12 months, so clause 9.2 applies.
- 2 × 12,400.00 = **24,800.00** (the 90 days' written notice is still required)

**3. Processing data in India:** No. India is outside the European Economic Area, so the Supplier needs the Customer's prior written consent first. Clause 11.4: "Customer personal data shall be processed only within the European Economic Area unless the Customer gives prior written consent."

*Note: the extract doesn't name a currency, so the amounts are shown without one.*

## sonnet

*3.2s, cost $0.0118, tokens in/out 2/327, served by claude-sonnet-5-5*

1. **Service credit (cl. 7.1):** 99.5 − 98.6 = 0.9 percentage points below target. Only full 0.5-point steps count, so that is 1 step. Credit = 5% × 12,400.00 = **620.00**. The 20% cap (2,480.00) isn't reached.

2. **Early-termination charge (cl. 9.2):** Termination at 8 months falls within the first 12 months, so the charge is two months' fees: 2 × 12,400.00 = **24,800.00**. The clauses don't say whether the 90-day notice period affects this. Month 8 is also still within the first 12 months either way.

3. **Data in India (cl. 11.4):** No. The clause says: "Customer personal data shall be processed only within the European Economic Area unless the Customer gives prior written consent." India is outside the EEA, so the Supplier needs the Customer's prior written consent.

The clauses give no currency, so the amounts are in unspecified currency units.

## haiku

*3.8s, cost $0.0009, tokens in/out 2/822, served by claude-haiku-5-5*

**1. Service credit for 98.6% availability: 620.00**

- Shortfall below 99.5%: 0.9 points.
- Full 0.5-point steps below 99.5%: 0.9 ÷ 0.5 = 1.8, so 1 full step (the 98.5% step is not reached).
- Credit: 5% × 12,400.00 = **620.00**. This is below the 20% cap (2,480.00).

**2. Early-termination charge after 8 months: 24,800.00**

Clause 9.2 applies because termination falls in the first 12 months. The charge is two months' fees: 2 × 12,400.00 = **24,800.00**.

**3. Processing customer data in India without asking: No**

Clause 11.4: "Customer personal data shall be processed only within the European Economic Area unless the Customer gives prior written consent."

The Supplier needs the Customer's prior written consent first.

## Your scoring (fill in)

| Tier | Correct? (0-3) | Followed length limit? | Would you trust it unchecked? |
|---|---|---|---|
| opus |  |  |  |
| sonnet |  |  |  |
| haiku |  |  |  |
