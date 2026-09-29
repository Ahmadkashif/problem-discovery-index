# Reviewers Who Approve Everything

**Niche:** [[niches/ai-agent-platforms/action-authorisation-policy/profile|Action Authorisation Policy]]
**Industry:** [[industries/ai-agent-platforms|AI Agent Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Human-in-the-loop approval is the category's standard safety mechanism, and a reviewer shown four hundred correct actions in a row approves the four hundred and first without reading it.
**Tags:** #worker-facing #evaluation-metrics #hypothesis-testing #confidence-intervals #descriptive-statistics #compliance #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to place the human approval gate where the evidence says it belongs rather than where a nervous product manager guessed — and whoever does that takes the account, because gate placement determines whether a deployment saves anything.

## The Problem
An approval queue presents the agent's proposed action with a button. The agent is right most of the time, so the reviewer is right to approve most of the time, and within a fortnight they are approving in under two seconds without reading. The gate is now a formality that costs throughput and provides no protection — and everybody's risk assessment still counts it as a control. When the agent does propose something wrong, it is approved, and the incident review concludes that the human-in-the-loop step failed, which is a mischaracterisation of a design that made that outcome inevitable.

## Why It's Still Broken
Approval fatigue is a known human factors result and the category has not engaged with it, partly because the gate's existence is what makes deployments approvable. Nobody measures whether reviewers catch errors, so the control's ineffectiveness is invisible. The reviewer is usually a support agent under handle-time pressure, for whom careful review is unrewarded. And a gate that is technically present satisfies the risk assessment regardless of whether it works.

## What a Fix Looks Like
Measure whether the gate works, then design it so it can. Inject known-bad proposals at a low rate and measure the catch rate, which is the only way to know whether a reviewer is reviewing and is a standard technique in screening work — this single measurement tells you whether the control exists. Show only what the reviewer needs to judge: what changed, why the agent chose it, what looks unusual, and the consequence if wrong — rather than a full transcript they will not read. Highlight the anomalous element rather than presenting a uniform summary, since attention is the scarce resource. Reduce volume so that review is possible, which means removing gates that catch nothing and is where the build note's evidence-based placement pays off. Vary and prioritise, so low-confidence proposals are visibly marked and get the attention. Give the reviewer a fast path to reject with a reason, since rejection is currently more effortful than approval, which is exactly backwards. Measure and report catch rate per reviewer and per action type as an operational metric. And stop counting an unmeasured gate as a control in the risk assessment, because that is the misrepresentation on which the whole arrangement rests.

## Who Feels the Pain
Reviewers clicking through a queue that trained them to click; customers affected by an action a formality approved; and the buyers whose risk assessment counted a control that was not functioning.

## Impact If Fixed
Injecting known-bad proposals at a low rate measures whether the control exists at all, and it is the standard technique in screening work. Making rejection easier than approval inverts an incentive that currently runs against the gate's entire purpose.
