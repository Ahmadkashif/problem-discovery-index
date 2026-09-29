# Build: Semantic Matching Before the Human

**Niche:** Submission Deduplication & Filtering
**Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An embedding-based pre-triage layer that finds the duplicate whatever words it used, classifies scanner output reliably, and checks scope mechanically — before any analyst reads anything.
**Tags:** #bert #word-embeddings #contrastive-learning #gradient-boosting #evaluation-metrics #confidence-intervals #automation #k-nearest-neighbors
**Contested on:** Whether the mechanical share of triage is removed before a human reads, or absorbed by analysts one submission at a time.

## The Problem

Two researchers find the same authorisation flaw a week apart. The first describes it as a broken access control on the account endpoint. The second describes it as an insecure direct object reference allowing horizontal privilege escalation. These are the same finding in different vocabulary, and a keyword search for either will not find the other.

So an analyst reads the second submission from scratch, reproduces it, assesses it, and only identifies the duplicate if they happen to recall the earlier one or search with the right term. Across a large programme this happens constantly, and the duplicate detection rate depends on the memory and search instincts of whoever is working the queue.

Scanner output has the same shape of problem. A submission consisting of a tool's output, lightly reformatted, is obvious to a human in three seconds and requires a human to spend those three seconds. Pattern-matching on tool names catches the lazy cases and misses anything edited.

Scope checking is worse: it consumes analyst attention to compare a target against a policy written in prose, which is a lookup a machine would do instantly if the policy were structured.

Together these three account for a large share of what analysts read, and none of them needs security expertise.

## Why Nobody Has Built This

**The false-negative fear dominates.** An automated screen that filters a real finding leaves a vulnerability in production. Platforms default to human review of everything, which is defensible and is also an argument for automation that assists rather than filters.

**Duplicate labelling is noisy.** Historical duplicate determinations are the obvious training signal and they contain the analysts' own misses — findings marked unique that were duplicates and vice versa. Training on them reproduces the error.

**Semantic similarity is not semantic equivalence.** Two submissions can be textually similar and describe genuinely different findings, or be textually unlike and describe the same one. The embedding has to capture the finding's identity — asset, weakness class, mechanism — rather than the prose style, which requires more than an off-the-shelf sentence encoder.

**Cross-programme signals are contractually awkward.** Detecting that a submission was also sent to nineteen other programmes is a strong signal and involves comparing one customer's submissions against another's.

**It is unglamorous infrastructure.** Platform engineering roadmaps favour visible features over queue plumbing, even where the plumbing is the margin.

## What to Build

**Embed the finding, not the prose.** A representation built from the structured aspects — target, weakness class, affected parameter or endpoint, the mechanism described, the demonstrated impact — extracted from the submission text, so matching operates on what the finding is rather than how it was written. This is the core technical choice and it determines whether the whole thing works.

**Surface candidates, never auto-close.** Ranked possible duplicates presented to the analyst with the matching evidence highlighted. The analyst confirms. This captures nearly all the time saving with none of the false-negative risk, and it is the design that platforms will actually deploy.

**Classify machine-generated output robustly.** Structural and statistical signals rather than tool-name matching — output regularity, boilerplate density, absence of a described mechanism, missing impact reasoning. Route to a lighter lane with a templated response rather than closing outright.

**Check scope mechanically.** Against the structured definition from [[niches/bug-bounty-platforms/scope-specification/profile|🎯 Scope Specification]], with the specific clause cited in the response. This is the cleanest automation in the whole industry: it is a lookup, it is unambiguous, and it currently consumes expert attention.

**Use cross-programme signals where contracts allow.** A submission sent to many programmes simultaneously is a strong prior for low-effort mass reporting. Handled as a ranking signal rather than a rejection, and abstracted so no programme's content is exposed to another.

**Measure the screen's own error rate.** Sample what the filters deprioritised and re-examine it. An automated layer whose miss rate is unknown is not safer than a human — it is differently unsafe, and unmeasured.

**Train on adjudicated labels, not raw history.** Use re-examined outcomes where available and treat the historical labels as noisy, because a model that learns the analysts' misses will confidently reproduce them.

## Target Customer

Platform engineering, where analyst-minutes per valid finding is the operational metric that matters and this is the most direct lever on it.

Programmes running self-hosted triage, who face the same mechanical load without the scale to justify building any of it.

## Impact If Built

Semantic duplicate detection is the single largest available reduction in analyst load, and the technique is commodity — this is a case where the industry has simply not applied something everyone else already uses.

Mechanical scope checking removes an entire category of expert attention spent on a lookup, and it is the automation with the least risk attached.

And surfacing duplicate candidates rather than closing them would improve researcher relations at the same time, because a duplicate identified with the matching evidence shown is a far better experience than an unexplained closure — which connects directly to the grievance in [[niches/bug-bounty-platforms/the-researcher/profile|🟣 The Researcher]].
