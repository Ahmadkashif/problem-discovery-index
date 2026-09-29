# The Same Exception Every Month

**Niche:** [[niches/ap-automation-vendors/invoice-exception-handling/profile|Invoice Exception Handling]]
**Industry:** [[industries/ap-automation-vendors|AP Automation Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** This vendor's invoice has excepted for the same reason every month for two years and the fix takes four minutes each time.
**Tags:** #quick-win #descriptive-statistics #automation #evaluation-metrics #workflow-orchestration #worker-facing #confidence-intervals #data-integration
**Contested on:** Every serious competitor in this niche is fighting to resolve the fifteen to thirty percent of invoices that survive automation — and whoever learns from how humans resolved the last million of them automates the part the category has never touched.

## The Problem
A supplier invoices with their legal entity name while the master file holds their trading name. Every invoice excepts. A clerk matches it manually, every month, for years. Another supplier includes freight on a separate line the purchase order does not contain, so every invoice fails three-way match by a small amount. Another bills in arrears for a service with no purchase order at all. Each is a known, stable, trivially fixable pattern, and each is rediscovered and re-resolved every cycle.

## Why It's Still Broken
The queue is worked item by item, so nobody sees the pattern across months — a workflow that presents one invoice at a time makes a two-year recurrence invisible. Fixing the root cause means changing a master record or a tolerance, which belongs to someone else. Clerks are measured on invoices processed. And no report groups exceptions by vendor and reason.

## What a Fix Looks Like
Group the queue and fix the repeats. Report exceptions by vendor and by reason over time, which is the fix and will show that a small number of vendors account for a large share of the queue. Propose the specific remedy for each recurring pattern — add the name variant, adjust the tolerance, create a standing purchase order — since the remedies are obvious once the pattern is visible. Apply the remedy with one action, because the barrier is usually effort rather than knowledge. Show the clerk that this exception has occurred thirty times before and how it was resolved, which turns four minutes into ten seconds even before any fix. Count the hours each recurring pattern consumes, as that number is what gets the root cause prioritised. Flag new recurring patterns as they emerge, so the list stays current. Give procurement the vendor-level view, since some fixes require a conversation with the supplier. Track whether applied remedies actually stopped the recurrence, because some will not. Compare exception profiles against other customers of the same supplier, which is available and would show whether the problem is the vendor or the buyer's setup. And measure the queue's composition, since it is currently just a number.

## Who Feels the Pain
Clerks re-resolving the same item monthly; AP managers whose queue never shrinks; suppliers paid late for reasons nobody addresses; and customers paying for automation that handles the easy cases.

## Impact If Fixed
A workflow that presents one invoice at a time makes a two-year recurrence invisible. Grouping exceptions by vendor and reason surfaces the handful of stable patterns behind most of the queue and each has an obvious remedy.
