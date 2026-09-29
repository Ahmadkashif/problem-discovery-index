# Application Inventory and Governance

**Industry:** [[no-code-app-builders|No-Code App Builders]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Admin consoles list every app in the tenant, which is useful only if the company knows which tenants exist — and the premise of the category is that people sign up without asking.
**Tags:** #gradient-boosting #bert #graph-neural-networks #k-means-clustering #evaluation-metrics #compliance #data-integration

## The Problem
An IT or security function needs to know what applications process company data, what data they hold, who can access them, and whether they meet whatever obligations apply. That is basic and it is the premise of every compliance framework.

No-code makes it structurally difficult. The category's growth model is individual and team adoption without procurement, so applications exist in tenants IT does not administer, built by people who did not consider themselves to be creating an application, connected to systems through credentials the builder pasted in.

The consequences are ordinary and cumulative. Customer data copied into a tool nobody reviewed. An app sharing a public link that was convenient at the time. Credentials embedded by someone who has since left. An access model that is whatever the default was.

Where a governed platform exists — the Microsoft estate is the best case — the admin console genuinely helps. Everywhere else the inventory is a survey, and surveys find the apps people remember to mention.

## What Already Exists
Admin consoles and audit logs are provided by every major platform. Microsoft Power Platform has the deepest environment and data-loss-prevention story. SaaS management platforms (Zylo, Torii, Productiv) discover applications from expense and single sign-on data. Cloud access security brokers detect unsanctioned usage from network traffic. Data classification tools exist for known repositories.

## The Customisation Gap
Discovery is the first gap and is partially solvable with existing signals — expense records, single sign-on grants, OAuth consent to corporate accounts — which SaaS management tools use and which no-code vendors do not surface to their own enterprise customers.

Data sensitivity classification is the second and is where the real risk sits. Knowing that an app exists is far less useful than knowing it holds customer personal data, and that is inferable from the schema and the sample content rather than from asking the builder, who will underestimate.

Risk scoring should combine what the app holds, who can reach it, whether it is externally shared, and how critical it has become — which is the same criticality signal that matters for maintenance, computed once and used twice.

Credential hygiene is the third gap and is concrete: embedded credentials, tokens belonging to departed employees, and connections using personal rather than service accounts are all detectable and are rarely reported.

## Impact If Solved
Every organisation with no-code adoption has data in applications it cannot enumerate, and the governance response has been either a survey or a prohibition that drives usage underground. Inferring existence, sensitivity and risk from signals already available makes proportionate governance possible without contradicting the category's premise.
