# Livelihood Decisions Made by Systems That Cannot Explain Themselves

**Industry:** [[ugc-video-platforms|UGC Video Platforms]]
**Type:** High Impact
**One-liner:** A classifier removes a video, demonetises a channel or quietly reduces its distribution, and the person whose income just changed receives a policy category and no way to find out what happened.
**Tags:** #transformers #cnns #large-language-models #confidence-intervals #evaluation-metrics #bayesian-inference #compliance #worker-facing

## The Problem
Enforcement on a platform receiving hundreds of hours of video a minute must be automated. Classifiers evaluate uploads against policy — violence, hate, adult content, misinformation, advertiser suitability — and apply outcomes: removal, age restriction, demonetisation, or reduced distribution. The last is the most common and the least visible, because nothing tells the creator it happened; the video simply does not travel.

What the creator receives is a category. "Harmful or dangerous content." "Not suitable for most advertisers." Nothing states which part of the video, which moment, which phrase, or on what basis. For a video of any length this is unactionable: a creator cannot fix what they cannot locate, and the practical response across the industry is defensive self-censorship — bleeping words that may be fine, avoiding subjects that may be acceptable, adopting substitute vocabulary. An entire linguistic adaptation has emerged among creators specifically because the boundary is unknowable.

Appeals are the part that fails hardest. The queue is enormous, the reviewer sees limited context, and the outcome frequently arrives with no additional explanation. Creators describe appeals resolved within seconds of submission for videos an hour long, which does not require malice to explain — automated appeal handling is an obvious response to unmanageable volume — but it does mean the appeal is not functioning as a check.

The consequences are unevenly distributed. Established creators have partner managers and back channels; everyone else has a form. Documented false-positive patterns fall disproportionately on discussion of subjects that resemble violations without being them — journalism about violence, health and sex education, LGBTQ content, content in languages where classifier performance is weakest, and reclaimed speech within the communities it belongs to.

## Why It's Unsolved
Volume is the honest first answer. No platform can staff human review proportional to upload volume, so automation is not a choice, and an appeal process that provides individualised reasoning at that scale is a genuinely large cost centre with no revenue attached.

Explanation is also strategically fraught. A platform that states precisely which feature triggered enforcement provides a map for evading it, and adversaries — spammers, coordinated abuse operations, scam networks — read documentation. That is a real tension and it is also frequently overstated: telling a creator the decision concerned the thirty seconds beginning at 4:12 is not a circumvention manual, and platforms that provide nothing have chosen the easiest point on that trade.

Technically, many enforcement systems are ensembles whose outputs were never designed to be interpretable, and retrofitting explanation is real work. But the same organisations build models that localise and describe content precisely for other purposes, which makes this a question of where the effort was spent.

And the accountability incentives were weak until recently. The affected party is a creator with no leverage; the cost of a false positive is borne entirely by them. Regulation — the Digital Services Act's statement-of-reasons and appeal requirements above all — has begun to change that calculus from the outside.

## What a Solution Looks Like
Localise the decision. Enforcement should name the segment: which timespan, which visual or audio element, which transcript passage. This is directly achievable with the content understanding these platforms already run and it converts an unactionable notice into something a creator can address. It also makes internal error analysis possible, which is currently very hard.

Report calibrated confidence and route by it. A high-confidence detection of an unambiguous violation and a marginal advertiser-suitability judgement should not carry the same consequence or the same review path. Low-confidence decisions with significant economic impact are precisely where human review should be spent, and prioritising the appeal queue by expected error and by the size of the consequence would concentrate scarce review where it does most good.

Measure the error rate and publish it. A sampled, independently adjudicated audit of enforcement decisions gives a false-positive rate by policy category, by language and by content type. That number does not exist publicly for any major platform, and its absence is why the discussion is conducted in anecdote. Reporting it by language matters most, because that is where the disparity is largest and least examined.

Make the appeal a genuine check. An appeal reviewed by the same automated system that made the decision is not a check. Human review on appeals where the economic consequence is material, with the reviewer seeing the localised evidence, is affordable if the queue is prioritised rather than uniform.

## Impact If Solved
These decisions determine whether a large population of people can earn a living, and they are currently made by systems whose reasoning is unavailable to the person affected and whose error rate is unpublished. Localised reasons make enforcement actionable and end the defensive self-censorship that distorts what gets made. Confidence-routed appeals put human judgement where it changes outcomes. And a published, language-broken-out error rate turns a decade of anecdote into a measurable property that can be improved — which is the precondition for the regulatory obligations now arriving being met in substance rather than in form.
