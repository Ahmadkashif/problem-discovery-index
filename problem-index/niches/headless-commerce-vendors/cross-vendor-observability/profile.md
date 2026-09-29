# Cross-Vendor Observability

**Parent Industry:** [[industries/headless-commerce-vendors|Headless Commerce Vendors]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to make one trace span six companies' systems — and whoever does that solves the category's acknowledged weak point, because the standard exists and stops at every vendor boundary.

## Profile
**Market Size:** ~$380M US
**Share of Parent Industry:** ~9% of category revenue
**Digital Adoption:** Low — the acknowledged weak point
**Target Buyer:** Platform engineering across the composition
**Automation Potential:** Very High — the standard and the tooling exist

## What Makes This a Distinct Niche
Observability across the composed stack is the acknowledged weak point, with distributed tracing available and inconsistently implemented across vendor boundaries. The standard for propagating a trace across service boundaries is published, widely adopted inside organisations, and stops the moment a call crosses into a vendor's system — which is every interesting boundary in this architecture. The result is that a request the customer experiences as one operation is observable as six disconnected fragments, only one of which the retailer holds. The capability is not missing; the adoption across a commercial boundary is, and that is a coordination problem rather than a technical one, which is precisely why it has not been solved by the engineering that solved everything around it.

## Current Tools & Gaps
Tracing inside the retailer's own services, vendor-specific dashboards, and correlation by timestamp. The gaps: trace context is not propagated into or out of vendor systems; vendors do not return their own timing in a usable form; there is no agreed convention for commerce spans; the retailer cannot see inside a vendor's processing even in aggregate; and correlating a customer complaint to a trace is frequently impossible.

## Problems
- [[niches/headless-commerce-vendors/cross-vendor-observability/build|🔨 Build: One Request, Six Disconnected Traces]]
- [[niches/headless-commerce-vendors/cross-vendor-observability/buy|🛒 Buy: Distributed Tracing Standards]]
- [[niches/headless-commerce-vendors/cross-vendor-observability/fix|🔧 Fix: Correlating a Complaint to a Request]]
