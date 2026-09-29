# Slowly Changing Dimensions From Data Warehousing

**Niche:** [[niches/revops-consultancies/snapshot-retention/profile|Forecast Snapshot Retention]]
**Industry:** [[industries/revops-consultancies|RevOps Consultancies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Data warehousing solved keeping history of changing records decades ago, and revenue systems overwrite in place.
**Tags:** #data-integration #automation #workflow-orchestration #compliance #evaluation-metrics #descriptive-statistics #sets-and-logic #quick-win
**Contested on:** Every serious competitor in this niche is fighting to capture every forecast at every level before it is overwritten, because nothing downstream is possible without that series — and whoever captures it takes the account.

## The Problem
Data warehousing solved this exact problem long ago and gave it a name. Slowly changing dimension handling, point-in-time snapshots, temporal tables and change data capture all exist to answer the question of what a record looked like at a given moment. The patterns are textbook, the tooling is commodity, and no data engineer would design a system where the history of a business-critical value is destroyed weekly. Revenue systems do exactly that.

## What Already Exists
Slowly changing dimension patterns; point-in-time snapshot tables; temporal table support in databases; change data capture from operational systems; and as-of query semantics.

## The Customization Gap
The adaptation is to a CRM whose history facilities are partial and whose semantics are business-defined. It requires: (1) capture from a SaaS platform through APIs with rate limits rather than from a database with change logs — this is the substantive difference and shapes the whole capture design; (2) the business meaning of a forecast requiring capture of a hierarchy rather than a row; (3) snapshot timing that must align to a business rhythm rather than a technical schedule; (4) fields that are business-configured and change definition over time, so the schema itself is a slowly changing thing; and (5) a buyer who is a revenue operations person rather than a data engineer, so it must arrive as a product rather than a pattern.

## Target Customer
Revenue operations teams, RevOps consultancies, CRM and revenue intelligence vendors, and data platform providers.

## Impact If Solved
Warehousing solved keeping the history of changing records decades ago with textbook patterns and commodity tooling. Capture from a rate-limited SaaS API on a business rhythm, delivered to a non-engineer, is what has to be productised.
