# Test Coverage Gap Discovery

**Niche:** [[niches/electronics-contract-mfg/test-engineering-departments/profile|Test Engineering Departments]]
**Industry:** [[industries/electronics-contract-mfg|Electronics Contract Manufacturing]]
**Type:** Fix (Pain Point)
**One-liner:** Test coverage analysis — determining what percentage of the BOM's components and circuits are actually tested by the ICT/FCT test program — is performed manually by the test engineer comparing the test program to the schematic, missing gaps that later surface as field failures attributed to untested functionality.
**Tags:** #automation #compliance #revenue-impact

## The Problem
A test program typically covers 85-95% of a BOM's testable components and functions — the remaining 5-15% is untested due to test access limitations (no test point), measurement limitations (component cannot be isolated for in-circuit test), or test program development time constraints (FCT did not include every functional test case). The test engineer may or may not know which components and functions are not covered. Documenting test coverage — which components are tested by ICT, which functions are tested by FCT, and which are not tested at all — requires manually cross-referencing the test program against the BOM and schematic. This analysis is rarely performed comprehensively because it takes 4-8 hours per program and is not required by most customers. When a field failure occurs on an untested component, the root cause investigation reveals the coverage gap — by which time hundreds or thousands of boards have shipped with the untested component.

## Why It's Still Broken
ICT systems report which test vectors are included in the program, but they do not cross-reference against the full BOM to identify untested components. FCT coverage is entirely dependent on what the test engineer included in the functional test sequence — there is no automatic mapping between schematic functionality and test coverage. The analysis requires understanding of the circuit at the schematic level (which components are in which functional blocks, which blocks are tested by which test steps), which is currently performed only by the test engineer's manual review.

## What a Fix Looks Like
A test coverage analysis tool that ingests the BOM, schematic netlist, ICT test program, and FCT test sequence, maps each component and functional block to its test coverage status (tested by ICT, tested by FCT, tested by both, not tested), generates a coverage report with risk assessment for untested areas (what failure modes are undetected?), and recommends additional test steps or alternative test methods for critical gaps. The tool updates automatically when the test program or BOM changes.

## Who Feels the Pain
Test engineers who discover coverage gaps only when field failures are reported. Quality managers who must explain to customers why a field failure was not caught in test. Program managers who face warranty chargebacks from OEM customers for field failures attributable to inadequate test coverage.

## Impact If Fixed
Untested component field failures decrease by 50-70%. Test coverage documentation becomes automatic, satisfying customer requirements for test coverage reporting. Test development becomes targeted — engineers invest test development time where coverage gaps have the highest risk, not where they happen to start.
