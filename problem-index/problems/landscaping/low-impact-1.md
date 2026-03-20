# Route Optimization for Multi-Stop Lawn Care Days

**Industry:** [[landscaping|Landscaping]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic route optimization tools (Google Maps, routific) solve the traveling salesman problem for stop sequences but don't understand lawn care-specific constraints: crew productivity by property size, gate access requirements, scheduled vs. on-demand stops, mowing day restrictions by HOA rule, and the crew truck's equipment configuration affecting which properties it can service.
**Tags:** #gradient-boosting #linear-regression #feature-engineering #evaluation-metrics #optimization-fundamentals #automation #workflow-orchestration #revenue-impact

## The Problem

A lawn care crew running 15-25 stops per day needs a route that minimizes drive time between stops while respecting constraints that generic route tools don't model: service day windows (some customers can only be serviced on specific days due to HOA rules or watering schedules), property-specific time estimates (a 5,000 sq ft property takes 18 minutes, a 12,000 sq ft takes 35), gate codes and access notes (must call ahead for dogs in the back yard), equipment carried on the truck (a crew with only a 36" mower can't service wide-gate properties efficiently), and crew skill level (a junior crew may not be assigned to complex landscape maintenance stops).

Generic optimization minimizes distance but produces routes that fail on-site — a sequence that looks geographically efficient routes the crew to a property they can't access, or to a difficult property when the crew is fatigued late in the day.

## What Already Exists

Jobber and Service Autopilot have basic route optimization. DPR (Desco Pro) offers landscaping-specific routing. Real Green Systems has territory management and routing for lawn care programs. None of these incorporate crew-specific equipment constraints or property-specific service time estimates from historical job duration data.

## The Customisation Gap

A landscaping route optimization tool needs: (1) property-specific service time estimates trained on historical job duration data from the firm's own records; (2) constraint modeling for gate access, service day windows, and HOA restrictions; (3) crew-equipment matching (which truck configuration can service which property); (4) real-time adjustment when a stop takes longer than estimated or a customer cancels. The historical service time model is the differentiator — using the firm's own job records to estimate how long each property actually takes instead of using manual time estimates.

## Impact If Solved

Reduces daily drive time by 15-25% through better stop sequencing. Eliminates on-site routing failures from access constraint violations. Improves crew productivity by matching difficult or time-intensive properties to the most capable crews.
