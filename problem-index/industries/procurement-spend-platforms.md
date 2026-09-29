# Procurement & Spend Platforms

## Profile
**Category:** Horizontal SaaS
**Market Size:** ~$9B US procurement, source-to-pay and spend management software
**Tech Maturity:** High at the transaction layer, weak at the classification one — Coupa, SAP Ariba, Oracle, Jaggaer and Zip run requisition, approval and purchase order workflow; Ramp, Brex and Navan have attacked the same problem from the card side. Every one of them reports spend by category, and the categories are wrong.
**Workforce:** Category managers, procurement analysts, supplier master data staff, implementation consultants, sourcing specialists, contract compliance analysts

## Key Pain Themes
Spend analytics is the category's central promise and rests on two things that are broken everywhere: transactions classified into categories by an engine that reads a supplier name, and a supplier master that contains the same vendor eleven times. Everything downstream — negotiation leverage, consolidation opportunity, tail spend analysis, savings reporting — inherits both errors. Beneath that, contracted prices are negotiated carefully and then not enforced, because nobody compares the invoice line against the contract term at the moment of payment. Supplier risk monitoring has become a real requirement through concentration, sanctions and resilience concerns, and is served by expensive external subscriptions that tell a company nothing about its own exposure. The people doing the work — category managers assembling sourcing events, and analysts chasing intake requests that arrive as Slack messages — spend their time on assembly rather than on negotiation.

## Current Tech Landscape
Coupa and SAP Ariba dominate enterprise source-to-pay with long implementations; Jaggaer serves specific verticals; Zip and Oro have grown on intake and orchestration, which is where the real friction turned out to be. Spend classification is offered by the suites and by specialists, typically at supplier level. Supplier risk data is licensed from Dun & Bradstreet, EcoVadis, Craft and others. Contract lifecycle management sits adjacent and rarely connects to invoicing. Card-based spend management has taken a growing share of tail spend by making the employee experience better than the requisition process.

## Problems
- [[problems/procurement-spend-platforms/high-impact|🔴 High Impact: Spend Classification and the Supplier Master]]
- [[problems/procurement-spend-platforms/low-impact-1|🟡 Low Impact: Contract Price Compliance at Invoice]]
- [[problems/procurement-spend-platforms/low-impact-2|🟡 Low Impact: Supplier Risk and Concentration Monitoring]]
- [[problems/procurement-spend-platforms/worker-life-1|🟢 Worker Life: Analyst Intake Request Triage]]
- [[problems/procurement-spend-platforms/worker-life-2|🟢 Worker Life: Category Manager Sourcing Event Assembly]]
- [[problems/procurement-spend-platforms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/procurement-spend-platforms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
A procurement platform serving thousands of enterprises observes the same suppliers, the same commodities and the same contract terms across all of them. What a given item actually costs, what terms are achievable, which suppliers deliver on time and which do not — these are answerable across the customer base and are asked constantly by every customer individually. The vendors instead sell each enterprise a view of its own spend, classified by an engine that guesses from a supplier name, which is the narrowest possible use of the broadest available dataset.
