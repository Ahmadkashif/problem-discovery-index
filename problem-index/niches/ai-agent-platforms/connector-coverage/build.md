# Individually Shallow, Collectively Endless

**Niche:** [[niches/ai-agent-platforms/connector-coverage/profile|Connector Coverage]]
**Industry:** [[industries/ai-agent-platforms|AI Agent Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Tool calling is a solved model capability and connector standards now exist, and every deployment still stalls on integrations to the customer's own systems that are individually shallow and collectively endless.
**Tags:** #data-integration #large-language-models #automation #workflow-orchestration #evaluation-metrics #graph-theory #descriptive-statistics #compliance
**Contested on:** Every serious competitor in this niche is fighting to reach a customer's own systems without a bespoke integration project per deployment — and whoever does that takes the account, because integrations are where deployments stall after the agent already works.

## The Problem
An agent is working in a sandbox after two weeks. Production requires reaching the customer's order system, their internal returns service, their warehouse interface and a partner API. The order system has an interface specification that is three years out of date. The returns service has no documentation and one person who understands it. The warehouse interface returns success for operations that did not happen. The partner API behaves differently in this customer's tenancy. Four months later the agent goes live. The model capability was never the constraint and the connector standard addressed the protocol rather than any of this.

## Why Nobody Has Built This
The integration work looks bespoke because each customer's system is different, which conceals that the process of integrating is identical every time. Vendors staff it with forward-deployed engineers, which makes it a delivery cost rather than a product problem. Connector standards solved the protocol layer, which made the problem look addressed. And the semantics that actually matter are not in any specification, so there is nothing to automate against without eliciting them.

## What to Build
Generate what can be generated and elicit the rest deliberately. Generate connectors from whatever specification exists — interface definitions, schemas, database structures, existing client code — which handles the mechanical share and is now straightforward, and turns weeks into hours for the systems that are documented. Probe undocumented systems by observing existing traffic and inferring the interface, which is how the awkward internal services get covered and is what engineers do manually today. Elicit semantics with a structured checklist rather than by conversation: what does this status actually mean, which fields are required in practice, what happens on retry, what does a success response not guarantee — these are the questions whose answers determine whether the agent works and they are currently discovered by failing. Test the connector against agent-shaped behaviour — unusual sequences, retries, partial failures, concurrent calls — since agents exercise interfaces in ways a hand-written client never does and this is where integrations break in production. Build a reusable library per common customer system, since many customers run the same order and ticketing platforms and the second deployment should be far cheaper than the first. Record which integrations consume the most deployment time, so investment goes where it pays. Verify effects rather than trusting responses, given that some systems report success for operations that did not occur. And treat the connector's semantic description as a first-class artefact, which the fix note develops.

## Target Customer
Vendor delivery organisations, customer integration teams, and the connector standard communities whose protocol work has outrun the semantic problem.

## Impact If Built
The protocol layer is solved and the semantics are where deployments stall. A structured semantic checklist replaces discovery-by-failure, and testing connectors against agent-shaped call patterns catches what a hand-written client never would.
