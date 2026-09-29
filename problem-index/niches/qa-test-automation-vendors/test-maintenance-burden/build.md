# Built, Decayed, Abandoned, Repeatedly

**Niche:** [[niches/qa-test-automation-vendors/test-maintenance-burden/profile|Test Maintenance Burden]]
**Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Writing tests is a project and maintaining them is a permanent staffing commitment, so organisations build suites, watch them decay, and abandon them — repeatedly, across the whole industry.
**Tags:** #graph-theory #bert #gradient-boosting #k-means-clustering #evaluation-metrics #confidence-intervals #automation #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to make a test suite survive two years of interface change without a permanent staffing commitment — and whoever does that takes the account, because the maintenance cost is where the entire economics of automated testing actually sits.

## The Problem
A company invests a year in an automated suite of two thousand end-to-end tests. It works. Over the following eighteen months the application's interface evolves normally — components are renamed, layouts change, a design system is adopted — and several hundred tests break for reasons that have nothing to do with behaviour. Two engineers repair them continuously. When budget tightens, the repair stops, failures accumulate, the suite is marked as advisory, and eighteen months later it is switched off. The company concludes that end-to-end testing does not work, which is the conclusion a great many companies have reached from the same sequence.

## Why Nobody Has Built This
The category sells the creation of tests, which is the part with a satisfying demonstration, and the maintenance cost appears afterwards as somebody's staffing problem. Self-healing was the industry's response and is implemented as heuristic selector matching — find the element that most resembles the one that used to be there — which repairs cosmetic breaks and also repairs breaks that were genuine, and the second behaviour is not detectable by the mechanism producing it. Distinguishing the two requires understanding whether the behaviour changed rather than whether the selector matched, and nothing in the category models behaviour.

## What to Build
Make repair cheap and safe by reasoning about behaviour rather than about selectors. Bind tests to semantic intent rather than to implementation detail — the element that submits the form rather than the third button in a container — derived from accessibility semantics, content and role, which is where the fragility originates and is largely avoidable. When a test breaks, diagnose the cause against the application change that preceded it: an element renamed, a layout altered, a flow reordered, or a behaviour genuinely changed — which is the classification the whole problem turns on and requires joining the test failure to the application diff. Repair automatically only where the change is demonstrably cosmetic, and fail loudly where it is not, with the evidence for the classification shown, since the hazard of self-healing is entirely in the cases it should not have healed. Repair in bulk, since one interface change breaks many tests in the same way and repairing them individually is most of the manual effort. Track suite health as a first-class metric — tests disabled, tests repaired, repairs per change — so decay is visible while it is happening rather than after. And report the maintenance cost continuously, because it is the number that determines whether the suite survives and nobody has it.

## Target Customer
Quality engineering and platform leadership at organisations with substantial suites, and the testing vendors whose customers' suites decay and are abandoned on a predictable cycle.

## Impact If Built
The abandonment cycle is industry-wide and is caused by a maintenance cost nobody measures and a repair mechanism that cannot distinguish cosmetic change from regression. Semantic binding removes much of the fragility and cause classification is what makes automatic repair safe.
