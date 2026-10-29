# Every Stay Checked Against IPF Documentation Rules Daily

**Niche:** [[niches/psychiatric-hospitals/medicare-recertification-audit-defence/profile|Medicare Recertification, Active-Treatment Records & Audit Defence]]
**Industry:** [[industries/psychiatric-hospitals|Psychiatric Hospitals]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Psychiatric hospitals learn that a stay's certification, treatment plan or active-treatment notes were deficient when an auditor samples it, and no product checks every open stay against the IPF rules while it can still be fixed.
**Tags:** #large-language-models #transformers #gradient-boosting #compliance #evaluation-metrics #automation
**Contested on:** Every serious competitor in this niche is fighting to make each Medicare and Medicaid psychiatric day defensible when an auditor reads the record later, and whoever has the lowest share of audited paid days recouped takes the account.

## The Problem
Internal audits sample a few charts a month. A missed day-12 recertification, a treatment plan never updated, or two weeks of identical notes is found a year later, when the days are already paid and recoupable.

## Why Nobody Has Built This
The rules are IPF-specific and the evidence is prose. Coding-audit tools look at codes, and EHRs only check that a form exists, not whether its content supports the day.

## What to Build
A daily checker for every open Medicare and Medicaid stay. It tests certification and recertification dates and signers, treatment-plan currency, weekly progress notes, active-treatment evidence (groups attended, medication changes, therapy), and changes between notes. It sends each unit a short deficiency list to fix before discharge, and a risk score built on past audit findings ranks closed stays for the internal audit sample. All development runs on synthetic charts.

## Target Customer
Compliance officers at chains and freestanding hospitals, especially those under a Corporate Integrity Agreement.

## Impact If Built
If deficiencies fixed before discharge cut recoupment on audited stays from ~10% to ~5% of paid days (estimate), a hospital with $10M of audited Medicare and Medicaid payments a year keeps ~$500,000.
