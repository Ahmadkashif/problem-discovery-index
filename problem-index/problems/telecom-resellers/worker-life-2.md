# One-Way Audio on a Network You Don't Own

**Industry:** [[telecom-resellers|Telecom Resellers]]
**Type:** Worker Life Changing
**One-liner:** A tier-2 VoIP support engineer spends nights proving whose fault a dropped or one-way call was, the customer's firewall, the provider's platform or an underlying carrier, and gets back sleep and standing when the evidence assembles itself.
**Tags:** #random-forests #lstms-and-grus #feature-engineering #evaluation-metrics #worker-facing #automation #data-integration

## The Problem
A dental office calls: patients can hear the receptionist, but the receptionist can't hear them. Or calls drop at exactly 32 seconds. Or audio is choppy every afternoon. The tier-2 engineer at the hosted-voice provider pulls the SIP trace from the session border controller, finds the call legs, reads the SDP to see which IP and port each side offered for audio, checks RTCP statistics for jitter and packet loss, and looks for the usual suspects. A firewall's SIP helper may be rewriting headers, NAT may be sending media to a private address, a session timer may be expiring, or the underlying carrier may be dropping the re-INVITE. The customer's network, the reseller's platform and the wholesale carrier that terminated the call each blame one of the others.

Complaints arrive in volume. A hosted-voice provider supporting thousands of small offices handles a steady stream of call-quality tickets, and the hard ones are intermittent. They reproduce only at certain times, with certain carriers or certain handsets.

## Why It Matters to the Worker
The engineer is diagnosing a path through two networks they can't touch, then has to persuade both owners. The customer's IT person insists the firewall is fine. The wholesale carrier's NOC wants a trace with exact timestamps before opening a ticket and answers a day later. Meanwhile the customer threatens to leave, and the account manager asks the engineer why it isn't fixed. The skill is real and slow to learn. A senior engineer glances at a ladder diagram and says "that's SIP ALG". A junior spends three hours getting there, so the hard tickets queue for the few seniors, who end up carrying the on-call nights.

## What a Solution Looks Like
When a quality complaint arrives, the system pulls the matching call records, SIP traces and RTCP statistics automatically. It classifies the likely fault domain (customer premises, provider platform, underlying carrier) and the specific pattern (one-way audio from NAT, header rewriting by a firewall helper, session-timer drops, codec mismatch, jitter on the customer's uplink). It attaches the evidence and drafts the two messages the engineer would otherwise write: instructions for the customer's IT contact, and a carrier ticket with the exact call IDs and timestamps.

## Impact If Solved
Junior engineers close the common patterns without escalation. Seniors spend their time on the genuinely novel faults, and tickets that took hours of trace reading take minutes (estimate). Carrier tickets that arrive with complete evidence get worked the same day instead of bounced back.
