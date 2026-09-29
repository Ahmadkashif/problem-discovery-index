# Two Technicians Grade the Same Swatch Differently and Nothing Notices

**Niche:** [[niches/alterations-tailoring/softlines-testing-labs/profile|Softlines Testing & Quality Assurance Labs]]
**Industry:** [[industries/alterations-tailoring|Alterations & Tailoring]]
**Type:** Fix (Pain Point)
**One-liner:** A large share of the tests that gate a shipment are graded by eye against a reference scale, and the lab does not measure its own agreement.
**Tags:** #evaluation-metrics #hypothesis-testing #tacit-knowledge-ml #worker-facing #automation

## The Problem
Much of softlines testing is instrumental and reproducible. A meaningful share is not. Colourfastness is graded against grey scales by a technician under controlled lighting. Pilling is rated against photographic standards. Appearance after laundering, seam appearance, surface distortion and hand are assessed by trained judgment.

Those subjective grades sit on the same pass/fail line as the instrumental ones. A grade of four passes and a grade of three-four fails, and the shipment moves or it does not.

Inter-rater variation on visual textile assessment is a known and studied phenomenon; the reference scales exist precisely because unaided judgment varies. What labs generally do not do is measure their own. Technicians are trained and qualified, which tests knowledge of the method rather than agreement with colleagues on real specimens.

So the variance is invisible and it propagates. A brand comparing results across two of the lab's sites, or across years, is comparing graders. A supplier who fails at one site and passes at another has a dispute nobody can adjudicate on evidence. And the failure archive — the corpus the predictive work above would be fitted on — carries grader noise as if it were fabric behaviour.

The same silence covers the technicians' own knowledge. Experienced graders know which fabric constructions are hard to grade, which finishes mislead, and where the scale is least reliable. None of it is recorded.

## Why It's Still Broken
Throughput is the operating metric. Round-robin exercises and duplicate grading consume capacity that is already committed to a turnaround commitment.

Accreditation regimes require proficiency testing and inter-laboratory comparison, and labs treat satisfying those as the answer to the question. They demonstrate competence periodically; they do not measure routine agreement continuously.

And publishing internal variance is uncomfortable in a business whose entire product is the reliability of a judgment.

## What a Fix Looks Like
**Duplicate-grade a rolling sample.** A small percentage of subjective assessments routed to a second technician, continuously. That single change turns agreement from an assumption into a measured statistic.

**Report agreement by method, site and grader.** Where agreement is weak, the response is targeted calibration rather than general retraining, and the lab learns which methods genuinely need instrumental replacement.

**Treat borderline grades as a distinct outcome.** A result at the pass boundary carries more risk than one well inside it, and the report currently says only pass or fail. Flagging boundary results to the brand is more honest and more useful.

**Capture grading difficulty.** A one-tap note that a specimen was hard to grade, with the reason, builds the record of where the scale performs badly — the knowledge that currently retires with senior technicians.

**Use imaging where the scale allows.** For pilling and colour change, calibrated image capture and instrumental comparison exist and are underused, and the duplicate-grading data is what identifies where they are worth deploying.

**Feed calibration into the archive.** Historical grades from a period of measured drift should be weighted accordingly when the failure model is fitted, rather than treated as ground truth.

## Who Feels the Pain
Brands making shipment decisions on a boundary grade they cannot interrogate; suppliers failing at one site and passing at another with no way to contest it; technicians whose judgment carries a shipment and is never calibrated; and the lab, whose product is trust in a grade whose reproducibility it has not measured.

## Impact If Fixed
Subjective grading sits on the gate for a large share of global apparel shipments, and the lab's own agreement rate is unknown. Measuring it makes the pass/fail line defensible when disputed, directs instrumentation where it actually pays, and cleans the failure archive that every predictive use of this data depends on.
