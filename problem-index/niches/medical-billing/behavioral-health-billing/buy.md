# BH Billing Module for Generic PM Systems

**Niche:** [[niches/medical-billing/behavioral-health-billing/profile|Behavioral Health Billing]]
**Industry:** [[industries/medical-billing|Medical Billing]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Generic PM systems used by billing companies don't understand BH carve-out networks, psychotherapy code time requirements, or 42 CFR Part 2 disclosure restrictions — a BH-specific billing module would prevent the category of denials unique to behavioral health claims.
**Tags:** #decision-trees #feature-engineering #compliance #data-integration #workflow-orchestration #automation

## The Problem
When a billing company takes on behavioral health clients and processes their claims through AdvancedMD or Kareo, the PM system treats BH claims like any other medical claim. It doesn't know that a patient's Blue Cross card may route BH claims to Optum Behavioral Health (a carve-out with a different provider directory, different fee schedule, and different submission portal). It doesn't validate that 90837 (53+ minute psychotherapy) requires the provider's note to document at least 53 minutes of face-to-face psychotherapy time. It doesn't flag that a SUD (substance use disorder) claim may require redaction of certain information under 42 CFR Part 2 before coordination of benefits with a secondary payer. These BH-specific requirements cause denials that a generic PM system cannot prevent because it has no concept of BH billing rules.

## What Already Exists
BH-specific EHRs (TherapyNotes, SimplePractice, Valant) handle BH clinical documentation and basic claim generation but are designed for the provider, not the billing company. Generic PM systems handle claim lifecycle management but lack BH-specific validation. Clearinghouses process BH claims without BH-specific scrubbing rules.

## The Customization Gap
A BH billing module that plugs into generic PM systems and adds: (1) Carve-out network detection — maintains a database mapping medical payers to their BH carve-out administrators, automatically routing BH claims to the correct entity and validating provider credentialing with the carve-out network. (2) Time-based code validation — cross-references the billed CPT code (90834 vs. 90837) against documented session duration, flagging claims where the time documented doesn't support the code selected. (3) Authorization cadence tracking — for each BH payer, tracks the authorization cycle (number of sessions authorized, review intervals, reauthorization lead time) and alerts before authorization expires. (4) 42 CFR Part 2 compliance layer — when processing SUD claims, applies disclosure restrictions to coordination of benefits and secondary payer communications, ensuring that SUD diagnosis information is not transmitted to entities without proper consent. This module makes a generic PM system BH-aware without requiring the billing company to switch to a BH-specific platform.

## Target Customer
Medical billing companies that serve behavioral health providers alongside their medical clients, using generic PM systems that lack BH-specific billing rules, experiencing higher denial rates on BH claims than on medical claims and unsure why.

## Impact If Solved
Reduces BH-specific denial rate by 30-50% by preventing carve-out routing errors (the single largest BH denial cause), time-code mismatches, and authorization lapses. For a billing company processing 1,500 BH claims/month with a 15% BH denial rate, cutting that to 8% prevents 105 denials/month × $120 average BH claim = $12,600/month in preserved revenue. Eliminates the 42 CFR Part 2 compliance risk that currently makes many billing companies refuse to take on SUD treatment clients.
