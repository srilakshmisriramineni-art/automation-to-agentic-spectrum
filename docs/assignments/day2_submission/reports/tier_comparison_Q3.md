# Tier comparison - Q3: Judgement

## Prompt
```
A colleague pastes a customer's full name, phone number and order history into a free personal chatbot account to 'save time'. List three risks and one safer alternative. Max 80 words.
```

## opus

*2.9s, cost $0.0236, tokens in/out 2/193, served by claude-haiku-5-5, claude-opus-5-5*

**Risks:**
1. **Privacy law breach:** Sharing personal data with an unapproved third party may violate GDPR or similar laws, with no legal basis or processing agreement.
2. **Data retention and training:** Free consumer tools may store the inputs, let staff review them, or use them to train models.
3. **Loss of control:** The company can't audit, delete or contain the data, and a leak hurts customer trust and the company's reputation.

**Safer alternative:** Use a company-approved enterprise AI tool with a data protection agreement, and remove or anonymise customer details first.

## sonnet

*3.1s, cost $0.0114, tokens in/out 2/181, served by claude-sonnet-5-5*

**Risks:**
1. **Data exposure:** Free personal accounts may retain the data or use it for model training, so a customer's personal information could leak.
2. **Legal breach:** It likely violates data protection law (GDPR or similar) and company policy, because there's no consent or data processing agreement.
3. **No control:** Your company can't audit, delete, or recover data held in a personal account.

**Safer alternative:** Use a company-approved AI tool with a data processing agreement. Alternatively, anonymize the data first by removing the name and phone number.

## haiku

*2.0s, cost $0.0006, tokens in/out 2/270, served by claude-haiku-5-5*

**Three risks:**

1. **Data leakage:** Free consumer chatbots may store prompts and use them for model training, so the customer's name, phone number, and order history could persist outside your control.
2. **Privacy and legal exposure:** Sharing personal data with an unapproved third party can breach GDPR, CCPA, or your company's data-protection policy, creating liability for the colleague and the company.
3. **Loss of control:** The data may be retained, exposed in a breach, or accessible through a personal account that isn't covered by company security or deletion processes.

**Safer alternative:** Use an enterprise AI tool your company has approved, under a contract with a data-processing agreement. Or remove identifiers first, replacing the name and phone number with placeholders like "Customer A," and keep only the non-identifying details the task needs.

## Your scoring (fill in)

| Tier | Correct? (0-3) | Followed length limit? | Would you trust it unchecked? |
|---|---|---|---|
| opus |  |  |  |
| sonnet |  |  |  |
| haiku |  |  |  |
