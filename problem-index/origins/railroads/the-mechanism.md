# The Mechanism: Tracking, Scheduling Discipline, and a Federal Interlock

**Origin:** [[origins/railroads/profile|Railroads]]
**Tags:** #graph-theory #dynamic-programming #optimization-fundamentals #combinatorics-and-counting #time-series-forecasting #data-integration #workflow-orchestration #compliance #automation

> Three different systems get called "how railroads computerised," and they are not the same system, solving the same problem, or even close together in time. Keeping them apart is the point of this file.

## Part One: TOPS — a Database Problem, Not an Optimisation Problem

TOPS's data model is a record per car: identity, current location, load status, condition, and the waybill linking it to a shipment. The "algorithm," such as it was, was **querying and updating that record reliably across a distributed network of yard offices** — a data-integration and workflow problem, solved with 1960s mainframe batch and terminal technology.

**TOPS did not compute an optimal routing, blocking or train-makeup plan.** It made the current state of the fleet queryable. What a dispatcher did with that visibility remained a matter of experience and local judgement for decades afterward.

## Part Two: Precision Scheduled Railroading — a Discipline, Not an Algorithm

**PSR is a heuristic operating philosophy, not a computational optimisation breakthrough** — the single most important correction in this file. [[origins/railroads/the-fight|Harrison's change]] was to impose a fixed structure — published point-to-point schedules, consolidated yards, a smaller standing fleet — and hold operations to it by management discipline, not to solve a previously-intractable routing problem with new mathematics.

The genuine underlying problem PSR sits on top of — car-blocking, yard classification, crew scheduling and locomotive assignment across a shared, congested network — is a large stochastic **integer scheduling and routing problem** and **remains, honestly, only partially solved.** Genuine network-flow optimisation for blocking and yard operations is still an active area of operations-research work, not a settled, deployed capability. PSR did not close that gap mathematically; it closed it organisationally, by refusing to let trains wait for the yard to fill.

**The teaching point:** the railroad industry's most famous "computing revolution" of the last thirty years was, underneath the branding, a management decision to stop optimising locally (fill the yard, then run) in favour of a globally simpler but individually less efficient rule (run on time, regardless). That is a legitimate lever. It is not the algorithmic breakthrough it is sometimes described as.

## Part Three: Positive Train Control — a Safety Interlock, Not a Scheduling System

**PTC is mathematically and organisationally unrelated to PSR, and the two are frequently conflated because both are post-2000s "rail computing" stories.** PTC is a federally mandated collision-avoidance system. PSR is a private cost-and-schedule discipline. Neither depends on the other.

PTC was mandated by the **Rail Safety Improvement Act of 2008**, passed after the **12 September 2008 Chatsworth, California** head-on collision between a Metrolink commuter train and a Union Pacific freight train. The mechanism: onboard computers combine **GPS positioning, a digital track database and wireless data-radio communication with dispatch** to continuously check a train's speed and position against its authorised movement limits, and **automatically enforce braking** if it exceeds them — a hard interlock that does not ask the crew's permission.

The original deadline was **31 December 2015** across roughly 58,000 required route-miles. Congress extended it to **December 2018**, with the FRA authorised to grant further extensions to **31 December 2020**. The FRA confirmed PTC operational across all **57,536 required route-miles by 29 December 2020** — **twelve years after the original statutory deadline, at an industry-wide cost of roughly $15 billion.**

## What It Gave Up

**TOPS traded optimisation for visibility** — a defensible sequencing given 1960s computing limits, whose second half arguably still hasn't been fully solved sixty years later.

**PSR traded slack for cost.** Fewer spare locomotives, fewer spare crews, less time buffer — all of which lower operating ratio and all of which had, [[origins/railroads/the-fight|contested and unresolved]], also functioned as safety and service margin.

**PTC traded discretion for a hard floor.** A PTC-equipped train cannot exceed its authorised speed or movement limit no matter what the crew believes is safe in the moment — a deliberate, federally imposed removal of human judgement from one specific failure mode.

## The Transferable Pattern

> **Three different technologies can all get called "the railroad's computer system" and be doing entirely different jobs — visibility, scheduling discipline, safety enforcement — solved at different times, by different actors, and only one of them was ever a genuine optimisation win. Separating these three questions comes before proposing an algorithm for any of them.**

**Sources:** IBM corporate history, Southern Pacific TOPS; trade-press accounts of PSR's operating-ratio effects across Illinois Central, Canadian National, Canadian Pacific and CSX; Rail Safety Improvement Act of 2008 statutory text and deadlines; FRA Positive Train Control implementation status records, confirming completion 29 December 2020; 2008 Chatsworth collision investigation records.
