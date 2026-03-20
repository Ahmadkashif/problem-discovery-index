# Dispatch Optimization and ETA Accuracy

**Industry:** [[towing-companies|Towing Companies]]
**Type:** High Impact
**One-liner:** Every wrong-truck dispatch is a wasted round trip that burns fuel, violates motor club SLAs, and drops the company in rotation ranking — accurate first-dispatch and realistic ETAs keep revenue flowing.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #bias-variance-tradeoff #gradient-descent #probability-distributions #tacit-knowledge-ml #revenue-impact

## The Problem
When a call comes in, the dispatcher has 60–90 seconds to determine which truck type is needed (wheel-lift vs. flatbed vs. medium-duty wrecker), which available driver can reach the scene fastest given current traffic and job queue, and what ETA to quote the motor club or customer. Get the truck type wrong and the driver arrives, cannot perform the service, and a second truck must be dispatched — doubling response time and halving margin. Motor clubs like AAA and Agero enforce strict ETA windows (typically 30–45 minutes); companies that consistently miss ETAs lose their rotation position, which can represent 40–60% of monthly call volume. Experienced dispatchers develop an intuitive read on calls — they parse vague caller descriptions ("my car is stuck in a ditch off Route 9"), cross-reference vehicle type with likely service needs, and factor in terrain, weather, and time-of-day patterns that no current dispatch software captures.

## Why It's Unsolved
The tacit knowledge problem is severe: the best dispatchers carry a mental model built from thousands of calls that integrates caller reliability (consumers routinely misidentify their vehicle type or location), local road knowledge, driver skill profiles, and real-time truck availability. This judgment is never recorded — dispatch tickets capture outcomes, not the reasoning process. Current dispatch platforms like Towbook are record-keeping tools, not decision-support systems. Building a predictive model requires instrumenting the dispatch decision itself: what information was available, what decision was made, and what the actual outcome was (correct truck? actual vs. quoted ETA? job duration?). Most towing companies lack the data infrastructure to capture this feedback loop.

## What a Solution Looks Like
A model that takes incoming call data (caller description, vehicle year/make/model from plate lookup, GPS coordinates, time of day, weather, historical zone data) and outputs: (1) recommended truck type with confidence score, (2) predicted job duration, (3) ranked list of available drivers with estimated arrival times accounting for current position and job queue. The dispatcher sees recommendations overlaid on their existing workflow — not a replacement, but a co-pilot that catches the 15–20% of calls where intuition-based dispatch would send the wrong truck or quote an unrealistic ETA.

## Impact If Solved
Reducing wrong-truck dispatches from an industry-average 12–18% to under 5% saves a typical 10-truck operation $8,000–$15,000/month in wasted trips. Maintaining motor club ETA compliance above 90% protects rotation position worth $30,000–$80,000/month in call volume.
