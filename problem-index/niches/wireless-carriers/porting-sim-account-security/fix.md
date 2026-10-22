# The Port-Out PIN a Care Agent Can Reset

**Niche:** [[niches/wireless-carriers/porting-sim-account-security/profile|Number Porting, SIM Changes & Account Takeover Defence]]
**Industry:** [[industries/wireless-carriers|Wireless Carriers]]
**Type:** Fix (Pain Point)
**One-liner:** The strongest control on a port-out is a PIN, and the weakest point is the care call where a convincing stranger asks for it to be reset.
**Tags:** #bert #large-language-models #evaluation-metrics #compliance #worker-facing #quick-win
**Contested on:** Every serious competitor in this niche is fighting to approve every legitimate port-out, eSIM transfer and SIM change in seconds while stopping the takeover attempts hidden among them, and whoever delivers the lowest fraud at the least customer friction takes the account-security budget.

## The Problem
Care agents are measured on resolving calls and satisfying customers. A caller who sounds distressed, knows some account details and asks for a PIN reset or SIM change puts the agent in an impossible position, and social engineering targets exactly that.

## Why It's Still Broken
Policies say "verify identity", but the tools leave the decision to the agent, and the agent is rewarded for helping. Takeover outcomes reach the agent's team weeks later, if ever.

## What a Fix Looks Like
Remove sensitive resets from agent discretion: route them to step-up verification the agent can't bypass. Analyse the call in real time for known social engineering patterns, show the agent a clear risk flag, and give them a script that protects them when they refuse.

## Who Feels the Pain
Care agents under pressure, customers whose numbers are stolen, and fraud teams cleaning up afterwards.

## Impact If Fixed
The most common takeover path is closed and agents are no longer the last line of defence.
