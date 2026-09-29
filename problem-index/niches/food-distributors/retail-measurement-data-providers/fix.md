# The Foodservice Channel Is Invisible and Sold as Though It Were Not

**Niche:** [[niches/food-distributors/retail-measurement-data-providers/profile|Retail Measurement Data Providers]]
**Industry:** [[industries/food-distributors|Food Distributors]]
**Type:** Fix (Pain Point)
**One-liner:** Roughly half of what Americans eat is bought away from home, retail measurement sees none of it, and category share is reported as though the retail shelf were the market.
**Tags:** #descriptive-statistics #confidence-intervals #bayesian-inference #hypothesis-testing #evaluation-metrics #feature-engineering #dimensionality-reduction #data-integration #compliance #revenue-impact

## The Problem
A manufacturer reads a category share report and takes it as their position in the market. It is their position in measured retail. Foodservice — restaurants, schools, hospitals, and the distributors who supply them — is a comparable share of food consumption and is entirely outside the panel. For categories where the away-from-home channel is large and growing, the reported share can move for reasons that have nothing to do with the manufacturer's performance, and the client has no way to see it. The provider knows the boundary precisely and reports the number without it, because the boundary is not what the product was built to measure and stating it invites the question of what the number actually means.

## Why It's Still Broken
Retail measurement was built when the retail shelf was a reasonable proxy for the market, and the panel infrastructure, the taxonomy, and the commercial model all assume it. Measuring foodservice requires a completely different collection approach — distributor shipment data and operator research rather than retail scan — which is a separate business, and the providers that do it are separate firms. Internally, adding a caveat to a flagship metric is a commercial decision nobody wants to make unilaterally while competitors state theirs without one.

## What a Fix Looks Like
Channel scope stated as a first-class property of every reported figure, with an estimate of the unmeasured share for that category. That estimate is buildable from sources the provider can obtain or license — distributor shipment aggregates, operator research, and category-level away-from-home consumption benchmarks — without building a full foodservice measurement business. Where the unmeasured share is small, the caveat costs nothing; where it is large and moving, it is the single most important thing a client should know about the number they are acting on. Reported trend then distinguishes movement in measured retail from likely movement in total category, which is what a manufacturer's planning actually requires. For the provider, this is also the entry into a genuinely adjacent product rather than a concession — total category view is what clients ask for and currently assemble themselves from two vendors who do not reconcile.

## Who Feels the Pain
Manufacturers planning against a share number whose denominator excludes half the market; category managers reconciling two vendors' incompatible views by hand; the provider's client service teams explaining discrepancies they cannot resolve; and the measurement business itself, whose relevance narrows as consumption shifts to channels it does not see.

## Impact If Fixed
Turns a structural blind spot into a stated scope and an adjacent product. In a category facing exactly the criticism that its panel no longer represents the market, being explicit about what is measured is a stronger position than confident silence — and the total-category view is what clients are already trying and failing to assemble.
