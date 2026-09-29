# A Delivery Model That Does Not Scale

**Niche:** [[niches/ai-agent-platforms/the-forward-deployed-engineer/profile|The Forward-Deployed Engineer]]
**Industry:** [[industries/ai-agent-platforms|AI Agent Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Forward-deployed engineers live inside customer deployments tuning agents by hand against edge cases, in a role that is the vendor's entire delivery model and does not scale.
**Tags:** #worker-facing #automation #evaluation-metrics #tacit-knowledge-ml #data-integration #workflow-orchestration #descriptive-statistics #large-language-models
**Contested on:** Every serious competitor in this niche is fighting to make a deployment work without a person living inside it — and whoever does that takes the market, because the delivery model is currently a headcount line that grows with revenue.

## The Problem
An engineer spends eleven weeks at a customer. Four weeks on integrations, three on discovering that the customer's returns policy has six exceptions nobody documented, two tuning prompts against those exceptions, and two on the escalation rules. The deployment works. The next customer, in the same industry, with the same platform vendor and a similar returns policy, gets a different engineer who spends eleven weeks discovering five of the same six exceptions from scratch. Nothing from the first deployment exists in a form the second can use, and the company's growth plan requires hiring engineers at the rate it signs customers.

## Why Nobody Has Built This
Each deployment feels bespoke because each customer's business genuinely differs, which hides how much of the work is the same. The engineers are the only people who could build the reusable layer and they are permanently deployed. Delivery cost is tolerated during a growth phase in a way it will not be later. And the knowledge is tacit — the engineer knows which prompt shape works for which task and cannot easily say why.

## What to Build
Turn the deployment into a product with a person at the judgement points. Build vertical deployment templates — for support, for order operations, for a given industry — carrying the workflows, the common exceptions, the escalation patterns and the integration set, so the eleventh customer in a vertical starts at seventy percent rather than at zero, which is the core of the build and the thing that breaks the linear headcount relationship. Maintain an edge case library per domain, which the fix note develops and which is the most reusable artefact the engineers produce. Structure the discovery process into a questionnaire, since the exceptions the engineer finds in week five are mostly things the customer could have said in week one if asked precisely. Capture every tuning decision with its reason, because that is the tacit knowledge and a one-line reason field collects it at almost no cost. Instrument where deployment time goes, so investment targets the actual bottleneck rather than the remembered one. Generate the initial configuration from the customer's own historical task data, which is available and unused and would replace a large part of manual discovery. Make the engineer a reviewer of a generated deployment rather than its author, which is the shape this should converge on. And feed recurring customer-specific work back into the product, since anything done at five customers is a product gap.

## Target Customer
Vendor delivery organisations and their leadership, the engineers living on site, and the investors valuing a business whose delivery cost currently scales with revenue.

## Impact If Built
The delivery model is a headcount line growing with revenue in a business valued as though it is not. Vertical templates plus a domain edge-case library are what break that relationship, and generating the initial configuration from the customer's own task history replaces much of the manual discovery.
