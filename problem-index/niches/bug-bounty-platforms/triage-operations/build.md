# Build: Triage by Expected Value

**Niche:** Triage Operations
**Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A triage layer that predicts validity before a human reads, orders the queue by expected value, and executes the researcher's reproduction steps automatically.
**Tags:** #gradient-boosting #bert #large-language-models #word-embeddings #evaluation-metrics #confidence-intervals #automation #workflow-orchestration
**Contested on:** Whether a qualified analyst's attention is spent on submissions that might be real, or spread evenly across a queue that is mostly not.

## The Problem

An analyst opens a queue. The submissions arrive in roughly the order they were received. Most are not real: a scanner's output pasted in, a description of intended behaviour presented as a flaw, a finding on an asset that was never in scope, the fourth report this week of the same missing header.

The analyst reads each one, because the only way to know which category a submission belongs to is to read it, and the cost of skipping the one real finding is a vulnerability left in production. So the most expensive and scarcest resource in the operation — someone who could be doing security research — is applied uniformly to a queue whose information content is concentrated in a small minority of items.

Every signal that would let the queue be ordered better exists. The submitting researcher's history of validity across every programme they have ever worked. The textual character of scanner output, which is highly distinctive. Whether the target is in scope, which is mechanically checkable. Whether a near-identical submission exists. Whether the described behaviour matches known intended functionality. None of it is combined into a prediction, so the tenth-percentile submission and the ninetieth arrive looking identical.

## Why Nobody Has Built This

**Automated dismissal is the feared failure.** A model that closes a submission as invalid, wrongly, leaves a real vulnerability in production and burns a researcher who was right. The asymmetry is severe enough that platforms default to reading everything, which is defensible and expensive.

**Reputation is already used and is a blunt instrument.** Queue ordering by researcher reputation exists and entrenches incumbents — a capable newcomer sits behind an established name regardless of the submission's content. Any prediction must weight the submission itself heavily or it becomes a reputation system with extra steps.

**Adversarial by construction.** Researchers who learn that certain phrasing improves queue position will adopt it. The model operates on text written by sophisticated people who will infer its behaviour, which rules out naive text features.

**The training signal is contaminated.** Historical triage outcomes are the obvious labels and they contain the analysts' own errors, including the real findings wrongly closed. A model trained on them learns to reproduce those errors, which is the same failure mode that afflicts every system trained on its predecessor's judgements.

**Reproduction automation is genuinely hard.** Researchers describe steps in prose with screenshots. Turning that into something executable is difficult in general, though a large share of web findings follow patterns regular enough to attempt.

## What to Build

**Predict validity, never act on it alone.** A probability per submission from researcher history, submission text character, scope check, duplicate proximity and target characteristics — used to order the queue and allocate depth, not to close anything. Every submission is still read; the difference is what the analyst reads first and how much time they bring to it.

**Detect scanner output explicitly.** The most confidently separable category. Tool-generated text has strong signatures, and identifying it lets those submissions go to a lighter-weight lane with a templated response, which is a large slice of the queue removed from expensive attention.

**Make duplicate detection semantic.** Embedding-based matching over prior submissions, so the same finding described in different words is caught. Keyword search fails precisely where the researcher used different vocabulary, which is most of the time, and semantic matching is a solved technique waiting to be applied.

**Execute the reproduction.** Where the submission describes a request sequence, run it in a sandboxed environment and show the analyst the actual response alongside the researcher's claim. For the large class of web findings with clear steps this converts a ten-minute manual reproduction into a glance, and it is the largest single time saving available.

**Route by specialism.** Analysts have depth in different areas. Matching submission class to analyst strength improves both speed and accuracy, and no platform does more than coarse queue assignment.

**Measure the expensive error.** Periodically re-examine a sample of submissions closed as invalid, with a second analyst, blind to the original decision. The rate of real findings wrongly closed is the most important quality metric in the operation and is currently unknown at every platform. Publishing it internally would change how triage is managed.

**Train carefully on contaminated labels.** Use adjudicated re-examinations rather than raw historical outcomes wherever possible, and treat the contamination as a known property rather than ignoring it.

## Target Customer

The platforms, where triage is the dominant operational cost and any reduction in analyst-minutes per valid finding is direct margin.

Programme managers running self-hosted programmes, who carry the same burden without the platform's scale and are the reason many organisations never open a public programme.

## Impact If Built

Analyst attention concentrates where findings are. The queue's information is concentrated and the effort is uniform, which is the central inefficiency and is fixable with signals the platform already holds.

Automated reproduction would remove the single most repetitive task in triage and would improve accuracy at the same time, since an analyst looking at an actual response judges better than one reading a description.

And measuring the rate of real findings wrongly closed would name the error that matters most — the one that leaves a vulnerability live and drives good researchers away — which no operation in this industry currently tracks.
