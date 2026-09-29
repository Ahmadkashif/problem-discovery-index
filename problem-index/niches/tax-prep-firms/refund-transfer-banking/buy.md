# Consumer Credit Risk Stacks Do Not Survive a Ten-Week Year

**Niche:** [[niches/tax-prep-firms/refund-transfer-banking/profile|Refund Transfer & Advance Banking]]
**Industry:** [[industries/tax-prep-firms|Tax Preparation Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Every component of a modern lending risk stack exists off the shelf, and all of them assume a continuous book, a bureau-scored borrower and time to retrain — three things a refund advance operation does not have.
**Tags:** #gradient-boosting #logistic-regression #feature-engineering #transfer-learning #evaluation-metrics

## The Problem
The bank behind refund advances runs the same functions as any consumer lender: application scoring, limit assignment, fraud screening, portfolio monitoring, collections. It has to run them at extraordinary compression — millions of decisions inside ten weeks, most of them in the first three, against a borrower population that is thinly filed and often invisible to a bureau.

The obvious move is to buy the stack. Decisioning platforms, fraud consortia, alternative-data scores, model governance tooling and monitoring dashboards are all mature, well-supported markets. The teams here have bought some of it, and it fits badly enough that a great deal of the operation still runs on internally maintained rules and spreadsheets rebuilt each autumn.

## What Already Exists
Loan origination and decisioning platforms handle application flow, rule execution and adverse action. Bureau and alternative-data scores rank consumer credit risk. Device intelligence and identity verification vendors are strong and improving. Fraud consortia share negative data across institutions. Model risk governance tooling handles documentation and monitoring. Portfolio analytics platforms track vintage performance.

Each of these is built for a lender with a book that runs all year.

## The Customization Gap
**The year is ten weeks and the model cannot learn inside it.** A continuous lender retrains on rolling performance. Here, performance for the entire cohort resolves after the season is essentially over — the refund either arrives or it does not, weeks after the advance was made. Every decision in a season is made by a model trained on the last one. Off-the-shelf monitoring assumes a feedback loop that closes in days; this one closes annually. The tooling flags drift it cannot act on and stays silent about the shift that actually matters, which is a change in tax authority processing that arrives without warning in week two.

**The predictor is not the borrower.** A refund advance is repaid by the IRS, not the customer. Creditworthiness in the ordinary sense is close to irrelevant; what matters is whether this specific return will produce this specific refund on time. Bureau scores and alternative-data scores rank the wrong thing. The genuinely predictive features are return-level — credit claims, income documentation type, prior-year filing history, preparer identity — and no vendor model has ever seen them.

**Fraud here is a preparer-level phenomenon.** The unit of concern is often not an individual application but an office producing a pattern of them. Consortium fraud tools are built around consumer identity and device, and are close to blind to the case where a legitimate identity is used on a fabricated return by an office doing it at volume. The signal is in the relationships between returns, preparers and refunds — a network structure the bought tooling does not represent.

**Population and volume shape break the score.** The borrower base skews toward thin-file and unbanked consumers, precisely the group vendor scores rank least reliably. And the volume curve — near zero, then everything, then near zero — breaks capacity planning, threshold setting and every monitoring baseline that assumes a stable denominator.

**Governance built for one product, applied to a seasonal one.** Model risk management expectations are real and the tooling assumes annual review cycles that sit awkwardly against a product where the model must be frozen before the season and cannot be touched during it. The documentation burden is genuine; the tooling does not reduce it for this shape.

## Target Customer
Head of Credit Risk or Chief Data Officer at a refund-product bank or programme manager. The buying case is narrow and honest: keep the bought decisioning, identity and governance layer, and replace the scoring and monitoring core with something built for a return-level predictor, a ten-week volume curve and an annual feedback loop.

## Impact If Solved
The season is unforgiving — a scoring error found in week four cannot be corrected until next February, and the losses are already booked. An operation running on last year's model with this year's IRS is the normal state of affairs, and the gap between the two is where the entire risk sits.
