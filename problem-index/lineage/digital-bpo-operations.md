# Lineage: Digital BPO Operations

**Industry:** [[industries/digital-bpo-operations|Digital BPO Operations]]
**Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**The tool:** the Galaxy automatic call distributor (ACD) — a computer-controlled switch that queued inbound calls and routed each to the next free agent, first sold to Continental Airlines in 1973
**Builder:** Collins Radio
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

An airline sold seats by telephone, and a telephone call could only go where a human operator sent it.

Airline reservations in the early 1970s meant hundreds of agents answering calls from the public. Getting a call to a free agent was the bottleneck: a switchboard or a hunt group rang lines in a fixed order, so some agents were swamped while others sat idle, and callers waited or hung up. Nobody could see, in the moment, how many callers were waiting or which agents were free. Adding agents helped only if calls actually reached them.

## What Got Built

A computer between the trunk lines and the headsets.

The **Galaxy ACD** held incoming calls in a queue and handed each one to the next available agent, in order, without an operator. Because a computer made every routing decision, it also knew — for every call — when it arrived, how long it waited, when an agent picked it up and when it ended. In later configurations, according to Wikipedia's description, the system ran on three DEC PDP-11/24 minicomputers: one distributing calls, one producing reports, one on standby.

That second processor is the point. Distribution was the purpose; measurement came free with it. **Once a machine connects every call, every call has a timestamp at both ends, and handle time becomes a number per agent, per call, to the second.**

## Who Built It, And Why Them

**Collins Radio**, of Cedar Rapids, Iowa — an avionics and communications company — through the switching unit led by engineer **Robert Hirvela**, who received the patent. Continental Airlines bought the first Galaxy in **1973** and, by Tedium's account, used it for 23 years.

Why an avionics firm and not the telephone company is the load-bearing detail. Tedium reports that **AT&T declined** Continental's request, estimating it would take eight years to build the technology to automate call routing. Collins, meanwhile, was already working with Continental on navigation systems: it had the customer relationship, and as a communications-electronics manufacturer it had engineers who were not waiting on the Bell System's priorities. A large customer whose phone monopoly would not serve it went to the supplier already in the building.

The corporate name is unsettled at the build date. Rockwell took control of Collins in 1971, and Hirvela's alumni profile calls it "the Rockwell business unit"; Rockwell's own 1996 press release, as quoted in secondary sources, says the Switching Systems Division was "originally part of the Collins Radio Co." at the time of the first sale. It is keyed here by that build-time name and was later sold as the Rockwell Galaxy.

## What It Cost

**What the switch could see became what the operation was paid on.**

The ACD measures everything about a call's *duration* and nothing about its *outcome*. It knows the call lasted 412 seconds; it does not know whether the customer's problem was solved. Because timestamps were free and outcomes required a person to listen, the metrics that grew up around the ACD — average handle time, service level, adherence to schedule — were all clock readings. Quality was checked by sampling recorded calls, a few per agent per month.

When customer service was outsourced, those clock readings were the obvious things to write into the contract, because both sides could read them off the same report. The BPO industry inherited an airline's switch statistics as its unit of account.

## What You Still Touch

Every chat, email and ticket queue in a digital BPO still reports handle time and service level first — the ACD's vocabulary carried over to channels that have no phone line.

- [[problems/digital-bpo-operations/high-impact|🔴 Handle Time Is Measured to the Second and Resolution Is Sampled at Two Percent]] — the switch's clock, written into contracts
- [[problems/digital-bpo-operations/worker-life-1|🟢 The Agent Under Adherence Monitoring]]
- [[problems/digital-bpo-operations/worker-life-2|🟢 The Quality Analyst Scoring a Sample]] — the part the switch could not see
- [[niches/digital-bpo-operations/contract-metric-reform/profile|Contractual Metric Reform]]
- [[niches/digital-bpo-operations/full-population-scoring/profile|Full-Population Resolution Scoring]]
- [[niches/digital-bpo-operations/workforce-forecasting/profile|Workforce Forecasting & Scheduling]]

**Sources:** Tedium, "Call Centers: Newer Than You Think", 2 August 2016 (Continental's 1973 purchase, 23 years' use, Hirvela patent, Rockwell's 1971 acquisition of Collins, the Continental–Collins navigation relationship, AT&T's eight-year estimate); Michigan Tech ECE alumni profile, *Robert J. Hirvela* (1973, "led the Rockwell business unit that invented and developed the first Digital Automatic Call Distributor", Collins HF Communications Division from 1959); Wikipedia, *Automatic call distributor* (ACDs from the 1950s, New York Telephone's modified 5XB for 4-1-1 in the early 1970s, Hirvela patent, PDP-11/24 configuration); Rockwell press release, "Rockwell Sells Call Center System to Continental Airlines", HPCwire, 17 May 1996 (Collins Radio Switching Systems Division; claim to the first digital ACD) — page returned HTTP 403, quoted only via search summaries. ⚠️ **Not established:** "first" — ACDs existed from the 1950s, so the Galaxy's claim is to the first *digital* ACD and comes from Rockwell itself. The Hirvela patent number was not found. The PDP-11/24 configuration cannot describe the 1973 system (that model is later) and is cited only as a later Galaxy. Which reports the original Galaxy produced — including whether it reported per-agent handle time in 1973 — was not found; the handle-time argument above follows from the routing mechanism, not from a documented feature list. Whether Collins or Rockwell should be the key is a judgment call, noted for the orchestrator.
