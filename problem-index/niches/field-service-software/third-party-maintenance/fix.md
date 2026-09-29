# The Harvested Inventory Only One Person Understands

**Niche:** [[niches/field-service-software/third-party-maintenance/profile|Third-Party Maintenance — Parts Without the Manufacturer]]
**Industry:** [[industries/field-service-software|Field Service Software]]
**Type:** Fix (Pain Point)
**One-liner:** Third-party maintainers hold warehouses of components harvested from decommissioned machines, worth a great deal and catalogued in a spreadsheet whose meaning depends entirely on the person who wrote it.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #data-integration #workflow-orchestration #automation #worker-facing #revenue-impact
**Contested on:** Every serious competitor in third-party maintenance software is fighting to source, verify and certify a part for equipment its customer's manufacturer would rather it did not service — and whoever makes parts provenance reliable takes the account.

## The Problem
A maintainer decommissions machines and harvests components — boards, assemblies, detectors, drives — into a warehouse. The inventory is real money, frequently the organisation's largest asset after its people. Its catalogue is a spreadsheet with shorthand descriptions, shelf locations that are approximate, and no record of which items have been tested. Finding whether a needed part is in stock means asking the warehouse manager. When he is away, the organisation buys parts it already owns. When he leaves, a substantial share of the asset becomes effectively unfindable.

## Why It's Still Broken
Cataloguing harvested parts properly is slow, skilled work — identifying a component pulled from a machine requires knowing what it is — and it competes with revenue-generating work for the same people. Inventory systems assume items arrive with identities from a supplier, which harvested parts do not. And the organisation has functioned this way for years, so the risk is familiar and therefore invisible until the person who holds it takes another job.

## What a Fix Looks Like
Make identification happen at harvest, when the context is present and free. A component pulled from a machine is at that moment fully identified — the machine, its configuration, the position the part came from, its service history — and capturing that takes a photograph and a tap rather than research. Record condition and whether it was working when removed, which is knowledge that exists only at that instant. Test status becomes an explicit state with a date rather than an assumption. Location is a scannable bin rather than a memory. Everything that follows — searching stock before purchasing, valuing the asset, deciding what to harvest from the next decommission — falls out of that. Backfilling the existing warehouse is a real project and should be prioritised by value and by turnover rather than attempted wholesale.

## Who Feels the Pain
Warehouse managers who cannot take a holiday; technicians told a part is not in stock when it is on a shelf; and owners whose largest asset is documented in one person's handwriting.

## Impact If Fixed
Capturing identity at harvest costs seconds and is the difference between an asset and a pile, and organisations that do it routinely stop buying parts they already own — which in a margin-thin segment is immediate. Removing the single-person dependency is the larger structural gain and is the one nobody prices until it happens.
