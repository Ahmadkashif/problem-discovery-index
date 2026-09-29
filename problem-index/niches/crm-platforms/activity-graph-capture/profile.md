# Activity Graph Capture

**Parent Industry:** [[industries/crm-platforms|CRM Platforms]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in activity capture is fighting to reconstruct a complete, correctly attributed engagement graph from email and calendar without asking a representative to do anything — and whoever holds coverage and attribution accuracy highest takes the account.

## Profile
**Market Size:** ~$2.1B US activity capture, engagement tracking and sales engagement platforms
**Share of Parent Industry:** ~6% of CRM revenue
**Digital Adoption:** High — capture is widely deployed and its completeness is rarely measured
**Target Buyer:** Revenue operations as the technical owner; sales leadership as the sponsor
**Automation Potential:** Very High — this is entity resolution over a stream, with clean ground truth available

## What Makes This a Distinct Niche
The engagement graph is the record of who from the selling side interacted with whom on the buying side, when, through what channel, and with what response. It is the substrate for behavioural forecasting, for multi-threading analysis, for account planning and for territory and coverage decisions, and it is reconstructed from email headers, calendar entries, engagement events and phone metadata rather than from anything a representative types. That makes it a resolution problem: matching an email address to a contact, a contact to an account, an account to the right node in a corporate hierarchy, and an interaction to the deal it concerns. Every one of those matches can fail quietly, and a graph with 70% coverage looks identical to one with 95% coverage in every dashboard built on it. Unlike its sibling sub-niche there is no recording, which removes the consent conversation about customers and replaces it with a different one about reading employees' mailboxes.

## Current Tools & Gaps
Salesforce and HubSpot both offer native capture; Clari, Outreach, Salesloft and People.ai built businesses on doing it better; the email and calendar platforms expose the necessary APIs. Capture works and coverage is uneven. The gaps: nobody publishes or even computes a coverage figure, so a customer cannot tell what proportion of real interactions the graph contains — which is the single most important property of the product and is invisible; contact-to-account resolution fails on personal addresses, contractors, subsidiaries and people who have changed jobs, and the failures are silent; deal attribution — which of the account's several open opportunities an email concerns — is frequently a guess; and the employee privacy position is handled by policy rather than by design, in a product that reads a person's mailbox continuously.

## Problems
- [[niches/crm-platforms/activity-graph-capture/build|🔨 Build: A Graph With a Published Coverage Figure]]
- [[niches/crm-platforms/activity-graph-capture/buy|🛒 Buy: Entity Resolution and Identity Graph Tooling]]
- [[niches/crm-platforms/activity-graph-capture/fix|🔧 Fix: Reading the Mailbox Without a Designed Privacy Position]]
