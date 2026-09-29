# Tool and Connector Coverage

**Industry:** [[ai-agent-platforms|AI Agent Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Tool calling is a solved model capability and connector standards now exist, and every deployment still stalls on integrations to the customer's own systems that are individually shallow and collectively endless.
**Tags:** #large-language-models #transformers #evaluation-metrics #transfer-learning #data-integration #workflow-orchestration #automation

## The Problem
An agent is only as capable as what it can reach. A support agent needs the ticketing system, the order system, the subscription database, the shipping provider and the customer's own internal knowledge base. A sales agent needs the CRM, the calendar, the quoting tool and the contract repository.

Each integration is straightforward and each is different. Authentication varies. Pagination varies. Error semantics vary. Rate limits vary. The customer's instance has custom fields, a workflow nobody documented, and a legacy system with a SOAP interface.

So every deployment includes an integration phase, performed by the vendor's forward-deployed engineers, that is largely undifferentiated engineering work. It sits on the critical path to value, it recurs at every customer, and the same integration is built repeatedly with per-customer variations.

Then the customer's systems change and the integration breaks, and maintaining a long tail of connectors across a growing customer base becomes a permanent cost the vendor did not price for.

## What Already Exists
Tool calling is reliable in current models and no longer the constraint. The Model Context Protocol has emerged as a connector standard with meaningful adoption and solves the interface problem cleanly. Integration platforms (Workato, Tray, Merge, Paragon) offer unified APIs across categories of SaaS application. OpenAPI specifications exist for most modern APIs. Authentication patterns are standard.

## The Customisation Gap
Unified API products normalise the common fields across vendors in a category and stop exactly where the customer's configuration begins. Custom fields, custom objects and customer-specific workflow are the parts that matter for a real deployment and are by definition outside any pre-built normalisation.

Tool description quality is the underappreciated gap. An agent's ability to use a tool correctly depends heavily on how the tool is described, and descriptions are written by engineers as an afterthought. Which descriptions actually produce correct tool selection is measurable from trajectory data and is not measured, so a systematic source of agent failure is treated as a model limitation.

Generating integrations from specifications is the obvious unexploited path. An OpenAPI document plus the customer's instance schema plus the vendor's corpus of prior integrations is enough to propose a working connector with sensible tool descriptions, and the vendor has built hundreds of them.

Breakage detection is the fourth gap: connector failures in production surface as agent failures, which are attributed to the agent rather than to the integration, which sends debugging in the wrong direction.

## Impact If Solved
Integration is the critical path to every deployment and a permanent maintenance cost that scales with the customer base rather than with revenue. Generating connectors from specifications and measuring which tool descriptions actually work converts undifferentiated engineering into a product capability, and fixes a source of agent failure currently blamed on the model.
