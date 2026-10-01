# Product Analytics for a Seat Business

**Niche:** [[niches/financial-data-vendors/terminal-desktop-workflow/profile|Terminal & Desktop Workflow]]
**Industry:** [[industries/financial-data-vendors|Financial Data Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** SaaS product analytics measures engagement in clicks and sessions; a terminal seat is renewed on whether its data reached a deliverable the client was paid for.
**Tags:** #gradient-boosting #survival-analysis #feature-engineering #evaluation-metrics #causal-inference #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to be the surface where the analyst's model actually gets built — the Excel add-in, the API pull and the screen that feeds the memo — and whoever is embedded in that workflow keeps the seat when the client's market data office comes looking for cuts.

## The Problem
Seat cancellations happen in the client's annual market data review, where a manager looks at a usage report and cuts the seats that look idle. Vendors respond with usage reports of their own, built on logins and function calls. Neither side measures the thing that matters: whether the seat's data fed models, screens and documents that the client's research or deal process depended on.

## What Already Exists
Product analytics platforms (Amplitude, Mixpanel, Pendo), churn prediction in customer success tools (Gainsight), and survival models for subscription retention are mature and widely used across SaaS.

## The Customization Gap
The adaptation is to a seat whose value is mostly realised outside the application: (1) value flows through the Excel add-in and API, so engagement must be measured as data pulled into persistent artefacts, not as sessions; (2) the renewal decision is made by a market data manager, not the user, on a cost-review calendar the vendor can predict; (3) seats are fungible within a client but users are not, so a heavy user leaving the client is the real churn signal; (4) competitive substitution is per function — a client may keep the seat for one dataset and buy everything else elsewhere — so risk must be modelled by content set; and (5) the intervention is usually training on a workflow, which has a measurable causal effect on retention that should be estimated rather than assumed.

## Target Customer
Desktop product and client success leadership at terminal and platform vendors.

## Impact If Solved
Seat churn is the revenue line most exposed to client cost-cutting, and it is currently forecast from metrics that do not measure value. Modelling embedding rather than activity tells the vendor which seats are at risk early enough to change the outcome.
