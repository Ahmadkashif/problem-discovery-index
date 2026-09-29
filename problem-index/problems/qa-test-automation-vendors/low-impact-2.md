# Browser and Device Matrix Selection

**Industry:** [[qa-test-automation-vendors|QA & Test Automation Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Device and browser grids are mature commercial services offering thousands of combinations, and nobody can tell a customer which ones are actually earning their cost.
**Tags:** #gradient-boosting #k-means-clustering #hypothesis-testing #confidence-intervals #dimensionality-reduction #evaluation-metrics #optimization-fundamentals

## The Problem
Web and mobile applications must work across browsers, versions, operating systems, devices and screen sizes. The combination space is enormous and grids exist precisely to provide access to it.

Which combinations to test is decided by convention. The most popular browsers, the most common devices, whatever the previous engineer configured. The matrix grows when a bug appears on something untested and shrinks when the grid bill is questioned. Nobody knows which combinations have ever caught a defect that others did not.

The cost is real on both sides. Grid time is billed and the matrix multiplies every test run, so a suite that takes ten minutes on one configuration takes hours across twenty. That directly extends the feedback loop that developers already find too slow.

The evidence to decide better exists in two places. The vendor sees, across thousands of customers, which combinations actually produce distinct failures. The customer sees, in their own analytics, which browsers and devices their users actually use. Neither is joined to the matrix decision.

## What Already Exists
Device and browser grids from BrowserStack, Sauce Labs, LambdaTest and others offer very broad combination coverage with parallel execution. Real device clouds handle mobile. Browser usage statistics are published publicly. Visual regression testing across combinations is a standard feature. Some platforms report which configurations failed.

## The Customisation Gap
Failure correlation across combinations is the analysis nobody performs. If two browsers have never produced different results across thousands of runs, testing both is redundant, and that is directly measurable from execution history — at the vendor across their whole customer base, and at the customer across their own.

Real user weighting is the other half. A customer's own analytics say which combinations their users actually use and at what value, and the matrix should be derived from that rather than from global popularity statistics that describe a different population.

Risk-based selection follows: test broadly on changes that touch rendering, layout or platform-specific behaviour, and narrowly on changes that cannot plausibly differ across environments — which is determinable from the diff.

Minimum covering set is the formal version of the question. Given the observed failure correlation structure, what is the smallest matrix that would have caught every distinct defect historically found — a well-posed optimisation on data the vendor holds and does not compute.

## Impact If Solved
The matrix multiplies every test run in both time and cost and is chosen by convention with no evidence about which combinations distinguish anything. Failure correlation analysis is straightforward on execution history, and a minimum covering set would let customers cut the matrix substantially without losing coverage they were actually getting.
