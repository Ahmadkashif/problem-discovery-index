# Correlating a Complaint to a Request

**Niche:** [[niches/headless-commerce-vendors/cross-vendor-observability/profile|Cross-Vendor Observability]]
**Industry:** [[industries/headless-commerce-vendors|Headless Commerce Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** A customer reports that checkout failed yesterday afternoon, and there is no way to find the requests that constituted their session, so the investigation begins by guessing.
**Tags:** #data-integration #graph-theory #evaluation-metrics #automation #descriptive-statistics #worker-facing #quick-win #compliance
**Contested on:** Every serious competitor in this niche is fighting to make one trace span six companies' systems — and whoever does that solves the category's acknowledged weak point, because the standard exists and stops at every vendor boundary.

## The Problem
A customer contacts support: checkout failed twice yesterday, they do not know the time precisely, they were not signed in for the first attempt. The support agent escalates. The engineer has traces indexed by trace identifier, logs indexed by service, and vendor systems indexed by whatever each vendor uses. There is no path from a customer, an order attempt or an email address to the set of requests that made up their experience. The investigation is a search through a window of time for something that looks like the description, and most of these end unresolved.

## Why It's Still Broken
Tracing was built for engineers investigating from an alert, where the entry point is a trace identifier or a metric, and the customer-initiated entry point was not designed for. Correlating a session to traces requires propagating a session identifier through every layer including the front end, which nobody set up. Personal data considerations make some teams reluctant to index traces by customer. And the unresolved investigations are absorbed as the cost of a complex architecture.

## What a Fix Looks Like
Index the traces by the things a customer can tell you. Propagate a session identifier from the front end through every service call and into every trace and log, which is a small instrumentation change and is what makes a customer-initiated investigation possible at all — this is the fix. Index traces by session, order attempt, cart and customer where available, so a support enquiry becomes a lookup. Give the customer or the agent a reference at the point of failure, since an error screen with a reference is the cheapest correlation mechanism available and is frequently absent. Handle personal data properly with retention limits and access controls rather than by not indexing, since the investigation is a legitimate purpose and the reluctance is solvable. Capture front-end errors and correlate them to the backend trace, since a substantial share of these failures are client-side and are invisible in server traces entirely. Retain enough history for a complaint arriving days later, which the sampling strategy frequently does not. Give support agents a read-only view so routine correlations do not require an engineer. And measure the share of complaints that can be traced to a request, because it is currently low and is the number this fix moves.

## Who Feels the Pain
Engineers searching time windows for a customer's session; support agents unable to answer what happened; and customers told the problem cannot be reproduced.

## Impact If Fixed
Tracing was designed for an engineer starting from an alert and the customer-initiated entry point was never built. Propagating a session identifier and indexing by it is a small change that turns a search through a time window into a lookup.
