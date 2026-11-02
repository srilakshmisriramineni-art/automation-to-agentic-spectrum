# Tier comparison - Q2: Short summarisation

## Prompt
```
Summarise in two sentences for an executive: SERVICES AGREEMENT - EXTRACT (fictional, for training use)

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

```

## opus

*2.5s, cost $0.0258, tokens in/out 2/185, served by claude-haiku-5-5, claude-opus-5-5*

The Customer pays a fixed fee of 12,400.00 per month for managed support (the extract doesn't name a currency), and invoices unpaid after 30 days incur interest at 1.5% per month. If monthly availability drops below 99.5%, the Customer gets service credits capped at 20% of that month's fee; either party can terminate on 90 days' notice, but the Customer pays two months' fees if it terminates in the first 12 months, and personal data must stay in the EEA unless the Customer agrees in writing.

## sonnet

*2.0s, cost $0.0123, tokens in/out 2/161, served by claude-sonnet-5-5*

The Customer pays a fixed monthly fee of 12,400 for managed support, with late invoices accruing 1.5% monthly interest after 30 days, and the Supplier owes service credits of up to 20% of the monthly fee if availability drops below 99.5%. Either party can exit on 90 days' notice, though early termination by the Customer in the first 12 months costs two months' fees (about 24,800), and personal data must stay within the European Economic Area unless the Customer consents otherwise.

## haiku

*1.3s, cost $0.0008, tokens in/out 2/149, served by claude-haiku-5-5*

The Customer pays a fixed €12,400 monthly fee for Managed Support, with late invoices accruing 1.5% monthly interest after 30 days. Service credits of up to 20% of the monthly fee apply if availability drops below 99.5%, either party may terminate on 90 days' notice (with a charge of two months' fees if the Customer leaves within the first year), and Customer personal data must stay within the EEA unless the Customer consents in writing.

## Your scoring (fill in)

| Tier | Correct? (0-3) | Followed length limit? | Would you trust it unchecked? |
|---|---|---|---|
| opus |  |  |  |
| sonnet |  |  |  |
| haiku |  |  |  |
