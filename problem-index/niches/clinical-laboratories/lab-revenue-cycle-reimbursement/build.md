# A Collectable-Value Forecast for Every Requisition

**Niche:** [[niches/clinical-laboratories/lab-revenue-cycle-reimbursement/profile|Lab Revenue Cycle & Reimbursement]]
**Industry:** [[industries/clinical-laboratories|Clinical Laboratories]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A lab learns what a requisition was worth only when the last remittance arrives; nobody estimates it while the specimen is still in the building and the problem can still be fixed.
**Tags:** #gradient-boosting #logistic-regression #feature-engineering #large-language-models #revenue-impact #automation #data-integration
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor in this niche is fighting to collect what each requisition is owed. But routine tests and molecular or genetic tests are won on different things. Routine testing is a volume game of a few dollars a line, won by whoever recovers the most net dollars per thousand claims through the 2027 fee schedule reset. Molecular testing is a coverage game of hundreds or thousands of dollars a test, won by whoever gets paid on the highest share of tests performed through authorization, Z-codes and appeals. Staff, vendors and win conditions differ, so the niche is decomposed into contested sub-niches below.

## The Problem
Every requisition carries an expected payment that depends on the payer, the plan, the tests, the diagnosis codes, the contract and, for some tests, an authorization. Labs see the answer weeks later, line by line, after denials and adjustments. By then the ordering office has moved on, the patient has received a bill, and fixing a missing diagnosis code means a call nobody returns. Collection teams then work denials by date or dollar, not by the odds of recovery.

## Why Nobody Has Built This
Billing systems start at the claim, not at accessioning, and lab information systems do not hold payer contracts or denial history. The two halves sit in different systems with different owners: lab operations and revenue cycle. Vendors sell either the LIS or the billing engine.

## What to Build
A model that scores each requisition at accessioning: probability of payment per test line, likely denial reason and expected dollars, trained on the lab's own claim and remittance history. It routes the requisitions worth fixing to client services the same day with the exact missing item, and holds high-dollar tests until coverage is clear. For finance it rolls up into a daily forecast of collectable revenue by client, payer and test.

## Target Customer
VP of revenue cycle at a regional or specialty lab billing 5,000–50,000 requisitions a day, and the outreach director at a health-system lab.

## Impact If Built
Problems get fixed while they are cheap. A lab collecting $150M a year that turns avoidable write-offs worth 2% of revenue into same-day fixes gains ~$3M (estimate), and client services call the offices that matter instead of every office.
