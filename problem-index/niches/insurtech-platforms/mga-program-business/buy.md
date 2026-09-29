# Data Exchange Standards for Bordereaux

**Niche:** [[niches/insurtech-platforms/mga-program-business/profile|MGA & Programme Business]]
**Industry:** [[industries/insurtech-platforms|Insurtech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Structured data exchange between counterparties is a solved problem in every industry that does it at scale, and delegated authority reporting runs on spreadsheets emailed monthly in formats negotiated per relationship.
**Tags:** #data-integration #evaluation-metrics #confidence-intervals #compliance #workflow-orchestration #automation #descriptive-statistics #hypothesis-testing
**Contested on:** Every serious competitor serving MGAs is fighting to give a programme a reliable loss ratio signal early enough to correct it — and whoever shortens the time from inception to a trustworthy performance picture takes the programme.

## The Problem
An MGA reports to its carrier and its reinsurers monthly through bordereaux — spreadsheets listing policies written and claims incurred, in a format agreed with each counterparty, produced by an analyst, validated by the recipient, and returned with queries. An MGA with four capacity relationships produces four different files. The recipients each validate in their own way and raise discrepancies that are usually formatting rather than substance. The whole exchange consumes real effort on both sides and delivers data late and in a form neither party can use directly.

## What Already Exists
Structured data exchange standards, schema validation, and automated reconciliation between counterparties are mature and unremarkable in banking, healthcare claims and supply chain. Within insurance, ACORD has published standards relevant to this exchange, and the London market has invested substantially in bordereaux standardisation with real if incomplete adoption. Data validation frameworks are free. The standards largely exist; the adoption does not.

## The Customization Gap
The adaptation is to a bilateral relationship where neither party can impose a format. It requires: (1) a canonical internal model with per-counterparty projections, so the MGA maintains one dataset and generates four bordereaux rather than four datasets — which is the same lossy-projection pattern that appears in restaurant menu middleware and is the right shape here; (2) validation run before submission rather than after, using the counterparty's own rules, so discrepancies are resolved by the party that can actually fix them; (3) automated reconciliation against the counterparty's acknowledgement, since the current process discovers mismatches through email; (4) incremental and more frequent exchange where the counterparty will accept it, because the monthly cadence is a convention rather than a requirement and weekly claim counts are far more useful than monthly loss amounts; and (5) a migration path that works while counterparties remain on spreadsheets, since a solution requiring everyone to adopt a standard simultaneously will not start.

## Target Customer
MGAs and programme administrators, carriers and reinsurers receiving delegated authority reporting, and the platform vendors on both sides.

## Impact If Solved
Bordereaux production and validation is pure friction consuming analyst effort at both ends of every delegated authority relationship. Canonical generation removes it for the MGA, pre-submission validation removes the query cycle, and the higher cadence it enables is what makes the continuous performance signal in the build note achievable.
