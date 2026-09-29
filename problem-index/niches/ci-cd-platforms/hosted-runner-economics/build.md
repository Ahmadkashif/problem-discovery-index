# Queue Time Nobody Counts

**Niche:** [[niches/ci-cd-platforms/hosted-runner-economics/profile|Hosted Runner Economics]]
**Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A large share of the time between pushing a change and getting a result is spent waiting for a runner and warming a cold machine, and neither is reported as part of pipeline duration.
**Tags:** #time-series-forecasting #gradient-boosting #optimization-fundamentals #descriptive-statistics #evaluation-metrics #confidence-intervals #automation #revenue-impact
**Contested on:** Every serious competitor in hosted execution is fighting to deliver a started, warm, cache-local runner in seconds at the lowest cost per change — and whoever does that takes the account, because this market is compared on a spreadsheet and switching is a configuration change.

## The Problem
A developer pushes at 10:04 and sees a result at 10:19. The pipeline duration is reported as nine minutes. The other six were spent waiting for a runner during the morning peak, starting a fresh machine, installing tools that are identical on every run, and pulling dependencies from a mirror in another region. None of that is in the reported duration, none is in the vendor's performance claims, and the developer experiences all of it.

## Why Nobody Has Built This
Duration is measured from job start because that is when the vendor's meter begins, which makes queue time invisible in exactly the reporting the customer sees. Cold start is treated as inherent to ephemeral execution rather than as a cost to be engineered away, although warm pools and snapshotting make most of it avoidable. Capacity is provisioned for the average and the demand is strongly peaked around working hours and merge queues, which is forecastable and mostly not forecast. And no vendor benefits from publishing a metric on which they may compare badly.

## What to Build
Optimise and report the whole interval from push to result. Forecast demand, which in this workload is unusually predictable — working hours, days of the week, release cadences, merge queue bursts — and provision warm capacity against the forecast rather than reacting to the queue, which is where most queue time comes from. Maintain warm pools with the toolchain already present, so cold start is paid rarely rather than on every job. Snapshot the prepared environment rather than rebuilding it, which is standard in other ephemeral compute contexts and is not in this one. Place execution near the cache and the dependency mirrors, and report the data transfer share of each job so a customer can see it. Right-size per job class from observed resource use rather than per pipeline from a human guess, since most jobs are given the wrong instance and the error runs in both directions. And report time-to-result rather than execution time, including queue and startup, because that is what the developer experiences and what the vendor should be judged on.

## Target Customer
Platform teams with high pipeline volume, hosted CI vendors competing for exactly those accounts, and the cloud providers whose capacity underlies all of them.

## Impact If Built
Queue and startup are a large share of the interval that matters and are excluded from the metric everyone reports. Forecast-driven warm capacity addresses the largest component, and reporting time-to-result would change what the market competes on.
