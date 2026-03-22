# Flat-Fee Scope Creep Detection

**Niche:** [[niches/small-law-firms/immigration-boutiques/profile|Immigration Boutiques]]
**Industry:** [[industries/small-law-firms|Small Law Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Immigration cases are typically flat-fee but scope routinely expands — unexpected RFEs, additional family members, changes in strategy — and no tool tracks actual time against the flat fee to alert the attorney when a case has become unprofitable before they've invested 40 unrecoverable hours.
**Tags:** #gradient-boosting #logistic-regression #feature-engineering #evaluation-metrics #revenue-impact #worker-facing

## The Problem
An immigration boutique charges $4,500 for an H-1B petition. The engagement letter defines the scope: initial petition preparation, filing, and standard employer correspondence. But immigration cases routinely expand beyond the defined scope: USCIS issues an RFE requiring 8-15 additional attorney hours, the employer adds a dependent requiring a separate I-539, the beneficiary's circumstances change requiring an amended petition, or the case is denied and the attorney feels obligated to assist with an appeal or re-filing. Each scope expansion erodes the flat fee — but because the firm doesn't track time, nobody knows the case has become unprofitable until the attorney "feels" it. By then, the firm has invested 30-40 hours into a case that was priced for 20 hours of work. The attorney faces an uncomfortable choice: absorb the loss, try to renegotiate the fee with a client who was promised a flat rate, or cut corners on the remaining work.

## Why It's Still Broken
Flat-fee practices resist time tracking because it contradicts their value proposition ("we charge by the case, not by the hour"). Introducing time tracking feels like a step backward and creates paralegal resentment. But without time tracking, there's no early warning system for scope creep. The firm discovers unprofitable cases only in retrospect — and by then, the loss is sunk. Experienced immigration attorneys develop intuition for scope creep warning signs (employer is unresponsive, beneficiary has a complicated background, the specialty occupation arguments are weak), but this pattern recognition takes years to develop and is unreliable under volume pressure.

## What a Fix Looks Like
A lightweight scope monitoring tool that tracks case activity without requiring traditional time entry. Instead of logging hours, the system monitors proxy signals: number of emails exchanged per case, number of documents drafted, number of INSZoom activity entries, number of client portal interactions, and milestone progression rate. A gradient-boosted model trained on completed cases establishes a "normal" activity profile for each case type and alerts the attorney when a case's activity is tracking 1.5x or 2x the expected volume — a leading indicator of scope creep. The alert comes early enough to trigger a scope review conversation with the client before the losses accumulate. The system also generates post-mortem profitability reports for completed cases, helping the attorney adjust flat fees for case types that consistently exceed expected scope.

## Who Feels the Pain
The immigration firm owner who quotes flat fees competitively to win clients, then watches margins evaporate as cases expand beyond scope — and the paralegal who works overtime on over-scoped cases knowing the firm is losing money on every additional hour.

## Impact If Fixed
Early detection of scope creep (when the case is at 1.5x expected activity instead of 3x) gives the attorney a window to renegotiate fees, bringing the client into an honest conversation about additional costs before resentment builds on both sides. For a firm where 20-30% of cases experience significant scope creep, addressing it early recovers $50K-150K in annual revenue that currently evaporates into unbilled work. The secondary benefit is data-driven flat-fee pricing: understanding true cost-to-deliver by case type enables accurate pricing that protects margins without overcharging straightforward cases.
