# Benefits Enrolment and Carrier Feed Reconciliation

**Industry:** [[hr-tech-platforms|HR Tech Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Benefits administration and carrier EDI feeds are standard, established plumbing that silently diverge — and the failure is discovered when an employee's claim is denied at a pharmacy counter.
**Tags:** #change-point-detection #hypothesis-testing #descriptive-statistics #confidence-intervals #evaluation-metrics #data-integration #compliance

## The Problem
An employee enrols in benefits through the HR platform. That election must reach the carrier, the pharmacy benefit manager, the dental and vision carriers, the life insurer, the flexible spending administrator and the payroll deduction. Each connection is an EDI feed or an API integration, each has its own format and cadence, and each can fail quietly.

The failures are ordinary. A mid-year life event processed in the platform that never reaches the carrier. A termination that does not propagate, so coverage continues and premiums are paid for someone who left. A dependent added without the corresponding change in the payroll deduction. A plan year change that maps benefit tiers incorrectly.

Nobody notices, because nothing reconciles. The platform believes the employee is enrolled; the carrier's system says otherwise; the discrepancy sits there until the employee tries to use the coverage. Then an HR generalist spends days on the phone with a carrier reconstructing what happened, while the employee is exposed to a bill.

## What Already Exists
Benefits administration modules are standard in every HCM platform. EDI 834 is a mature standard for enrolment transmission. Benefits administration specialists and brokers provide connectivity services. Carrier portals allow manual verification. Some platforms provide feed transmission logs.

## The Customisation Gap
Transmission is confirmed; enrolment is not. A feed that transmitted successfully has proven only that a file was sent, and the interesting failure is when the carrier received it and did not apply it, or applied it differently. Nothing compares the platform's belief about who is enrolled in what against the carrier's belief.

Regular reconciliation — comparing the platform's enrolment census against the carrier's, per plan, per month — is straightforward, is what a careful benefits team does by hand for the largest plan, and is not done systematically anywhere. Detecting the discrepancy is the whole product.

Anomaly detection on the feed itself is the cheaper first step. A feed whose record count drops sharply, whose termination volume spikes, or which stops containing a plan is broken in a way that is visible immediately and is currently visible to nobody.

Premium reconciliation is the third piece and the one with money attached: comparing what the carrier invoices against who the platform believes is enrolled routinely reveals employers paying for terminated employees, sometimes for years.

## Impact If Solved
Benefits failures land on individual employees at the worst possible moment and on employers as premiums paid for coverage nobody holds. Reconciliation is unglamorous, entirely tractable, and absent from a category that has been transmitting these files for thirty years.
