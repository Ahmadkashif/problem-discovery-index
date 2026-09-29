# Retries That Amplify an Origin Problem

**Niche:** [[niches/edge-cdn-providers/dynamic-application-delivery/profile|Dynamic Application Delivery]]
**Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]
**Type:** Fix (Pain Point)
**One-liner:** An origin slows down, the edge retries, the client retries, the application library retries, and a degradation becomes an outage through a multiplication nobody configured deliberately.
**Tags:** #markov-chains #descriptive-statistics #monte-carlo-methods #hypothesis-testing #confidence-intervals #quick-win #automation #workflow-orchestration
**Contested on:** Every serious competitor here is fighting to reduce tail latency for content that cannot be cached at all — and whoever does that takes the application platform account, because the bytes are trivial and the milliseconds are the entire product.

## The Problem
The origin starts responding slowly under load. The edge's retry policy retries twice. The client library retries three times. The mobile application retries on failure. The load balancer in front of the origin retries. A single user action becomes many origin requests, arriving precisely when the origin has least capacity, and the degradation becomes a complete outage. Each retry policy was configured separately by a different person, each is individually sensible, and their product is a multiplier nobody has calculated.

## Why It's Still Broken
Retry configuration is distributed across layers owned by different teams and different vendors, and nobody owns the total. Each layer's default is chosen to be helpful in isolation, which is correct for a transient single failure and catastrophic for a correlated one. The multiplication is arithmetic and nobody does it, because no single view shows all the layers. And the failure only manifests under correlated load, which is exactly when it does the most damage.

## What a Fix Looks Like
Calculate the multiplier and coordinate the layers. Enumerate the retry policies across the whole path — client, edge, load balancer, service mesh, application library — and compute the worst-case amplification, which is multiplication and regularly produces a startling number that immediately changes the configuration. Retry at one layer rather than at every layer, which is the standard resilience recommendation and is almost never implemented because no one team can see all of them. Apply exponential backoff with jitter everywhere retries remain, which is well understood and is still not the default in several widely used libraries. Implement a retry budget at the edge, capping retries as a fraction of total requests, which bounds the amplification structurally rather than relying on each layer behaving. Distinguish retryable from non-retryable failures properly, since retrying a request the origin rejected deliberately is pure amplification. Detect a retry storm in progress and shed rather than forward, which is the edge's unique ability and the reason it is the right place for the budget. And report the observed amplification factor during incidents, since the number is computable from the logs and is the evidence that makes the configuration change happen.

## Who Feels the Pain
On-call engineers watching a slowdown become an outage; origins failing under a load that is mostly their own retries; and teams whose individually sensible configurations multiply into a system nobody designed.

## Impact If Fixed
The amplification is arithmetic over configurations that already exist and is almost never computed, and the number alone typically prompts the change. A retry budget at the edge bounds the multiplication structurally, which is more reliable than expecting every layer to behave.
