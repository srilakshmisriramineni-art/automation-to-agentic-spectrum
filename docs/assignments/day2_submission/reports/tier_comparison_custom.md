# Tier comparison - custom: Custom prompt

## Prompt
```
You are helping an IT service desk analyst. Using ONLY the policy below, answer:
1. The payroll team (12 people) cannot open the payroll system at all; everyone else can work. Which priority is this, and within what time must it be resolved?
2. A manager phones and asks the desk to reset the password of a team member who is on leave. What must the desk do? Quote the clause.
3. A P3 ticket was logged on Monday at 10:00 and is still open on Wednesday at 10:00. Must it be escalated to the Duty Manager under clause 5.1?
Keep the answer under 120 words.

<policy>
IT SERVICE DESK POLICY - EXTRACT (fictional, for training use)

2.1 Priorities. P1: a whole site or a critical system is down. P2: one team is blocked. P3: one user is affected and has a workaround. P4: a request or question.

2.2 Targets. P1: respond within 15 minutes, resolve within 4 hours. P2: respond within 1 hour, resolve within 8 business hours. P3: respond within 4 business hours, resolve within 3 business days. P4: resolve within 5 business days.

3.4 Password resets. The service desk may reset a password only after verifying the caller with a one-time code sent to the phone number already on file. A reset requested by a third party on behalf of a colleague must be refused and logged.

5.1 Escalation. A P2 ticket not resolved within its target is escalated to the Duty Manager ([EMAIL], [PHONE]).
</policy>
```

## opus

*4.0s, cost $0.0258, tokens in/out 2/419, served by claude-opus-5-5*

1. **P2** (one team is blocked). It must be **resolved within 8 business hours** and responded to within 1 hour. If the payroll system counts as a "critical system" being down, it would be P1 instead, but the policy doesn't define which systems are critical.

2. **Refuse the reset and log the request.** Clause 3.4: "A reset requested by a third party on behalf of a colleague must be refused and logged."

3. **No.** Clause 5.1 covers only P2 tickets. Also, Monday 10:00 to Wednesday 10:00 is 2 business days, so the ticket is still within its P3 target of 3 business days.

## sonnet

*2.7s, cost $0.0113, tokens in/out 2/261, served by claude-sonnet-5-5*

1. **Priority:** The scenario fits P2 (one team is blocked) under clause 2.1. The policy doesn't define "critical system", so P1 is arguable. But everyone else can work, and the whole site isn't down. Under 2.2, P2 must be resolved within 8 business hours.

2. **Password reset:** Refuse the request and log it. Clause 3.4: "A reset requested by a third party on behalf of a colleague must be refused and logged." The desk can reset only after verifying the caller with a one-time code sent to the phone number on file.

3. **Escalation:** No. Clause 5.1 covers only P2 tickets. The P3 target is 3 business days, so the ticket is still within target at 2 days. Clause 5.1 doesn't apply to P3 either way.

## haiku

*3.7s, cost $0.0009, tokens in/out 2/740, served by claude-haiku-5-5*

**1. Payroll outage:** This is most likely **P2** ("one team is blocked"), because only the payroll team is affected. It needs a response within 1 hour and resolution within 8 business hours. If the payroll system counts as a "critical system" under P1, the targets would be a 15-minute response and 4-hour resolution. The policy doesn't define "critical," so confirm that before setting the priority.

**2. Password reset by phone:** Refuse it and log the request. Clause 3.4 says: "A reset requested by a third party on behalf of a colleague must be refused and logged."

**3. P3 ticket open on Wednesday:** No. Clause 5.1 applies only to P2 tickets. A P3 ticket's resolution target is 3 business days, so it isn't overdue until Thursday.

## Your scoring (fill in)

| Tier | Correct? (0-3) | Followed length limit? | Would you trust it unchecked? |
|---|---|---|---|
| opus |  |  |  |
| sonnet |  |  |  |
| haiku |  |  |  |
