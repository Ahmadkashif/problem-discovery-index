# The Burglary Claim Settled Without the Gate Log

**Niche:** [[niches/self-storage-operators/tenant-protection-insurance-programmes/profile|Tenant Protection & Tenant Insurance Programmes]]
**Industry:** [[industries/self-storage-operators|Self-Storage Operators]]
**Type:** Fix (Pain Point)
**One-liner:** A tenant reports a break-in, and the adjuster settles from photos and a police report while the store's own gate and lock logs, which show who opened the door and when, are never pulled.
**Tags:** #change-point-detection #hidden-markov-models #evaluation-metrics #data-integration #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to attach tenant protection or tenant insurance at move-in under each state's insurance rules, and whoever earns the most protection margin per occupied unit takes the account.

## The Problem
Burglary is the claim that drives storage losses, and the hardest to verify. The tenant says the unit was emptied; the police report repeats them. The store has a gate log showing every code entry and, where smart locks are fitted, every unit-door event. That record could show a forced entry or the tenant's own code at 2 a.m. But claims are handled by an administrator who never sees it, and the store manager is not asked.

## Why It's Still Broken
Claims sit with the administrator or the captive; access logs sit with the operator and its lock vendor. There is no standard request for the log, and pulling it by hand from a gate system takes the manager an hour they do not have.

## What a Fix Looks Like
Attach the access record to every claim automatically. When a claim is filed, the system pulls the unit's lock and gate events for the claimed period, plus the tenant's payment status and any recent move-out pattern in the access data. It summarises them for the adjuster: forced-entry signal, own-code entries, delinquency. Claims with clean corroboration pay faster, and contradictions get a call.

## Who Feels the Pain
Adjusters at administrators and captives; store managers fielding the tenant's anger; operators whose protection margin pays for unverified losses.

## Impact If Fixed
If ~5–10% of burglary claims are contradicted by the access record (estimate), a 500-store programme paying ~$2M a year in burglary claims (estimate) saves ~$100,000–200,000 a year. Honest claimants also get paid faster.
