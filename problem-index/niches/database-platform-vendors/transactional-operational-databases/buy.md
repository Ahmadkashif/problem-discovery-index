# Queueing Theory for Connection and Concurrency

**Niche:** [[niches/database-platform-vendors/transactional-operational-databases/profile|Transactional & Operational Databases]]
**Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Sizing a server pool against an arrival rate and a service time distribution is textbook queueing theory, and database concurrency is configured by copying a number from a blog post.
**Tags:** #markov-chains #monte-carlo-methods #optimization-fundamentals #time-series-forecasting #confidence-intervals #evaluation-metrics #automation #hypothesis-testing
**Contested on:** Every serious competitor here is fighting to hold tail latency and availability under real application traffic while making a database as easy to obtain as a container — and whoever does that takes the application platform account, because those are the two properties application teams are judged on.

## The Problem
Determining how many servers are needed to hold a latency target given an arrival rate and a service time distribution is one of the oldest results in operations research, with closed-form answers for the simple cases and simulation for the rest. Database concurrency configuration — pool sizes, worker counts, connection limits, statement timeouts — is set by copying values from documentation written for different hardware and a different workload.

## What Already Exists
Queueing theory with standard models and results; simulation for systems that violate the analytical assumptions; capacity planning methodology; little's law and its operational consequences; and load testing tools that measure the inputs. All classical and taught universally.

## The Customization Gap
The adaptation is to database workloads with heavy-tailed service times and resource coupling. It requires: (1) empirical service time distributions rather than exponential assumptions, since database query durations are strongly heavy-tailed and the classical results mislead badly — which pushes toward simulation using the observed distribution, and the service can measure it; (2) modelling the coupling between concurrency and service time, because unlike a simple queue more concurrency makes each query slower through lock and resource contention, which is the key non-classical property and is why naive capacity calculations fail; (3) a tail latency objective rather than a mean, since the ninety-ninth percentile is what the application experiences and the mean is comfortably met in configurations that are failing; (4) autoscaling interaction, because the application's instance count varies and the correct configuration must hold across the range rather than at a point; and (5) a safety margin derived from the observed variability rather than a fixed multiplier, since the whole purpose is surviving the load event that has not happened yet.

## Target Customer
Managed operational database vendors, application framework and pooling projects, and platform engineering teams.

## Impact If Solved
A classical discipline answers the configuration question directly and the category answers it with folklore. Concurrency-dependent service times and a tail objective are the two adaptations, and both are measurable by the service from its own traffic.
