# Attributing a Bad Flight's Wi-Fi to Its Real Cause

**Niche:** [[niches/satellite-operators/aviation-maritime-connectivity/profile|Aviation & Maritime Connectivity]]
**Industry:** [[industries/satellite-operators|Satellite Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** When passengers complain about Wi-Fi on a flight, the airline blames the satellite provider, the provider blames the aircraft modem or cabin network, and nobody can prove which it was.
**Tags:** #causal-inference #gradient-boosting #bayesian-inference #feature-engineering #revenue-impact #data-integration
**Contested on:** Every serious competitor in this niche is fighting to keep every aircraft and vessel connected at a guaranteed speed as it crosses beams, orbits and borders, and whoever can show the airline or ship operator per-flight and per-voyage performance it trusts takes the fleet contract.

## The Problem
A connected flight's experience depends on a chain: satellite beam congestion, handovers between beams or satellites, the aircraft's antenna and modem, the cabin wireless network, the portal and authentication, and the passengers' own devices. Poor flights are reported as complaints, social posts and NPS dips. Each party sees its own segment of the chain.

## Why Nobody Has Built This
The data belongs to different companies — the satellite operator, the airline, the cabin equipment maker, sometimes a service integrator — and contracts rarely require sharing it. Each party's tools stop at its own boundary.

## What to Build
A per-flight attribution model that joins beam load and handover logs, modem and antenna telemetry, cabin network and portal logs, and passenger feedback, and estimates for each poor flight the probability that each segment caused it. Fleet-level views show which tails, routes, beams and times of day drive complaints, and which fixes (capacity, antenna swap, portal change) would move experience most.

## Target Customer
VPs of mobility at satellite operators and their airline account teams; airline heads of connectivity at renewal time.

## Impact If Built
Disputes turn into joint fixes, capacity goes to the beams and routes that drive complaints, and the operator walks into renewal with evidence of what it delivered.
