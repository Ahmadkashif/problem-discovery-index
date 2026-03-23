# Move Estimation & Crew Scheduling Optimization

**Parent Industry:** [[industries/moving-companies|Moving Companies]]
**Category:** Highly Automatable

## Profile
**Market Size:** $1-2B (embedded operational cost across the industry)
**Share of Parent Industry:** Estimation and scheduling represent 15-20% of operational overhead at the average moving company
**Digital Adoption:** Low-Medium — Estimators use digital checklists but not predictive models; dispatchers use whiteboard scheduling or basic calendar tools with no optimization logic.
**Target Buyer:** Estimator or dispatcher at a moving company running 5-30 moves per day
**Automation Potential:** High — Both estimation and crew scheduling involve structured inputs, quantifiable outputs, and historical data that ML models can learn from directly

## What Makes This a Distinct Niche
Estimation and crew scheduling are the two operational functions where small improvements create outsized financial impact. A 5% improvement in estimation accuracy recovers 3-5% of gross margin on mispriced jobs. Optimizing crew-to-move assignment by even one fewer labor-hour per move saves $25-40 per move — at 200 moves/month, that's $5,000-8,000/month in labor savings. These functions are distinct from the general moving workflow because they require analytical capability (pattern recognition for estimation, combinatorial optimization for scheduling) rather than physical execution. They're also the two areas where experienced practitioners develop the deepest tacit knowledge — a veteran estimator's "eye" for cubic footage and a veteran dispatcher's "feel" for which crew handles which type of move best.

## Current Tools & Gaps
SmartMoving and MoveitPro offer digital inventory checklists for estimation, but these are data entry forms, not predictive models — they don't learn from historical estimate-vs-actual outcomes. Dispatch modules in these platforms handle calendar-based scheduling but don't optimize crew-to-move assignment based on crew skills, move complexity, drive time, or historical performance data. No tool connects the estimate (predicted hours, crew size, truck capacity) to the scheduling decision (which specific crew and truck) in a feedback loop.

## Problems
- [[niches/moving-companies/estimation-crew-scheduling/build|🔨 Build: Estimate-to-Actual Feedback Learning System]]
- [[niches/moving-companies/estimation-crew-scheduling/buy|🛒 Buy: Crew-to-Move Assignment Optimization]]
- [[niches/moving-companies/estimation-crew-scheduling/fix|🔧 Fix: Dispatcher Overload from Manual Schedule Juggling]]
