# Crew Routing & Scheduling

**Parent Industry:** [[industries/landscaping|Landscaping]]
**Category:** Highly Automatable

## Profile
**Market Size:** $5-8B (embedded across all landscaping sub-segments)
**Share of Parent Industry:** Cross-cutting operational function
**Digital Adoption:** Medium — Jobber and LMN provide calendar-based scheduling, but actual route optimization (sequencing stops, balancing crew loads, handling disruptions) is done manually by operations managers in every landscaping company with 3+ crews.
**Target Buyer:** Operations manager or owner at a multi-crew landscaping company (3-10 crews, 100-500+ properties)
**Automation Potential:** Very High — daily crew routing is a constrained vehicle routing problem with well-established algorithmic solutions, but landscaping-specific constraints (equipment matching, weather disruptions, seasonal service changes) have prevented generic routing tools from gaining adoption

## What Makes This a Distinct Niche
Every multi-crew landscaping company faces the same daily optimization problem: assign N crews to M properties such that total drive time is minimized, crew workloads are balanced, equipment requirements are matched, and service frequency commitments are met — then re-solve the entire problem when rain cancels a day's route. This is not a scheduling problem (deciding which day to service a property) but a routing and sequencing problem (deciding the order of stops per crew per day to minimize windshield time). A company with 5 crews and 300 properties makes this decision manually every morning — the operations manager reviews the day's scheduled properties, mentally clusters them by geography, assigns clusters to crews based on equipment and capability, and sequences each crew's stops. This 30-60 minute daily ritual is the single highest-leverage automation target in landscaping operations. The routing knowledge is deeply tacit: the ops manager knows that the crew should hit the gated community first because the gate code changes at 9am, that the Johnson property takes twice as long after rain because of the slope, and that Crew 2's trailer can't fit in the cul-de-sac on Oak Street so they always take the alley entrance. None of this is documented anywhere.

## Current Tools & Gaps
Jobber shows scheduled jobs on a map but doesn't optimize stop sequence or crew assignment. LMN provides job scheduling and time tracking but no routing. Aspire handles scheduling for commercial operations but routing is manual. Generic route optimization tools (OptimoRoute, Routific) can sequence stops efficiently but don't model landscaping constraints: crew-equipment matching, weather-driven rescheduling, seasonal service frequency changes, and property-specific access rules. No tool addresses the cascade problem — when one day's route is disrupted, the remaining week must be rebalanced, and every existing tool requires the ops manager to manually rebuild the schedule.

## Problems
- [[niches/landscaping/crew-routing-scheduling/build|🔨 Build: Dynamic Daily Route Optimizer]]
- [[niches/landscaping/crew-routing-scheduling/buy|🛒 Buy: Route Intelligence for Jobber/LMN]]
- [[niches/landscaping/crew-routing-scheduling/fix|🔧 Fix: Rain Day Rescheduling Cascade]]
