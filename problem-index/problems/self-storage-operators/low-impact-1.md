# Lien Notices Run Through Fifty State Statutes

**Industry:** [[self-storage-operators|Self-Storage Operators]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Facility software already sends late notices and schedules auctions. What it does not do is run each delinquent unit through the right state's notice days, delivery proof, advertising and sale rules, and keep proof of every step.
**Tags:** #large-language-models #workflow-orchestration #compliance #automation #data-integration #evaluation-metrics

## The Problem
When a tenant stops paying, a collections or lien clerk at the operator or third-party manager takes over. The unit moves through a statutory sequence: a preliminary notice, overlock and denial of access, a notice of lien sale, an advertisement, the sale, and the handling of any surplus. Each step has a deadline and a required delivery method, and both differ by state. In California the owner may send the preliminary notice once rent is 14 days unpaid, the lien attaches 14 days later, and the sale needs another notice at least 14 days ahead. Since 2026-01-01 an email notice there counts only with evidence the renter opened or acknowledged it (AB 498). Illinois, according to trade summaries, now presumes email delivered only with a delivery receipt and otherwise requires verified mail (search summary). A vehicle or boat in the unit adds a title and lienholder search. A tenant on active military duty brings federal protections that stop the sale without a court order.

A clerk at a multi-state operator works hundreds of these files a month. Miss a step and the sale becomes a wrongful-sale claim. New York City's 2026 settlement with Extra Space required "stronger due process protections" before lockouts or auctions, after complaints of wrongful lockouts and auctions.

## What Already Exists
Storable sells Collections and Auctions modules inside Sitelink and Storable Edge. OpenTech Alliance sells automated collections and runs the StorageTreasures auction site, and Lockerfox publishes a lien-law reference beside its own auctions. Certified-mail and e-signature services handle delivery, and law firms and state associations sell standard leases and notice templates. The Illinois association sells its standard lease to members for $295.

## The Customisation Gap
The generic tools send the notice the operator configured. They do not know that the configuration is wrong for this unit. The industry-specific layer is a statute engine keyed to the facility's state and the unit's contents. It needs day counts and the start event for each, accepted delivery methods and the evidence each needs (an "opened" receipt in California, a delivery receipt in Illinois), and advertising rules: newspaper, online, or both, and for how long. It also needs the vehicle title and lienholder steps, the military-status check, the surplus-proceeds rule and any city overlay such as New York's licence conditions. It should read the lease the tenant actually signed to confirm email consent, flag files where the evidence chain is broken before the sale date, and package the proof for a dispute. A language model can read signed leases and returned mail. The rules themselves must be written and maintained by people who track each legislature.

## Impact If Solved
A clerk who now checks each file against a binder could clear a lien file in ~10 minutes instead of ~30 (estimate), across ~1–2% of units reaching lien each year (estimate). The larger value is avoided claims. One wrongful sale can cost more than a year of a store's lien fees, and New York City's settlement with one operator came to $1.7M.
