# Level-Funded and Stop-Loss Quoting Engines Adapted to PEO Prospects

**Niche:** [[niches/professional-employer-organizations/new-client-health-underwriting/profile|New-Client Health Underwriting]]
**Industry:** [[industries/professional-employer-organizations|Professional Employer Organizations]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Carriers and stop-loss underwriters already quote small groups from a census and a prescription score in minutes; a PEO needs the same engine to price admission to a pool, with workers' comp and unemployment risk on the same decision.
**Tags:** #gradient-boosting #logistic-regression #feature-engineering #evaluation-metrics #automation #data-integration
**Contested on:** Every serious competitor in this niche is fighting to decide, from a census, a few health questionnaires and a prescription-history score, which 25-person prospects to admit to the master plan and at what rate before the broker's quote deadline, and whoever's admitted groups run closest to their priced loss ratio in the first plan year takes the account.

## The Problem
PEO underwriters quote by moving data between a census spreadsheet, a morbidity-score portal, a carrier rating tool and a workers' comp rating sheet, then assembling a composite bid by hand.

## What Already Exists
Level-funded carriers and medical stop-loss underwriters run small-group quoting engines that take a census and prescription-history scores and return a rate and an accept or decline. The stop-loss side is logged under [[niches/self-insured-benefit-pools/medical-stop-loss-underwriters/profile|🔍 Medical Stop-Loss Underwriters & MGUs]].

## The Customization Gap
A PEO's version must price entry to a pooled master plan rather than a stand-alone group, which means composite or tiered rates set against the PEO's plan rate table and pooling point. It must apply the PEO's own risk appetite by NAICS code (Insperity avoids certain higher-risk codes), combine the health decision with workers' comp class rates and the client's unemployment experience into one bundled price, and offer a workers' comp-only or HR-only fallback when health is declined. Every step must also be recorded in the acceptance ledger.

## Target Customer
New-business underwriting teams at mid-sized PEOs that quote hundreds of groups a month without in-house modelling staff.

## Impact If Solved
Quote turnaround measured in hours rather than days, with the PEO's appetite applied consistently, on an engine whose core already exists.
