# Client Change-Order Management

**Parent Industry:** [[industries/software-dev-agencies|Software Dev Agencies]]
**Category:** Highly Automatable

## Profile
**Market Size:** $1B (internal spend)
**Share of Parent Industry:** N/A (operational cost, not revenue)
**Digital Adoption:** Low — Most agencies manage change orders through email threads, Slack messages, and verbal agreements, with formal documentation created retroactively (if at all).
**Target Buyer:** Project managers and account managers at dev agencies who handle client requests for scope changes during active projects.
**Automation Potential:** High — Change order workflows follow a deterministic process: client requests change, PM evaluates impact (hours, timeline, cost), client approves, scope is updated, contract is amended.

## What Makes This a Distinct Niche
Every dev agency project experiences scope changes — clients realize they need additional features, want to modify approved designs, or discover requirements they did not articulate initially. The average project has 3-5 change requests. Each change requires: documenting what the client wants, estimating the effort, communicating the cost and timeline impact, getting client approval, updating the project plan, and amending the contract. Most agencies handle this through informal channels — a Slack message saying "can you also add X?" followed by a verbal agreement, with the PM updating the project plan but not the contract. This informality leads to scope creep (changes without cost recovery), disputes (client denies approving additional cost), and margin erosion (changes absorbed to maintain the relationship).

## Current Tools & Gaps
JIRA and Linear track tasks but do not model the commercial dimension of changes (cost impact, contract amendment, client approval). PandaDoc and DocuSign handle contract amendments but are disconnected from the project management workflow. No tool provides an integrated change order workflow: request capture, impact assessment, client approval, scope update, and contract amendment in a single flow tied to the project management system.

## Problems
- [[niches/software-dev-agencies/client-change-order-mgmt/build|🔨 Build: Integrated Change Order Workflow for Dev Projects]]
- [[niches/software-dev-agencies/client-change-order-mgmt/buy|🛒 Buy: Scope Change Impact Calculator]]
- [[niches/software-dev-agencies/client-change-order-mgmt/fix|🔧 Fix: Verbal Approval Audit Trail Gap]]
