# Every Dig Verifies a Prediction and the Verifications Are Filed

**Niche:** [[niches/utility-contractors/pipeline-integrity-management/profile|Pipeline Integrity Management & In-Line Inspection]]
**Industry:** [[industries/utility-contractors|Utility Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Anomaly sizing is a prediction that gets physically checked with a measuring tool every time a pipe is dug up, and no vendor publishes how accurate its predictions were.
**Tags:** #gradient-boosting #bayesian-inference #evaluation-metrics #confidence-intervals #survival-analysis

## The Problem
An in-line inspection produces a list: at this location, a metal loss anomaly, so deep, so long, so wide. The depth number decides everything downstream. Above a threshold the operator must excavate and repair within a regulator-set window; below it, the anomaly is left and reassessed later. Every one of those calls is a prediction about buried steel made from an indirect magnetic or ultrasonic signal.

Then the operator digs. A technician cleans the pipe and measures the anomaly directly. That measurement is the ground truth for the prediction — recorded, reported, and required.

The comparison exists in a limited, conventional form. Vendors state tool specifications as a sizing accuracy within a tolerance at a confidence level, and unity plots comparing predicted to measured depth are a standard part of dig verification. What does not exist is a maintained, systematic performance record across many runs, operators, pipe populations and anomaly types — an answer to where the tool is biased, on what wall thickness, in what pipe grade, near which features, and how that has changed across tool generations.

The consequence is expensive in both directions. Under-calling a defect leaves a real threat in the ground. Over-calling sends a crew to excavate a pipe that did not need it, at very large cost per dig, which is where a substantial share of integrity budgets go. Operators know their vendors have characteristic tendencies and manage it as folklore.

## Why Nobody Has Built This
The specification is the commercial promise. A vendor publishing measured accuracy that differs from its stated tolerance creates a contractual and reputational problem, and one that will be used against it in the next procurement.

The verification data is also fragmented by ownership. Dig results belong to the operator; inspection data belongs to the operator too, with the vendor holding a copy under contract. Assembling a cross-operator record means negotiating access to data every party treats as sensitive — and pipeline data is additionally sensitive for security reasons.

And the field's methods are conservative for good reason. Assessment methods are codified, referenced by regulation, and defended in enforcement proceedings. A statistically better method that is not in the code is harder to use, not easier.

## What to Build
A calibration and prediction layer over the vendor's own accumulated verification record.

**Assemble the paired dataset.** Predicted sizing against measured sizing, joined to pipe attributes, tool type, run conditions and anomaly morphology. This is the asset, it accumulates with every dig, and it is currently spread across project files.

**Model sizing error, not just report it.** Bias and spread as functions of wall thickness, pipe grade, anomaly type, proximity to welds and features, and tool generation. The output is a corrected depth with an honest interval, which is a materially different product from a point call with a blanket tolerance.

**Make the dig decision an expected-cost calculation.** With a predictive distribution over true depth, the choice to excavate becomes a comparison between the cost of a dig and the probability-weighted cost of leaving a defect. That is the decision the operator is actually making and it is currently made against a deterministic threshold.

**Model growth as well as size.** Repeat inspections of the same pipe give observed growth. Treating remaining life as a survival problem over the joint distribution of current size and growth rate is the natural formulation and would replace assumed rates with estimated ones.

**Publish calibration on the vendor's terms.** A vendor that reports measured accuracy by pipe population, before a customer computes it themselves, sets the standard rather than answering it. In a market where every vendor quotes the same tolerance, being the one with evidence is the strongest available position.

## Target Customer
VP of Integrity Services or Chief Engineer at an in-line inspection vendor or integrity consultancy. The commercial argument is that tool specifications have converged, dig costs dominate operators' integrity budgets, and calibrated sizing is the only differentiation left that a competitor cannot simply claim.

## Impact If Built
US operators spend enormous sums excavating pipelines, a large share of it on anomalies that turn out not to have needed it, while under-called defects remain the mechanism behind the failures the whole regime exists to prevent. A calibrated sizing model with honest intervals reallocates that spending toward the digs that matter — and it is buildable from verification data that is already being collected, reported, and filed.
