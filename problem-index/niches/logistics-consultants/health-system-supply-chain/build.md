# Par Levels Learned From Actual Clinical Usage

**Niche:** [[niches/logistics-consultants/health-system-supply-chain/profile|Health-System Supply Chains]]
**Industry:** [[industries/logistics-consultants|Logistics Consultants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Hospital par levels are set from what was restocked, which includes everything nurses hoarded, rather than from what was used on patients.
**Tags:** #gradient-boosting #time-series-forecasting #probability-distributions #monte-carlo-methods #feature-engineering #data-integration #worker-facing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to set par levels and replenishment that clinical units trust enough to stop keeping shadow stock, and whoever wins that trust captures the inventory savings everyone else only models.

## The Problem
A medical-surgical unit's par for a dressing kit is the quantity a technician restocks to each day. If nurses pull extra to a cart or a drawer, restock volume rises and the next par review raises the par. Restock history measures distrust as much as demand, so par programmes built on it lock in the hoarding they were meant to remove.

## Why Nobody Has Built This
Usage on patients is recorded in other systems — charge capture, the electronic health record's documentation of supplies, procedure and case records — owned by clinical and revenue teams, not supply chain. Consultants rarely get access in a study timeframe, and joining clinical records to supply data raises privacy review the study budget does not cover.

## What to Build
A demand model per unit and item driven by clinical activity: census, admissions, procedure schedules and case mix, with consumption estimated from de-identified charge capture and case-cart pick records. Par levels and replenishment frequency are then sized to a stated stockout risk, and the gap between modelled usage and restock volume is reported per unit as an estimate of hoarding.

## Target Customer
VPs of supply chain at multi-hospital systems running a consolidated service centre, and the consultancies designing their replenishment programmes.

## Impact If Built
Par levels sized to patient activity rather than restock habits, with unit-level evidence a supply chain leader can take to nursing leadership; savings in on-hand inventory and expired product are plausible at ~10–20% of unit stock (estimate).
