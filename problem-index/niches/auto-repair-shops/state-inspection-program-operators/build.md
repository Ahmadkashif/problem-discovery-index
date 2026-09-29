# The Complete Inspection Record for a State, Reported as Compliance

**Niche:** [[niches/auto-repair-shops/state-inspection-program-operators/profile|State Vehicle Inspection Program Operators]]
**Industry:** [[industries/auto-repair-shops|Auto Repair Shops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every emissions test in an entire state flows through one contractor's system, and what gets modelled is whether the programme ran, not whether it worked.
**Tags:** #gradient-boosting #causal-inference #evaluation-metrics #survival-analysis #confidence-intervals

## The Problem
A programme operator runs a state's inspection regime end to end: the analysers in the shops, the network they report through, the fraud controls, and the statutory analysis delivered to the state and to the federal regulator. Every test, every failure, every repair, every retest in that state passes through them.

That produces something unusual — a complete census. Not a sample of vehicles, not a panel: every registered vehicle in the state that must be tested, tested on a fixed cycle, for years, joined to the shop that performed the test and to what happened when a failing vehicle came back.

What is built on it is compliance reporting. Test volumes, failure rates, programme coverage, network uptime, and the analysis the state implementation plan requires. All necessary, all backward-looking, all about whether the programme operated.

The question nobody answers is whether the programme is finding the right vehicles. Emissions from the fleet are dominated by a small tail of high emitters, and the inspection regime tests everything on a calendar. The census would support a direct estimate of which vehicles are actually worth testing — by age, model, prior test history, repair history and geography — and therefore how much emission benefit each test dollar buys.

The second unbuilt thing is repair effectiveness. A vehicle fails, is repaired, and returns. The census records the before, the intervention and the after. That is a treatment-and-outcome record on millions of vehicles, and it would say which repairs actually fix emissions and which shops actually fix cars — a question the state, the motorist and the honest repairer all want answered.

## Why Nobody Has Built This
The contract defines the deliverable. The operator is paid to run a programme and file statutory reports, and analysis outside that scope is unfunded work for a customer that did not request it.

There is also a delicate politics. A contractor demonstrating that most of the tests it is paid to administer produce little benefit is arguing against its own scope. And a contractor publishing which shops fail to fix vehicles is making enemies among the network it depends on.

The buyer set is tiny — roughly a dozen state contracts — which means nobody has ever had to differentiate on analytical capability, only on operational reliability and price.

## What to Build
Programme effectiveness as the product, not programme compliance.

**Estimate benefit per test by vehicle segment.** Which segments produce failures that matter, and which produce almost none. The census supports this directly and it is the analysis every state environmental agency wants and cannot commission.

**Model high-emitter probability before the test.** Prior history, model, age, mileage and geography predict failure well. That is the foundation of any targeted or remote-sensing-augmented regime, and states are actively debating those redesigns without evidence.

**Measure repair effectiveness by shop and repair type.** Failing test, repair performed, retest result. Which interventions hold, which vehicles return to failure a cycle later, and which shops produce durable fixes.

**Model waiver and drop-out.** Vehicles that fail and never return are the ones still on the road polluting, and the census identifies them precisely.

**Sell the effectiveness case into rebids.** Contracts are re-tendered, and an incumbent that can quantify what its programme achieved rather than what it processed is arguing on ground no competitor can reach.

## Target Customer
VP of Programme Operations or Director of Analytics at an inspection programme contractor. The commercial argument is that these contracts are won on price and operational credibility, both of which are commoditising, and effectiveness evidence is the only differentiation available.

## Impact If Built
State inspection programmes cost motorists and taxpayers substantial money annually on a test-everything cadence designed decades ago, while the emissions they exist to reduce concentrate in a small tail. The only party holding the complete record is contracted to report that the programme ran, and could instead say what it achieved.
