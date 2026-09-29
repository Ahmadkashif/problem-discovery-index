# Programme Oversight Without Programme Visibility

**Industry:** [[embedded-finance-platforms|Embedded Finance Platforms]]
**Type:** High Impact
**One-liner:** The platform is now accountable for how dozens of fintech programmes treat their customers, and can see only the API calls those programmes make.
**Tags:** #change-point-detection #gradient-boosting #bert #large-language-models #k-means-clustering #confidence-intervals #evaluation-metrics #compliance #data-integration

## The Problem
A sponsor bank supervises a fintech programme. After the consent orders of 2023 and 2024, what supervision means became concrete: the bank must know what the programme is marketing, to whom, with what disclosures, how it handles complaints, whether its transaction monitoring is calibrated, whether customer funds are correctly held and reconciled, and whether the programme is doing anything the bank would not do itself.

The bank cannot see any of that directly. It sees a ledger position and a reporting pack. The platform sits closer — it processes every transaction, holds the account records, and executes the programme's instructions — and still sees only a projection. A programme's marketing site, its in-app disclosures, its support scripts, its fee presentation, and its decisions about which customers to onboard are all outside the API.

So oversight is performed by inference and by questionnaire. The platform asks programmes to attest. It reviews marketing on a schedule. It monitors transaction patterns for anomalies. And it discovers problems the way everyone discovers them: a complaint pattern, a bank partner's question, a regulator's letter, or a programme's sudden failure.

The Synapse collapse demonstrated the extreme version. End users could not reach deposits because the reconciliation between the platform's sub-ledger and the banks' FBO accounts did not resolve, and no party held a complete, verified picture of who owned what. That was a ledger problem and an oversight problem at once, and it was visible in the data before it was visible in the news.

Meanwhile the reporting burden runs in the other direction. Each bank partner wants oversight evidence in its own format and cadence, and a platform with several bank partners and dozens of programmes is producing a matrix of reports assembled largely by hand.

## Why It's Unsolved
The three-party structure distributes responsibility away from visibility on purpose. The programme wants product control and got it. The bank wanted fee income without operational burden and is now being told it cannot have that. The platform monetises volume and inherited a supervisory function it was not designed for and does not price for.

Oversight has no standard. There is no agreed schema for what a programme must evidence, no common taxonomy of programme risk, and no shared definition of the metrics banks ask for. Every relationship negotiates its own, which makes the work bespoke and makes cross-programme comparison — the platform's actual advantage — hard to perform even internally.

The signals are weak individually and meaningful only in aggregate. A single unusual transaction pattern in one programme means nothing. The same pattern appearing in the two programmes built by the same founding team, or in every programme using a particular onboarding vendor, is the finding — and that comparison requires treating all programmes as one dataset, which platforms generally do not do because each programme is a separate tenant.

And the incentive is uncomfortable. A platform that detects a programme behaving badly must act against its own paying customer, in a market where programmes can migrate to a competitor. That tension is real and is the reason detection capability lags detection capacity.

## What a Solution Looks Like
Treat the programme portfolio as a single comparative dataset. The platform runs the same primitives for dozens of products, which means a programme's transaction mix, dispute rate, onboarding funnel, complaint themes, fee incidence and customer tenure can be positioned against a distribution rather than judged in isolation. Outliers on those distributions are the earliest available signal and require no new data collection at all.

Observe what is observable outside the API. Programme marketing sites, app store listings, disclosure pages and public review text are all fetchable, and changes to them are exactly what oversight is meant to catch. A programme that quietly changed its fee disclosure or began advertising to a new population has done something the platform can see without asking.

Precursor modelling on known failures. The platform has a history of programmes that failed, were wound down, or triggered regulatory attention, with full transaction and behavioural data preceding each. Those are labelled examples of a rare and expensive event and nobody models them.

Continuous reconciliation with proof. Sub-ledger to FBO position, reconciled continuously with a verifiable record per end customer, is the specific control whose absence produced the sector's worst failure. It is an engineering discipline, not a model.

Oversight evidence generated once and rendered per bank. The underlying facts are the same; only the format differs.

## Impact If Solved
Supervisory expectation has already shifted and the platforms are the only party positioned to meet it, because they hold the data and the banks do not. Turning the programme portfolio into a comparative dataset converts oversight from questionnaire-and-hope into measurement, and the same capability is the product differentiator in a market where a bank partner chooses a platform based on whether it will survive an examination.
