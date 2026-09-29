# Predicting Whether a Task Will Succeed

**Industry:** [[ai-agent-platforms|AI Agent Platforms]]
**Type:** High Impact
**One-liner:** Customers need to know before deployment what fraction of tasks an agent will complete correctly and which ones it will fail, and the category answers with a demo and a pilot.
**Tags:** #gradient-boosting #logistic-regression #confidence-intervals #evaluation-metrics #hypothesis-testing #large-language-models #markov-decision-processes #revenue-impact

## The Problem
An agent handles a task end to end: read the request, gather context from several systems, decide, act, confirm. Sometimes it works. Sometimes it retrieves the wrong record, misreads an ambiguous instruction, calls a tool with a subtly wrong argument, or completes something that looks successful and is not.

The customer's question is straightforward and unanswerable: what proportion of our tasks will this handle correctly, and can you tell me in advance which ones it will get wrong.

Ninety per cent is a good demo number and an unusable production number for anything where failure has a cost. A refund issued to the wrong account, a record deleted, a customer told something untrue — these are not degraded outputs, they are incidents, and a rate of one in ten is intolerable.

Failures are not uniformly distributed either. They concentrate on inputs with particular characteristics: unusual phrasing, multiple intents in one request, missing context, an edge case in the customer's own data. Which characteristics is discoverable only in production.

So deployments proceed as pilots with human review of everything, then human review of a sample, then human review of whatever the team is nervous about — a progression driven by accumulated comfort rather than by measurement.

## Why It's Unsolved
Evaluating a trajectory is genuinely much harder than evaluating an output. A task can be completed correctly by several different paths, so path comparison against a reference is wrong. It can also reach a plausible final state that is incorrect for reasons only visible in the customer's own system.

Ground truth is expensive and slow. Determining whether a task was handled correctly frequently requires a human who understands the customer's business, and at production volume that is exactly the cost the agent was bought to remove.

The tail is unbounded. The inputs that cause failure are by construction the ones nobody thought of, and no test set assembled in advance contains them. This is the same problem autonomous vehicles have and it is not solved there either.

Non-determinism compounds it. The same input can produce different trajectories, so a task that succeeded in testing may fail in production without anything having changed, which makes small-sample evaluation misleading in both directions.

And there is a commercial disincentive: a vendor able to state an honest completion rate would be publishing a number their competitors are not, in a market currently sold on demonstrations.

## What a Solution Looks Like
Per-task success prediction before or during execution. Whether this specific request is within the agent's demonstrated competence is predictable from features of the request and the agent's history on similar ones, and it turns a uniform review policy into a targeted one — review the ten per cent of tasks most likely to fail rather than a random sample.

Trajectory-level anomaly detection. A task whose trajectory diverges from the pattern of successful trajectories for that task type — unusual tool sequences, repeated retries, unexpected state transitions — is a candidate failure detectable during execution, which is when intervention is still cheap.

Outcome inference from downstream signals. Whether the customer came back, whether a human corrected the action, whether a subsequent request contradicts the first — these are free labels that arrive without human review and are largely unexploited.

Coverage measurement over the real input distribution. Clustering production requests and reporting per-cluster success rates tells a customer exactly where the agent is reliable and where it is not, which is the answer they actually wanted.

## Impact If Solved
Reliability is the constraint on every deployment in the category, and the current approach — pilot, watch, gradually relax review — is slow, expensive and unmeasured. Predicting failure per task lets human attention go where it is needed and lets a vendor state a completion rate honestly, which is what would move this market from demonstrations to procurement.
