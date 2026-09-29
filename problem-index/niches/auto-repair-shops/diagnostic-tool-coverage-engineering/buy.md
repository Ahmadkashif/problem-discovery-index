# Automotive Reverse Engineering Has No Vendor Market and Buys Software Written for Someone Else

**Niche:** [[niches/auto-repair-shops/diagnostic-tool-coverage-engineering/profile|Diagnostic Tool Coverage Engineering]]
**Industry:** [[industries/auto-repair-shops|Auto Repair Shops]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The tooling a coverage group can buy — protocol analysers, test automation, requirements and release management — all assumes you have a specification and can regression-test on demand, and this organisation has neither.
**Tags:** #transfer-learning #cross-validation #evaluation-metrics #automation #workflow-orchestration

## The Problem
A coverage organisation looks like a software engineering group and is procured as one. It has requirements, releases, a test function, a defect backlog and quarterly commitments. So it buys what software groups buy: application lifecycle management, test automation frameworks, CI, defect tracking, CAN and protocol analysis tools, bench automation.

The fit is poor in a specific way. Every one of those tools assumes the system under test is documented and available. Here the system under test is a proprietary undocumented module inside a car that must be physically bought, and the specification is precisely what the engineer is trying to discover.

## What Already Exists
Protocol analysers and CAN tooling capture and decode bus traffic. Hardware-in-the-loop and bench automation platforms drive test sequences. ALM and requirements platforms track coverage items to releases. Test automation frameworks execute regression suites. Vehicle simulation and residual bus simulation products can stand in for missing hardware. Defect trackers and release pipelines handle the rest.

This is a well-served market — for people building vehicles, who have the specifications.

## The Customization Gap
**There is no specification, so requirements tooling has nothing to hold.** ALM assumes a requirement exists before implementation. In coverage work the requirement is the discovery: what does this module do, which service identifiers does it answer, what does response 0x7F mean here. The tools end up used as glorified checklists of vehicle-model-function triples, which is what most coverage roadmaps actually are.

**Regression testing needs the car back.** A software regression suite reruns on every commit. Verifying that a change did not break coverage on a 2016 model requires that 2016 model, physically, on a bench, with a technician. Vehicle access — owned fleet, borrowed dealer stock, partner shops — is the binding constraint on the entire operation, and no bought tool models or schedules it. The scheduling of scarce vehicles against a coverage backlog is a real optimisation problem being solved on a whiteboard.

**Simulation is only as good as the thing you have not reverse-engineered yet.** Residual bus simulation replaces a vehicle you already understand. It cannot replace one you do not, which is exactly the population being worked on.

**Nothing transfers knowledge across platforms.** Modules and protocol behaviour repeat across models, across model years and sometimes across brands via shared suppliers. Engineers carry this in their heads and rediscover it constantly. There is no product that says "this module family behaves like that one you did last year," because no vendor holds a cross-manufacturer corpus — only the coverage groups do, and they store it as code and tribal memory.

**Field outcomes never reach the test function.** Bought test tooling reports on the bench. Whether the function completed in a shop on a car with a different trim, a different software revision and a corroded connector is the only validation that matters, and it arrives as support tickets in a different system owned by a different department.

**Release commitments are dated by calendar, not by evidence.** Quarterly coverage releases are promised against model-year timing. How long a given vehicle will actually take to reverse-engineer is estimable from history — module family, manufacturer, protocol generation, security posture — and is estimated by asking the engineer.

## Target Customer
Director of Vehicle Coverage or VP of Engineering at a diagnostic tool maker. The buy-and-adapt case is narrow: keep the ALM, defect and release layer, and build the three things no vendor supplies — a vehicle access scheduler that treats cars as the scarce resource they are, a cross-platform module knowledge base, and a field validation loop that closes back into test.

## Impact If Solved
The coverage backlog is the product roadmap, it is bounded by engineer time and vehicle access, and both are allocated with tools designed for organisations that have the specification sheet.
