# Emissions Reporting Adapted for Upstream Oil and Gas

**Niche:** [[niches/oil-gas-field-services/regulatory-reporting-automation/profile|Regulatory Reporting Automation]]
**Industry:** [[industries/oil-gas-field-services|Oil & Gas Field Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Environmental compliance platforms like Encamp and Sphera handle general EHS reporting but cannot perform the upstream-specific emissions calculations required by EPA GHGRP Subpart W and state methane rules.
**Tags:** #regression #tabular-ml #compliance #automation #data-integration

## The Problem
Upstream oil and gas operators must calculate and report greenhouse gas emissions under EPA's Greenhouse Gas Reporting Program Subpart W (petroleum and natural gas systems), state-level methane rules (Colorado Regulation 7, New Mexico OCEA rules, Pennsylvania GP-5A), and increasingly under ESG disclosure requirements from lenders and investors. These calculations require upstream-specific emission factor methodologies — fugitive emissions from wellhead components, pneumatic device venting rates, tank flash gas calculations, combustion emissions from flares and engines — that general EHS platforms do not support.

## What Already Exists
Encamp, Sphera (formerly thinkstep), Intelex, and EHS Insight offer environmental compliance platforms with emissions tracking, incident management, and regulatory reporting. These tools handle general emissions reporting (TRI, Tier II, air permits) well but treat upstream oil and gas as a generic source category. They do not include Subpart W calculation methodologies, component-level fugitive emission factors (API/EPA Leak Detection and Repair protocols), or state-specific methane rule calculators.

## The Customization Gap
The emissions calculation engine needs upstream-specific modules: Subpart W emission factor tables for each source category (wellheads, separators, dehydrators, tanks, pneumatics, flares), LDAR (Leak Detection and Repair) survey data integration for fugitive emission quantification, tank flash gas calculators using composition data from gas chromatography analysis, and state-specific reporting format generators for Colorado, New Mexico, Pennsylvania, and other states with standalone methane rules. The underlying platform architecture (data collection, workflow routing, audit trail) works — the domain-specific calculation layer is missing.

## Target Customer
Environmental compliance managers at independent operators with 50-500 wells in states with active methane regulations, who already use or are evaluating a general EHS platform but cannot find one that handles their upstream-specific reporting requirements.

## Impact If Solved
Eliminates the parallel spreadsheet-based emissions calculation workflow that currently runs alongside the EHS platform, reduces emissions reporting preparation from 2-3 weeks to 2-3 days per reporting cycle, and provides defensible calculation documentation that withstands EPA and state agency audits.
