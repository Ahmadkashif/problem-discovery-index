# Solo Mobile Technician Dispatch and Routing

**Niche:** [[niches/towing-companies/roadside-tire-battery/profile|Roadside-Only Tire & Battery Services]]
**Industry:** [[industries/towing-companies|Towing Companies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No dispatch tool is designed for a solo mobile operator handling 8-15 short roadside calls per day across a metro area.
**Tags:** #reinforcement-learning #automation #workflow-orchestration #quick-win

## The Problem
A solo roadside technician receives calls throughout the day via phone, text, and motor club dispatch. Each call is a 15-30 minute job at a scattered location. With 10-12 calls per day, the order in which they're handled dramatically affects total mileage and earnings: handling the call 5 miles away before the call 25 miles away (even though the far call came in first) might save 40 minutes of drive time, enabling 1-2 additional calls per day. But the technician accepts calls as they come and routes via Google Maps one call at a time, with no optimization across their daily queue.

## Why Nobody Has Built This
Towing dispatch software (Towbook, TOPS) is designed for fleet dispatchers managing multiple drivers, not for a solo operator self-dispatching. Route optimization tools (Route4Me, OptimoRoute) are designed for delivery routes with known stops, not for roadside service where new calls arrive continuously throughout the day and must be interleaved with pending calls. The solo roadside technician market (~15,000-20,000 operators) is too small and too low-revenue-per-user for route optimization vendors to build for.

## What to Build
A mobile app that manages the solo technician's call queue and optimizes routing in real time. New calls enter the queue with location and estimated service time. The app continuously re-optimizes the sequence to minimize total drive time while respecting customer wait-time limits ("Mrs. Johnson has been waiting 40 minutes — she must be next regardless of location"). Shows the technician: next call, route, estimated arrival, and how many more calls they can fit before end of shift. Updates routing as new calls arrive.

## Target Customer
Solo roadside service operators handling 8-15 calls/day who currently route themselves one call at a time via Google Maps.

## Impact If Built
Reduces total daily drive time by 20-30%, enabling 1-3 additional calls per day at $50-$80 each. Worth $300-$600/week in incremental revenue for a solo operator.
