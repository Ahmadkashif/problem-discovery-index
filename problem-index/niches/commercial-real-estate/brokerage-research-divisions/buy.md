# The Firm Buys Market Data It Partly Generates, and Cannot Join It to Its Own Deals

**Niche:** [[niches/commercial-real-estate/brokerage-research-divisions/profile|Brokerage Research Divisions]]
**Industry:** [[industries/commercial-real-estate|Commercial Real Estate]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Commercial property data platforms are mature, expensive and central to how a brokerage works, and none of them can tell the firm that the building in their database is the one its own broker leased last quarter.
**Tags:** #word-embeddings #dbscan #feature-engineering #data-integration #evaluation-metrics

## The Problem
A brokerage research division runs on bought data. Commercial property databases supply building inventory, ownership, tenancy, comparable sales and lease comps across markets. Public records aggregators supply recorded transactions and debt. Economic data services supply employment and demographic series. Business intelligence and visualisation platforms produce the charts. Increasingly there are analytics products layered on top of the same property databases.

The bought stack is good. It is also the same stack the competing brokerages buy, from the same vendors, which means the published research from four global firms is substantially derived from one shared source — and everybody's numbers converge because everybody's inputs are identical.

The differentiating data is internal, and joining it to the bought data is the problem nobody has solved.

## What Already Exists
Commercial property data platforms hold inventory, comps, tenancy and ownership at national scale. Public records and deed aggregators supply recorded transaction and mortgage data. Economic and demographic data services are mature. Valuation and underwriting models exist as products. BI and mapping tools handle presentation. Brokerage CRM systems track deals and commissions. Document AI can extract from leases.

## The Customization Gap
**Nothing resolves a building across sources.** The same property appears in the data vendor's inventory, in county records under a legal description, in the firm's CRM as a broker typed it, in a lease document as the tenant's counsel wrote it, and in a valuation file under a portfolio name. Matching them is a hard entity resolution problem across addresses, parcels, legal descriptions and colloquial building names, with the added complication that ownership structures nest through single-purpose entities. Every meaningful internal analysis requires this join and it is done by hand, per project.

**The CRM was built to pay brokers.** Deal records exist to track commission, so the fields that matter analytically — concession package, tour history, competing shortlist, why the tenant chose this building — are inconsistent, optional or absent. The pipeline is the firm's most valuable dataset and its quality reflects what it was collected for.

**Lease economics live in documents.** Free rent, tenant improvement allowance, escalations, options and expansion rights determine effective rent and sit in lease PDFs. Document extraction handles the structured clauses reasonably and the negotiated, non-standard terms poorly — and the non-standard terms are the ones that move the number.

**The data vendor is a dependency, not a supplier.** The primary property database is close to a monopoly in several markets, it prices accordingly, it competes with its customers by selling analytics, and it constrains through licensing what the firm may republish from data partly contributed by that firm's own brokers. Any research strategy built on top of it is built on someone else's terms.

**Market boundaries are conventions.** Submarket definitions differ between the vendor, the firm's own research and local broker practice, and reconciling them silently changes published statistics. Nothing in the bought stack surfaces the discrepancy.

**BI presents, it does not forecast.** The visualisation layer is strong and is doing all the work in most divisions, which is a reasonable description of why the output is descriptive.

## Target Customer
Global Head of Research or Chief Data Officer at a brokerage. The build is not a replacement for the property database — that fight is not worth having. It is the property resolution layer, the pipeline data quality it enables, and lease economics extraction: the three things that turn a shared industry dataset into a proprietary one.

## Impact If Solved
Four global research divisions publish from the same purchased source and differ mainly in commentary. The data that would separate them is inside each firm, unjoined to anything, in a system built for paying commissions.
