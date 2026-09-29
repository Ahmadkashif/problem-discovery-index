# Lines Executed, Behaviours Unknown

**Niche:** [[niches/qa-test-automation-vendors/behaviour-coverage-measurement/profile|Behaviour Coverage Measurement]]
**Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Coverage tooling is universal, accurate and reports lines executed, which tells a team nothing about whether the behaviours that matter are actually verified.
**Tags:** #graph-theory #bert #large-language-models #gradient-boosting #evaluation-metrics #confidence-intervals #compliance #automation
**Contested on:** Every serious competitor here is fighting to tell a team which behaviours that matter are actually verified — and whoever does that takes the quality function, because the universal metric reports lines executed and answers a different question.

## The Problem
A service reports eighty-four percent line coverage and the team treats it as well tested. The checkout flow's handling of a declined payment followed by a retry is not tested at all; the lines involved are covered by other tests that pass through them without exercising that path. The refund path is covered by a test that calls it and asserts nothing. The permission check that prevents one customer seeing another's data is at one hundred percent coverage from a test that only exercises the allowed case. Every one of those is a behaviour that matters, and the metric that the team manages to says nothing about any of them.

## Why Nobody Has Built This
Line coverage is free, precise and produced automatically by every language toolchain, which is why it became universal, and its weakness has been common knowledge for decades without changing anything. Measuring behaviour coverage requires an enumeration of behaviours, which does not exist outside regulated industries where traceability is mandated — and where it is maintained by hand at considerable cost. Deriving the enumeration automatically from requirements, code structure and observed usage has become feasible and nobody has attempted it commercially. And a behaviour coverage number would be much lower than a line coverage number, which is not a comfortable thing to introduce.

## What to Build
Enumerate the behaviours and measure against those. Derive a behaviour inventory from the available sources: requirements and issue text where they exist, the code's own conditional structure and error paths, the interface's user-reachable actions, and the production usage record — which shows what users actually do and is the most under-used source of all. Determine which behaviours are verified by which tests, and verified how strongly, distinguishing a test that exercises a path from one that asserts its outcome. Weight by risk: user reach from the usage record, financial or safety consequence, and historical defect density, so the report ranks the unverified behaviours that matter rather than listing all of them. Report unverified behaviour rather than uncovered lines, which is the output a team can act on and is the whole point. Connect production incidents back to the behaviour that failed and whether it was covered, which validates the inventory and identifies what it is missing. And report alongside line coverage rather than replacing it immediately, since the comparison is itself the argument.

## Target Customer
Quality engineering and engineering leadership, the coverage tooling vendors whose metric is universally misread, and regulated industries who maintain this by hand.

## Impact If Built
The universal metric measures execution and is read as verification, which means every team managing to it is managing to the wrong thing. The production usage record is the most under-used source for enumerating what matters, and risk weighting is what turns a long list into a short priority.
