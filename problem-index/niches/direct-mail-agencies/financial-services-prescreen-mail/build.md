# Booked-Account Selection Across Prescreen Waves

**Niche:** [[niches/direct-mail-agencies/financial-services-prescreen-mail/profile|Financial Services Prescreen & Acquisition Mail]]
**Industry:** [[industries/direct-mail-agencies|Direct Mail Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Prescreen selection is tuned to predict who responds, while the issuer pays for mail to produce accounts that are approved, activated and profitable — a different target nobody models end to end.
**Tags:** #gradient-boosting #survival-analysis #causal-inference #evaluation-metrics #feature-engineering #revenue-impact #compliance
**Contested on:** Every serious competitor in this niche is fighting to lower the cost per booked, activated account across prescreen waves — mailing names the issuer's credit policy will approve and that will actually respond — and whoever closes the loop from mailed name to funded account fastest takes the account.

## The Problem
An issuer mails a prescreen wave of several million pieces every few weeks. The selection model ranks bureau-qualified names by likelihood to respond, and the wave is judged on response rate and cost per application. But a response becomes revenue only if the applicant is approved under current underwriting, activates the card, and spends or revolves. Segments with high response and high decline or low activation look good in the mail report and poor in finance's.

## Why Nobody Has Built This
The funnel stages sit in different systems owned by different teams — marketing, underwriting, card operations — and the agency that runs the mail sees only response. Activation and early spend arrive 60–120 days after the drop (estimate), by which time three more waves have been selected. FCRA rules on how prescreen data may be used make teams cautious about joining it to later outcomes.

## What to Build
A wave-level selection model whose target is expected booked value per piece: probability of response × approval under current criteria × activation × early spend, each modelled separately with time-to-event methods so partially matured waves contribute. Each wave carries randomised holdouts and challenger cells, and the model updates as earlier waves mature, with every selection decision documented for the issuer's compliance review.

## Target Customer
Acquisition marketing heads at card issuers, consumer lenders and insurers mailing prescreen programmes, and the agencies and integrated mailers that run those programmes for them.

## Impact If Built
Shifting mail from high-response, low-value segments to names that book and activate cuts cost per funded account on the largest mail budgets in the industry, and gives the agency a result finance accepts rather than one only marketing reports.
