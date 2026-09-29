# The Triager Reading the Two Hundredth Report

**Industry:** [[bug-bounty-platforms|Bug Bounty Platforms]]
**Type:** Worker Life Changing
**One-liner:** A skilled security analyst spends their day reading mostly invalid submissions, and the consequence of missing the one real finding is a breach.
**Tags:** #bert #transformers #gradient-boosting #k-nearest-neighbors #confidence-intervals #evaluation-metrics #worker-facing #automation

## The Problem
Triage analysts read every submission to a programme. Most are duplicates, out of scope, scanner output or misunderstandings, and each must be read carefully enough to be sure — because the cost of dismissing a real finding is not a metric, it is an incident.

The work is repetitive at volume and high-stakes at the margin, which is an unusual and tiring combination. Concentration has to be maintained across hundreds of low-value reports so that the rare significant one is recognised, and the failure mode is the one that occurs when attention has already been spent.

The interpersonal load is substantial. Researchers are frequently frustrated, believe their finding is more severe than the triager rated it, and dispute duplicate determinations. Triagers deliver those decisions and receive the response, and some of it is aggressive.

They are also caught structurally. The programme wants costs controlled and the researcher wants payment, and the triager's rating sits directly between them — with the platform's commercial interest closer to the programme.

And the work is measured on throughput and turnaround, which are the metrics that pressure the careful reading the role depends on.

## Why It Matters to the Worker
This role requires real security expertise and is structured like queue work, which is why it is a hard position to keep skilled people in. The expertise required to correctly dismiss a subtle non-issue is the same expertise that would command more elsewhere.

The asymmetry of consequences weighs. Nobody notices correct dismissals; a missed finding that becomes an incident is career-defining. That shape produces defensive escalation, which raises programme costs and is a rational response to the incentive.

And the disputes are personally directed. Researchers know the triager's name, the decision affected their income, and the response arrives accordingly. Absorbing that repeatedly, while being measured on turnaround, is the substance of the job.

## What a Solution Looks Like
Order the queue by expected validity. Report structure, researcher history in the relevant technology, evidence specificity and scope match all predict validity, and processing a well-ordered queue rather than a chronological one puts the analyst's attention where it matters — provided nothing is dropped, only ordered, since the unlikely report is occasionally the important one.

Filter at intake, politely. Unvalidated scanner output has recognisable signatures and can be returned with a request for validation rather than a rejection, which removes a large share of volume without alienating anyone.

Supply the duplicate evidence. Substance-based duplicate matching that surfaces the candidate original, with its report, turns a judgement into a comparison — which is faster, more accurate and far more defensible when disputed.

Calibrate severity against the platform's own corpus. A reference range drawn from how comparable findings were rated across thousands of programmes gives the triager a defensible starting point instead of an unsupported judgement, which is exactly what makes disputes personal.

And separate throughput from the careful cases. A metric that pressures turnaround on every report pressures it on the hard ones too, and the hard ones are the entire reason the role requires a skilled person.

## Impact If Solved
Triage is the operating cost that determines whether programmes can stay open and the role that carries the consequence of a miss. Validity-ordered queues, intake filtering and evidence-supported duplicate and severity decisions would return the analyst's attention to the small number of reports that matter — and would make the disputes about evidence rather than about a person's judgement, which is what makes this role sustainable.
