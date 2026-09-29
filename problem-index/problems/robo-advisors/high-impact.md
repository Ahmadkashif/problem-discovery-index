# Risk Tolerance Assessed Once and Never Validated

**Industry:** [[robo-advisors|Robo-Advisors]]
**Type:** High Impact
**One-liner:** The single input that determines a client's allocation is a self-report from a six-question form, and the platform watches every client's actual behaviour in every drawdown without ever checking the two against each other.
**Tags:** #logistic-regression #gradient-boosting #survival-analysis #causal-inference #bayesian-inference #confidence-intervals #evaluation-metrics #feature-engineering #revenue-impact

## The Problem
At account opening the client answers a short questionnaire. How would you react to a twenty percent decline. What is your investment horizon. Which of these hypothetical portfolios would you prefer. The answers produce a risk score, the score selects a model portfolio, and that allocation persists until the client changes a goal or the glide path moves it.

Everything known about this instrument suggests it measures something other than what it claims to. Answers are strongly framing-dependent and are given in calm conditions about hypothetical losses. People systematically overestimate their tolerance for a decline they have not experienced. The score is a prediction of future behaviour collected under conditions maximally unlike those in which the behaviour occurs.

Then the market falls, and the platform observes what actually happens. Logins increase. Some clients do nothing. Some move to a more conservative allocation at the bottom. Some withdraw entirely. Some stop contributing, which is quieter and often more costly over a working life than a single panic sale.

Each of those is a direct observation of realised risk tolerance, arriving with a timestamp, an account balance, a drawdown magnitude and a complete prior history. The platform records all of it and uses it for retention analytics rather than for advice.

The consequence is a mismatch that runs in both directions. Clients whose stated tolerance exceeds their actual tolerance are allocated too aggressively, and they discover this at the worst possible moment by selling at the bottom — which converts a temporary decline into a permanent loss and is, in realised-return terms, by far the largest destroyer of value in the product. Clients whose actual tolerance exceeds their stated tolerance are allocated too conservatively and quietly give up return for decades without ever knowing.

Neither error is measured. The platform reports assets, flows and market-relative performance, none of which surfaces the gap between the allocation a client holds and the allocation they can actually live with.

## Why It's Unsolved
The questionnaire exists partly for compliance rather than for accuracy. Suitability documentation requires a recorded basis for the recommendation, and a completed questionnaire is a defensible artefact. Replacing it with a behavioural estimate raises the question of what the platform is supposed to do when its estimate disagrees with the client's own stated preference, which is a genuinely unsettled question under a fiduciary standard and not merely an engineering one.

Drawdowns are rare, which makes the labels sparse in the dimension that matters. A platform founded after 2010 has a small number of genuine stress events, and behaviour in a brief sharp decline may not predict behaviour in a long grinding one. The data is rich in volume and thin in the conditions of interest.

Intervening is commercially delicate. Telling a client their stated tolerance appears wrong is a difficult message, and de-risking someone who then misses a recovery is a visible error where leaving them alone is not. The asymmetry pushes toward passivity.

And the objective is ambiguous. Reducing panic selling is good for the client and also reduces outflows, which makes any intervention look like retention work. That ambiguity is real, is uncomfortable, and has to be resolved deliberately rather than avoided — the honest framing is that the two interests genuinely coincide here, which is unusual and worth stating.

## What a Solution Looks Like
A behavioural risk estimate maintained continuously alongside the stated one. Login frequency and timing relative to market moves, allocation changes and their direction, contribution pauses, withdrawal patterns, time spent on performance screens, and behaviour in each prior drawdown — all of it updates an estimate of what this client actually does under stress. The gap between that estimate and the stated score is the number that matters and nobody computes it.

Pre-emptive identification rather than reactive intervention. The clients who will sell at the bottom are identifiable before the bottom, from their behaviour in prior declines and from early-warning signals in the current one. The intervention that works is almost certainly earlier and lighter than the one currently attempted, which is an email sent after the sale.

Interventions measured as experiments. Which message, at which moment, through which channel, actually changes the decision — this is directly testable and is currently decided by a marketing team's judgement. Reporting uplift rather than open rates would change the practice entirely.

The realised cost of behaviour, per client and in aggregate. The difference between the client's time-weighted and money-weighted return is the behaviour gap, it is computable exactly, and it is almost never shown to the client or tracked by the platform as a performance metric of its own advice.

Allocation adjusted for behavioural capacity, with the reasoning disclosed. A client who has twice sold in a decline is demonstrably not in the risk bucket their questionnaire placed them in, and a fiduciary that observes this and does nothing is making a choice.

## Impact If Solved
Realised investor returns fall short of fund returns primarily because of when people buy and sell, and a digital advice platform is the only institution that observes this behaviour completely, at scale, alongside the stated preference it was supposed to follow. Closing that loop is the largest available improvement in client outcomes in the category, it is measurable in basis points, and it is currently sitting in a database being used to forecast churn.
