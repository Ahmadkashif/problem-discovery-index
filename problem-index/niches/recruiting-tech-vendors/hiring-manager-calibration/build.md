# Build: Criteria Inferred From Decisions Rather Than Asked For

**Niche:** [[niches/recruiting-tech-vendors/hiring-manager-calibration/profile|Hiring Manager Feedback & Calibration]]
**Industry:** [[industries/recruiting-tech-vendors|Recruiting Tech Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Infer what a hiring manager actually wants from which candidates they advance and reject, and show them the inference so they can correct it.
**Tags:** #bayesian-inference #gradient-boosting #large-language-models #confidence-intervals #evaluation-metrics #word-embeddings #tacit-knowledge-ml #worker-facing
**Contested on:** Whether a manager's tacit criteria can be recovered from a dozen decisions.

## The Problem

Hundreds of applications per role, hiring managers who will not give feedback, and a metric that measures how fast the requisition closed rather than whether the hire was right.

The feedback failure is the operative one. A manager rejects a candidate because of something they could articulate if asked properly — the candidate has never worked at this scale, the writing sample was weak, they want someone who has done the migration rather than managed people who did. Instead they click reject, or write "not a fit", and the recruiter learns nothing.

The information exists in the decisions. Six rejections and one advance, across candidates who differ in specific ways, is a preference revealed. Recovering it requires comparing the advanced to the rejected on the dimensions that distinguish them, which is a well-posed inference on a small sample.

## Why Nobody Has Built This

Asking managers for feedback is the obvious approach, has been the approach for decades, and does not work — managers are busy, feedback is unrewarded, and the form is one more thing between them and their actual job.

Inferring from decisions was not feasible cheaply. Comparing resumes along the dimensions that distinguish an advance from a rejection requires reading them and reasoning about differences, which is a recent capability.

And the recruiting function's metrics do not point here. Time to fill and requisition load are measured; whether the recruiter understands the manager's criteria is not.

## What to Build

An inference layer over the manager's own decisions, presented for correction.

**Compare advanced to rejected on the dimensions that differ.** For each decision, extract structured attributes from the application — scale of prior work, industry, specific technologies, depth versus breadth, individual contribution versus management, career trajectory, seniority signals — and find which of them separate the advanced from the rejected. With a dozen decisions this is a small-sample inference and it is informative well before it is conclusive.

**State it back as a hypothesis, not a conclusion.** "It looks like you are prioritising candidates who have operated at this scale and are less concerned about industry background — is that right?" A manager reading that will correct it in one sentence, and that one sentence is the criteria elicitation that the intake meeting failed to produce.

**Update continuously.** Each decision refines the estimate, and the recruiter sees the current picture rather than waiting for a calibration meeting. Confidence should be shown, since after four decisions the inference is weak and saying so prevents the recruiter from over-adjusting.

**Detect divergence from the job description.** Where the inferred criteria and the published requirements disagree, flag it. This is the common case, it is the direct cause of wasted screening on both sides, and it is invisible today.

**Make the ask cheap where you do ask.** When a manager rejects, offer two or three specific options derived from the candidate rather than a generic dropdown: "closer to the scale you wanted but weaker on the migration experience?" One click, informative, and far more likely to be answered than a text box.

**Feed it into the screen.** The inferred criteria become the screening criteria, which is the point — the recruiter stops screening against a job description nobody is using and starts screening against what the manager has revealed.

## Target Customer

Recruiting leadership at organisations where manager feedback is the named bottleneck, which is most of them. Also ATS vendors, for whom this is a genuine intelligence feature over data they already hold, and where the alternative features in this category are matching claims they cannot support.

## Impact If Built

The criteria a manager actually holds get recovered from their decisions rather than requested in a form they will not complete. Divergence between the job description and the real requirements becomes visible in week two rather than month three. And the recruiter stops guessing, which is the single largest source of wasted effort in the function.
