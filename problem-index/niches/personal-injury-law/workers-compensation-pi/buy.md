# WC-Tort Lien Coordination Tracker

**Niche:** [[niches/personal-injury-law/workers-compensation-pi/profile|Workers' Compensation PI]]
**Industry:** [[industries/personal-injury-law|Personal Injury Law]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Attorneys handling parallel WC and third-party tort claims stop losing money to uncoordinated lien resolution — a single tracker shows WC carrier lien amounts, subrogation rights, and how the tort settlement allocation must account for both claims.
**Tags:** #logistic-regression #feature-engineering #evaluation-metrics #data-integration #compliance #workflow-orchestration

## The Problem
When a workplace injury has a third-party tort component (a worker is hit by a truck while on the job — WC claim against the employer's insurer, tort claim against the truck driver), the WC carrier has a statutory lien on the tort recovery. The attorney must track both claims simultaneously, knowing that the tort settlement must first reimburse the WC carrier's lien (paid medical bills and indemnity benefits) before the client receives their share. But lien amounts change as the WC carrier continues paying benefits during the tort litigation. The attorney doesn't know the final lien amount until they request a "final lien letter" from the carrier — which often takes weeks and sometimes arrives after the tort settlement has been distributed. In some states, the WC carrier must share in attorney's fees on the tort recovery (the "common fund" doctrine), reducing the effective lien. These rules are state-specific and the calculations are error-prone.

## What Already Exists
Filevine and SmartAdvocate track lien amounts as manual data entries. Medicare secondary payer compliance tools (Synergy, Tower MSA) handle Medicare/Medicaid liens but not WC carrier liens. Lien resolution companies (Garretson, Cattie & Gonzalez) negotiate liens as a service but don't provide real-time tracking tools. No existing case management platform models the interaction between WC and tort recoveries with state-specific subrogation rules.

## The Customization Gap
The missing layer is a WC-tort coordination module that integrates with the case management system and provides: real-time WC lien balance tracking (with automated lien letter requests to the WC carrier at configurable intervals), state-specific subrogation rule application (does the carrier share in attorney's fees? Is there a "made whole" doctrine? Does the carrier have first-dollar or proportional recovery?), settlement allocation modeling (given a tort settlement of $X, here's how the distribution works after WC lien, attorney's fees, and costs), and deadline tracking for lien dispute windows. This requires a continuously updated database of state-specific WC subrogation rules and common fund doctrines — information that currently lives in state statutes, case law, and the heads of experienced practitioners.

## Target Customer
Attorneys handling dual WC-tort claims who currently track lien amounts in spreadsheets and compute settlement allocations manually, risking errors that either shortchange the client or expose the firm to WC carrier collection actions.

## Impact If Solved
Prevents settlement distribution errors that expose the firm to liability — distributing funds without satisfying the WC lien can result in the carrier pursuing the attorney for the full lien amount. Reduces lien negotiation time by providing accurate, real-time lien balances instead of waiting weeks for carrier responses. Recovers client money through proper application of common fund and made-whole doctrines — in states where these apply, proper calculation can reduce the effective WC lien by 20-40%.
