# Financial Data Vendors

## Profile
**Category:** Capital Markets & Investment Research
**Market Size:** ~$44B global spend on financial market data, analytics and news in 2024 (Burton-Taylor estimate), with Bloomberg and LSEG Data & Analytics together taking roughly half; the fundamentals, estimates, private-markets and reference-data segments covered here are an estimated ~$15–20B of that
**Tech Maturity:** High at the delivery layer, manual at the production layer — Bloomberg Terminal, FactSet Workstation, S&P Capital IQ Pro, LSEG Workspace, PitchBook and Preqin ship polished desktops, APIs, Excel add-ins and cloud feeds, but the numbers inside them are still produced by thousands of collection analysts reading filings, keying and mapping line items, chasing brokers for estimates and phoning general partners for fund data.
**Workforce:** Content collection and quality analysts (largely in operations centres in India, the Philippines and Eastern Europe), estimates and consensus specialists, private-markets researchers, transcript editors, reference and corporate-actions data operators, entitlements and exchange-reporting staff, client support and data specialists, product and data engineers

## Key Pain Themes
The product is a number that a client will paste into a model without checking, and that number was produced by a person making a judgement the client never sees. A company reports "other operating income, net" with a restructuring gain buried in it; a collection analyst decides whether it belongs in operating income or below the line, and every screen, comp table and backtest built on that vendor's standardised EBIT inherits the decision. The judgement is tacit, inconsistent across analysts, and invisible until a client's model disagrees with a competitor's terminal and a support ticket asks why.

Around that core sit three clocks the vendor does not control. Filings and earnings calls land on the issuer's schedule and clients expect them structured within hours; brokers revise estimates whenever they like and the consensus must reflect it the same day; and exchanges audit the vendor's usage reporting on their own timetable, with back-billing attached. Private-markets data has no clock at all, which is its own problem: fund cash flows arrive from FOIA requests to public pensions and GP surveys months late, and private company rounds surface through press releases, Form D filings and phone calls.

## Current Tech Landscape
Collection runs on internal tooling built over decades — keying screens, XBRL pre-population, rules-based validation, sample QA — with offshore teams at FactSet, S&P Global Market Intelligence, LSEG and Morningstar/PitchBook doing the reading. XBRL from EDGAR and ESEF has automated the easy part of fundamentals and left the judgement part untouched. Transcripts are produced by mixed ASR-and-editor pipelines (FactSet CallStreet, LSEG StreetEvents, S&P, Bloomberg, and newer entrants such as Aiera and Quartr). Entitlements run on vendor-specific systems such as LSEG's DACS and Bloomberg's EMRS, with exchange declarations assembled monthly in spreadsheets. Large language models are now being bolted onto the delivery layer — chat interfaces over the terminal — far faster than onto the production layer where the cost and the errors sit.

## Problems
- [[problems/financial-data-vendors/high-impact|🔴 High Impact: The Standardisation Judgement Inside Every Number]]
- [[problems/financial-data-vendors/low-impact-1|🟡 Low Impact: Entitlements and Exchange Usage Reporting]]
- [[problems/financial-data-vendors/low-impact-2|🟡 Low Impact: Earnings Call Transcription for Finance]]
- [[problems/financial-data-vendors/worker-life-1|🟢 Worker Life: The Collection Analyst at 2 a.m. in Earnings Season]]
- [[problems/financial-data-vendors/worker-life-2|🟢 Worker Life: The Data Specialist Asked Why the Numbers Differ]]
- [[problems/financial-data-vendors/ml-opportunity|🧠 ML Opportunities]]
- [[problems/financial-data-vendors/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
A financial data vendor is a research workflow sold by the seat. Its corpus is not the filings — those are public — but the tens of millions of collection decisions layered on top of them: how each issuer's idiosyncratic line items were mapped, which broker estimates were excluded from consensus and why, which restatement superseded which figure, which private round was confirmed by whom. That decision history is the actual moat, and almost no vendor stores it as a decision record with the reasoning attached; it stores the resulting number and overwrites the rest. The competitive question for the next decade is not who has the best chat interface over the terminal, it is who can turn their own collectors' accumulated judgement into a model that standardises a new filing the way their best analyst would, explains itself to the client who asks why, and lets the analysts spend their time on the cases no model has seen. Adjacent markets are covered elsewhere: alternative-data brokerage in [[industries/data-marketplace-brokers|Data Marketplace Brokers]], web collection in [[industries/web-data-extraction-firms|Web Data Extraction Firms]], and fund classification and ratings in the [[niches/wealth-management-rias/investment-research-fund-data/profile|Investment Research & Fund Data Providers]] pocket.
