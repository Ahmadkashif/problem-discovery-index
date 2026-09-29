# Containment That Counts Resolution Rather Than Abandonment

**Niche:** [[niches/customer-support-platforms/voice-contact-centre/profile|Voice Contact Centre]]
**Industry:** [[industries/customer-support-platforms|Customer Support Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Voice containment is measured as the share of calls that did not reach an agent, which rewards a system for exhausting the caller, and the callers most likely to be exhausted are the ones with the fewest alternatives.
**Tags:** #descriptive-statistics #gradient-boosting #survival-analysis #evaluation-metrics #confidence-intervals #hypothesis-testing #automation #worker-facing
**Contested on:** Every serious competitor in voice support is fighting to resolve a caller's issue without a human while they are on the line, and to make the agent faster when a human is needed — and whoever raises containment without raising repeat calls takes the account.

## The Problem
A caller navigates four menu levels, is asked to confirm details by voice, is told an answer that does not address their situation, and hangs up. The system records a contained call. They call back the next day, reach an agent, and are resolved. The organisation's containment rate improved and its total cost went up, and the customer's experience was an hour across two days. Containment measured as non-arrival at an agent rewards exactly this, and the callers most affected are those who cannot resolve their issue any other way — which in voice skews toward older customers, those without reliable internet access and those whose issue is genuinely unusual.

## Why Nobody Has Built This
Containment is the metric the economics run on, it is easy to compute from call routing data, and it has been the industry's headline number for decades. Measuring resolution instead requires linking a contained call to whether the customer came back, which requires identity resolution across a repeat call and an appetite for a metric that will be lower. And there is a structural problem the industry rarely states: the party that benefits from aggressive containment is the operator, the party that bears it is the caller, and no metric currently represents the second.

## What to Build
Containment redefined as resolution and measured by what happened next. A contained call is counted as successful only if the caller did not return within a window on a related issue, which is computable from the same call records with basic identity resolution and immediately corrects the most flattering part of the metric. Abandonment is separated from containment and reported prominently, since a caller who hung up inside the automated flow is a failure and is currently counted as a success. Intent recognition is used to route rather than to menu, with the automated path attempted only where the organisation's own history shows that intent is genuinely resolvable without an agent — which is a per-intent decision the data supports and that is currently made uniformly. And the exit to a human is made easy and prominent rather than hidden, because a caller who wants an agent and is prevented from reaching one produces a worse outcome on every measure including cost, once the repeat call is counted.

## Target Customer
Contact centre platform vendors, support operations leaders whose cost model rests on containment, and the regulated industries where a customer's inability to reach a person is a conduct concern.

## Impact If Built
Recomputing containment as resolution reliably shows that a meaningful share of contained calls return, which changes the economics of aggressive containment and the design decisions that follow from it. The abandonment separation is free and is the honest correction, and making the path to a human easy is the change that most improves outcomes for the callers with the fewest alternatives.
