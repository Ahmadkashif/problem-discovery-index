# Customer Care That Can't See the Host Network

**Niche:** [[niches/telecom-resellers/consumer-mvnos/profile|Consumer MVNOs]]
**Industry:** [[industries/telecom-resellers|Telecom Resellers]]
**Type:** Fix (Pain Point)
**One-liner:** When an MVNO subscriber has no service, the care agent can't see whether the cause is a host outage, a stuck provisioning order or the phone, so they run a script and escalate to a host queue with a multi-day turnaround.
**Tags:** #large-language-models #bert #feature-engineering #worker-facing #workflow-orchestration #data-integration
**Contested on:** *Not terminal as stated.* Consumer MVNOs split into cable and converged MVNOs, which win on offloading traffic from the host network, and independent digital MVNOs, which win on keeping subscribers past acquisition payback; see the parent profile.

## The Problem
"No service", "can't send texts", "data stopped working" are the most common MVNO care contacts. The agent sees the MVNO's own account record and line status, but not cell-site outages, the host's provisioning state for the SIM, or whether the number is mid-port. They walk the subscriber through restarting the phone and resetting network settings, then open a ticket with the host or enabler, which answers on its own service level. The subscriber, who chose the brand for its price, concludes the brand is unreliable and leaves.

## Why It's Still Broken
The host exposes only limited status interfaces to resellers, and the enabler sits between them with its own ticketing. Each MVNO negotiates visibility separately, so most get a portal and a queue. Nobody classifies the incoming contacts against the host's events, so the MVNO can't even prove a pattern to the host.

## What a Fix Looks Like
Join care contacts, line status, provisioning events and the host's published outage and maintenance notices by area and time. Classify each contact automatically (host outage, provisioning fault, device configuration, coverage), answer the outage cases at once with what is known, and escalate provisioning faults with the evidence attached. Report recurring host-side faults with counts in the next wholesale review.

## Who Feels the Pain
Care agents with no answer to give; subscribers without service; and MVNO operations leads who can't show the host that its faults drive their churn.

## Impact If Fixed
Contacts get resolved on first touch where the cause is known, escalations to the host come with evidence instead of a script, and the MVNO stops paying in churn for faults that aren't its own.
