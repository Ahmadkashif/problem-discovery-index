# Support Engineer on Cache Misses and Origin Errors

**Industry:** [[edge-cdn-providers|Edge & CDN Providers]]
**Type:** Worker Life Changing
**One-liner:** CDN support engineers stop spending every ticket explaining that a cache miss was caused by the customer's own response headers, because the analysis can be delivered to the customer before they open the ticket.
**Tags:** #gradient-boosting #bert #k-means-clustering #change-point-detection #evaluation-metrics #automation #workflow-orchestration #worker-facing

## The Problem
A customer's hit ratio is lower than they expected, or their origin is receiving more traffic than it should, or users are seeing errors. They open a ticket.

The cause is usually in the customer's own application. A response header that prevents caching. A cookie set on every response, which fragments the cache key. A query parameter appended by an analytics tag, creating a unique key per visitor. A Vary header that is broader than necessary. An origin returning intermittent errors that the CDN faithfully passes through. A purge issued far more broadly than intended.

The support engineer establishes this by reading the customer's configuration, sampling their traffic, and identifying the header or parameter responsible. It takes time, and the outcome is telling a customer that the problem is theirs — which is true, unwelcome and repeated many times a day.

The analysis is mechanical. The provider carries every request and response and could identify a cache-defeating header or a fragmenting parameter automatically, continuously, for every customer.

## Why It Matters to the Worker
CDN support engineers are strong network and HTTP specialists, and the queue rarely requires that depth. It requires patiently explaining caching semantics to application developers who did not choose to become experts in them.

The delivery problem is the hard part of the job. Telling a customer that their low hit ratio is caused by their own analytics tag is correct and lands as blame, so the engineer manages a relationship while delivering a finding. Doing that fifteen times a day is wearing, and the engineer knows the finding will recur next month at another customer.

The recurrence is what makes it demoralising. Every experienced engineer in the function can list the ten causes that account for most tickets, and none of them are detected proactively, so the queue is a treadmill of the same ten explanations.

## What a Solution Looks Like
Continuous configuration analysis delivered to the customer before the ticket. Cache-defeating response headers, fragmenting query parameters, unnecessarily broad Vary headers, cookies set on cacheable responses — all detectable from traffic and all reportable in the customer's own dashboard with the specific example and the fix.

Hit ratio decomposition. A customer with a low hit ratio should see exactly why: this proportion of misses is caused by this header, that proportion by this parameter, this proportion is genuinely uncacheable. That decomposition converts an argument into a work list.

Origin error attribution, distinguishing errors originating at the customer's application from those introduced in transit, definitively, so the blame question is settled by evidence rather than by discussion.

Purge impact analysis, since over-broad invalidation is a common and self-inflicted hit ratio problem that customers do not realise they are causing.

And clustering of tickets so the ten recurring causes are visible as a product finding — a default that should change, a documentation gap, a validation that should exist.

## Impact If Solved
CDN support is dominated by mechanically detectable configuration problems in customers' own applications, delivered as unwelcome findings by engineers whose expertise is not required for it. Proactive detection removes the volume and the blame dynamic together, and the customer gets the answer weeks before they would have asked.
