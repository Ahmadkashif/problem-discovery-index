# The Tracking That Broke and Nobody Noticed

**Niche:** [[niches/affiliate-networks/the-small-merchant-programme/profile|The Small Merchant Programme]]
**Industry:** [[industries/affiliate-networks|Affiliate Networks]]
**Type:** Fix (Pain Point)
**One-liner:** A theme update removed the conversion tag in February, the programme has recorded no sales since, and the merchant concluded affiliate does not work.
**Tags:** #change-point-detection #automation #evaluation-metrics #data-integration #quick-win #workflow-orchestration #revenue-impact #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to run a working affiliate programme for a merchant with nobody to run it — and whoever does that opens a merchant base the networks priced themselves out of.

## The Problem
Conversion tracking is a tag on the order confirmation page. A theme update, a checkout change, a consent banner, a plugin conflict or a platform migration removes or blocks it. From that moment the programme records clicks and no sales. Publishers keep sending traffic and earn nothing, and drift away. The merchant sees a channel producing no revenue and concludes it does not work. Nobody is watching, because a programme with no conversions looks exactly like a programme with no performance, and for a small merchant with no manager there is no one to tell the difference.

## Why It's Still Broken
Tracking is verified at setup and then assumed, which is the whole defect — an integration checked once and never again in an environment that changes constantly. A zero is not an error and produces no alert. Publishers assume poor performance rather than breakage and simply stop. And the merchant has no benchmark against which a zero looks wrong.

## What a Fix Looks Like
Monitor the tracking continuously. Alert when the click-to-conversion ratio breaks from its own history, which is the fix, needs only the network's existing data, and detects almost every breakage within a day. Synthesise test transactions periodically to verify the tag end to end, which catches failures that a ratio cannot and is standard practice in every other integration-dependent product. Detect the known causes — platform updates, consent banners, checkout changes — by watching for their signatures, since a handful of causes account for most incidents. Tell both the merchant and the affected publishers, because publishers who know it is broken will wait rather than leave. Provide a recovery path that credits the lost period where evidence supports it, which is what keeps publishers from abandoning the programme. Verify after any platform or theme change by integrating with the commerce platform's own change signals, which is where the breakage originates. Install through the platform rather than as a manual tag where possible, since a managed integration survives updates that a pasted snippet does not. Show a tracking health indicator in the merchant's view, so the state is visible rather than inferred. Prevent payout and reporting from presenting a broken period as genuine performance, which is how the wrong conclusion gets drawn. And report mean time to detection, because the current answer is frequently months and that single number explains a large share of small-merchant churn.

## Who Feels the Pain
Merchants who concluded the channel does not work; publishers who sent traffic for nothing and left; and networks losing merchants to a failure their own data could have caught in a day.

## Impact If Fixed
An integration verified once, in an environment that changes constantly, with a failure mode that produces a zero rather than an error. Watching the click-to-conversion ratio against its own history catches nearly every breakage within a day using data the network already has.
