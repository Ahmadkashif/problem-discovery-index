# Buy: Adjudication Practice From Clinical Trials

**Niche:** Precision Verification
**Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Clinical research established how to reach consistent verdicts on ambiguous events across many sites, and security operations records a disposition dropdown under time pressure.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #bayesian-inference #expectation-variance-covariance #compliance #data-integration
**Contested on:** Whether, when an indicator fires, anyone can establish that the activity it flagged was genuinely malicious.

## The Problem

Deciding whether an ambiguous event counts as the thing being studied, consistently, across many sites and many assessors, is the adjudication problem — and clinical research solved it because trial outcomes depend on it.

The solution is a defined apparatus. Endpoint definitions specified in advance with explicit criteria. An independent adjudication committee that reviews ambiguous cases blinded to treatment assignment. Source documentation requirements so a verdict can be re-examined. Inter-rater reliability measured and reported. And a protocol that says what happens when the evidence is insufficient to decide.

Security operations has a dropdown. An analyst under a queue pressure selects true positive, false positive or benign, against definitions that vary by organisation and frequently by analyst, with no adjudication of hard cases, no reliability measurement and no protocol for the unresolved.

The data produced is the ground truth on which any precision measurement must rest, and it is generated under conditions clinical research specifically designed its apparatus to avoid.

## What Already Exists

Clinical adjudication: endpoint definitions, independent adjudication committees, blinded review, source data verification, and reporting standards for how events were classified.

Reliability measurement: kappa statistics and inter-rater agreement reporting as standard practice in any study relying on human classification.

Annotation quality: the machine learning labelling world, with gold-standard injection, multi-annotator agreement and adjudication workflow — the same apparatus in a commercial setting.

Security operations: case management platforms with disposition fields, and the detection engineering practice that has begun measuring rule precision.

Incident classification: some maturity in incident severity taxonomies, applied to incidents rather than to the far larger population of alerts.

## The Customization Gap

**No endpoint definition.** Clinical trials define precisely what counts as the outcome. Security has no shared definition of what makes an alert a true positive, and the ambiguity is not at the margins — an indicator matching a connection to infrastructure that was once malicious and is now a legitimate host is genuinely contestable.

**No adjudication of hard cases.** Every ambiguous alert is decided by whichever analyst picked it up, under time pressure, with no route to a second opinion. A standing adjudication process for contested dispositions would improve both the data and the analyst's position.

**Reliability is never measured.** Nobody knows how consistently two analysts would classify the same alert, which means nobody knows how noisy the ground truth is. Double-classifying a sample would answer it and is done nowhere.

**Volume and latency are inverted.** Clinical adjudication handles hundreds of events over months. Security handles thousands of alerts a week with same-day expectations, so the apparatus has to be lighter — sampling rather than reviewing everything.

**The unresolved case has no protocol.** Many alerts close without a firm conclusion. Clinical practice specifies how insufficient evidence is handled; security defaults to whatever closes the ticket, which systematically biases the resulting precision estimate.

**Gold standards are the cheap import.** Seeding known-disposition alerts into the queue would give continuous calibration data for individual analysts, exactly as annotation platforms do, and no security operation does it.

## Target Customer

Security operations leadership at organisations large enough to run a quality programme, for whom disposition reliability affects everything downstream — detection tuning, feed evaluation and reporting.

Case management and detection platform vendors, who could ship a disposition taxonomy, an adjudication workflow and a reliability measurement as features.

Vendors and independent evaluators building precision measurements, who need the ground truth to be less noisy than it currently is and have the strongest interest in improving it.

## Impact If Solved

The ground truth underlying every precision claim becomes measurably reliable rather than assumed, which is the precondition for the measurement being believed.

Gold-standard seeding is cheap, borrowed directly from annotation practice, and would give both analyst calibration and an estimate of disposition noise.

And a protocol for unresolved alerts would remove the systematic bias that currently determines the answer — because how the ambiguous majority is treated is what any precision figure mostly measures.
