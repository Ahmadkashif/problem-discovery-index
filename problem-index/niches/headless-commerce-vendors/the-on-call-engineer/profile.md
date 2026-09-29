# The On-Call Engineer

**Parent Industry:** [[industries/headless-commerce-vendors|Headless Commerce Vendors]]
**Category:** Underserved Audience
**Contested on:** Every serious competitor in this niche is fighting to let the person holding the pager see across the vendors whose systems they are responsible for — and whoever does that shortens the incidents, because the engineer currently owns an outcome and can see one component of it.

## Profile
**Market Size:** ~$260M US in incident cost and on-call attrition
**Share of Parent Industry:** ~6% of category revenue
**Digital Adoption:** None — an incident across systems they cannot see
**Target Buyer:** Retail engineering organisations
**Automation Potential:** High — the visibility is buildable within the architecture

## What Makes This a Distinct Niche
An on-call engineer owns an incident spanning six vendors' systems on the highest-revenue day of the year, with visibility into their own integration code and nothing else. They can see that checkout is failing and cannot see whether the payment provider, the tax service, the inventory service or the commerce platform is the cause; they have no access to any of those systems, no way to raise a priority incident with most of them outside business hours, and no standing to demand an answer. They are accountable for the retailer's revenue and equipped with their own logs. It is the operational expression of the accountability vacuum, experienced by one person at three in the morning.

## Current Tools & Gaps
Their own monitoring, vendor status pages, support portals and an account manager's phone number. The gaps: no cross-vendor tracing; vendor status pages report the vendor's view rather than the retailer's experience; no contractual incident response commitment from most vendors; no single incident channel spanning the parties; and no runbook for a failure whose cause is somebody else's system.

## Problems
- [[niches/headless-commerce-vendors/the-on-call-engineer/build|🔨 Build: Owning an Incident You Cannot See Into]]
- [[niches/headless-commerce-vendors/the-on-call-engineer/buy|🛒 Buy: Incident Command and Multi-Party Response]]
- [[niches/headless-commerce-vendors/the-on-call-engineer/fix|🔧 Fix: A Status Page That Says Everything Is Fine]]
