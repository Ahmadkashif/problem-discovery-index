# Projection Factors Set by Method and Never Scored Against Truth

**Niche:** [[niches/pharmacy-independents/prescription-market-intelligence/profile|Prescription Market Intelligence Providers]]
**Industry:** [[industries/pharmacy-independents|Independent Pharmacies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The whole product is a national number extrapolated from a partial sample, and the extrapolation has never been validated against an actual national count.
**Tags:** #gradient-boosting #causal-inference #evaluation-metrics #confidence-intervals #time-series-forecasting

## The Problem
These firms do not observe every prescription in the United States. They observe a large, non-random sample — the pharmacies, chains and switches that supply data — and project it to a national estimate. That projection is the product. A manufacturer sets sales force deployment, incentive compensation, and forecast accountability against it; a payer benchmarks against it; an investor trades on it.

Projection is done with methodology: stratify by geography and outlet type, estimate coverage within each cell, gross up. The methods are decades old, carefully constructed, defended in documentation, and — in the sense that matters — never tested. There is no independent national count of prescriptions to check against.

The consequences are structural, not occasional. Coverage is not uniform: independent pharmacies, long-term care, mail order, specialty pharmacy and 340B contract pharmacies are each captured at different and shifting rates, and a product whose dispensing skews toward a weakly covered channel is systematically mismeasured. Coverage also drifts as supplier contracts are won and lost, which produces changes in the reported series that look like market movements and are not.

The people who build these models know all of this. What does not exist is a measurement of how wrong the projections are, where, and by how much.

## Why Nobody Has Built This
The absence of ground truth is real, and it has been treated as the end of the discussion rather than the start of one. If no national count exists, the reasoning goes, projection accuracy is unknowable.

The commercial incentive points the same way. A single authoritative number is easier to sell, easier to contract against, and easier to build a customer's internal process around than a number with an interval. Customers have built incentive compensation systems on these figures; a vendor that started publishing uncertainty would be telling thousands of sales representatives that their bonus basis has error bars.

And methodology is the competitive claim. Vendors describe projection methods as proprietary strengths. Publishing measured error would convert a described strength into a testable one.

## What to Build
Validation without a census, which is a solvable problem the industry has not tried to solve.

**Hold out suppliers.** The firm holds data from many sources. Systematically withhold one from the projection, project without it, and compare the projection to what that supplier actually reported. Repeat across suppliers, channels and geographies. This produces a direct, honest error distribution and it can be run today on data already in hand.

**Anchor against independent aggregates.** Manufacturer shipment data, federal and state programme utilisation, wholesaler distribution volumes, and payer-published statistics each cover part of the same reality from a different angle. None is a census; together they constrain the estimate and reveal where projections are inconsistent with a stronger signal.

**Model coverage as a quantity that moves.** Coverage rate by channel and geography is currently a periodically re-estimated parameter. It is a time series driven by contract wins, chain consolidation, and channel shift, and treating it as such makes drift a modelled effect rather than a surprise in the output.

**Predict error, not just estimate volume.** Given a product's channel mix, therapeutic area, geographic concentration and dispensing pattern, predict how reliable its projection is. That is directly sellable: a customer who knows a specialty product in a weakly covered channel has wide uncertainty makes better decisions than one who does not.

**Publish intervals.** Start with the analytics where uncertainty is largest and the customer already suspects it. The vendor that reports honest error first defines the standard everyone else has to answer.

## Target Customer
Chief Data Officer or SVP of Data Science at a prescription data provider. The commercial argument is that projection methodology is the last undifferentiated part of the product, and measured accuracy is the only claim in this market that a competitor cannot simply assert.

## Impact If Built
Billions of dollars of pharmaceutical commercial decisions — sales force sizing, incentive compensation, launch forecasting, investor models — run on projected national figures with no published error. Measuring and reporting that error, channel by channel, is both a genuine improvement in the decisions and the strongest differentiation available in a market where every vendor claims methodological rigour and none demonstrates it.
