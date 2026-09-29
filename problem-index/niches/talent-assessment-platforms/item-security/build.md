# Build: Exposure Detection and Economical Rotation

**Niche:** [[niches/talent-assessment-platforms/item-security/profile|Item Security & Content Leakage]]
**Industry:** [[industries/talent-assessment-platforms|Talent Assessment Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Detect an item's exposure from its own drifting statistics and from the public channels where it circulates, and retire it before it stops measuring anything.
**Tags:** #change-point-detection #maximum-likelihood-estimation #hypothesis-testing #confidence-intervals #evaluation-metrics #large-language-models #automation #bayesian-inference
**Contested on:** Whether exposure can be detected early enough to retire an item before it degrades the score.

## The Problem

An item is developed, calibrated, deployed and leaked. After the leak it behaves differently: more candidates answer correctly, the correct answers cluster among those who prepared rather than those with the underlying ability, and its discrimination — how well it separates high from low ability — falls.

None of that is watched. The item continues in the pool, contributing a score component that measures preparation. Aggregate scores drift upward, which reads as a stronger applicant pool. The instrument's validity, established before the leak, is quietly no longer the instrument's validity.

Both detection channels are available. The statistical channel is in the response data the platform already collects. The public channel is forums, coaching sites and video platforms, which are indexed and searchable.

## Why Nobody Has Built This

Item security has been treated as a legal and proctoring problem — pursue the sites, watch the candidate — rather than as a measurement problem, and the measurement response is not in the category's repertoire.

Continuous recalibration is also not how item banks are maintained. Items are calibrated once, at development, and treated as having fixed parameters, which is an assumption that leakage violates.

And the answer to a detected leak is retirement, which costs a calibrated item and requires a replacement that takes months to produce — so detecting more leaks means needing more items, which is why nobody wants to look too hard.

## What to Build

Two detection channels and a rotation economics that supports acting on them.

**Recalibrate continuously.** Item parameters estimated on a rolling window, with change-point detection on difficulty and discrimination. A leaked item's difficulty falls and its discrimination falls further — a distinctive signature, and one that distinguishes leakage from a genuine shift in applicant ability, which moves all items together.

**Monitor the public channels.** Forums, coaching sites, question banks and video walkthroughs, searched for items matched semantically rather than by exact string, since leaked items circulate paraphrased. This is a retrieval and matching task that is now routine and that essentially nobody does systematically.

**Seed detectably.** Variant items distributed to small candidate subsets allow a leak to be traced to a channel and sometimes to a time window, which tells the content team where the exposure is coming from and is far more actionable than knowing that it happened.

**Retire on evidence, automatically.** An item crossing an exposure threshold is removed from the pool without a meeting. The value of a leaked item is negative — it adds noise and measures the wrong thing — so retirement should be the default rather than a decision.

**Make replacement economical.** Generative drafting produces candidate replacements quickly; the calibration remains the cost. Seeding new items at low exposure alongside operational items lets them calibrate during live administration, which is standard practice in high-stakes testing and rare here.

**Report exposure to clients.** An employer should know what proportion of the items their candidates saw are compromised, because it bears directly on whether the score means anything. This is uncomfortable and it is the information they are entitled to.

## Target Customer

The established test publishers, whose instruments are the most exposed and whose validity claims depend on integrity. Also employers in high-volume hiring, where exposure is highest and the score is most consequential, and the coaching industry's existence is itself the evidence of the market size.

## Impact If Built

Leaked items get detected from their own statistics and from the channels where they circulate, and retired before they degrade the score. Replacement becomes economical enough that rotation is continuous rather than occasional. And an employer can be told how much of the instrument they are relying on is still measuring what it claims.
