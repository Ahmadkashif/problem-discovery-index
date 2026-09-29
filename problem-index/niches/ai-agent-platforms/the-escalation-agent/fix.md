# Apologising Without Authority to Fix It

**Niche:** [[niches/ai-agent-platforms/the-escalation-agent/profile|The Escalation Agent]]
**Industry:** [[industries/ai-agent-platforms|AI Agent Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The support agent handling an agent's mistake frequently has less authority to correct it than the agent had to make it, so they apologise and escalate again.
**Tags:** #worker-facing #compliance #workflow-orchestration #evaluation-metrics #automation #descriptive-statistics #quick-win #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to hand a human the full account of what the agent did and a way to put it right — and whoever does that takes the account, because this handoff is where every agent failure becomes a customer's experience.

## The Problem
An agent issued a three-hundred-dollar refund in error. The support agent handling the complaint has a discretionary limit of one hundred dollars and cannot reverse a refund at all. To correct an action the software took autonomously they must escalate to a supervisor, who is in a meeting. The customer waits. The organisation granted more authority to a piece of software than to the experienced person cleaning up after it, which nobody decided deliberately — the agent's permissions were configured by a product team and the human's by a policy written years earlier, and no one compared the two.

## Why It's Still Broken
Agent permissions are configured in a platform and human permissions in an unrelated policy, and the two are owned by different functions who have never met. Granting the human matching authority looks like loosening a control, which is a harder conversation than granting it to software. The mismatch surfaces one escalation at a time and is never aggregated. And the support agent experiencing it has no standing to raise it.

## What a Fix Looks Like
Match the authority to the mess. Compare agent permissions against the human permissions of the people who handle its failures, which is a one-off audit that almost no organisation has done and which routinely finds the software better empowered than the staff. Grant the escalation handler at least the authority the agent had, since they are correcting its actions and a lesser authority guarantees a second escalation on every error. Provide a specific reversal authority for agent-caused actions, distinct from ordinary discretion, which is tightly scoped and does not require loosening general policy — this is the practical route through the objection. Make the reversal path direct rather than requiring the agent to reconstruct which systems changed. Pre-authorise correction within the magnitude of the original action, since correcting a three-hundred-dollar error is not a three-hundred-dollar decision. Track how often an escalation requires a further escalation, which measures the mismatch and is currently unmeasured. Give supervisors a queue view of agent-caused escalations, since these need a faster path than ordinary approvals. And review the permission comparison whenever agent permissions change, because the mismatch is reintroduced every time somebody widens the agent's scope.

## Who Feels the Pain
Support agents apologising for something they cannot fix; customers waiting twice for one error; and organisations that granted a system more authority than their staff without ever making that decision.

## Impact If Fixed
A one-off comparison of agent permissions against those of the staff who clean up after it routinely finds the software better empowered. A scoped reversal authority for agent-caused actions grants what is needed without loosening general policy.
