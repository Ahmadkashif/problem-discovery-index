# No-Code App Builders

## Profile
**Category:** Horizontal SaaS
**Market Size:** ~$6B US no-code and low-code application development
**Tech Maturity:** Very high for building, near zero for owning — Airtable, Retool, Bubble, Glide, Softr, Zapier and Microsoft Power Platform have made it genuinely easy for a non-engineer to build something that works. Nothing in the category addresses what happens in year two, when the builder has changed roles and the app runs a business process.
**Workforce:** Solutions consultants, template and component authors, integration engineers, platform governance staff at large customers, customer success managers

## Key Pain Themes
Every successful no-code app eventually crosses from convenience into dependency, and that crossing is invisible. An operations person builds something to track a workflow, it spreads by usefulness, and within a year a real business process runs on an application with no owner, no documentation, no tests, no error handling and no backup plan. When the builder leaves, nobody can safely change it, and nobody can safely turn it off. Around that sit two chronic problems: integration connector coverage, where the marketplace is enormous and the connector for the specific system that matters is always missing or shallow; and governance, where IT cannot inventory what exists because the whole premise was that people build without asking. The citizen developer, meanwhile, has quietly acquired an unpaid second job supporting software, and the IT administrator inherits applications they did not build and cannot read.

## Current Tech Landscape
Airtable and Notion occupy the structured-data-plus-interface space; Retool serves developers building internal tools quickly; Bubble targets full application development; Glide and Softr build interfaces over existing data. Microsoft Power Platform has the deepest enterprise governance story by virtue of tenancy and licensing. Zapier and Make handle automation between systems. AI-generated application building has arrived quickly and accelerates creation, which sharpens the maintenance problem rather than addressing it. Governance and inventory tooling is thin everywhere except the Microsoft estate.

## Problems
- [[problems/no-code-app-builders/high-impact|🔴 High Impact: The Maintenance Cliff]]
- [[problems/no-code-app-builders/low-impact-1|🟡 Low Impact: Integration Connector Coverage]]
- [[problems/no-code-app-builders/low-impact-2|🟡 Low Impact: Application Inventory and Governance]]
- [[problems/no-code-app-builders/worker-life-1|🟢 Worker Life: The Citizen Developer's Second Job]]
- [[problems/no-code-app-builders/worker-life-2|🟢 Worker Life: IT Inheriting Orphaned Applications]]
- [[problems/no-code-app-builders/ml-opportunity|🧠 ML Opportunities]]
- [[problems/no-code-app-builders/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
These platforms hold something unusual: a complete, structured specification of thousands of business processes that were never documented anywhere else. A no-code app is, in effect, an executable description of how a particular company handles returns, or approvals, or onboarding — built by the person who actually does the work rather than by an analyst interviewing them. That corpus describes how organisations really operate, at a granularity no process documentation achieves, and the vendors use it to render an interface.
