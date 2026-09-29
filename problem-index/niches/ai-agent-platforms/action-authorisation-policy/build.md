# The Gate Placed by a Nervous Guess

**Niche:** [[niches/ai-agent-platforms/action-authorisation-policy/profile|Action Authorisation Policy]]
**Industry:** [[industries/ai-agent-platforms|AI Agent Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every platform offers human-in-the-loop approval and permission scopes, and where to put the approval gate is decided by a nervous product manager guessing, which produces either an agent nobody trusts or one that reviews everything and saves nothing.
**Tags:** #markov-decision-processes #confidence-intervals #evaluation-metrics #hypothesis-testing #gradient-boosting #descriptive-statistics #compliance #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to place the human approval gate where the evidence says it belongs rather than where a nervous product manager guessed — and whoever does that takes the account, because gate placement determines whether a deployment saves anything.

## The Problem
A product manager configures an agent for order management. They gate refunds above fifty dollars, because fifty felt right. They do not gate address changes, because those felt safe — and an address change on a high-value order is how fraud works. They do not gate account merges, which are irreversible. The agent's actual error rates by action type are recorded in the trajectory data and were not consulted, because nobody thought to ask and nothing surfaces it. Six months later the policy has been adjusted twice, both times after an incident, and it is still a set of guesses.

## Why Nobody Has Built This
Gate placement was treated as a configuration option rather than as a decision the platform should inform, so the product surface is a screen rather than a recommendation. The inputs — per-action error rate, cost of error, reversibility, reviewer catch rate — are spread across the trajectory data, the buyer's business knowledge and nowhere at all. Recommending a lighter gate means accepting some responsibility for an error. And the failure of a bad placement shows up as either an incident or an absence of savings, neither of which is traced back to the configuration screen.

## What to Build
Recommend the gate from evidence. Estimate per-action error rates from the trajectory corpus, which the platform holds and which is the first of the four inputs and the one it can supply entirely on its own. Capture cost of error and reversibility per action type from the buyer, since those are business facts the buyer knows and is never asked for in a structured way — and reversibility should dominate, because a reversible mistake is an inconvenience and an irreversible one is an incident, and the current configuration screens do not distinguish them at all. Measure reviewer catch rate, which the fix note develops, because a gate whose reviewer catches nothing is pure cost. Compute the recommended placement from the four quantities, expressed as an expected cost comparison rather than a rule of thumb. Gate on confidence rather than on action type where a per-task confidence exists, since a low-confidence refund and a high-confidence one deserve different treatment and action type alone is a crude proxy. Report what each gate costs in throughput and what it is estimated to prevent, so the trade is explicit. Adapt as the agent improves, loosening gates where the evidence supports it, which is how a deployment's value grows over time rather than staying frozen at its launch configuration. And log every gate decision so the policy can be evaluated later.

## Target Customer
Risk owners approving agent deployments, product leads configuring them, and the platforms whose configuration screen currently carries the whole decision.

## Impact If Built
Four measurable quantities determine the right gate and none are consulted. Reversibility should dominate the decision and no configuration screen distinguishes reversible from irreversible actions at all.
