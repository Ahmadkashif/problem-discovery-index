# A Status Page That Says Everything Is Fine

**Niche:** [[niches/headless-commerce-vendors/the-on-call-engineer/profile|The On-Call Engineer]]
**Industry:** [[industries/headless-commerce-vendors|Headless Commerce Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Vendor status pages report aggregate service health across all customers and regions, so a failure affecting one retailer's tenant, region or usage pattern shows as operational while their checkout is down.
**Tags:** #evaluation-metrics #change-point-detection #descriptive-statistics #confidence-intervals #automation #worker-facing #quick-win #compliance
**Contested on:** Every serious competitor in this niche is fighting to let the person holding the pager see across the vendors whose systems they are responsible for — and whoever does that shortens the incidents, because the engineer currently owns an outcome and can see one component of it.

## The Problem
The engineer checks six status pages during an incident. All six are green. One vendor is in fact degraded for their tenant specifically — a rate limit, a regional issue, a bad deployment to their shard — and the status page reflects an aggregate across thousands of customers in which that is invisible. The engineer, reasonably, concludes it is not a vendor problem and spends forty minutes looking at their own code. Status pages are the instrument the whole category relies on during incidents, they answer a question nobody is asking, and the discrepancy is systematic rather than occasional.

## Why It's Still Broken
Status pages are public marketing surfaces with an incentive to report green, and a per-tenant view would surface more incidents to more customers. Aggregate reporting is genuinely simpler and is what the tooling produces. There is no convention for a per-customer health signal. And the retailer accepts the page as evidence because it is the only thing offered.

## What a Fix Looks Like
Stop relying on the vendor's view and build your own. Measure each vendor's behaviour from the retailer's own instrumentation and treat that as the authoritative health signal, since it is the only one that describes the retailer's actual experience and it requires nobody's cooperation — this substitution is the fix. Ask vendors for a tenant-scoped health signal, which several can provide and none offer by default, and make it a procurement requirement. Compare the vendor's reported status against the retailer's measured experience continuously, which produces a record of how often the page is wrong and is a powerful commercial artefact. Alert on the retailer's measured degradation rather than on the status page, which removes the false reassurance from the incident path entirely. Record status page accuracy per vendor and use it in renewal conversations. Treat a green page with a measured degradation as an escalation trigger rather than as a contradiction to resolve. Share measured vendor behaviour across retailers where a neutral party can host it, since a vendor degraded for one tenant is frequently degraded for several and none of them can see it. And write the contractual availability definition against the retailer's experience rather than against the vendor's aggregate, because that is the number the retailer is actually buying.

## Who Feels the Pain
Engineers spending forty minutes in their own code because a page said green; retailers whose contractual availability is measured on somebody else's aggregate; and vendors whose genuine incidents reach their customers slowly.

## Impact If Fixed
The status page answers a question nobody is asking and is the instrument the whole category relies on in an incident. Retailer-side measurement is authoritative for the retailer's experience, requires nobody's cooperation, and removes the false reassurance from the incident path.
