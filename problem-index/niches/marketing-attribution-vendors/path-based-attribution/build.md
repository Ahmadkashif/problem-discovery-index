# Assigning Credit Along a Journey You Cannot See

**Niche:** [[niches/marketing-attribution-vendors/path-based-attribution/profile|Path-Based Attribution]]
**Industry:** [[industries/marketing-attribution-vendors|Marketing Attribution Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Multi-touch attribution divides credit along the touchpoints it can observe, and the share of the journey it can observe has been collapsing for years.
**Tags:** #graph-theory #bayesian-inference #confidence-intervals #causal-inference #evaluation-metrics #hypothesis-testing #expectation-maximization #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to say something defensible about journeys that are now mostly unobservable — and whoever handles the missing paths honestly replaces a method that survives on familiarity.

## The Problem
A conversion is recorded with three observed touchpoints. The actual journey included a social impression on a device the system cannot link, a search on a browser that blocks the identifier, a recommendation from a friend, and a display impression the platform reported only in aggregate. The model divides credit among the three it saw, as though they were the journey. The result is not an approximation of the truth with some noise; it is a systematically distorted picture in which observable channels are credited for the influence of unobservable ones, and the distortion has grown every year as identity has fragmented.

## Why Nobody Has Built This
The method was built when paths were mostly observable and its assumptions were never revisited as that changed — a model whose premise erodes gradually keeps producing output and is trusted long past the point it should be. Representing the unobserved portion means admitting how much is missing, which makes the product look weaker. Clients ask for path reports because they are intuitive. And the alternative requires the aggregate methods the same vendors often disparage.

## What to Build
Model the missing journey rather than ignoring it. Estimate observability explicitly — what share of journeys and touchpoints are visible, by channel, device and audience — which is the foundation and is a number no vendor currently reports despite being computable. Treat the unobserved touchpoints as missing data with a mechanism rather than as absent, since they are missing in a way that correlates strongly with channel, which is the specific reason the distortion is systematic rather than random. Impute where imputation is defensible and report bounds where it is not, which is the honest output of a method operating on a majority-missing path. Calibrate against aggregate methods and experiments, since the aggregate captures what the path cannot see and the two are complementary rather than competing. Distinguish influence from presence, because a touchpoint appearing near a conversion is not evidence of causing it and the method's original weakness has never been addressed. Report credit with uncertainty that reflects the observability, so a channel whose paths are largely visible and one whose paths are largely not are not presented identically. Use the method where it is strong — within-session and within-platform journeys — and say where it is not. Flag conversions whose paths are too incomplete to attribute rather than attributing them anyway. Publish the observability rate to clients, since it is the single most important disclosure this method can make. And validate against experiments, because a method built on eroding assumptions needs external checking more than any other.

## Target Customer
Measurement vendors with path-based products, client analytics teams, and the advertisers whose channel reporting is distorted by what cannot be seen.

## Impact If Built
A model whose premise erodes gradually keeps producing output and is trusted past the point it should be, crediting observable channels for the influence of unobservable ones. Treating unobserved touchpoints as missing-not-at-random is what makes the distortion addressable rather than invisible.
