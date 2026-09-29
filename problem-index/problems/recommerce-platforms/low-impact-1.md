# Condition Grading Consistency

**Industry:** [[recommerce-platforms|Recommerce Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Grading rubrics are written, trained and audited at every serious platform, and two graders looking at the same jacket still assign different grades — which propagates into price, listing and returns.
**Tags:** #cnns #semantic-segmentation #object-detection #bayesian-inference #hypothesis-testing #confidence-intervals #evaluation-metrics #worker-facing

## The Problem
Condition determines price, buyer expectation and return rate. Platforms define grades — new with tags, excellent, very good, good — with written criteria and photographic examples, and train graders against them.

Consistency remains poor. The same item graded by two people, or by the same person at different times of day, receives different grades. This is a well-documented property of human visual judgement under production quota and is not a training failure.

The consequences propagate. A generously graded item disappoints the buyer and is returned, which costs a return shipment, a reprocessing and a dissatisfied customer. A conservatively graded item is underpriced and gives away margin. Neither error is visible until much later, and neither is attributed back to the grading decision.

Grades are also coarse relative to the price differences they drive. Two items in the same band can differ by a factor of two in realised value, which means the grade is discarding the information the platform most needs.

## What Already Exists
Written rubrics with photographic references are standard. Grader training and calibration programmes exist at the larger platforms. Quality audit sampling is common. Computer vision is deployed for defect detection — stains, tears, pilling, scuffs — with genuine capability. Controlled photography setups with consistent lighting are standard in managed intake. Some platforms publish condition definitions to buyers.

## The Customisation Gap
Inconsistency is not measured properly, which means it cannot be managed. Sending the same items through multiple graders periodically produces a disagreement rate and identifies which criteria and categories are unreliable, and this costs a small fraction of intake capacity and is rarely done.

Grades are used as the output when they should be an intermediate. What matters is realised price and return rate, and those are the labels available in abundance — so condition assessment could be trained against economic outcomes rather than against a rubric, which sidesteps the human inconsistency entirely.

Continuous condition scoring rather than bands would preserve the information the grade discards. A model producing a continuous condition score per item, calibrated against realised prices, is strictly more useful than a four-band assignment.

Defect localisation is the fourth gap. Knowing that an item has a stain is coarser than knowing where it is and how visible it is, and photographs already capture that.

## Impact If Solved
Condition is the dominant price variable and the largest source of return-driving expectation mismatch, and it is assigned by human judgement under quota with unmeasured variance. Training against realised economic outcomes rather than against a rubric turns a consistency problem into a measurement one and preserves information the grading bands currently throw away.
