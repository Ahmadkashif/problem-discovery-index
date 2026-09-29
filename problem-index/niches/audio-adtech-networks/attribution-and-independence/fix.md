# The Error Rate Nobody Publishes

**Niche:** [[niches/audio-adtech-networks/attribution-and-independence/profile|Attribution & Independence]]
**Industry:** [[industries/audio-adtech-networks|Audio Adtech Networks]]
**Type:** Fix (Pain Point)
**One-liner:** The attribution method has known failure modes that every practitioner can list, and no vendor has ever published how often it is wrong.
**Tags:** #confidence-intervals #evaluation-metrics #hypothesis-testing #compliance #quick-win #descriptive-statistics #bayesian-inference #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to establish that hearing an advertisement caused something, credibly enough to be believed by a buyer — and whoever does that from a position the sellers do not own becomes the channel's only referee.

## The Problem
Ask any practitioner about household IP attribution and they will list the failure modes without hesitation: shared addresses, carrier translation, virtual private networks, rotation, listeners who convert on another network. Ask how often each of these causes a wrong answer and nobody knows, because no vendor has published it and no advertiser has required it. The method's limitations are common knowledge and its error magnitude is unknown, which is the worst of both positions — everyone discounts the numbers by an amount they invent, and the discount varies by whoever is in the room.

## Why It's Still Broken
Publishing an error rate would be unilateral and would make the publisher's numbers look worse than a competitor's silence, which is the same first-mover problem as elsewhere in this cluster — silence is a dominant strategy while no norm exists. Estimating the rate requires a validation exercise with seeded tests and advertiser data. Advertisers have not asked. And the informal discount lets everyone proceed.

## What a Fix Looks Like
Estimate it and publish it. Run a validation with seeded conversions and advertiser-confirmed outcomes on a sample, which is the fix, is achievable at modest cost, and produces the first real number the channel has ever had about its own method. Report false positive and false negative rates separately, since they have opposite consequences and a single accuracy figure hides which way the channel is being mismeasured. Estimate the rates by segment — address type, network, device mix — because the failure modes are concentrated and an average conceals where the method works and where it does not. Publish the methodology, so the number can be scrutinised and improved rather than merely asserted. Adjust reported attribution for the estimated rates, which turns a disclosure into a better number. Have an industry body sponsor the validation, which resolves the first-mover problem by making publication simultaneous. Require disclosure as a condition of buying, which is within any large advertiser's power and has never been exercised. Re-estimate as the network environment changes, since the failure modes are worsening with address rotation and privacy features. Compare against incrementality results where both exist, which is the external check. And report what share of the channel's claimed performance survives the correction, because that figure is the honest state of audio advertising's commercial case.

## Who Feels the Pain
Advertisers discounting by invented amounts; publishers whose genuinely effective inventory is discounted along with everyone's; and a channel that cannot demonstrate its own value because it never measured its own instrument.

## Impact If Fixed
Silence is a dominant strategy while no norm exists, so everyone discounts by an amount they invent. A seeded validation on a sample produces the first real number the channel has had about its own method, and an industry-sponsored version makes publication simultaneous and therefore safe.
