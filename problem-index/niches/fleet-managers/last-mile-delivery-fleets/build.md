# Wear-Pattern-Aware Vehicle Rotation Optimizer

**Niche:** [[niches/fleet-managers/last-mile-delivery-fleets/profile|Last-Mile Delivery Fleets]]
**Industry:** [[industries/fleet-managers|Fleet Managers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool optimizes which vehicle runs which route based on accumulated wear patterns — a van that did 200 stops yesterday in hilly terrain shouldn't do the same route tomorrow.
**Tags:** #reinforcement-learning #time-series-forecasting #tabular-ml #automation #revenue-impact

## The Problem
Last-mile delivery fleets typically assign vehicles to routes by convenience (the nearest available van) or by driver preference (Driver A always takes Route 3). This creates uneven wear: the vehicle running the hilliest route with the most stops wears brakes, transmission, and suspension 2-3x faster than the vehicle running a flat suburban route. Over 12 months, some vehicles need $8,000 in maintenance while identical vehicles on easier routes need $3,000. Smart rotation would equalize wear, extending fleet life and reducing peak maintenance costs — but no tool calculates optimal rotation based on route characteristics and accumulated vehicle wear.

## Why Nobody Has Built This
Connecting route characteristics (stop count, elevation change, traffic density) to vehicle wear patterns requires correlating telematics data (hard braking events, idle time, acceleration patterns) with maintenance records (what broke, when, and on which route). This cross-domain data integration between routing systems, telematics platforms, and maintenance management systems doesn't exist. Each system operates in isolation.

## What to Build
A rotation optimizer that ingests route profiles (from routing software), vehicle telematics (from Samsara/Motive), and maintenance history (from Fleetio/Fleet Complete), calculates cumulative wear scores per vehicle per system (brakes, drivetrain, suspension, electrical), and recommends daily vehicle-to-route assignments that equalize wear across the fleet. It flags vehicles approaching maintenance thresholds and avoids assigning them to high-stress routes.

## Target Customer
Delivery fleet operations managers overseeing 50-500 vehicles who currently see a 2-3x spread in per-vehicle maintenance costs across their fleet.

## Impact If Built
Equalizes per-vehicle maintenance costs by 30-40%, extending average fleet life by 12-18 months. For a 100-vehicle fleet spending $500K/year on maintenance, this saves $150K-$200K annually and defers $300K-$500K in replacement vehicle purchases.
