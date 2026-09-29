# The Waterfall Nobody Tested

**Niche:** [[niches/identity-verification-vendors/orchestration-and-routing/profile|Orchestration & Routing]]
**Industry:** [[industries/identity-verification-vendors|Identity Verification Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The fallback vendor has not been exercised in eight months and nobody knows whether the integration still works.
**Tags:** #quick-win #workflow-orchestration #automation #evaluation-metrics #data-integration #descriptive-statistics #confidence-intervals #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to send each applicant to the verification path that will actually verify them — and whoever measures which path works for which kind of person owns the decision layer above every individual vendor.

## The Problem
The configuration has a primary vendor and two fallbacks. Almost all traffic goes to the primary. The fallbacks are invoked rarely, their integrations have not been updated in months, and when the primary has an outage — which is when the fallback matters — the fallback path fails too, because an API changed, a credential expired, or a field mapping drifted. The failure occurs at precisely the moment there is no capacity to fix it.

## Why It's Still Broken
The fallback was configured once during implementation, so it inherits the state of the world on that day — a path that is not exercised is not maintained, and nothing in the product exercises it. Testing a fallback means sending real applicants to it. Monitoring covers the primary. And outages are rare enough that the risk stays theoretical until it is not.

## What a Fix Looks Like
Exercise the fallback continuously. Send a small continuous share of traffic down each fallback path, which is the fix and both keeps the integration alive and produces the comparison data routing needs. Synthetically test every path on a schedule, since even a health check catches expired credentials and changed contracts. Monitor each vendor's availability and latency independently rather than only the aggregate. Alert on a path that has not been used in a defined period, as dormancy is the leading indicator of breakage. Rehearse an outage failover deliberately, because a plan never executed is an assumption. Version and review the configuration, since it drifts silently as vendors change their APIs. Report per-path success rates, which is a natural by-product of the continuous sample. Keep an owner for each vendor relationship and integration. Fail gracefully to manual review rather than rejecting when all paths fail, since applicants should not be rejected because of an outage. And measure time to detect a path failure, which is currently unbounded.

## Who Feels the Pain
Applicants rejected during an outage; operations teams discovering a broken fallback in a crisis; customers whose resilience exists only on a diagram; and vendors blamed for failures that were integration drift.

## Impact If Fixed
A path that is not exercised is not maintained, and nothing in the product exercises it. A small continuous traffic share keeps every fallback alive and produces the per-path comparison data routing needs anyway.
