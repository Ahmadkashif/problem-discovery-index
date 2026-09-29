# Autoscaling and Right-Sizing From Cloud Operations

**Niche:** [[niches/ci-cd-platforms/hosted-runner-economics/profile|Hosted Runner Economics]]
**Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Predictive autoscaling, instance right-sizing and spot capacity management are mature cloud operations practices, and CI capacity is provisioned by a concurrency limit in a pricing tier.
**Tags:** #time-series-forecasting #gradient-boosting #optimization-fundamentals #convex-optimization #evaluation-metrics #confidence-intervals #automation #revenue-impact
**Contested on:** Every serious competitor in hosted execution is fighting to deliver a started, warm, cache-local runner in seconds at the lowest cost per change — and whoever does that takes the account, because this market is compared on a spreadsheet and switching is a configuration change.

## The Problem
Forecasting demand and provisioning ahead of it is routine cloud operations. Choosing the right instance type from observed utilisation is a standard product category. Using interruptible capacity for tolerant workloads is normal practice. CI workloads are unusually well suited to all three — they are bursty, predictable, and individually restartable — and are typically run on a fixed concurrency allowance with a single instance size chosen by a human.

## What Already Exists
Predictive autoscaling with demand forecasting; right-sizing recommendations from utilisation telemetry; spot and preemptible capacity management with interruption handling; bin packing for placement; and queueing theory for capacity sizing against a latency target. All mature, widely deployed, and free or commodity.

## The Customization Gap
The adaptation is to a bursty, latency-sensitive, restartable workload. It requires: (1) forecasting at a fine time granularity, since the demand pattern has sharp working-hour and merge-queue structure and an hourly forecast misses the peak that causes the queue; (2) an objective on wait time rather than utilisation, because the point is the developer not waiting and a utilisation-optimised pool will always be too small at the peak — which is the opposite trade-off from most autoscaling and is why importing the defaults fails; (3) exploitation of restartability, since a build interrupted on spot capacity can simply be re-run, making this one of the best candidate workloads for interruptible capacity and one where it is rarely used; (4) job-class-level right-sizing, since a lint job and an integration test suite have entirely different profiles and are typically given the same machine; and (5) cache and mirror locality as a placement constraint, because a cheaper machine far from the data is not cheaper.

## Target Customer
Hosted CI vendors, cloud providers offering build services, and the platform teams running their own runner fleets on cloud capacity.

## Impact If Solved
The workload is close to ideal for these techniques and they are largely unapplied, which leaves queue time and over-provisioning coexisting. A wait-time objective rather than a utilisation objective is the adaptation that matters most, and spot capacity is an unusually good fit here.
