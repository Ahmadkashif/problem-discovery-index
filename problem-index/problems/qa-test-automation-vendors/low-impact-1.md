# Coverage That Measures the Wrong Thing

**Industry:** [[qa-test-automation-vendors|QA & Test Automation Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Coverage tooling is universal, accurate and reports lines executed, which tells a team nothing about whether the behaviours that matter are actually verified.
**Tags:** #graph-theory #gradient-boosting #hypothesis-testing #confidence-intervals #k-means-clustering #evaluation-metrics #feature-engineering

## The Problem
Every language has coverage tooling and every organisation reports a coverage percentage. It measures which lines executed during the test run.

It is a poor proxy for what anyone wants to know, which is whether the software's important behaviours are verified. A test that calls a function and asserts nothing produces coverage. A suite covering ninety per cent of lines can miss every error path, every boundary condition and every integration between components. And coverage is uniform where risk is not: the payment flow and the internal admin page count identically.

Because it is the only number available it becomes a target, and targeted coverage produces tests written to execute lines rather than to verify behaviour. Most experienced engineers know this and report the number anyway, because leadership asks for it.

The information that would say something useful exists elsewhere and is not joined. Which code paths have caused production incidents. Which areas change most frequently. Which flows carry business value. Which code has never been exercised by any test in any environment.

## What Already Exists
Line, branch and statement coverage tooling is mature in every language and integrated into every CI platform. Mutation testing exists and directly measures whether tests detect changes, which is a much better signal, and it is slow enough that adoption is limited. Coverage trend reporting and pull request gating are standard. Some platforms report coverage by module or ownership.

## The Customisation Gap
Risk weighting is the missing dimension. Coverage should be reported against the code that matters — code that has caused incidents, code that changes frequently, code on high-value user paths — and every one of those signals exists in systems adjacent to the coverage tool and is never joined to it.

Behaviour rather than execution is the deeper gap, and mutation testing is the right idea made impractical by cost. Selective mutation, targeted at the highest-risk code rather than run exhaustively, would make the technique affordable and is not offered by anyone.

Assertion quality is unmeasured entirely. A test that executes a path and asserts nothing meaningful is invisible to coverage tooling and is common, particularly in suites written to hit a target.

Gap prioritisation is what a team actually needs: not a list of uncovered lines but a short list of the uncovered things most likely to hurt, which requires the risk weighting to exist.

## Impact If Solved
Coverage is the only quality number most organisations have and it measures execution rather than verification, which is why teams with high coverage still ship regressions. Risk-weighted coverage and affordable selective mutation testing would give a team a number that means something, using signals that already exist in adjacent systems.
