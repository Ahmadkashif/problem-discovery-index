# Nobody Measures Whether the Programme Bought Security

**Industry:** [[bug-bounty-platforms|Bug Bounty Platforms]]
**Type:** High Impact
**One-liner:** Programmes report spend, submission counts and time to triage, and cannot say whether the vulnerabilities they paid for were ones anything else would have found.
**Tags:** #causal-inference #survival-analysis #bayesian-inference #confidence-intervals #hypothesis-testing #gradient-boosting #evaluation-metrics #revenue-impact

## The Problem
An organisation runs a bounty programme and spends a budget. At the end of the year it can report how much it paid, how many valid findings it received, the severity distribution and how quickly it triaged. What it cannot report is whether it bought anything.

The counterfactual questions are the ones that matter and none is answered. Would internal testing have found these? Would a scanner? Would the next release have removed the vulnerable code anyway? Did any of these findings correspond to something an attacker was actually positioned to exploit? What would a larger or smaller bounty budget have produced?

The category's implicit claim is that paying researchers surfaces vulnerabilities that would otherwise have remained, and that some of those would have been exploited. Both halves are plausible and neither is measured. Programmes are justified internally on the severity distribution of what was found, which is a statement about the findings and not about the risk avoided.

Bounty pricing compounds the opacity. Payout tables are set by comparison with other programmes rather than by any estimate of what a finding is worth, and the relationship between price and the quality of attention a programme receives is unmeasured — so a programme deciding whether to raise its critical payout is guessing about its own supply curve.

And the comparison against alternatives never happens. An organisation choosing between bounty spend, additional penetration testing, more internal application security engineers and better static analysis has no comparative evidence, so the allocation is made on preference and vendor relationships.

## Why It's Unsolved
The counterfactual is genuinely hard. Establishing that a finding would not have been found otherwise requires knowing what the alternatives would have found, which means running them in parallel — expensive, and organisations run them sequentially or not at all.

Incident outcomes are the natural measure and are rare, confidential and weakly linked. A programme that prevents a breach cannot observe the breach it prevented, and organisations do not publish the ones that happen.

The platforms are not incentivised to build it. Their revenue is a share of payouts and a fee for triage, and a measurement layer that told some customers their programme was not buying much would reduce spend. The same structure appears in every assurance business in this vault.

And the data is split. The platform sees submissions and payouts; the organisation sees its internal testing results, its scanner output, its incident history and its release cadence. Joining them requires a customer willing to share, and nobody has framed the ask.

## What a Solution Looks Like
Measure overlap, which is the tractable proxy. For a given finding, was it within the scope of the organisation's scanning, was it in code covered by recent internal testing, had it been flagged and deprioritised, and does the class appear in the organisation's own backlog. A programme where most paid findings were already visible internally is buying attention rather than discovery, which is a legitimate thing to buy and a different one from what is being claimed.

Estimate the supply curve. The relationship between payout level, scope breadth and the volume and quality of researcher attention is estimable across the platform's whole customer base — different programmes pay differently for comparable scopes and receive measurably different attention. That is the platform's unique asset and it would let a programme price deliberately rather than by imitation.

Run the comparison honestly where it is possible. Some organisations do run scanning, internal testing and a bounty programme over the same surface, and comparing what each surfaced — on the same code, in the same period — is a natural experiment already sitting in those customers' data.

Track time-to-discovery as the distinctive claim. The defensible argument for bounty programmes is not that they find things nothing else would, but that they find them sooner and continuously. Measuring the interval between a vulnerability being introduced and being reported, and comparing it to the interval for internally-found issues, is the metric that would substantiate the category's actual value.

## Impact If Solved
This category sells assurance and reports activity, which leaves every programme manager defending a budget with a severity histogram. Overlap measurement, an estimated supply curve and a time-to-discovery metric would let programmes be priced and sized deliberately — and would let the platforms make a claim about their value that survives a finance review, which the current reporting does not.
