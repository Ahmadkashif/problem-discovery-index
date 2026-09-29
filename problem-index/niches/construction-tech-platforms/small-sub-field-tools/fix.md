# Entering the Same Day Into Three Systems

**Niche:** [[niches/construction-tech-platforms/small-sub-field-tools/profile|Small Subcontractor Field Tools]]
**Industry:** [[industries/construction-tech-platforms|Construction Tech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A small subcontractor enters the same day's work into the general contractor's portal, its own payroll system and its own accounting, three times, by hand, because none of them speak to each other and the sub is too small to matter to any of the vendors.
**Tags:** #data-integration #evaluation-metrics #descriptive-statistics #workflow-orchestration #automation #worker-facing #quick-win #revenue-impact
**Contested on:** Every serious competitor selling to small subcontractors is fighting to let a foreman with dirty hands and a phone record what happened in under a minute, from a site with no signal — and whoever gets that interaction shortest takes the account.

## The Problem
The general contractor requires daily reports in its platform. Payroll requires hours by job and cost code. Accounting requires the same hours against the same jobs to produce job costing. The owner, or his wife, or a part-time bookkeeper, enters the same information three times every week. On jobs for three different general contractors using three different platforms, it is five or six times. The duplication is not a rounding error in this business — it is most of the administrative burden of running a small subcontracting company, and it is performed after hours by the person who is also estimating tomorrow's bid.

## Why It's Still Broken
The small subcontractor is nobody's integration priority. General contractor platforms are built for the GC and treat subcontractor users as guests, with limited or paid API access. Payroll and accounting vendors integrate with each other and with enterprise construction systems, not with the sub's field tool. Each individual integration is small work and there is no one party for whom the whole set is worth building — the sub cannot pay for it and the vendors do not compete for the sub. So the person at the kitchen table absorbs it, indefinitely.

## What a Fix Looks Like
Enter once and push out. A single field record — hours by person, by job, by cost code, with the day's narrative and photos — becomes the source for all three destinations. The general contractor's daily report is generated in that platform's required shape and submitted through whatever channel is available, including form filling where no API exists, because the constraint is the GC's product and not the sub's willingness. Payroll and accounting receive the same hours through their standard integrations, which do exist at this end. The subcontractor's own job costing is a by-product rather than a fourth entry. Where a GC platform genuinely cannot be written to, the fix is still worth most of its value, because two of the three entries disappear.

## Who Feels the Pain
The owner or bookkeeper doing evening data entry; foremen asked for the same numbers by two people; and the business itself, whose job costing is late because the entry is late.

## Impact If Fixed
Eliminating duplicate entry recovers five to ten hours a week in a business where that time comes directly out of estimating and selling. It also makes job costing weekly rather than monthly, because the delay was never the calculation — it was the typing.
