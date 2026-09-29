# Choosing What the Bits Mean

**Niche:** [[niches/app-marketing-firms/conversion-value-schema/profile|Conversion Value Schema Design]]
**Industry:** [[industries/app-marketing-firms|App Marketing Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A handful of bits must encode whatever the team most needs to know about an early user, and the choice determines what every downstream model can ever learn.
**Tags:** #entropy-cross-entropy-kl-divergence #mutual-information #evaluation-metrics #confidence-intervals #optimization-fundamentals #bayesian-inference #revenue-impact #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to decide what a handful of bits should encode about an early user — and whoever designs that against measured information content sets the ceiling on everything the team can ever learn.

## The Problem
The team must decide what a small integer means. Revenue in buckets, with boundaries they choose. Or a count of a key event. Or a flag combination indicating retention and purchase. Whatever they choose is the only thing they will ever know about an early user's behaviour on that platform. It determines the achievable accuracy of every prediction, the resolution of every campaign comparison, and the ceiling on every optimisation for years. In most organisations this was decided in an afternoon during integration, using a template, by someone who was not the person who would later be held to the payback numbers.

## Why Nobody Has Built This
The decision arrived as a configuration step inside an integration, which framed a strategic information design choice as setup — and a setup step gets setup-level attention. Evaluating a schema requires simulating what could have been learned under alternatives, which nobody has tooling for. Changing it later loses comparability with historical data, which makes revision feel costly. And vendors supply templates, which makes accepting one the default.

## What to Build
Design the schema as an optimisation. Measure how much information each candidate schema carries about eventual value, using the app's own historical user-level data from before the constraint or from the platform where it does not apply — this is the core, is computable, and is what turns a template choice into a designed one. Optimise the bucket boundaries rather than inheriting round numbers, since the boundaries determine the resolution where it matters and evenly spaced revenue buckets are almost never optimal for a skewed distribution. Design for the decision, since the schema should maximise information about the quantity actually used for bidding rather than about revenue in the abstract. Simulate prediction accuracy under each candidate, which is the direct comparison and the most persuasive output. Account for the delay and suppression structure, because a schema that encodes a later event loses more to the timing rules. Support deliberate revision with a comparability plan, so a better schema is adoptable rather than blocked by the loss of history. Differentiate by app type, as a subscription app, a game and a commerce app have entirely different early signals and the templates are generic. Re-evaluate as the app's monetisation changes, since a schema designed for the launch economics decays. Provide the analysis as a product, because most teams cannot do this and it is a one-off engagement with a large durable effect. And report the information the current schema is leaving on the table, which is the number that gets the decision revisited.

## Target Customer
User acquisition and data teams, mobile measurement vendors supplying templates, and the studios whose measurement ceiling was set in an afternoon.

## Impact If Built
A strategic information design choice arrived framed as a configuration step and got setup-level attention. Measuring information content against eventual value, and optimising bucket boundaries for a skewed distribution, turns a template into a designed instrument.
