# Every Test Is Run Because a Protocol Says So, Not Because Anything Is Likely to Fail

**Niche:** [[niches/alterations-tailoring/softlines-testing-labs/profile|Softlines Testing & Quality Assurance Labs]]
**Industry:** [[industries/alterations-tailoring|Alterations & Tailoring]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The lab holds years of pass/fail results by factory, fabric construction and test method, and still runs the full panel on everything.
**Tags:** #gradient-boosting #logistic-regression #evaluation-metrics #confidence-intervals #causal-inference

## The Problem
A garment programme cannot ship until the lab clears it. The brand's protocol specifies a panel — colourfastness to crocking, washing and light, dimensional stability, seam slippage and strength, pilling, flammability, restricted substances — and the lab runs it, on samples, from every supplier, every season.

The panel is fixed by protocol. It does not vary with the probability of failure. The same battery is run on a fabric construction from a factory with a five-year clean record and on a first-order supplier working an unfamiliar finish.

The lab knows the difference. Its own archive records, across thousands of brands and tens of thousands of suppliers, which factories fail which tests, which fabric constructions fail dimensionally, which dye classes fail lightfastness, and which failures recur after a corrective action and which do not. That is the best empirical picture in existence of who actually makes reliable garments — better than any brand's, because no brand sees the factory's work for its competitors.

Two things follow that nobody does. Failure is predictable, which means test panels could be risk-weighted — deeper on the likely failures, lighter where the record is long and clean — cutting cost and turnaround without weakening the gate. And the prediction itself is a product: a brand deciding whether to place with a new factory would pay real money for a failure-risk estimate that the lab could compute today.

The blocker is real: results belong to the brand that commissioned them, and cross-brand aggregation is contractually barred. But within a single large brand's own programme the archive is already the lab's to use, and it is not used there either.

## Why Nobody Has Built This
The invoice is per test. A model that reduces the number of tests reduces revenue directly, which is an unusually blunt disincentive and the honest reason this has not been built.

Protocols are also the brand's, not the lab's. A lab proposing to skip tests is proposing to change its customer's quality standard, which is a conversation labs avoid.

And confidentiality is genuine. The cross-brand view is the valuable one and is the one that cannot be sold without a governance structure nobody has attempted.

## What to Build
Failure prediction, positioned as risk-based assurance rather than as fewer tests.

**Model failure probability per test, per submission.** Factory, fabric construction, fibre blend, dye class, finish, construction details, and the supplier's own history. The archive supplies both features and labels at scale.

**Reframe the commercial model around coverage, not count.** Risk-based panels sold as a programme fee — same or better defect detection, fewer tests — aligns the lab with the brand instead of against it, and is the only version that survives the revenue objection.

**Sell factory risk within the brand's own footprint.** A brand's sourcing team placing a new order would pay for a failure-risk estimate built from that brand's own historical results, which needs no cross-brand permission at all.

**Model corrective action effectiveness.** After a failure, a corrective action is agreed and the factory re-tests. Whether the fix held is observable in later submissions, and nobody measures which corrective actions actually work.

**Build the consented cross-brand layer deliberately.** A de-identified factory risk index, contributed to and consumed by participating brands, is a genuine industry product. It requires a governance design first and a model second.

## Target Customer
VP of Softlines or Global Technical Director at a testing, inspection and certification group. The strategic argument is that per-test pricing is under permanent pressure from in-house brand labs and low-cost regional competitors, and risk-based assurance is the only version of this business that is not a commodity.

## Impact If Built
Apparel testing is a gate every garment programme passes through, priced per test and run to a fixed protocol regardless of risk. Making it risk-weighted cuts cost and cycle time for brands while improving detection where it matters — and converts a lab's failure archive from a filing cabinet into the only credible supplier-reliability signal in the industry.
