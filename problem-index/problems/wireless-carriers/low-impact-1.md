# Tower Lease and Site Loading Reconciliation

**Industry:** [[wireless-carriers|Wireless Carriers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** A national carrier rents tens of thousands of tower positions under master lease agreements and site-level amendments, and nobody routinely checks whether the equipment actually on each tower matches what the lease allows and what the carrier is billed for.
**Tags:** #large-language-models #transformers #feature-engineering #evaluation-metrics #data-integration #automation #quick-win

## The Problem
A carrier's sites sit mostly on towers owned by American Tower, Crown Castle (a pure-play tower company since it sold its fibre and small-cell businesses in May 2026), SBA and smaller owners, plus rooftops and utility structures. Rent is set by master lease agreements renegotiated every several years and by site-level amendments each time equipment changes: more antennas, heavier radios, a new cable run, a higher mount. Each amendment carries loading entitlements (antenna count, weight, wind load, centreline height) and often a modification fee or rent increase. A 5G overlay can touch every site in a market in one year.

The lease file and the tower diverge. Equipment is removed and never taken off the lease. Amendments are signed for equipment that never went up. Tower owners' site audits find equipment above entitlement and bill for it. Escalators compound on the wrong base. The carrier's real estate team has the lease PDFs, the network team has the installed-equipment records, and the two rarely meet.

## What Already Exists
Lease administration platforms such as Visual Lease and CoStar Real Estate Manager abstract leases and schedule payments. Sitetracker, built on Salesforce, manages site deployment programmes. Contract AI tools extract clauses from documents. The tower owners run their own portals and audit programmes, and the carrier pays rent through accounts payable.

## The Customisation Gap
Generic lease tools treat a tower lease like an office lease: rent, term, escalator, options. A tower lease is an equipment entitlement. The gap is tower-specific abstraction (antenna and radio counts, mount positions, weights, cable counts, RAD centre and ground space from exhibits and drawings), linked amendment chains rather than single documents, and a reconciliation of entitlements against the carrier's own inventory of what is installed. That inventory comes from network configuration, site audit photos and the last structural analysis. Disputes need the MLA's specific rules on when a modification triggers a fee and how loading is counted. Extraction has to handle scanned exhibits and drawings, not just clean text.

## Impact If Solved
A reconciled site file lets the real estate team recover overbilling, remove decommissioned equipment from rent, and walk into an MLA renegotiation knowing its true loading. Across tens of thousands of sites, a correction of a few hundred dollars a year per site adds up to millions (estimate). It also shortens the next site modification, because the lease position is already known.
