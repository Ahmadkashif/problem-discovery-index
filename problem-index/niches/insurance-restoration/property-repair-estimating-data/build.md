# Published Prices Nobody Compares to What Jobs Actually Cost

**Niche:** [[niches/insurance-restoration/property-repair-estimating-data/profile|Property Repair Estimating Data]]
**Industry:** [[industries/insurance-restoration|Insurance Restoration]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every property claim in America settles on these unit costs, and the company has the completed jobs to check them against and does not.
**Tags:** #tabular-ml #gradient-boosting #time-series-forecasting #anomaly-detection #evaluation-metrics

## The Problem
The monthly price list is the product: for every repair task, in every postal code, a material cost, a labour cost, and an equipment cost. Carriers settle on it, contractors estimate on it, and Pass 1 records that line-item accuracy against it is one of the criteria deciding whether a restoration company keeps carrier work worth most of its revenue.

Prices are set by market research — surveying suppliers and contractors, tracking material indices, applying regional factors. It is a survey operation, and it produces a number that is asserted rather than measured.

Meanwhile the company sits on the other half. Essentially every property repair estimate in the country is written in its software, many of them are revised as the job proceeds, supplements are added when the scope changes, and a large share reach a final settled amount. The gap between the published unit cost and what the job actually settled at is computable, line by line, geography by geography, month by month. It is not computed.

So nobody knows where the price list is wrong, in which direction, or by how much — while the entire industry argues about exactly that, continuously, on every claim.

## Why Nobody Has Built This
The business is a publishing operation with a survey function attached, and its quality process is about survey rigour rather than outcome validation. Accuracy has always meant that the research was done properly, not that the number matched reality.

There is also a real institutional caution: the company's position depends on being seen as neutral between carriers and contractors, and publishing an analysis showing its own prices run low in a trade would be read as taking a side. That concern is genuine and it is also why a measurable question has stayed unmeasured for decades.

And the estimate corpus belongs, contractually, to the customers who wrote the estimates. Using it in aggregate is a permissions question — solvable, and never solved, because nobody has needed to.

## What to Build
Close the loop between published price and settled cost.

**Assemble the outcome set.** Original estimate, supplements, revisions, and final settled amounts by line item and geography, aggregated so no individual job or customer is identifiable. The permissions work is the hard part and the analysis is straightforward once it is done.

**Measure divergence by line item and market.** Which tasks are systematically supplemented upward, in which regions, in which seasons. A line item that is supplemented on a third of jobs in one metro is a price that is wrong, and it is discoverable today.

**Model price movement rather than surveying it.** Material indices, labour market conditions, and post-catastrophe demand surges move costs faster than a monthly survey cycle detects. A forecast fitted on observed settlements would lead the survey rather than lag it — which matters most after a catastrophe, when demand surge is exactly what the list fails to capture and when the largest volume of claims is being settled.

**Publish confidence.** A line item priced from forty recent observations in a dense market and one priced from an extrapolation in a rural county are not the same number, and today they look identical. Saying which is which is honest, useful, and something no competitor could match.

## Target Customer
VP of Data or Chief Product Officer. The neutrality argument runs the other way once stated plainly: a price list validated against outcomes is more defensible to both sides than one defended by describing the survey methodology, and every dispute in this industry is ultimately about whether the number is right.

## Impact If Built
Underscoping means the contractor absorbs the cost; overscoping triggers carrier audits and programme penalties — Pass 1's framing of the operator's central risk, and both are functions of whether the published price matches reality. Every point of divergence removed is money moved to the party that should have it, across an entire national claims system. And the validation data has been accumulating inside the company for twenty years.
