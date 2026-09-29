# Asking Which Receipts Are Needed

**Niche:** [[niches/spend-management-platforms/documentation-and-receipts/profile|Documentation & Receipts]]
**Industry:** [[industries/spend-management-platforms|Spend Management Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An enormous automated effort collects documentation that nobody has established is required.
**Tags:** #compliance #large-language-models #evaluation-metrics #automation #data-integration #descriptive-statistics #confidence-intervals #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to collect only the documentation that is actually needed and to get it without nagging anybody — and whoever asks the auditors what they require first stops chasing most of it.

## The Problem
The platform requires a receipt above some threshold, chases it relentlessly, and escalates to freezing the card. The requirement came from a general belief about audit and tax expectations rather than from an examination of what auditors actually test, what the tax treatment genuinely requires for each category, or what the card network data already establishes. For a large share of transactions the merchant name, amount, date and category are fully known from the authorisation, and the receipt adds nothing that will ever be looked at.

## Why Nobody Has Built This
The requirement was inherited from paper-era expense policy, so it was automated rather than reconsidered — automating an unexamined rule is faster than questioning it and produces a visible feature. Nobody wants to be the party that relaxed a control before an audit. Auditors were never asked directly. And the cost is paid in employee minutes, which no system measures.

## What to Build
Scope the requirement, then satisfy it from data. Establish what auditors and tax treatment actually require by category, amount and context, which is the core and is a research exercise the category has skipped entirely. Use the transaction data itself as documentation where it is sufficient, since merchant, amount, date and category are captured and are what most receipts would show. Obtain itemisation directly from merchants where integrations allow, because that removes the employee from the loop for the largest recurring categories. Require receipts only where they add something — itemisation for meals with attendees, business purpose for ambiguous merchants, tax detail where treatment depends on it — which is a much smaller set. Capture business purpose at the moment of spend rather than chasing it later, as the employee knows it then and has forgotten it in a fortnight. Extract and validate automatically rather than storing an image nobody reads, since an unread image is not evidence of anything. Measure how many collected receipts are ever examined, which will be a very small number and is the finding that changes the policy. Vary the requirement by company and auditor, because it genuinely differs and a single global threshold satisfies nobody exactly. Keep evidence retrievable for the periods that matter, since the audit case is real even if it is narrower than assumed. And report employee time spent on documentation, as it is the cost that justifies the whole exercise.

## Target Customer
Product and accounting leadership, employees chasing their own receipts, controllers enforcing a rule nobody validated, and auditors who were never consulted.

## Impact If Built
An unexamined rule was automated rather than reconsidered, because automating is faster and produces a visible feature. Establishing what auditors actually test — and substituting transaction data where it suffices — removes most of the chase.
