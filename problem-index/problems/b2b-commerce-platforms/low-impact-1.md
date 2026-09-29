# Procurement System Integration

**Industry:** [[b2b-commerce-platforms|B2B Commerce Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Punchout and electronic ordering standards have existed for decades and are supported by every platform, and connecting to each large customer's procurement system remains a per-customer project measured in weeks.
**Tags:** #bert #word-embeddings #large-language-models #evaluation-metrics #transfer-learning #data-integration #workflow-orchestration

## The Problem
A large business customer buys through their own procurement system. Their buyer stays inside that system, punches out to the supplier's catalogue, selects items, and returns a requisition that flows through their approval process and comes back as a purchase order.

The standards for this — cXML, OCI, EDI — are old and well documented, and every B2B platform supports them.

Each connection is nonetheless a project. The customer's procurement platform is configured their way, with their custom fields, their account structure, their approval routing and their specific requirements for how the requisition must be formatted. Their unit of measure conventions differ from the supplier's. Their part numbering is their own and must be cross-referenced. Their tax and shipping expectations are configured on their side.

Weeks of integration work per customer, repeated for every large account, maintained as either side changes. For a distributor with hundreds of such customers this is a permanent team.

## What Already Exists
cXML, OCI and EDI standards are mature and widely implemented. Punchout is supported natively by every serious B2B platform. Specialist integration providers (TradeCentric and others) offer managed connectivity. Procurement platforms document their requirements. Electronic invoicing and purchase order flows are standard. Testing tools exist for the protocols.

## The Customisation Gap
The standards specify the envelope and the customer's configuration fills it, so compliance with cXML says almost nothing about whether a specific connection will work. The variation is in fields, conventions and expectations rather than in the protocol.

Nothing learns across connections. The same supplier has integrated to the same procurement platform dozens of times, with configurations that are largely repeats, and each new customer starts from the specification document.

Cross-reference mapping is a substantial and separate burden. The customer orders by their own part number and the supplier's catalogue uses another, and building and maintaining that crosswalk is manual per customer — and it is exactly the kind of matching problem that is now tractable.

Failure diagnosis is the fourth gap. When a requisition does not flow, the failure is somewhere between two systems and the supplier's integration team debugs it from their side with limited visibility, which is slow and is a recurring source of customer frustration at exactly the accounts that matter most.

## Impact If Solved
Procurement integration is the gate on selling to large customers electronically and is a permanent staffed cost that scales with the customer base. Learning configurations across prior connections and automating cross-reference mapping turns a multi-week project into a short one, which directly determines how many large accounts a supplier can serve.
