# Nobody Measures What Maintenance Costs

**Niche:** [[niches/qa-test-automation-vendors/test-maintenance-burden/profile|Test Maintenance Burden]]
**Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Organisations decide to build a test suite without any estimate of what keeping it will cost, and the cost is the variable that determines whether the suite survives.
**Tags:** #descriptive-statistics #survival-analysis #hypothesis-testing #confidence-intervals #evaluation-metrics #quick-win #revenue-impact #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to make a test suite survive two years of interface change without a permanent staffing commitment — and whoever does that takes the account, because the maintenance cost is where the entire economics of automated testing actually sits.

## The Problem
A quality initiative is approved on the basis of the effort to write the tests. Nobody estimates the ongoing cost, because nobody has a figure for it: how many tests break per interface change, how long a repair takes, how that scales with suite size and application volatility. Two years later the maintenance consumes two engineers permanently, which was never budgeted, and the response is to stop doing it rather than to have made a different decision at the start. Every input to the estimate — breakages per change, repair duration, suite size, change rate — is recorded in the version control and test execution history.

## Why It's Still Broken
Maintenance effort is absorbed into engineers' general workload and never attributed, so no organisation has the number even retrospectively. The vendors have no incentive to publish it, since it is the least attractive fact about their product category. And the initiative's business case is made by the people who will write the tests rather than by those who will maintain them, which is a different team a year later.

## What a Fix Looks Like
Measure it and use it in the decision. Attribute repair effort by identifying commits that modify tests without modifying behaviour, which is detectable from the change pattern and produces the maintenance cost retrospectively without anyone recording anything new. Compute breakages per application change and repairs per test per year, which are the rates that make a forward estimate possible. Relate the cost to suite characteristics — test type, binding strategy, the part of the application covered — since end-to-end tests bound to the interface and unit tests bound to a function have maintenance costs that differ by an order of magnitude and the choice is frequently made without reference to that. Report the total cost of the suite as ownership rather than creation, which is the number a business case should contain. Forecast it forward for a proposed suite from the application's own change rate, which is observable. And track it continuously, since a rising repair rate is the early indication of the decay that ends in abandonment and currently has no warning at all.

## Who Feels the Pain
Engineers maintaining suites nobody budgeted for; leaders who approved a quality initiative without its ongoing cost; and organisations that abandoned automated testing and concluded the approach does not work.

## Impact If Fixed
Repair effort is detectable from the commit history and produces the missing number retrospectively at no cost. Relating maintenance cost to binding strategy is what would change the design decisions that cause it, and the rising repair rate is an early warning of abandonment that nobody currently has.
