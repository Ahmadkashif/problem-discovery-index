# Build: Delivered Versus Promised

**Niche:** The Content Reviewer
**Industry:** [[industries/content-moderation-services|Content Moderation Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An assurance layer that measures whether the wellness provisions written into a moderation contract were actually delivered on each shift, and reports the gap to the party that specified them.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #change-point-detection #compliance #worker-facing #data-integration
**Contested on:** Whether the protections a reviewer is promised in a contract are the protections they actually receive on a shift.

## The Problem

Moderation contracts increasingly specify worker protections. So many minutes of wellness time per shift. Access to clinical support within a defined window. Limits on consecutive time in severe queues. Break structures. Language-appropriate counselling. These provisions exist because of litigation, journalism and regulatory attention, and platforms point to them when asked about their supply chain.

Nothing measures whether they are delivered. The vendor reports throughput, turnaround and quality, because those are the reported terms. Wellness provisions are written into the agreement and then live in an operational reality where volume spikes, adherence targets and staffing shortfalls all push against them — and when something has to give on a bad Tuesday, it is not the service level.

The result is a system where a provision that is honoured and one that is systematically cancelled produce identical documentation. The platform sees a contract with good terms. The vendor sees a service level being met. The reviewer experiences a wellness session that was cancelled for the fourth week running and has no way to make that fact exist anywhere.

This is not primarily a story about bad faith. It is that nobody built the instrument, so the erosion is invisible to everyone above the team-lead level who might have prevented it.

## Why Nobody Has Built This

**Measuring creates evidence of breach.** The instant delivery is measured, a gap becomes a documented contractual failure with financial and legal consequences. The vendor is the party who would have to build it and the party it would indict. No commercial logic supports that, which is why it has to be specified by the client or required externally.

**Attendance is not delivery and the difference is hard.** Recording that a wellness session was scheduled is easy; recording that it happened, was the right length, was in the right language, and was not a group session with forty people is much harder, and the easy version produces a comfortable number that means nothing.

**Self-report is compromised by the power relationship.** Asking reviewers whether they received their break, through a system their employer administers, in a job with high turnover and easy replacement, does not produce reliable data. Any credible instrument needs a route that does not run through the employer.

**It spans systems nobody joins.** Scheduling, queue assignment, badge and presence data, counselling bookings and payroll all sit in different systems, sometimes different vendors, and the join is the product.

**Privacy cuts both ways, genuinely.** Tracking whether an individual took a break is surveillance. The instrument has to report reliably at the cohort and site level while resisting individual monitoring, and getting that boundary right is a real design constraint rather than a compliance footnote.

## What to Build

**Instrument delivery from operational systems, not from self-report.** Scheduled versus actual wellness time, derived from queue assignment and presence data. Counselling appointment requests versus appointments held, with the interval between. Consecutive severe-queue time against the specified limit, from routing records. Break duration and displacement. All of it computed from systems the operation already runs, without asking anyone to fill in a form.

**Report at cohort and site level by default.** Individual-level data used only for enforcing protective limits in routing, never surfaced as a performance or attendance signal. The distinction has to be architectural and auditable, because a wellness instrument repurposed into a surveillance tool would be worse than none and the workforce will assume that is what it is.

**Add a confidential channel that does not route through the employer.** An independent mechanism for reviewers to report that a provision was not delivered, aggregated and reported without attribution, with enough volume protection that individual reports are not identifiable. Emergency services and healthcare both have well-tested versions of this, and it is the only way to capture what the operational data cannot see.

**Report to the party that specified the term.** The platform wrote the provision and is the only actor with the leverage to enforce it. Delivery reporting should go to them on the same cadence as service-level reporting, which is the change that makes the whole thing self-sustaining.

**Detect erosion as a pattern.** Alert when delivery degrades — a site where wellness time has been cancelled three weeks running, a shift where severe-queue limits are routinely exceeded, a language where counselling wait times have doubled. Erosion is gradual and is invisible without a trend.

**Design for third-party audit.** The most credible form of this is operated independently and audited, because a vendor self-reporting its own compliance carries limited weight with a regulator, a court, or the reviewers themselves.

## Target Customer

Platforms are the buyer, not vendors. They specified the provisions, they carry the reputational and increasingly the regulatory exposure for supply-chain labour conditions, and they are the only party whose interest aligns with measuring delivery. The argument is simple: you are paying for protections you cannot confirm exist.

Secondary: regulators and auditors as supply-chain labour standards firm up; worker organisations and worker-representation bodies as an independent evidence source; and insurers underwriting this line of business, who currently price a risk nobody quantifies.

## Impact If Built

The gap between the contract and the shift becomes visible for the first time, which is the precondition for it closing. Provisions that are currently eroded quietly would be eroded visibly, and visible erosion gets fixed.

It gives platforms something they need and cannot get: a defensible account of working conditions in their supply chain, based on operational data rather than on a supplier's assurance.

And it changes what a good vendor can prove. Firms that genuinely deliver their provisions are currently indistinguishable from those that do not, which means the market rewards the cheaper option — and delivery measurement is what would let conditions become something to compete on.
