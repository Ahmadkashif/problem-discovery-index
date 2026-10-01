# Entitlements and Exchange Usage Reporting

**Industry:** [[financial-data-vendors|Financial Data Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Identity and billing systems handle users and seats perfectly well; none of them knows that an exchange counts a non-display algorithm, a derived index and a delayed quote on a second monitor as three different fee events.
**Tags:** #large-language-models #bert #feature-engineering #evaluation-metrics #data-integration #compliance #workflow-orchestration #automation

## The Problem
A vendor redistributing exchange data owes each exchange a monthly declaration: which subscribers received which feeds, at what level (real-time, delayed, end-of-day), on how many devices, and whether the data was used for display, non-display (algorithmic) or derived-data purposes. Each exchange — NYSE, Nasdaq, Cboe, LSEG, Deutsche Börse, dozens more — publishes its own policy with its own definitions and fee categories, and revises them annually. Exchanges audit vendors and their clients periodically, and an audit finding means back-billing, sometimes for years.

The declaration is assembled from the vendor's entitlement system (LSEG DACS, Bloomberg EMRS, or proprietary equivalents), client self-declarations of non-display use, and contract terms, and it is reconciled by a small team in spreadsheets against each exchange's policy document.

## What Already Exists
Identity and access management, SaaS subscription billing and usage metering are mature generic categories. Vendors have entitlement systems that switch feeds on and off per user. On the client side, inventory and cost platforms such as TRG Screen and Calero-MDSL track what was bought. Exchanges provide declaration templates and portals.

## The Customisation Gap
The gap is policy interpretation. Generic metering counts logins; exchange policy cares about the purpose of use, the device count, whether a display was "controlled," and whether a calculated value derived from exchange prices is itself fee-liable. Those rules live in policy PDFs that change every January, and their mapping onto entitlement events lives in one specialist's head.

What is missing is an obligation layer: each exchange policy parsed into structured fee rules, versioned by effective date, joined to entitlement and usage events, with every declared number traceable to the rule that produced it. Classifying client non-display self-declarations against policy categories, and flagging the client whose usage pattern does not match what they declared, are well-shaped language and anomaly tasks. A pre-audit reconciliation that reproduces last year's declarations under the policy then in force is what turns an audit from a dispute into a lookup.

## Impact If Solved
Exchange back-billing and audit disputes are a direct revenue leak for vendors and their clients, and the declaration work is done monthly by a handful of people whose departure is an existential risk to the process. Making the policy-to-declaration mapping explicit and testable removes most of the audit exposure and most of the month-end spreadsheet labour.
