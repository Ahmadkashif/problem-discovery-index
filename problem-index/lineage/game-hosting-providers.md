# Lineage: Game Hosting Providers

**Industry:** [[industries/game-hosting-providers|Game Hosting Providers]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** Agones — the open-source Kubernetes controller whose GameServer and Fleet resources give a dedicated game server an Allocated state that scale-down and rolling updates will not delete
**Builder:** Google
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A dedicated game server is a strange workload, and general-purpose infrastructure kept getting it wrong.

It holds the whole match simulation in memory. It lives for minutes or hours, not months. Each player's client must connect straight to that process's IP and port, because a load balancer adds latency to a game that is measured in milliseconds. And, critically, **it cannot be killed early**: terminating a web server loses a request, terminating a game server ends a match for everyone in it.

Those properties broke the operating model that the rest of the cloud had converged on. Container orchestrators assume replicas are interchangeable, sit behind a load balancer, and can be removed at will when demand falls. A studio that wanted to scale its fleet up for a launch and back down afterwards therefore faced a choice: build a proprietary allocator, or accept that every scale-down would disconnect players. Google's own launch announcement put it plainly — the game industry "has created a myriad of proprietary solutions."

## What Got Built

Agones, announced on 14 March 2018, extends Kubernetes with custom resources shaped around that lifecycle.

- A **GameServer** resource that moves through explicit states — Scheduled, RequestReady, Ready, Allocated, Shutdown — reported by the game process itself through an SDK.
- A **Fleet** of warm GameServers held in Ready, from which a matchmaker requests one when a match forms; the server then flips to Allocated.
- A controller that respects that flip. Per the Agones documentation, "Allocated GameServers are not deleted until they are specifically shutdown through the game servers SDK, as they are expected to have players on them"; rolling updates shut down Ready servers while "skipping Allocated GameServers."

That one state is the design. Everything else is Kubernetes; the Allocated flag is what makes Kubernetes safe to point at players. The GitHub repository was created in December 2017 and version 1.0.0 was released on 17 September 2019.

## Who Built It, And Why Them

Google Cloud, with Ubisoft as founding contributor. The announcement was written by Mark Mandel, a Google Cloud developer advocate, and quotes Carl Dionne of Ubisoft's Online Technology Group on running servers "in optimal datacenters."

The commercial logic is Google's, not the studios'. Google had given the world Kubernetes and was selling managed Kubernetes compute; game servers were a large, bursty compute workload that its orchestrator could not host without an adaptation layer. Publishing that layer as open source made Kubernetes the default substrate for fleets — and every studio that adopted it became a portable customer for the cloud that ran Kubernetes best. Ubisoft, by contrast, had the problem and the fleets but no reason to sell a standard to rivals.

I did not find a statement from Google giving this rationale in its own words; the argument above is inference from the announcement's framing, flagged as such.

## What It Cost

**Agones made the fleet safe to shrink, but not smart about when.** A warm buffer of Ready servers is the cost of instant allocation, and its size is a number somebody chooses. The autoscaler adds servers when the Ready buffer falls below a threshold; it does not forecast a free weekend, a streamer moment or a regional launch. The capacity decision was pushed up a layer, not solved.

Protecting Allocated servers also means a rolling update can take as long as the longest match, and a stuck server that never calls Shutdown holds its node indefinitely.

## What You Still Touch

When a new season drops and the queue says "finding match" for ninety seconds, one likely cause is a Ready buffer sized by hand the week before — the gap Agones left open.

- [[problems/game-hosting-providers/high-impact|🔴 Capacity for a Curve Nobody Can Forecast]] — the decision the Ready buffer turns into a single number
- [[problems/game-hosting-providers/worker-life-1|🟢 The Engineer on Call for Launch Night]]
- [[niches/game-hosting-providers/capacity-forecasting/profile|Capacity Forecasting & Allocation]]
- [[niches/game-hosting-providers/fleet-cost-optimisation/profile|Fleet Cost Optimisation]] — the bill for the warm buffer
- [[niches/game-hosting-providers/server-build-and-rollout/profile|Server Build & Rollout]] — where "skipping Allocated GameServers" becomes a deployment schedule

**Sources:** Google Cloud Blog, Mark Mandel, "Introducing Agones: Open-source, multiplayer, dedicated game-server hosting built on Kubernetes" (14 March 2018), including the Ubisoft quote and the "myriad of proprietary solutions" line; agones.dev documentation, *Fleet Updates* and *GameServer* reference (state names, Allocated-protection quotes); GitHub API for googleforgames/agones — repository created 2017-12-07, v1.0.0 published 2019-09-17. ⚠️ **Not established:** Google's own stated business rationale (the "Why Them" argument is inference); the division of engineering work between Google and Ubisoft; any date for Amazon GameLift, the main proprietary alternative, which I could not confirm this session (Wikipedia URL returned 404). WebSearch was unavailable this session (session budget exhausted); research used WebFetch on known URLs and the GitHub API only.
