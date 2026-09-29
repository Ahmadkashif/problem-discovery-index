# Hundreds of Analysts Spend the Quarter Assembling the Report and a Week Thinking About It

**Niche:** [[niches/commercial-real-estate/brokerage-research-divisions/profile|Brokerage Research Divisions]]
**Industry:** [[industries/commercial-real-estate|Commercial Real Estate]]
**Type:** Fix (Pain Point)
**One-liner:** The quarterly reporting cycle across hundreds of markets and property types consumes most of the research organisation's capacity in data assembly and document production, and delivers a description of a quarter that ended weeks ago.
**Tags:** #time-series-forecasting #descriptive-statistics #automation #workflow-orchestration #evaluation-metrics

## The Problem
A global brokerage research division publishes on a quarterly cycle across a very large matrix: office, industrial, retail, multifamily and specialty, across hundreds of metropolitan markets and their submarkets, in several regions, in multiple languages. Each cell of that matrix produces a report with the same skeleton — vacancy, absorption, deliveries, under construction, asking rent, notable transactions, a paragraph of outlook.

Producing it is an assembly operation. Analysts pull from the property database, reconcile it against internal deal records, chase brokers for detail on transactions, correct the inventory where the vendor is wrong, rebuild the submarket rollups, populate a template, write the commentary, route it through review and design, and publish.

Then the next quarter begins.

The people doing this are trained economists and analysts. Most of their time goes to reconciliation and document production. The analytical content of a market report — the part requiring their training — is a small fraction of the effort, and it is the part squeezed when the deadline compresses.

The output has the corresponding shape. It describes what happened, competently, some weeks after it happened. Clients who need a view rather than a description hire someone else, and the division's own economists produce the forward-looking work in a separate, much smaller stream that the quarterly machine leaves no room for.

Every firm in the industry runs this same cycle, on the same underlying data, and the reports are close to interchangeable.

## Why It's Still Broken
The cycle is the marketing calendar. The reports exist to keep the brand in circulation and to give brokers something to send clients, and that purpose is served by coverage breadth and reliable cadence — which is precisely what makes the matrix so large and so repetitive.

Coverage is competitive. No division will drop markets or property types while rivals publish them, because the comparison is made on the list of what you cover.

Data reconciliation resists automation for real reasons. The vendor's inventory has errors in every market, local brokers know the corrections, and capturing that knowledge is the analyst's genuine contribution. It is also the same corrections, quarter after quarter, applied by hand.

Analysts are measured on delivery. Reports out, on date, without errors. Nothing measures whether the outlook paragraph was any good, and nobody has ever gone back to check.

And the tooling reflects the priority. The stack is a property database, a spreadsheet layer and a design template, connected by people.

## What a Fix Looks Like
**Automate the assembly completely.** Every statistic in a standard market report is a deterministic computation from known sources. Generating the numbers, the charts and the standard narrative sections without human assembly is achievable and it is where nearly all the capacity currently goes.

**Make corrections persist.** An analyst's correction to the vendor's inventory should be recorded once, attributed, and reapplied automatically every quarter. Today it is re-derived each cycle from memory, and it leaves with the analyst.

**Publish continuously instead of quarterly.** Where the underlying data updates weekly, so can the market view. The quarterly cadence is a print convention on a live dataset, and moving off it changes the product from a document to a service.

**Redirect analyst time to what the data cannot answer.** Why a tenant chose one submarket over another, what a corporate occupier's footprint change means, where a supply pipeline is overstated — these need judgment and local knowledge and are exactly what is being crowded out.

**Score the outlook.** Forecast statements should be recorded with the date and the horizon and evaluated when the horizon arrives. It costs almost nothing and it is the only route to knowing whether the analytical half of the report is worth reading.

**Standardise the definitions once.** Submarket boundaries, vacancy definitions and rent measurement should be settled globally and applied mechanically. The current reconciliation happens per market, per quarter, per analyst.

## Who Feels the Pain
The analyst, hired as an economist and spending the quarter reconciling a spreadsheet. The research director, whose capacity is consumed by a matrix that grows every time a competitor adds a market. The broker, sending a client a report that describes a quarter the client already lived through. And the investor or lender, underwriting a long-lived asset against a statistic that is descriptive, lagging and identical to the one from the firm across the street.

## Impact If Fixed
The largest research organisations in commercial real estate employ hundreds of trained analysts and spend most of that capacity assembling documents. Freeing it is not an efficiency exercise — it is the difference between a division that reports the market and one that has a view of it.
