# Fix: Four Contacts a Month Decide a Career

**Niche:** [[niches/digital-bpo-operations/quality-and-resolution/profile|Quality & Resolution Measurement]]
**Industry:** [[industries/digital-bpo-operations|Digital BPO Operations]]
**Type:** Fix (Pain Point)
**One-liner:** Four contacts per agent per month, scored against a rubric that rewards saying the greeting, and those scores decide coaching, bonuses and sometimes employment.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #cross-validation #worker-facing #quick-win #compliance
**Contested on:** Whether a score built on four observations will be treated as the noisy estimate it is.

## The Problem

An agent handles several hundred contacts a month. Four of them are selected, listened to by a quality analyst, and scored against a rubric. The average of those four scores becomes the agent's quality score, and it determines their coaching, their bonus and sometimes whether they keep the job.

The statistical problem is severe and obvious. Four observations from a highly variable population produce an estimate whose confidence interval is wide enough to span most of the score range. An agent scoring 82 and one scoring 91 are frequently indistinguishable, and month-to-month movement in an individual's score is mostly which four contacts were drawn.

Agents know this. They describe the quality score as a lottery, which corrodes the coaching it is supposed to support — advice based on a number people believe is random is not taken seriously.

Compounding it, the rubric weights what is verifiable: the greeting, the disclosure, the closing phrase, the hold procedure. Those things are checkable and are not the substance of whether the customer was helped.

## Why It's Still Broken

Sampling at two percent is what a human-analyst quality function can afford. The rate was set by analyst capacity and then became the standard, and the standard outlived the constraint that produced it.

The rubric's composition has the same origin: it scores what an analyst can verify consistently, and consistency between analysts is the metric the quality function is itself held to. A rubric weighted toward problem-solving would have lower inter-analyst agreement, which looks like a worse rubric by the function's own measure.

And nobody has reported the uncertainty. A quality score presented as 86 looks like a measurement; presented as 86 with an interval spanning 70 to 95, it would be used entirely differently.

## What a Fix Looks Like

Report the uncertainty, fix the rubric weights, and stop attaching consequences to four observations.

**Publish the confidence interval on every agent quality score.** It is a standard error over the sampled scores and it takes an afternoon. Once leadership sees that most agents' intervals overlap, the use of these scores for ranking and bonus allocation becomes visibly indefensible, which is the point.

**Do not attach individual consequences to a four-contact sample.** Use it for coaching conversations, which is what it can support, and suspend its use for bonus and employment decisions until the coverage supports it. This is a policy change and it costs nothing.

**Aggregate over longer windows for individual decisions.** Twelve contacts over a quarter is still thin and is three times better than four over a month, and it is free.

**Reweight the rubric toward substance.** Problem identification, solution appropriateness, commitment made and recorded, and whether the customer's stated issue was addressed should dominate; greeting and closing phrases should be a small compliance component. Accept the lower inter-analyst agreement this produces and measure it honestly rather than optimising the rubric for the convenience of scoring it.

**Measure analyst agreement and report it.** Route a standing sample to two analysts blind. If agreement is poor on the substantive items, the rubric needs work; if it is poor on everything, the score means nothing regardless of sample size. No quality function in this industry publishes this number.

**Then raise the coverage**, which is the build in this niche — and note that even before any automated scoring exists, the three fixes above cost nothing and remove most of the injustice.

## Who Feels the Pain

Agents, whose pay and employment turn on four draws from a noisy distribution, and who know it and say so. Quality analysts, who deliver coaching from a number they can see is unreliable. Team leaders, managing on the basis of it. And the BPO, whose entire quality apparatus rests on a sample size chosen by analyst headcount in a previous decade.

## Impact If Fixed

The score gets reported with the uncertainty it actually carries, which immediately changes how it can be used. Consequences stop attaching to four observations. The rubric starts weighting the substance of the contact rather than the phrases that were easy to verify. And coaching becomes credible, because it rests on something the agent does not believe is a lottery.
