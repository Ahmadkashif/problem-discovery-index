# Integrated Change Order Workflow for Dev Projects

**Niche:** [[niches/software-dev-agencies/client-change-order-mgmt/profile|Client Change-Order Management]]
**Industry:** [[industries/software-dev-agencies|Software Dev Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product connects the client's change request to impact assessment, approval, scope update, and contract amendment in a single workflow integrated with the agency's project management tool.
**Tags:** #workflow-orchestration #automation #revenue-impact #ai-agent

## The Problem
A client sends a Slack message: "Can we add CSV export to the reporting dashboard?" The PM mentally estimates the effort (8 hours), responds in Slack ("sure, that would be about $1,200 and push the timeline by 2 days"), the client says "OK," and the PM adds a task to JIRA. The contract is not updated. The estimate is not documented. Three weeks later, the client disputes the additional charge because "I thought it was included in the reporting feature." The PM digs through Slack history to find the approval. This pattern, multiplied across 3-5 changes per project and 15-20 concurrent projects, costs agencies 5-15% of project revenue in unrecovered scope changes.

## Why Nobody Has Built This
Change order management exists in construction and manufacturing (Procore, Autodesk Build) but these tools model physical construction workflows (materials, subcontractor coordination), not software development. Software agencies have historically treated change orders informally because the industry culture favors agile flexibility over contractual rigidity. Building a change order tool risks being perceived as adversarial to clients, making agencies reluctant to adopt formal processes. The tool must be collaborative (helping the client understand the impact) rather than defensive (protecting the agency's margin).

## What to Build
A change order module that integrates with JIRA/Linear/Asana and provides: (1) a client-facing change request form (what they want, why, by when), (2) PM-facing impact assessment template (effort hours, cost, timeline shift, dependencies affected), (3) client approval workflow with e-signature on the cost and timeline change, (4) automatic scope update in the project management tool (new tasks created, timeline adjusted), (5) contract amendment generation with the change itemized, and (6) a change order ledger showing cumulative impact on project budget and timeline. The client portal shows the original scope, all approved changes, and the current total.

## Target Customer
Dev agencies with 10+ concurrent projects where change orders are managed through Slack/email and scope creep costs 5-15% of annual revenue.

## Impact If Built
Recovers 80% of currently untracked scope changes, worth 5-10% of project revenue. For a $3M agency, that is $150K-$300K in recovered revenue annually. Eliminates change-related client disputes by providing a clear approval trail.
