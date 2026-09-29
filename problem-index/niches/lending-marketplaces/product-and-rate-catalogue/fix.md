# The Rate That Changed Last Tuesday

**Niche:** [[niches/lending-marketplaces/product-and-rate-catalogue/profile|Product & Rate Catalogue]]
**Industry:** [[industries/lending-marketplaces|Lending Marketplaces]]
**Type:** Fix (Pain Point)
**One-liner:** The lender updated their rates a week ago, the email went to someone on holiday, and borrowers are still being shown the old table.
**Tags:** #quick-win #automation #data-integration #compliance #evaluation-metrics #workflow-orchestration #descriptive-statistics #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to keep hundreds of lender products, eligibility rules, rate structures and state restrictions accurate without maintaining them by hand — and whoever does it stops showing borrowers offers that do not exist.

## The Problem
Rate changes arrive by email to individual partner managers. There is no queue, no acknowledgement, no deadline and no record of what was updated when. A change can sit unactioned for a week because the recipient was away, or be missed entirely because it was mentioned in the middle of a longer message. The borrower sees an advertised rate that the lender no longer offers, which is both a bad experience and an advertising compliance exposure.

## Why It's Still Broken
Updates arrive as correspondence rather than as instructions, so they inherit the properties of email — no tracking, no owner, no deadline — and nobody converted them into a process. The volume is high enough to be tedious and low enough to seem manageable. Errors surface as individual complaints rather than as a pattern. And nobody reports update latency.

## What a Fix Looks Like
Turn the email into a tracked task. Route all rate and term communications to a shared queue rather than to individuals, which is the fix and removes the single-point-of-failure that causes most delays. Acknowledge and timestamp every change, so latency becomes visible and measurable. Set a service level for applying changes, since without one there is no definition of late. Detect changes from lender public pages as a backstop, because the published materials frequently move before the email is sent. Report update latency and the number of stale entries, which is the diagnostic nobody has. Let lenders submit changes through a form rather than prose, as structured submission removes the interpretation step entirely. Show the last-verified date on every entry internally, so staleness is apparent at a glance. Alert on high-traffic products that have not been verified recently, which prioritises the tedium sensibly. Keep an audit trail of what was displayed when, because advertising disputes require reconstructing it. And review missed changes monthly to find where the process leaks, since the pattern will point at two or three recurring causes.

## Who Feels the Pain
Borrowers shown rates that no longer exist; partner managers blamed for stale entries; compliance functions exposed on advertised terms; and lenders whose current pricing is misrepresented.

## Impact If Fixed
Updates arrive as correspondence and inherit email's properties — no owner, no deadline, no tracking. A shared queue with acknowledgement and a service level removes the single-point-of-failure behind most stale entries.
