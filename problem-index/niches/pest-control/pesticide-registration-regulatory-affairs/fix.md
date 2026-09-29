# The Strategy Call Is the Product and It Lives in Four People

**Niche:** [[niches/pest-control/pesticide-registration-regulatory-affairs/profile|Pesticide Registration & Regulatory Affairs Consulting]]
**Industry:** [[industries/pest-control|Pest Control]]
**Type:** Fix (Pain Point)
**One-liner:** Clients hire the firm for the judgment of a handful of principals, none of the reasoning behind that judgment is recorded, and the profession is ageing.
**Tags:** #tacit-knowledge-ml #large-language-models #transformers #workflow-orchestration #worker-facing

## The Problem
When a registrant asks whether to fight a data requirement or accept it, the answer comes from a principal who has seen the situation before. They will explain their reasoning in a meeting, it will be summarised in three sentences of a strategy memo, and the analysis behind it — the four comparable products they were thinking of, the two agency decisions that made them confident, the reason they discounted an apparently similar precedent — will not be written down anywhere.

That reasoning is the asset. The dossier assembly work can be staffed; the strategy call is why the client pays a premium and why they chose this firm.

The exposure is straightforward. Regulatory science is an ageing profession with a thin pipeline, and the people carrying thirty years of agency experience are close to the end of their careers. When one leaves, the firm loses the reasoning and keeps the files.

The junior side of the same problem is that scientists learn this by apprenticeship — sitting in on submissions for years. That worked when engagements were long and teams stable. It transfers badly now, and it means a competent mid-level scientist cannot give advice a principal could give, even with the same files in front of them.

## Why It's Still Broken
Nobody bills for writing down reasoning. Every hour spent recording why a position was chosen is an hour not charged to a client, and the benefit lands years later on somebody else's engagement.

Recording it also feels risky. A written record of internal reasoning about a regulatory position is discoverable, and regulatory advice occasionally ends up in litigation or in an enforcement context. The safe institutional habit is to keep the memo short.

And the knowledge genuinely resists capture in the form firms have tried. Precedent libraries and lessons-learned databases get built, populated for six months, and abandoned, because they demand effort disconnected from the work in front of the person.

## What a Fix Looks Like
**Capture at the decision, not afterwards.** The moment worth recording is when a position is chosen: what was decided, what the alternatives were, what precedents were relied on, and what would change the answer. A short structured prompt attached to the strategy memo the firm already produces costs minutes, not hours.

**Let retrieval do the work.** Extract the precedent linkage from the archive rather than asking people to enter it — submissions, correspondence and agency decisions already reference the products and arguments involved. A retrieval layer over the firm's own matters that surfaces "the four most similar situations we have handled, and what happened" is useful from the first day, which is what determines whether people use it.

**Make the junior scientist the primary user.** The system succeeds if a mid-level scientist preparing a strategy recommendation gets the comparable engagements, the agency's stated reasoning on the point, and the firm's own prior positions in front of them before they ask a principal. Then the principal's time is spent on the genuinely novel question.

**Track what the principal changes.** Where a senior scientist overrides the retrieved precedent, capture the reason. That delta is precisely the tacit layer, and it is a small, high-value stream of labels that accumulates during work nobody had to schedule.

**Handle the discoverability question deliberately.** Decide with counsel what is recorded, in what form, and under what privilege posture, before building. Treating it as a reason not to record anything is the current default and it is costing more than the risk.

## Who Feels the Pain
The principals, who are the bottleneck on every engagement and cannot be in two client meetings at once; the mid-level scientists, who cannot progress without years of apprenticeship the firm can no longer supply; and the registrants, who receive a recommendation with no visible basis and cannot tell a well-founded position from a confident one.

## Impact If Fixed
The firm's core asset stops being four people's memories. A mid-level scientist gives advice closer to a principal's, principals spend their time on genuinely novel questions, and thirty years of agency experience survives a retirement — in a specialty where the experience takes thirty years to acquire and the pipeline to replace it does not exist.
