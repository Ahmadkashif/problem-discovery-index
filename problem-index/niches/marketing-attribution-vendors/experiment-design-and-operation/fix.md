# The Test That Could Never Have Detected Anything

**Niche:** [[niches/marketing-attribution-vendors/experiment-design-and-operation/profile|Experiment Design & Operation]]
**Industry:** [[industries/marketing-attribution-vendors|Marketing Attribution Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The experiment ran for three weeks across twelve regions, found no significant effect, and was reported as evidence the channel does not work — when it could only ever have detected an effect nobody expected.
**Tags:** #hypothesis-testing #confidence-intervals #monte-carlo-methods #evaluation-metrics #causal-inference #quick-win #descriptive-statistics #compliance
**Contested on:** Every serious competitor in this niche is fighting to make experiments cheap and continuous rather than occasional and expensive — and whoever does that supplies the ground truth the whole category needs and does not have.

## The Problem
A brand runs a geographic holdout to test a channel. Twelve regions, three weeks, a moderate budget. The result is not statistically significant. This is reported as evidence the channel is not incremental and budget is cut. The test had power to detect only an effect several times larger than anyone believed the channel had; a null result was the overwhelmingly likely outcome regardless of the truth. Nobody calculated this beforehand, and the absence of evidence has been converted into evidence of absence in a meeting where nobody present could identify the error.

## Why It's Still Broken
Power analysis takes an hour and would have prevented the test from running, which nobody wanted — the calculation is avoided because its answer is inconvenient, not because it is difficult. A null result feels like a finding and is reported as one. The audience cannot distinguish an underpowered null from a genuine one. And the experiment cost money, so producing no conclusion from it is unacceptable.

## What a Fix Looks Like
Calculate the power and refuse the test. Run a power analysis before every experiment and state the minimum detectable effect prominently, which is the fix and is an hour of work that prevents the category's most consequential measurement error. Refuse to run tests that cannot detect an effect of the size at stake, which is the product decision that matters and is what a serious experimentation platform does. Report the confidence interval rather than the significance verdict, since an interval spanning zero to a large positive effect plainly says the test was uninformative and a not significant label does not. Say uninformative rather than no effect when that is the truth, which is one word and prevents the most common misinterpretation. Design to the effect size that matters commercially rather than to a conventional threshold, because the question is whether the channel clears a return bar and not whether its effect differs from zero. Pool across tests and across clients to reach usable power, which is the only route for smaller advertisers. Extend duration rather than adding regions where that improves power more cheaply. Pre-register the analysis, since flexibility after seeing the data is how an underpowered test produces a confident conclusion. Teach the client what a null result means before the test runs, so the interpretation is agreed in advance. And report the minimum detectable effect alongside every result permanently, because it is the number that determines what the result can mean.

## Who Feels the Pain
Channels cut on tests that could not have detected them; clients who paid for an experiment that answered nothing; and the category, whose ground truth is frequently not evidence.

## Impact If Fixed
The power calculation is avoided because its answer is inconvenient rather than because it is difficult, and absence of evidence becomes evidence of absence. Stating the minimum detectable effect and reporting the interval rather than the verdict prevents the category's most consequential measurement error.
