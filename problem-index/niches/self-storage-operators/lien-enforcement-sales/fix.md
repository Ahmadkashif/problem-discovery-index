# The Sale Date Counted From the Wrong Notice

**Niche:** [[niches/self-storage-operators/lien-enforcement-sales/profile|Lien Enforcement & Delinquent-Unit Sales]]
**Industry:** [[industries/self-storage-operators|Self-Storage Operators]]
**Type:** Fix (Pain Point)
**One-liner:** A notice bounces, is re-sent by mail a week later, and the sale goes ahead on the original date, so the statutory clock was counted from a notice the tenant never received.
**Tags:** #workflow-orchestration #compliance #automation #quick-win #evaluation-metrics
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor is fighting to turn a delinquent unit back into money without a wrongful-sale claim. But the money comes from two places with different competitors: tenants who pay before the sale, where outreach and payment tools compete on past-due rent recovered per delinquent unit, and contents sold at the sale, where auction marketplaces compete on the share of the balance owed that each auctioned unit recovers. Decomposed into contested sub-niches below.

## The Problem
Statutes count days from a specific event: mailing, delivery, or proof the email was opened. When the first attempt fails and the notice is re-sent, the clock restarts. Facility software usually stores one notice date per stage. The auction listing is scheduled from that date, and the re-send never moves it.

## Why It's Still Broken
The re-send happens in a different system (a mail vendor, or the clerk's inbox) from the scheduler. The software was built when one certified letter was the only method. Email-with-proof rules such as California's AB 498 add a third possible start event.

## What a Fix Looks Like
Store every notice attempt with its method, result and evidence, and compute the sale date from the last valid one under the facility's state rule. Any failed or re-sent notice automatically moves the scheduled listing and alerts the clerk. Listings on auction sites are created only when the computed date is final.

## Who Feels the Pain
Lien clerks and store managers; tenants who lose belongings after a notice they never saw; operators facing the claim.

## Impact If Fixed
If ~2–5% of lien files have a re-sent notice (estimate) and a wrongful sale costs ~$5,000–25,000 to settle (estimate), an operator selling 2,000 units a year avoids ~$200,000–2.5M of exposure with a date check that costs almost nothing.
