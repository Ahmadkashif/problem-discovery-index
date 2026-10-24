# Two Departments, Two Versions of the Same Tract

**Niche:** [[niches/oil-and-gas-producers/mineral-title-lease-administration/profile|Mineral Title & Lease Administration]]
**Industry:** [[industries/oil-and-gas-producers|Oil & Gas Producers]]
**Type:** Fix (Pain Point)
**One-liner:** Land and division orders each keep their own ownership record, and they disagree.
**Tags:** #k-nearest-neighbors #feature-engineering #evaluation-metrics #data-integration #quick-win #automation
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every competitor here is fighting to keep the operator's right to drill and produce intact. Two contests with different winners sit inside it. Before a well, the contest is building drilling title from county records, won by whoever's ownership schedules need the fewest corrections after first production. After the lease is signed, it is keeping leases alive, won by whoever loses the fewest net acres to a missed obligation. Decomposed into contested sub-niches below.

## The Problem
The land department records leases and lessors; division orders records owners and decimals. After years of amendments, deaths and sales, the two lists drift: a lessor in land is a different spelling or a deceased owner in revenue, and a lease with an owner nobody pays shows up only when the owner calls.

## Why It's Still Broken
The systems were implemented separately, and reconciling them is nobody's job until an acquisition or an audit forces it.

## What a Fix Looks Like
A monthly reconciliation that matches lessors to revenue owners by name, address and tract using fuzzy matching, flags orphans on either side, and queues each mismatch with both records side by side for the right team.

## Who Feels the Pain
Division-order analysts, lease analysts, and owners whose payments are held.

## Impact If Fixed
Clearing even ~1% of mismatched owner records each month (estimate) prevents a steady flow of suspended payments and owner complaints at almost no cost.
