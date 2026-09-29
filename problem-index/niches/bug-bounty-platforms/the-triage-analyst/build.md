# Build: Support for a Consequential Judgement

**Niche:** The Triage Analyst
**Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A triage workbench that reproduces the submission, surfaces comparable prior decisions, and shows the analyst where their assessment sits relative to the market before they commit to it.
**Tags:** #bert #large-language-models #word-embeddings #gradient-boosting #evaluation-metrics #confidence-intervals #worker-facing #automation
**Contested on:** Whether the person reading the queue is supported as a specialist making consequential judgements, or measured as a throughput worker.

## The Problem

The analyst's actual task, on each submission, is a sequence of judgements: is this in scope, is it a duplicate, does it reproduce, is the described impact real, and what severity does it carry. Each is answerable with evidence. None is supported by anything.

Scope is checked by reading the policy page. Duplicates are found by keyword search that fails whenever the earlier researcher used different words. Reproduction is performed by hand, following prose instructions, setting up the request sequence manually, which is the single most repetitive part of the day. Impact is assessed from the researcher's claim and the analyst's own knowledge of the system, which for a platform analyst working across many programmes is necessarily shallow. Severity is assigned from experience with no reference to how comparable findings were rated anywhere.

So a specialist spends most of their attention on mechanical retrieval and setup, and arrives at the consequential judgement — is this real, and what is it worth — with the least support at the moment it matters most.

## Why Nobody Has Built This

**The role is treated as a cost centre.** Investment in triage is aimed at reducing cost per submission, which means throughput tooling rather than judgement support. Nothing in that framing funds a workbench.

**Automated reproduction is hard in general.** Researchers describe steps in prose with screenshots against systems the platform does not control. The general case is genuinely difficult, though the common case — a request sequence against a web application — is regular enough to attempt and would cover a large share of the queue.

**Cross-programme context is contractually delicate.** Showing an analyst how similar findings were handled at other programmes means exposing one customer's decisions to work on another's, which requires careful abstraction.

**Calibration feedback is uncomfortable.** Showing an analyst that their assessment is an outlier is useful and also a performance signal, and framing it as support rather than monitoring is a product design problem that determines adoption.

**Analysts are not the buyer.** Platform operations buys the tooling and is measured on cost and time, so features that improve judgement quality compete badly against features that improve speed — even though the expensive error is a quality failure.

## What to Build

**Execute the reproduction.** Where the submission describes a request sequence, run it in a sandbox and present the analyst with the actual request and response alongside the researcher's claim. This is the largest single time saving available and it improves accuracy at the same time, because judging an observed response is different from judging a description of one.

**Surface comparable prior decisions semantically.** Findings of the same class, in similar contexts, with how they were assessed and what they paid — abstracted across programmes where contracts allow, within the programme where they do not. Embedding-based retrieval catches the paraphrases that keyword search misses, which is where duplicate detection currently fails.

**Check scope automatically and cite the rule.** The submission evaluated against the structured scope from [[niches/bug-bounty-platforms/scope-specification/profile|🎯 Scope Specification]], with the specific clause shown. This removes an entire category of manual lookup and makes the rejection explicable to the researcher.

**Show the severity reference at the moment of assessment.** Where the analyst's proposed severity sits relative to the distribution for comparable findings, presented as information rather than correction. Most outliers are reconsidered or explained, and both outcomes improve the record.

**Route by specialism.** Match submission class to analyst strength. Analysts have genuine depth in different areas and are currently assigned by availability, which wastes expertise and produces worse judgements.

**Give the analyst a low-cost uncertainty path.** A defined escalation for genuinely borderline cases with no throughput penalty. The current structure makes uncertainty expensive to express, which pushes borderline cases toward closure — the exact mechanism that produces the expensive error.

**Provide calibration feedback privately.** Periodic, confidential comparison of the analyst's own assessments against adjudicated re-examinations and against peer distributions. Framed as development, held separately from performance management, because a calibration tool used as a performance instrument will be gamed and then ignored.

## Target Customer

Platform triage operations, where the reproduction automation pays for itself in analyst-minutes and the rest arrives alongside it.

Programme managers running self-hosted triage face the same problem with less scale and would buy a workbench outright.

The honest framing for the buyer is that this is quality tooling with a throughput side effect, rather than the reverse — and the throughput side effect is what will fund it.

## Impact If Built

Automated reproduction removes the most repetitive task in the job and improves the judgement it precedes, which is an unusual combination.

Semantic retrieval of comparable decisions gives the analyst the operation's accumulated experience at the moment of decision, rather than requiring them to have personally seen it before.

And a low-cost path for uncertainty directly addresses the structural cause of the error that matters most — an analyst who can say "I am not sure" without a penalty will say it, and today saying it is the expensive option.
