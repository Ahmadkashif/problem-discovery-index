# A Funding Path Planner for Each New Start

**Niche:** [[niches/physician-practices/medical-benefit-drug-access/profile|Medical-Benefit Drug Access (Buy-and-Bill & Infusions)]]
**Industry:** [[industries/physician-practices|Physician Practices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** For each new biologic or chemotherapy start, an experienced reimbursement specialist knows which payer, site-of-care rule, manufacturer programme and foundation fund will get the patient treated; that knowledge is in her head, not in any system.
**Tags:** #tacit-knowledge-ml #gradient-boosting #large-language-models #evaluation-metrics #revenue-impact #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to get each infused or injected drug approved, funded and paid before the first dose, and whoever starts the most patients on therapy with no denied or unfunded doses takes the account.

## The Problem
A rheumatologist prescribes an infused biologic. The reimbursement specialist must decide whether to buy and bill or route to a specialty pharmacy, which step-therapy evidence the plan needs, and whether the patient qualifies for the manufacturer's copay programme (commercial only) or needs a foundation fund that may be closed this month. Wrong choices delay the start by weeks or leave the practice with an unfunded dose.

## Why Nobody Has Built This
Hubs serve one manufacturer's drugs. Practices see every drug, and their outcome history (time to start, write-offs, approvals) sits in billing and spreadsheets. Foundation fund status changes weekly and is checked by hand.

## What to Build
A planner that takes the order, the patient's coverage and the practice's history, and recommends the path: benefit (medical or pharmacy), site of care, the evidence the authorization needs, and the funding sources in order of likelihood. A model trained on the practice's own new starts predicts time to first dose and write-off risk for each path. The reimbursement specialist's choices and overrides become labels.

## Target Customer
Oncology, rheumatology, gastroenterology and neurology groups with infusion suites, and the MSOs that run them.

## Impact If Built
Cutting time to first dose by ~1 week (estimate) and avoiding even a few unfunded doses a month, each worth ~$5,000–$20,000 (estimate), pays for the tool many times over.
