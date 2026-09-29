# Assessments Judged by Consensus Instead of Against Settled Trades

**Niche:** [[niches/metal-fabrication/metals-price-reporting-agencies/profile|Metals Price Reporting Agencies]]
**Industry:** [[industries/metal-fabrication|Metal Fabrication]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The published price settles real contracts and its accuracy is defended by methodology rather than measured against outcomes.
**Tags:** #tabular-ml #ml-time-series #anomaly-detection #evaluation-metrics #hypothesis-testing

## The Problem
A metals assessment is a judgment. Reporters collect bids, offers, and reported trades from market participants, weigh them against the methodology's specifications, and publish a number. Mill contracts, service centre agreements, and fabrication quotes are indexed to it, so the number moves real money.

Accuracy is defended procedurally. The methodology is published, the process is auditable, and disputes are handled through a documented review. What is not done is measuring the assessment against what the market actually settled at, because assembling that comparison would require the trade data the agency collects from participants and treats as inputs rather than as a test set.

The consequences are structural. Nobody knows which grades and regions are assessed well and which rest on three submissions in a thin week. Nobody knows whether an assessment leads or lags the market it describes. And nobody can say whether a methodology change improved anything.

## Why Nobody Has Built This
Price reporting is a journalism-derived discipline with an editorial identity. The reporter's judgment is the product, and subjecting it to statistical evaluation reads as a challenge to the profession rather than as support for it.

Regulatory scrutiny after the benchmark scandals of the last decade pushed hard on process — documented methodology, conflict management, auditability — and process compliance became the definition of quality. Outcome accuracy was not part of that agenda.

And thin liquidity makes the measurement feel impossible. In grades with few transactions, there is no obvious ground truth. That is exactly backwards: thin liquidity is where assessment error is largest and where quantifying uncertainty matters most.

## What to Build
Measure the assessments and publish what the measurement says.

**Assemble the submission and assessment history as a dataset.** Every input received, every assessment published, every methodology version, over years. The agency holds it as records and has never treated it as data.

**Estimate assessment uncertainty per grade and region.** Submission count, dispersion, and consistency with related assessments give a computable confidence. An assessment resting on three submissions in a wide range is not the same product as one resting on forty in a tight one, and today they look identical.

**Check for lead-lag and consistency.** Assessments across related grades, regions, and the futures curve should move coherently. Where they do not, one of them is wrong, and that is detectable continuously rather than at the next methodology review.

**Evaluate methodology changes.** When a specification or window changes, did dispersion narrow and did the assessment track related markets better? Nobody has ever asked, and it is answerable.

**Publish confidence.** Being the first agency to publish assessment uncertainty is a competitive move as much as a quality one — in a market where index licensing is the revenue and credibility is the moat, saying which of your numbers are strong is a claim no competitor can match without doing the work.

## Target Customer
Editorial director or chief data officer at a price reporting agency. The regulatory direction favours it: benchmark oversight has been moving from process compliance toward demonstrable representativeness, and the agencies that get there first define the standard.

## Impact If Built
These assessments settle physical contracts across an enormous supply chain and are used as hedging references. Knowing which of them are well-supported and which are thin — and saying so — improves every contract indexed to them, and gives the agency the one differentiation available in a business where everyone publishes a number.
