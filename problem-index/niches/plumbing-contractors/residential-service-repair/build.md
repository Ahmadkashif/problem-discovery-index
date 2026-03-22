# Emergency Call Triage and Dispatch Optimizer

**Niche:** [[niches/plumbing-contractors/residential-service-repair/profile|Residential Service & Repair]]
**Industry:** [[industries/plumbing-contractors|Plumbing Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An AI-powered dispatch system that scores incoming emergency calls by severity, matches them to the nearest available plumber with the right skills and truck inventory, and optimizes routes — replacing the dispatcher's gut-feel board with data-driven assignments.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #time-series-forecasting #optimization-fundamentals #tacit-knowledge-ml #revenue-impact #automation

## The Problem
When a homeowner calls a residential plumbing company with an emergency, a dispatcher — usually the owner or an office manager — must instantly decide: how severe is this call (active flooding vs. slow drip vs. no hot water), which plumber is closest and available, does that plumber have the skills for this job type (tankless water heater vs. sewer line vs. fixture repair), and does that plumber's truck have the likely parts needed? Today this decision is made entirely by memory and gut feel. The dispatcher remembers that "Mike is good with tankless" and "Sarah's truck probably has a 50-gallon Rheem" and "the Elm Street call has been waiting 45 minutes." When call volume spikes — a cold snap bursts pipes across town, or a Monday morning brings 15 queued calls — the dispatcher becomes the bottleneck. Mis-dispatches (sending a plumber who lacks the parts or skills) cost $75-150 per trip in wasted windshield time and delay revenue-generating work.

## Why Nobody Has Built This
Experienced dispatchers develop tacit knowledge over years: they learn each technician's strengths, typical truck loadout, driving speed, and close rate on different job types. This knowledge is never documented and walks out the door when the dispatcher quits. Building a replacement requires structured data on technician skills (not tracked in any FSM), truck inventory (not tracked at all), call severity indicators (buried in free-text call notes), and historical dispatch outcomes (which assignments resulted in first-trip completions vs. return visits). ServiceTitan's open API provides scheduling and job data but not the granular technician capability and inventory data needed for intelligent matching. The data collection infrastructure must be built alongside the optimization engine.

## What to Build
A dispatch intelligence layer that integrates with ServiceTitan or FieldEdge and adds three capabilities: (1) call severity scoring using a gradient-boosted classifier trained on call description keywords, property type, weather conditions, and time-of-day patterns to predict urgency tier (emergency/urgent/scheduled), (2) technician-job matching using a skills matrix, real-time GPS location, current truck inventory, and historical first-trip completion rates per job type, and (3) route optimization that minimizes total drive time across the active fleet while respecting severity-based SLAs. The system learns from dispatch outcomes — was the job completed on the first trip? Did the tech have the right parts? Did the customer convert on the upsell? — and continuously improves matching quality. Deployed as a dispatcher-facing dashboard that replaces the whiteboard with a ranked recommendation list for each incoming call.

## Target Customer
Residential plumbing service companies running 5-20 trucks with a dedicated dispatcher, currently using ServiceTitan or FieldEdge for scheduling but making dispatch decisions manually, losing 1-3 hours of tech time per day to mis-dispatches and supply house runs.

## Impact If Built
Reducing mis-dispatches by 40-60% recovers 45-90 minutes per technician per day in productive field time. For a 10-truck operation billing $150/hour, that translates to $150K-300K in recovered annual revenue. Faster emergency response also reduces customer churn — residential plumbing companies report that 30% of callers who wait more than 2 hours for a response call a competitor.
