# Commercial Building Benchmarking Data Integration

**Niche:** [[niches/energy-auditors/commercial-ashrae-auditors/profile|Commercial ASHRAE Auditors]]
**Industry:** [[industries/energy-auditors|Energy Auditors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** ENERGY STAR Portfolio Manager benchmarks commercial buildings, but auditors cannot pull benchmarking data directly into their audit workflow or energy models.
**Tags:** #data-integration #automation #quick-win

## The Problem
Before modeling a commercial building, auditors need benchmarking context: how does this building's energy use compare to peers? ENERGY STAR Portfolio Manager provides this through EUI (Energy Use Intensity) benchmarking and ENERGY STAR scores, and many jurisdictions now require annual benchmarking submissions. However, auditors access Portfolio Manager separately from their audit tools, manually transcribing utility data, building characteristics, and benchmark scores into their audit reports. When a city's benchmarking ordinance requires both a Portfolio Manager submission and an ASHRAE audit, the auditor enters the same building data twice — once in Portfolio Manager and once in their modeling software.

## What Already Exists
ENERGY STAR Portfolio Manager has a web services API that allows automated data exchange. Utility data aggregation services (ENERGY STAR's Automated Benchmarking System, WegoWise, Measurabl) pull utility bills into Portfolio Manager. Commercial building analytics platforms (Lucid, Aquicore) provide real-time energy monitoring. None of these integrate with the auditor's field-to-model-to-report workflow.

## The Customization Gap
Auditors need a Portfolio Manager integration that: pulls existing benchmarking data (EUI, ENERGY STAR score, utility consumption) into their audit workflow as pre-populated fields, uses the ENERGY STAR score to prioritize ECM analysis (a building scoring 30 needs different measures than one scoring 70), feeds audit-collected building data back to Portfolio Manager to update the benchmarking submission (satisfying ordinance requirements without separate data entry), and includes benchmarking comparisons in the audit report automatically.

## Target Customer
Commercial energy auditors operating in jurisdictions with benchmarking ordinances (New York, Chicago, Boston, San Francisco, Seattle, and 30+ other cities) who currently manage Portfolio Manager submissions separately from their audit work.

## Impact If Solved
Eliminates 2-4 hours of duplicate data entry per commercial audit, ensures benchmarking submissions and audit reports use consistent data, and provides auditors with peer comparison context that improves ECM prioritization and client communication.
