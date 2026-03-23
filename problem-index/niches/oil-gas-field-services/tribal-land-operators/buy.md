# Production Accounting Adapted for BIA/ONRR Reporting

**Niche:** [[niches/oil-gas-field-services/tribal-land-operators/profile|Tribal Land Operators]]
**Industry:** [[industries/oil-gas-field-services|Oil & Gas Field Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Production accounting platforms like Avocet and ARIES handle state commission reporting but have zero support for BIA lease terms, ONRR royalty formats, or tribal regulatory requirements.
**Tags:** #data-integration #compliance #automation #tabular-ml

## The Problem
Tribal land operators must report production volumes, calculate royalties, and submit compliance data to federal agencies (BIA, ONRR) rather than state commissions. The reporting formats, royalty rate structures, lease terms, and audit requirements differ fundamentally from state-regulated production. Operators running wells on both tribal and fee-simple lands must maintain two entirely separate reporting workflows — one in their production accounting system and one in spreadsheets for the tribal/federal side.

## What Already Exists
Production accounting platforms (Avocet, ARIES, Enertia, W Energy) handle decline curve analysis, volume allocation, and regulatory reporting for state commissions. They support RRC (Texas), NDIC (North Dakota), and COGCC (Colorado) submission formats out of the box. None support BIA or ONRR reporting formats, tribal lease term structures (which often include sliding-scale royalty rates, tribal employment requirements, and environmental bonding terms), or the unique allotment-based well grouping that BIA uses instead of state-defined spacing units.

## The Customization Gap
The core production accounting logic (volume tracking, allocation, decline analysis) works. What is missing is a reporting layer that maps production data to BIA lease numbers (not state API numbers), calculates royalties using tribal/federal rate schedules (not state severance tax rules), generates ONRR Form 2014 submissions, and tracks compliance with tribal-specific lease stipulations like employment quotas, road maintenance obligations, and cultural site avoidance requirements.

## Target Customer
Independent operators with 20-200 wells on tribal trust or allotted lands who already use a production accounting platform for their fee-simple wells and need the tribal/federal reporting side automated.

## Impact If Solved
Eliminates the dual-workflow burden that currently adds 15-20 hours/month of manual reporting per operator, reduces ONRR audit findings by ensuring submission accuracy, and allows operators to manage tribal and fee-simple production from a single system.
