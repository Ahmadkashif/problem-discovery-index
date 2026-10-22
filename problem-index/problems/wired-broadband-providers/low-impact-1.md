# Semiannual Availability Filings Against the Fabric

**Industry:** [[wired-broadband-providers|Wired Broadband Providers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every facilities-based provider reconciles its plant and customer records to the FCC's location Fabric twice a year to say which addresses it can serve at what speed, and most rebuild that reconciliation by hand in a GIS each time.
**Tags:** #k-nearest-neighbors #large-language-models #feature-engineering #evaluation-metrics #compliance #data-integration #automation #quick-win

## The Problem
Under the FCC's Broadband Data Collection, a provider reports, for every Broadband Serviceable Location in the Fabric, whether it can deliver service there within ten business days, over which technology and at what maximum advertised speeds. The Fabric is licensed from CostQuest, the FCC's contractor, and revised every six months. The filing for data as of June 30, 2026 was due September 1, 2026, the same day Fabric challenges for the December 2026 revision closed; the previous window closed March 2, 2026.

The filing matters beyond compliance. The national map decides which locations were eligible for BEAD and other subsidies, and an availability claim can be challenged by consumers, states or competitors. A provider that over-claims invites challenges and loses credibility; one that under-claims hands its territory to a subsidised competitor. For a rural telco or a 4,000-subscriber fibre ISP, the work falls to an engineer or regulatory manager who exports passings from the network map, geocodes billing addresses, matches them to Fabric location IDs, resolves apartments and unit counts, checks speeds by technology, and certifies the result. NRECA told the FCC the requirement that a licensed professional engineer certify the filing is a significant hardship for smaller ISPs.

## What Already Exists
General GIS (Esri ArcGIS, QGIS), the FCC's own BDC filing system and its data specifications, CostQuest's Fabric licence and bulk files, and fibre mapping tools such as Vetro FiberMap that can export served locations. Regulatory consultants file on clients' behalf, and many small operators simply pay one to do it each cycle.

## The Customisation Gap
Generic GIS answers "what is near this line"; the filing asks "which Fabric location IDs can I serve, by technology, at what speed, under the FCC's definition". The industry-specific logic is: matching passings and billing addresses to Fabric locations when addresses, geocodes and unit counts disagree; distinguishing passings that are truly serviceable within ten days from those needing a long drop or make-ready; carrying technology and speed per location rather than per area; diffing against the previous filing and the new Fabric revision so changes are explained; drafting Fabric challenges for missing or misplaced locations before the deadline; and keeping an evidence trail an engineer can certify and a challenge response can draw on. Each operator or consultant rebuilds this in spreadsheets every six months.

## Impact If Solved
A repeatable, versioned filing pipeline turns a two-to-four-week scramble (estimate) for a small operator's only engineer into a few days of review, cuts consultant fees, and produces filings accurate enough to survive challenges, which protects both the operator's territory and its eligibility for the next round of subsidies.
