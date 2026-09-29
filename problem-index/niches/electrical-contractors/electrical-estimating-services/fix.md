# Estimator Judgment Is the Product and Is Never Recorded

**Niche:** [[niches/electrical-contractors/electrical-estimating-services/profile|Electrical Estimating Service Bureaus]]
**Industry:** [[industries/electrical-contractors|Electrical Contractors]]
**Type:** Fix (Pain Point)
**One-liner:** An estimator decides this job needs a factor for congested ceiling space and that one does not, the decision moves the bid by tens of thousands of dollars, and the estimate records only the total.
**Tags:** #tacit-knowledge-ml #large-language-models #bert #transformers #evaluation-metrics #descriptive-statistics #feature-engineering #confidence-intervals #worker-facing #data-integration

## The Problem
Between the counted quantities and the delivered estimate sits a layer of judgment: productivity factors for site conditions, allowances for coordination difficulty, assessments of what the drawings omit, and views on how a particular general contractor runs a job. Those decisions determine whether the estimate wins work profitably, and they are applied and then discarded — the deliverable is a priced estimate, and the reasoning exists in the estimator's head and occasionally in a note nobody can query. The consequences are the ones this vault keeps finding: quality varies by who was assigned and nobody can measure by how much, a departing senior estimator takes the firm's capability with them, and a client challenging a number is answered from recollection.

## Why It's Still Broken
Estimating runs against bid dates where every minute is contested, so anything perceived as documentation loses to throughput. Estimating software stores quantities and prices because that is what it was built to produce; there is no structure for a judgment. And the trade regards estimating as craft — which it is — with the unexamined corollary that craft cannot be recorded, in an industry whose central identified crisis is precisely the failure to transfer tacit knowledge before it retires.

## What a Fix Looks Like
Structured capture of each judgment as it is applied, costing seconds: the factor or allowance, the reason from a controlled vocabulary grown from what estimators already write, the evidence in the drawings that prompted it, and the estimator's confidence. Once judgments carry reasons, several things follow. Consistency between estimators on comparable conditions becomes measurable, which is the quality control the firm has never had. Recurring judgment patterns become candidates for standardization, so what senior estimators do reliably becomes house method rather than personal practice. A new estimator learns from a searchable body of worked decisions instead of by sitting next to someone for three years. And when bid outcomes are captured, the judgments become evaluable — which factors improved bid positioning and which cost work — turning craft into evidence in a trade that has never had any.

## Who Feels the Pain
Estimators re-deriving judgments colleagues have already made; the chief estimator accountable for consistency across a book with no instrument; contractors receiving estimates whose assumptions they cannot see; and the firm, whose capacity is capped by senior estimator headcount and whose expertise leaves on the same demographic curve as the trade.

## Impact If Fixed
Converts the bureau's differentiator from personal expertise into institutional capital, which is what lifts both the quality ceiling and the capacity ceiling. It is also the prerequisite for everything else — outcome calibration is uninterpretable without knowing which judgments produced the estimate being scored.
