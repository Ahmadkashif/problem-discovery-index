# A Tool Description That Omits What Matters

**Niche:** [[niches/ai-agent-platforms/connector-coverage/profile|Connector Coverage]]
**Industry:** [[industries/ai-agent-platforms|AI Agent Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A tool is described to the agent by its parameters and a one-line summary, omitting that it is irreversible, that the status field means something counter-intuitive, and that calling it twice charges twice.
**Tags:** #large-language-models #data-integration #evaluation-metrics #compliance #automation #descriptive-statistics #quick-win #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to reach a customer's own systems without a bespoke integration project per deployment — and whoever does that takes the account, because integrations are where deployments stall after the agent already works.

## The Problem
The agent has a tool called issue_refund with three parameters and the description "issues a refund to the customer". Not stated: it is not idempotent, so a retry after a timeout refunds twice. Its success response means the request was accepted rather than that money moved. It cannot be reversed. It fails silently for orders older than ninety days, returning success. An engineer integrating this by hand would learn all four from the documentation or from a colleague. The agent has only the description, and every one of those four facts is a production incident waiting for the right input.

## Why It's Still Broken
Tool descriptions were written for the model to choose the right tool, not for it to use the tool safely, and the format reflects that. The facts that matter are known to the integration engineer at the moment they write the connector, and there is no field to put them in. Idempotency and reversibility are not part of any interface specification convention. And the consequences appear as agent errors, which are attributed to the agent rather than to the description it was given.

## What a Fix Looks Like
Put the operative facts in the description. Extend the tool definition with the properties the agent needs to act safely — idempotent or not, reversible or not, effectful or read-only, the meaning of each status, known failure modes including silent ones, and preconditions — which is a schema change and a few sentences per tool, and it is the highest-return fix in this niche. Require the integration engineer to fill them in, since they know the answers at the moment of integration and nobody will ever know them as cheaply again. Surface them to the agent at decision time and to the orchestration layer for authorisation and retry policy, so a non-idempotent tool is not blindly retried. Test the declared properties, since an engineer's belief that an operation is idempotent is sometimes wrong and verifying it is straightforward. Record observed failure modes back into the description, so the definition improves as the deployment runs. Describe what a success response does and does not guarantee, which is the single most common source of silent failure here. Version tool definitions, since a change in a tool's semantics changes the agent's behaviour and currently does so untracked. And propagate the properties into compensation and authorisation, since the whole reason to declare them is that other parts of the system need to act on them.

## Who Feels the Pain
Customers double-refunded by a retry; support agents explaining an action nobody intended; and the engineers who knew all four facts and had nowhere to write them down.

## Impact If Fixed
The integration engineer knows the operative facts at the moment they write the connector and there is no field to record them. A schema extension carrying idempotency, reversibility and the meaning of a success response feeds retry policy, authorisation and compensation at once.
