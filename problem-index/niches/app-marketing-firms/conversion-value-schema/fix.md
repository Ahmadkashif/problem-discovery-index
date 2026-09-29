# The Schema Set at Launch

**Niche:** [[niches/app-marketing-firms/conversion-value-schema/profile|Conversion Value Schema Design]]
**Industry:** [[industries/app-marketing-firms|App Marketing Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The conversion value schema was configured during the integration three years ago, the app's monetisation has changed twice since, and nobody has looked at it.
**Tags:** #evaluation-metrics #descriptive-statistics #entropy-cross-entropy-kl-divergence #confidence-intervals #quick-win #revenue-impact #hypothesis-testing #compliance
**Contested on:** Every serious competitor in this niche is fighting to decide what a handful of bits should encode about an early user — and whoever designs that against measured information content sets the ceiling on everything the team can ever learn.

## The Problem
The schema encodes revenue in six buckets with boundaries that made sense for the app's original pricing. Since then the app added a subscription, changed its onboarding, shifted its monetisation mix and moved into new markets with different price points. Most users now fall into the same two buckets, so the signal carries almost no information about which ones are valuable. Every prediction, every campaign comparison and every bid the team makes runs through this, and the configuration has not been examined since the week it was set.

## Why It's Still Broken
The schema is a configuration value that produces no error when it becomes uninformative — a setting that degrades silently is never revisited, which is the same pattern as the frequency cap and the ad load elsewhere in this batch. Changing it breaks comparability with historical data, which is a real cost and is used as a reason not to. Nobody owns it. And its degradation shows up as gradually worse prediction accuracy, which is attributed to the measurement environment.

## What a Fix Looks Like
Review it like a parameter that matters. Report the distribution of conversion values received, which is the fix and takes a single query — a schema where most users land in two buckets is visibly broken and nobody has looked. Compute the information the current schema carries about eventual value, so the degradation has a number rather than an impression. Schedule a review whenever monetisation changes, since that is what invalidates it and the trigger is knowable. Plan the transition properly with a period of parallel interpretation, which addresses the comparability objection rather than accepting it as a blocker. Version the schema explicitly in the data so historical analysis knows which encoding applied. Differentiate by market where price points differ substantially, since a global schema calibrated on one market's economics is wrong everywhere else. Assign ownership to the person accountable for payback, rather than leaving it with whoever integrated the measurement library. Document the rationale, since the next person will otherwise inherit a number with no explanation and repeat the cycle. Alert when the distribution collapses toward a few values, which is the automated version of the review. And report the achievable prediction accuracy under an optimised schema against the current one, because that comparison is what makes a team act.

## Who Feels the Pain
Teams bidding on predictions built from an uninformative signal; analysts whose models cannot improve because the input has no information in it; and studios whose measurement decays as their business improves.

## Impact If Fixed
A setting that degrades silently is never revisited, and a schema where most users land in two buckets is visibly broken to anyone who looks. A single distribution query exposes it, and versioning the schema removes the comparability objection that blocks every proposed change.
