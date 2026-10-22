# From a New Regulation to a Test Plan per Product

**Niche:** [[niches/testing-laboratories/product-compliance-regulatory-intelligence/profile|Product Compliance Regulatory Intelligence]]
**Industry:** [[industries/testing-laboratories|Testing Laboratories]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Regulatory intelligence vendors tell a manufacturer that a regulation changed; nobody tells it which of its products now need which tests, at which lab, before the effective date.
**Tags:** #large-language-models #transformers #graph-theory #k-nearest-neighbors #evaluation-metrics #compliance #revenue-impact
**Contested on:** Every serious competitor in this pocket is fighting to tell a manufacturer, before the effective date, exactly which of its products a new or changed regulation applies to and what evidence it needs — and whoever maps regulatory change to product scope most accurately and earliest keeps the compliance team's subscription.

## The Problem
A vendor's alert says a substance limit has tightened, a product category has been brought into scope, or a referenced standard has a new edition. The manufacturer's compliance team then has to work out, product by product, whether the change applies — which depends on materials, components, intended users and markets — and whether existing test reports still cover the product or new testing is needed. That second step is done by engineers in spreadsheets, often weeks after the alert, and it is the step that decides whether the client makes the effective date.

## Why Nobody Has Built This
Content vendors stop at the regulation because they don't hold the client's product data; product-compliance and PLM systems hold the products but not the interpreted regulation; testing labs see only the products clients send them. Joining the three requires a structured model of each regulation's scope and thresholds that the content vendor already maintains in prose.

## What to Build
Express each tracked regulation as machine-readable applicability rules — product scope, thresholds, exemptions, referenced standards and editions, effective dates — and match them against a client's product and material data to produce a dated worklist: affected products, the evidence gap for each, and the tests needed, ready to send to a lab for quotation. Every applicability decision carries a link to the clause and the vendor's interpretation, and client corrections feed back into the rules.

## Target Customer
Heads of regulatory content and product at product-compliance intelligence vendors, selling the capability to compliance directors at manufacturers with large multi-market portfolios.

## Impact If Built
The vendor's subscription moves from alerts to decisions, which is the difference that keeps a compliance team renewing, and manufacturers turn regulatory change into scheduled testing months before the effective date rather than shipment holds after it.
