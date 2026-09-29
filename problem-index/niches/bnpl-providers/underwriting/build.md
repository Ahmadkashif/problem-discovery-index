# A Credit Decision in a Checkout

**Niche:** [[niches/bnpl-providers/underwriting/profile|Underwriting]]
**Industry:** [[industries/bnpl-providers|BNPL Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A credit decision is made in a few hundred milliseconds inside a checkout, on an applicant the bureaus frequently cannot describe, with the decisive fact — what they already owe elsewhere — invisible by construction.
**Tags:** #gradient-boosting #logistic-regression #survival-analysis #confidence-intervals #evaluation-metrics #compliance #revenue-impact #causal-inference
**Contested on:** This niche is not terminal — inferring capacity from a thin file and seeing what a consumer owes elsewhere are different contests with different winners, and they are stated separately in the sub-niches.

## The Problem
A consumer reaches a checkout and chooses to split the payment. The provider has a few hundred milliseconds, an email address, a debit card, a device, a basket, and possibly a bureau record that may be empty. It must decide whether this person will make four payments over six weeks. Everything it can see suggests they can. What it cannot see is that they took five other plans this afternoon from five other providers, none of which will appear anywhere in time to matter. The decision is made competently on the available evidence and the available evidence structurally excludes the thing that most determines the answer.

## Why Nobody Has Built This
Furnishing to the bureaus is partial and the products that furnish tend to be the longer-term ones rather than the short instalment plans where accumulation actually happens — the reporting structure means the sector's central risk is invisible to every participant simultaneously, which is a coordination failure rather than a technical one. Each provider's own data is a competitive asset. The bureaus' formats were not designed for six-week obligations. And the growth has been fast enough that the structural gap has not yet been forced closed.

## What to Build
Do both halves of the problem. Model capacity from what the provider can see, which is the first sub-niche's contest and is where a provider can win alone — device, behaviour, basket, merchant, and the provider's own repayment history are a rich evidence base and the science applied to them is frequently shallow. Solve the visibility problem through furnishing, a consortium or a real-time sharing mechanism, which is the second sub-niche and cannot be solved by any provider's model. Predict repayment rather than default in the abstract, since the product's structure — four payments over six weeks against a debit card — makes the failure mode specific and different from a loan default. Use outcomes to validate the model at the horizon that matters, because six weeks is short enough that continuous validation is genuinely feasible and rare. Handle the affordability question rather than only the willingness one, since a consumer who will pay and cannot afford to is the outcome the sector is judged on. Report both errors, including the applicant declined who would have repaid, since growth and fairness both live in that error and it is invisible. Segment by product, as pay-in-four and longer interest-bearing instalments are different risks and are frequently scored by one stack. Build for the regulatory direction of travel, since affordability assessment expectations are tightening and a provider that can evidence its assessment is in a far better position. Feed the sector's own repayment data into the models properly, connecting to the intelligence niche. And report approval and loss by segment to leadership, because a business whose central decision is unexamined at that level is running on its growth rate.

## Target Customer
Credit risk leadership at instalment providers, the bureaus and consortium operators who could supply the missing visibility, and the regulators forming a view of the sector.

## Impact If Built
The reporting structure makes the sector's central risk invisible to every participant simultaneously, which is a coordination failure rather than a technical one. Doing the modelling half well and the sharing half at all are two different projects and the category has been treating them as one.
