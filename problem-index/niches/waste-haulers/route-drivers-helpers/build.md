# A Collection-Specific Risk Model for Every Stop

**Niche:** [[niches/waste-haulers/route-drivers-helpers/profile|Route Drivers & Helpers]]
**Industry:** [[industries/waste-haulers|Waste Haulers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Fleet safety systems score drivers on harsh braking and phone use, while collection crews are hurt backing into alleys, stepping off at the curb and lifting overloaded carts at specific, repeatable stops.
**Tags:** #gradient-boosting #cnns #object-detection #survival-analysis #worker-facing #compliance
**Contested on:** Every serious competitor in this niche is fighting to keep collection crews out of the injury and collision statistics, and whoever brings the crews' OSHA recordable incident rate lowest takes the account.

## The Problem
Collection incidents cluster at places and manoeuvres: the dead-end that forces a long reverse, the busy arterial where a helper crosses, the alley with a low wire, the stop with chronically overloaded carts. Generic fleet-safety scores average over the driver's day and miss where the risk sits.

## Why Nobody Has Built This
Video-telematics models are trained across all commercial fleets, and incident data per hauler is too small to learn collection-specific patterns; injury records sit in HR, video in the safety platform and routes in operations.

## What to Build
A stop-level risk model joining routes, telemetry (reversing events, speed, arm cycles), camera near-miss detections, injury and claim records, and street geometry. Outputs: a risk map per route that routing uses to eliminate reverses and crossings, stop-level warnings for unfamiliar drivers, and coaching targeted at the manoeuvres that precede incidents.

## Target Customer
EHS directors and route managers at haulers with 100+ collection trucks.

## Impact If Built
Eliminating the highest-risk reverses and crossings from routes could cut collisions and struck-by incidents by ~10–20% (estimate); at a 500-employee hauler with a TRIR near 5, that is ~2–5 fewer recordable injuries a year.
