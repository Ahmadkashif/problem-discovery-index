# The Remote Agent Answering for Forty Empty Offices

**Industry:** [[self-storage-operators|Self-Storage Operators]]
**Type:** Worker Life Changing
**One-liner:** When the office is empty, the gate intercom, the rental line and the angry tenant all reach one remote agent. Giving that agent the store in front of them, and letting software take the routine calls, turns a shift of blind firefighting into work they can do well.
**Tags:** #worker-facing #large-language-models #transformers #workflow-orchestration #automation #evaluation-metrics

## The Problem
Unstaffed and part-staffed stores route their phones and gate intercoms to a call centre. That might be a REIT's own customer care centre, CubeSmart's sales centre, OpenTech Alliance's "OpenTech Live!" storage counsellors, or Storable's Contact Connect. One agent may cover ~20–50 stores in a shift (estimate). The calls arrive in any order. A prospect wants a 10x10 tonight and asks whether it is climate-controlled. A tenant is stuck at the gate because their code was suspended for a missed payment. A caller says their rent went up and they were never told. Someone is inside the building after hours and the alarm is going off. An owner calls about the store's numbers.

The agent sees a softphone and a log-in to the facility software, often a different system for each client. They cannot see the gate, the unit or the tenant's last conversation with the store. To reopen a gate they must check the balance, take a payment, confirm identity and enter a code in the access-control system, all while the tenant waits in a truck. Many calls repeat the same five tasks. The rest are the hardest calls in the business, handled by someone who has never seen the store.

## Why It Matters to the Worker
The agent absorbs the anger the business model produces. A tenant who just received an increase, or who is locked out for non-payment, takes it out on the voice at the other end. Agents are measured on handle time and conversion, so the unresolvable call counts against them. Switching between client systems invites the mistakes that hurt most: a wrong code, or a payment posted to the wrong unit. Overnight shifts are lonely, and the one call that matters, someone in danger on site, comes with no context at all.

## What a Solution Looks Like
Two changes. First, software handles the routine calls end to end: availability and price quotes, reservations, move-ins, payments, and gate codes reissued after identity verification. Every action is written to the facility system with an audit trail. Storable was hiring a Senior Software Engineer, AI Agents in Seattle (first posted 2026-09-23) to build exactly this across voice, SMS, web chat and email, and OpenTech sells AI voice and chat agents with human escalation. Second, when a call does reach a person, the agent's screen shows the store: tenant balance and history in one view across client systems, the last notices sent, the gate camera, and a summary of what the software already tried. The model drafts the next step and the agent decides.

## Impact If Solved
If ~60% of calls are routine quotes, payments and gate resets (estimate), automating them cuts an agent's call load by more than half and lets one agent support the hard calls at ~40 stores without losing them. A unified tenant view should cut handle time on escalated calls by ~1–2 minutes (estimate) and remove most wrong-unit and wrong-code errors.
