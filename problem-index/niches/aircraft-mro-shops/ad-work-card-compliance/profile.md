# AD & Work-Card Compliance Checking

**Parent Industry:** [[industries/aircraft-mro-shops|Aircraft MRO & FBO Shops]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to prove every work card cites the current AD revision and an approved method of compliance for that serial number, and whoever has the lowest missed-applicability rate takes the account.

## Profile
**Market Size:** ~$250M a year in AD research, work-package compliance review and inspector checking time across repair stations, FBO shops and general aviation IAs (estimate)
**Share of Parent Industry:** ~1% of 488190's ~$23.3B receipts (estimate)
**Digital Adoption:** Medium-low — ADs are digital in the FAA's Dynamic Regulatory System and due lists are digital in tracking systems; the check of the work card against the AD is done by eye from printouts
**Target Buyer:** Director of maintenance or chief inspector at a repair station; IA-holding owners of general aviation shops
**Automation Potential:** High — ADs follow a fixed Federal Register structure and the rules are public, though each aircraft's configuration and AD status are customer records; the inspector keeps the signature

## What Makes This a Distinct Niche
The FAA published 317 final ADs in 2025 and 280 in 2024, plus ~250 proposed ADs each year (Federal Register). Each AD is applicable by model, serial range, part number or modification status, and many recur. Under 145.109(d) a repair station must have current ADs accessible when the work is done, and under 91.417 the owner's AD status record must show each AD's method of compliance and revision. The FAA also publishes every Service Difficulty Report (67,652 for 2025) as a yearly download, though ~93% come from air carriers and Cessna aircraft account for only 1,348, so SDRs say little about the business and general aviation fleets most small shops maintain. The rules are public and free; the aircraft's configuration, embodied service bulletins, AD status and work cards are customer records. ADs have no bulk download from DRS, so a library is built from the Federal Register, which does not carry every emergency AD. That still makes this the cheapest place in the industry to demonstrate an AI product, on public ADs against a synthetic aircraft: the owner's MVP is a work-card checker against ADs and SDRs. This niche is the forward check of the work about to be signed. Rebuilding an aircraft's past compliance history for a sale sits in [[niches/aircraft-mro-shops/maintenance-records-traceability/profile|Aircraft Maintenance Records & Logbook Audits]].

## Current Tools & Gaps
CAMP, Traxxall and Veryon's Flightdocs list due ADs per aircraft from their own AD research; AMOS, TRAX and IFS Maintenix hold AD libraries for airlines; Aircraft Technical Publishers and OEM portals publish libraries; Zymbly and Fleetcraft target the mechanic's documentation. The gaps: no tool reads the work card text against the AD's applicability, revision and method; AMOCs live in email; and SDRs are never surfaced at the task.

## Problems
- [[niches/aircraft-mro-shops/ad-work-card-compliance/build|🔨 Build: The Work-Card AD and SDR Checker]]
- [[niches/aircraft-mro-shops/ad-work-card-compliance/buy|🛒 Buy: Tracking-System AD Lists Extended to Card Text]]
- [[niches/aircraft-mro-shops/ad-work-card-compliance/fix|🔧 Fix: Recurring AD Intervals Counted From the Wrong Baseline]]
