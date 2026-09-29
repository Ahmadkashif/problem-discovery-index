# Action Authorisation Scoping

**Industry:** [[ai-agent-platforms|AI Agent Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every platform offers human-in-the-loop approval and permission scopes, and where to put the approval gate is decided by a nervous product manager guessing, which produces either an agent nobody trusts or one that reviews everything and saves nothing.
**Tags:** #gradient-boosting #logistic-regression #confidence-intervals #evaluation-metrics #hypothesis-testing #markov-decision-processes #compliance #workflow-orchestration

## The Problem
Agents take actions with consequences: issuing refunds, modifying records, sending communications, executing transactions. Deciding which actions require human approval is the central safety decision in every deployment.

The decision is made by intuition, usually conservatively, usually at the level of an action type. Refunds over a threshold need approval. Record deletions need approval. Emails to customers need approval.

The threshold is a guess. It was set at a hundred dollars because that sounded reasonable, and it stays there. It does not account for the agent's actual reliability on refund tasks, which is measurable, or for the fact that reliability varies enormously with the shape of the request.

The failure mode runs both ways. Set the gate too tight and a human reviews everything, which reproduces the cost the agent was meant to remove and — worse — produces rubber-stamping, since a reviewer approving three hundred correct actions in a row stops reading. Set it too loose and the first bad action becomes an incident that suspends the deployment.

Reversibility, which is the property that should dominate this decision, is barely represented. Sending an email is irreversible and cheap; modifying a record is reversible and feels serious.

## What Already Exists
Human-in-the-loop approval is standard across the frameworks and vertical products. Permission scoping through role-based access control is mature. Approval workflow tooling is widely available. Audit logging of agent actions is standard. Confidence thresholds are exposed as configuration in several platforms. Sandbox and dry-run modes exist for testing.

## The Customisation Gap
Nothing connects approval placement to measured reliability. The platform knows the agent's success rate on refund tasks, and how that rate varies by request characteristics, and the approval threshold is a static number set before any of that was known.

Risk-based routing is the obvious design and nobody offers it. Approval should be a function of predicted failure probability multiplied by the cost and reversibility of the action, evaluated per task rather than per action type, and every input to that calculation is available.

Reversibility is not modelled at all. Actions differ enormously in whether a mistake can be undone, and an authorisation model that does not represent this is optimising the wrong variable.

Reviewer behaviour is unmeasured, which is the quiet failure. Whether approvals are meaningful is testable — approval latency, whether reviewers ever reject, whether rejections correlate with genuinely bad actions — and a reviewer approving everything in two seconds is providing no safety while providing the appearance of it.

## Impact If Solved
Authorisation scoping determines whether an agent deployment delivers value or reproduces the cost it was meant to remove, and it is set by intuition and never revisited. Risk-based routing using measured reliability sends human attention to the small fraction of actions where it changes an outcome, which is the only version of human-in-the-loop that survives contact with volume.
