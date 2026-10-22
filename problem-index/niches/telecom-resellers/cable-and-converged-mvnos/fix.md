# The Phone That Won't Let Go of Cellular

**Niche:** [[niches/telecom-resellers/cable-and-converged-mvnos/profile|Cable & Converged MVNOs]]
**Industry:** [[industries/telecom-resellers|Telecom Resellers]]
**Type:** Fix (Pain Point)
**One-liner:** Phones stay on cellular at home when Wi-Fi is marginal, and the MVNO pays wholesale for traffic its own gateway was meant to carry, without being able to see which households it is happening in.
**Tags:** #change-point-detection #descriptive-statistics #feature-engineering #revenue-impact #quick-win #data-integration
**Contested on:** Every serious competitor in this sub-niche (home Wi-Fi and gateway analytics vendors, offload and connection-management suppliers, and the operators' own network teams) is fighting to carry each subscriber's traffic on the operator's own Wi-Fi and small cells instead of the host's macro network without the subscriber noticing the handoff, and whoever cuts the most wholesale gigabytes per line takes the account.

## The Problem
Modern phones switch to cellular when Wi-Fi quality drops, to protect the user's experience. In a house with a weak signal in some rooms, the phone may spend the evening on the host network. The subscriber notices nothing, the wholesale bill grows, and the operator sees only an average.

## Why It's Still Broken
Connection decisions belong to the device's operating system, not the operator. The wholesale usage files show gigabytes by line but not where the phone was. The household's gateway telemetry sits with another team, so nobody can see the at-home cellular use that is the cheapest to remove.

## What a Fix Looks Like
Use the operator's own app (with consent) or gateway association logs to flag hours when a line was at home but on cellular, and detect the change when a household's pattern shifts, such as a new phone, a moved gateway or new interference. Send these households a targeted fix: an extender offer, a channel change pushed to the gateway, or a nudge to enable Wi-Fi calling. Track wholesale gigabytes before and after.

## Who Feels the Pain
Mobile finance teams watching wholesale cost per line; network teams with no visibility into the home; and subscribers with poor Wi-Fi they don't know about.

## Impact If Fixed
A low-cost, targeted intervention removes avoidable wholesale usage in the households where it concentrates, without touching price or service.
