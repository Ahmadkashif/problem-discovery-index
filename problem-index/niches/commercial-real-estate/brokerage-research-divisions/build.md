# The Deal Pipeline Knows the Market Turned; The Quarterly Report Will Say So in Five Months

**Niche:** [[niches/commercial-real-estate/brokerage-research-divisions/profile|Brokerage Research Divisions]]
**Industry:** [[industries/commercial-real-estate|Commercial Real Estate]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** These research organisations publish the vacancy and rent statistics the entire industry cites, computed from recorded transactions, while sitting inside the firm whose own live deal flow precedes those recordings by months and whose brokers know the concessions that make the published rent wrong.
**Tags:** #time-series-forecasting #causal-inference #hypothesis-testing #confidence-intervals #gradient-boosting

## The Problem
The research divisions at the global brokerages are large, genuinely analytical organisations — economists, market researchers, analysts, hundreds of them — producing the quarterly market reports, vacancy and absorption series, cap rate surveys and outlook pieces that everyone in commercial real estate quotes. Lenders underwrite against them. Investors allocate against them. Appraisers cite them.

They are also, structurally, the marketing arm of a brokerage, and that shapes the product more than anyone in the field says out loud.

Two things sit inside the same firm and never reach the research.

The first is the pipeline. A brokerage sees a leasing deal from the first tour request, through the requirement, the shortlist, the term sheet, the negotiation, to signature — a process that runs for months before anything is recorded publicly. Investment sales run the same way, from the pitch through the marketing process, bids, best and final, to close. The published statistics are computed from the end of that pipeline. The firm's CRM holds the beginning of it. Tour volume, requirement counts, active bid depth and time-on-market at the firm's own scale are leading indicators of exactly the series the research division publishes with a lag, and they are used for broker management rather than for market analysis.

The second is concessions, and it is the more serious one. Published rent series are face rents. What a tenant actually pays after free rent periods, tenant improvement allowances and other inducements — the net effective rent — can differ enormously, and the difference moves sharply with the cycle. It is exactly what widens when a market weakens while face rents stay flat to protect valuations. The broker who did the deal knows the concession package. The firm knows it across thousands of deals. The published series does not carry it.

So the industry's reference statistics are a lagging measure of a number that is systematically distorted in the direction that matters most, produced by the one organisation holding both the leading indicator and the correction.

## Why Nobody Has Built This
The research division is funded as a lead generator. Its output justifies its budget by being cited, quoted and used in pitches. That rewards publication volume, market coverage and a confident narrative, and it does not reward a smaller number of genuinely predictive findings.

Publishing net effective rents would be commercially uncomfortable for the firm's own clients. Landlords are the brokerage's clients, their valuations rest on face rents, and a series showing effective rents falling twenty per cent while face rents held is a difficult conversation with the people paying the fees. This is the real reason, and it is why the whole industry has settled on face rent.

Using the pipeline raises a genuine internal question about client confidentiality and about signalling. A firm's own deal flow is client information, and an aggregate published from it is at minimum a matter for careful handling. It is worth separating that from the internal case: nothing prevents the firm from using its own pipeline to forecast the markets its clients ask it about, which is the use that has not been built.

And the research organisation does not own the pipeline data. It belongs to brokerage operations, in a CRM maintained for commission tracking, of variable quality, and there is no path from there to the research team's model.

## What to Build
**Nowcast the market from the firm's own funnel.** Tour requests, active requirements and bid depth lead recorded transactions by months. Relating them to the published series historically, and then running forward, gives a real-time read of a market where everyone else is looking backwards.

**Build the net effective rent series.** Face rent adjusted for free rent, tenant improvement allowance, and term. The firm has the components for thousands of its own deals. This is the single most valuable unpublished statistic in commercial real estate and the reason it stays unpublished is not analytical.

**Forecast with the model, not around it.** Market forecasting in these divisions is economist judgment supported by regional statistics. Adding the firm's own leading indicators as features, and then measuring forecast accuracy honestly against outcomes, is straightforward and almost nobody does the second half.

**Score forecast accuracy publicly.** No brokerage research division reports how its previous forecasts performed. The first one that does gains a credibility no marketing spend can buy, and it is a small piece of work.

**Estimate what actually moves rent.** Amenity packages, building improvements, submarket infrastructure, return-to-office policy shifts — these are argued about constantly and estimated rarely. The firm's transaction record supports real answers on several of them.

**Sell the research to occupiers and investors as a product.** The output is already at a quality people would pay for and is given away to generate brokerage leads. That is a decision, not a law, and the pipeline-derived pieces are the ones that could not be replicated by a data vendor.

## Target Customer
Global Head of Research or Chief Economist at a major brokerage. The honest framing matters here: the budget is marketing, so the pitch is not a research platform but a differentiated product that the competing firms cannot publish because they have not connected their own pipeline to their own research.

## Impact If Built
Trillions of dollars of property is underwritten, lent against and valued using vacancy and rent series that lag the market by months and omit the concessions that define the cycle. The organisations publishing them hold the leading indicator and the missing adjustment in the same building.
