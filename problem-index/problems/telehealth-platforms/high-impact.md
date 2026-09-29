# The Visit Closes and Nobody Measures Whether the Patient Got Better

**Industry:** [[telehealth-platforms|Telehealth Platforms]]
**Type:** High Impact
**One-liner:** The metrics are visit volume, wait time and satisfaction, and the question a clinician actually needs answered — did my decision work — is asked by nobody.
**Tags:** #survival-analysis #causal-inference #gradient-boosting #bayesian-inference #confidence-intervals #evaluation-metrics #compliance #hypothesis-testing

## The Problem
A virtual visit ends with a decision: reassure, prescribe, order a test, refer, or escalate to in-person care. The visit is recorded as complete, the patient rates it, and the platform's dashboards show throughput and satisfaction.

What happened next is not measured. Did the symptom resolve. Did the patient return within a week with the same complaint, possibly to a different clinician on the same platform who cannot see the first visit clearly. Did they present at an urgent care centre or an emergency department. Was the prescription filled, and was it refilled. Did the referral happen.

Much of that is knowable. Repeat visits are in the platform's own data. Prescription fill and refill data is available through pharmacy networks. Downstream utilisation is visible in claims for insured populations and through health information exchange networks. Patient-reported outcome follow-up is a message and is almost never sent.

The consequence is that clinical decision quality is invisible at every level. The individual clinician gets no feedback and cannot calibrate — a clinician who under-refers and one who over-prescribes both see their visits close and their ratings hold. The platform cannot identify which of its clinical protocols work. And the regulator, the payer and the employer buying the service are given throughput and satisfaction in place of outcomes.

Satisfaction is an actively misleading substitute here. A patient who wanted an antibiotic and received one rates the visit highly; the same patient told they have a viral infection and should rest rates it poorly. Optimising the measured metric and optimising care point in opposite directions on exactly the decisions that matter most, and the commercial pressure runs toward the satisfying answer.

## Why It's Unsolved
Episodic care makes outcomes hard to observe. A platform sees a patient for fifteen minutes and has no visibility of the following fortnight unless the patient returns, which is precisely the population it most needs to know about.

Data access is genuinely constrained. Claims data is available to payer-contracted platforms and not to direct-to-consumer ones; exchange network participation is uneven; and pharmacy fill data requires integration and a lawful basis. None of these are impossible and all are work.

The business model does not reward it. A per-visit or subscription business is paid for the visit, and outcome measurement produces findings that may reduce visit volume — a protocol that resolves problems in one visit rather than two is worse for revenue and better for patients, and nothing in the structure favours the second.

And the findings would be uncomfortable in the segments already under scrutiny. A direct-to-consumer prescribing platform that measured what proportion of its prescriptions were clinically indicated, refilled, or followed by adverse events would generate evidence that could be subpoenaed. That is a strong disincentive to look, and it is the clearest case in this cluster of measurement being avoided because of what it would find.

## What a Solution Looks Like
Start with what is internal and free. Return-visit rates for the same complaint within defined windows, by clinician and by protocol, are computable today from platform data alone and are the single most informative available signal of whether a decision resolved the problem.

Add the obtainable external signals. Prescription fill and refill data, downstream utilisation through claims for insured populations, and referral completion are each an integration rather than a research project, and together they cover most of what matters.

Ask the patient. A short structured follow-up at three and fourteen days — did the symptom resolve, did you seek other care, did you fill the prescription — costs a message and produces outcome data no other source provides. Response will be partial and its bias is characterisable.

Separate satisfaction from appropriateness explicitly. Reporting both, and showing where they diverge, protects clinicians who make the correct unpopular decision from a metric that punishes it. Antibiotic and controlled substance prescribing rates against clinical guidelines are the obvious first instances.

Give clinicians their own outcome feedback. A clinician who learns that their prescribing pattern differs from peers on comparable presentations, or that their patients return at a higher rate, has the information to calibrate — and no clinician on these platforms currently receives any of it.

## Impact If Solved
Virtual care is expanding into conditions and decisions that were previously in-person, in a regulatory environment increasingly asking whether the model is clinically sound, and the sector's answer is throughput and satisfaction. Return-visit and fill-rate measurement is available immediately at no external cost; patient follow-up is a message; and clinician-level outcome feedback is the first quality signal this workforce has ever been given. The platform that measures resolution rather than volume can defend its model with evidence — and will find things it would rather not know, which is the whole reason it has not been done.
