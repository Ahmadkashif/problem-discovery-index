# Factory OEE Software for Generating Fleets

**Niche:** [[niches/renewable-power-producers/fleet-asset-performance-om/profile|Fleet Asset Performance & O&M]]
**Industry:** [[industries/renewable-power-producers|Renewable Power Producers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Factories already break lost output into availability, performance and quality losses with standard reason codes across machines from many makers; a wind and solar fleet is the same problem with weather as the raw material.
**Tags:** #descriptive-statistics #feature-engineering #data-integration #automation #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is "every serious competitor is fighting to recover the most lost energy per dollar of operations and maintenance", but wind and solar lose energy in different ways, to different vendors, on different data: wind is won on avoiding crane-dependent drivetrain failures, solar on clearing the many small inverter, tracker and string losses. Decomposed into contested sub-niches below.

## The Problem
Fleet owners need loss accounting that is consistent across makers and sites, and each OEM supplies its own.

## What Already Exists
Overall equipment effectiveness and downtime-tracking software in manufacturing (from vendors such as Rockwell's and Siemens's MES lines and specialist downtime trackers) maps each machine's states to a standard reason-code tree and reports losses by cause across a plant.

## The Customization Gap
The adaptation needs: expected output from a power curve or irradiance model instead of a rated cycle time; weather and grid exclusions as first-class causes; curtailment split by type for PPA purposes; mapping of each OEM's event codes onto one tree; energy-based and time-based availability both computed; and contract availability guarantees derived from the same events.

## Target Customer
Asset performance and operations heads at owners with mixed fleets and no single OEM relationship.

## Impact If Solved
Replacing a monthly spreadsheet reconciliation that takes ~2 analyst weeks across a 30-site fleet (estimate) with a standard loss tree frees ~25 analyst weeks a year.
