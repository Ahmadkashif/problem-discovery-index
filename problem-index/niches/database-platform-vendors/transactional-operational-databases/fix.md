# Failover Measured From the Database's Side

**Niche:** [[niches/database-platform-vendors/transactional-operational-databases/profile|Transactional & Operational Databases]]
**Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** A managed service reports failover completed in thirty seconds and the application was unavailable for eleven minutes, because the clients did not reconnect and nobody measures that half.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #survival-analysis #quick-win #automation #worker-facing
**Contested on:** Every serious competitor here is fighting to hold tail latency and availability under real application traffic while making a database as easy to obtain as a container — and whoever does that takes the application platform account, because those are the two properties application teams are judged on.

## The Problem
A failover occurs. The service's own record shows a new primary accepting writes thirty-one seconds later, which meets the advertised objective. The application was down for eleven minutes: connection pools held stale connections, the driver's timeout was longer than anyone realised, the domain name cached, retries hammered the recovering instance, and one service required a restart. Every one of those is on the client side of a boundary the vendor's measurement stops at, and the customer's outage is the sum of both halves while the reported number covers one.

## Why It's Still Broken
Vendors measure what they control, which is defensible and produces a recovery objective that is true and not useful. The client-side behaviour depends on driver configuration, pool settings, name resolution caching and retry policy, all owned by the application team and none documented together. Failover is also rare enough that most applications have never actually experienced one outside a planned maintenance window, so the client-side deficiencies are undiscovered until the unplanned event.

## What a Fix Looks Like
Measure and fix the whole path. Define the recovery objective end to end — time until the application is serving successfully again — and measure it, which is the number the customer experiences and requires client-side observation the vendor can obtain through its own drivers. Test it routinely by triggering failovers in non-production and, with consent, in production, since an untested failover path is the same untested critical path the rollback niche describes and decays the same way. Ship drivers and reference configurations with correct timeout, retry and name resolution behaviour as defaults, because the client-side deficiencies are a small, known and enumerable set that every customer rediscovers. Detect dangerous client configurations from the connection behaviour the service observes, and warn — a driver with a timeout longer than the failover objective is a guaranteed extended outage and is visible to the vendor. Handle the retry storm explicitly, since a recovering primary being hit by every client's retries simultaneously is a predictable secondary failure. And publish the end-to-end distribution rather than a single objective, because the tail is what the customer will experience on the day.

## Who Feels the Pain
Application teams whose eleven-minute outage is reported as a thirty-second failover; on-call engineers restarting services after a database event; and organisations whose recovery objectives describe half the path.

## Impact If Fixed
The customer's outage is the sum of both halves and the reported number covers one, which is the measurement gap at the centre of this complaint. Correct driver defaults and warning on dangerous client configurations address a small, known set of causes that every customer currently rediscovers alone.
