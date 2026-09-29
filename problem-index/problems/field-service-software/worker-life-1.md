# Dispatcher Continuous Re-Planning

**Industry:** [[field-service-software|Field Service Software]]
**Type:** Worker Life Changing
**One-liner:** Dispatchers stop spending the whole day rebuilding a plan that reality destroys hourly, because the system re-optimises around each disruption and asks them to approve rather than to reconstruct.
**Tags:** #optimization-fundamentals #convex-optimization #gradient-boosting #time-series-forecasting #evaluation-metrics #workflow-orchestration #worker-facing #automation

## The Problem
A dispatcher starts the day with a plan: technicians assigned to jobs in a sequence, with arrival windows promised to customers. The plan survives about an hour.

A job takes three hours instead of one. A technician calls in sick. A no-heat emergency comes in and must go today. A part is not at the supply house. A customer is not home. Traffic. Each event invalidates part of the plan, and the dispatcher rebuilds it in their head, live, while the phone rings — moving cards, calling customers to change windows, calling technicians to change routes, deciding which promise to break.

Every platform in the category offers route and schedule optimisation. Adoption is low, and dispatchers explain why consistently: the optimiser does not know the things that determine the right answer. It does not know this customer is the commercial account that generates a fifth of revenue and cannot be moved. It does not know this technician should not be sent back to that address. It does not know the job described as a tune-up is at a property where the last two tune-ups turned into replacements. So it produces a plan that is arithmetically better and operationally wrong, once, and is never opened again.

## Why It Matters to the Worker
Dispatch is one of the highest-stress roles in the trades and is usually filled by someone who was a technician or has done it for a decade. It is continuous interruption with continuous consequence — every decision disappoints someone, and the dispatcher is the person who calls the customer to say the window has moved.

The load is invisible because dispatchers are good at it. The business sees a day that mostly worked; it does not see that one person held the entire plan in their head and re-derived it forty times. When that person is off, the day goes badly, which tells you where the knowledge lives.

Turnover in the role is costly precisely because the knowledge is unwritten. A new dispatcher takes many months to become adequate and the business runs worse throughout.

## What a Solution Looks Like
Re-optimisation on every disruption, presented as a proposal rather than an instruction. When a job overruns, the system should immediately produce the best available recovery — who to move, which window to renegotiate, which job to push to tomorrow — with the cost of each option shown, and let the dispatcher approve or override.

The constraints the dispatcher actually uses must be learnable rather than typed. Which customers cannot be moved, which technician-customer pairings to avoid, which job types run long at which properties — all of this is present in the platform's own history of what dispatchers actually did, and can be inferred from overrides rather than entered in a settings page.

Customer communication should be automatic on approval: the window change, the reason, the new time. That is a large share of the dispatcher's phone time and none of it requires judgement once the decision is made.

## Impact If Solved
The dispatcher is the single point of failure in most service businesses and the constraint on how many technicians a company can run. Removing the reconstruction work — while keeping the judgement with the person — raises the capacity of the role and makes it survivable for the people who are good at it.
