# Item Writers Know Why a Question Works and Record a Difficulty Number

**Niche:** [[niches/k12-private-schools/admission-testing-organizations/profile|Admission Testing Organizations]]
**Industry:** [[industries/k12-private-schools|K-12 Private Schools]]
**Type:** Fix (Pain Point)
**One-liner:** Experienced item writers can predict how a question will behave before it is field tested, and the organization stores only how it behaved.
**Tags:** #tacit-knowledge-ml #text-classification #evaluation-metrics #worker-facing #transfer-learning

## The Problem
An experienced item writer knows things that do not appear in any item's metadata. That a particular distractor is attractive to students who made a specific reasoning error, and that is why the item discriminates. That this passage's vocabulary will make the item harder for students from certain backgrounds without measuring anything the test intends. That a question phrased one way tests recall and phrased another way tests application. That items in a certain format tend to come back from field testing weaker than they look.

The item bank stores the item, its content codes, and its calibrated parameters after field testing. The writer's model of why the item works is not stored, and neither is the reasoning of the review committee that accepted or rejected it.

So a new writer learns by writing items and watching them fail field testing, which is the slowest and most expensive feedback loop available. And the accumulated craft of the writers who have done it for twenty years exists only in them.

## Why It's Still Broken
Psychometrics has an authoritative empirical answer — the calibrated parameters — and the profession trusts it, correctly. Because the empirical answer arrives eventually, the writer's prior reasoning has felt redundant.

It is not redundant, it is early. The parameters arrive after the expensive step; the writer's judgment is available before it, and the whole cost problem is in between.

Item review is also a committee process producing an accept, reject, or revise decision. The discussion is where the knowledge is, and the record is the outcome.

## What a Fix Looks Like
Capture the writer's and reviewer's model alongside the item.

**Predicted parameters, recorded before field testing.** The writer's expected difficulty and discrimination, entered as part of submission. This costs nothing, and comparing predictions to outcomes tells the organization which writers are well calibrated and on what — a training signal nobody currently has.

**Structured item design rationale.** What the item is intended to measure, what each distractor represents, and what the writer expects to make it hard. Distractor rationale in particular is the core of the craft and is written down nowhere.

**Review reasoning attached to the item.** Why a committee revised or rejected it, in typed categories. The rejected items and their reasons are as instructive as the accepted ones and are currently discarded.

**Feed it back at the point of writing.** A writer working on a slot should see comparable prior items, their predicted and actual parameters, and the review notes on similar attempts. That is how craft transfers in a year instead of five.

**Use it as training data.** Item text with design rationale, predicted parameters, and observed outcomes is exactly the corpus needed to build the difficulty prediction that would transform the development pipeline — and it only exists if the rationale is captured.

## Who Feels the Pain
New item writers, learning through field test failures. Senior writers, who are the organization's capability and cannot be scaled. Development managers, whose pipeline cost is driven by items that never survive. And the test itself, whose security depends on how fast good items can be produced.

## Impact If Fixed
Item writing craft is the organization's scarcest input and its least documented. Capturing prediction and rationale compresses the apprenticeship, improves first-pass survival rates directly, and builds the labelled corpus that everything else in this niche depends on — from work writers are already doing.
