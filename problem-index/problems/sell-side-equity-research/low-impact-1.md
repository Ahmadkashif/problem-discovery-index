# Pre-Publication Compliance Review

**Industry:** [[sell-side-equity-research|Sell-Side Equity Research]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every research report must clear disclosure, quiet-period, restricted-list and price-target-basis checks before release, and the supervisory analyst does most of it by reading.
**Tags:** #large-language-models #bert #evaluation-metrics #compliance #workflow-orchestration #automation #quick-win

## The Problem
Before a report is published a supervisory analyst (Series 16) and research compliance review it. They check that the company is not on the restricted list or inside a quiet period around an offering the firm is managing; that the conflict disclosures under FINRA Rule 2241 are complete and current — investment banking relationships in the past twelve months, market-making, ownership positions; that a price target has a stated valuation basis and stated risks; that the ratings distribution and price-target history chart are attached; that the Reg AC certification is present; and that the language does not promise or imply things the analyst cannot support. On earnings mornings dozens of reports arrive in the same two hours.

## What Already Exists
BlueMatrix and in-house publishing systems pull standard disclosures from a disclosure database and attach rating-history charts automatically. Communication surveillance vendors (Smarsh, Global Relay, NICE Actimize) review email and chat. Generic LLM proofreading tools exist. Restricted and watch lists are maintained by the control room.

## The Customisation Gap
What the tools do not do is read the report the way the supervisory analyst does. Does the price-target paragraph actually state a methodology and risks, or only a number? Does the text mention a company in the report body — a peer or a supplier — that carries its own disclosure obligation and is not in the disclosure block? Has the rating changed without the rating-change language? Does the tone in a report on a company where the firm is pitching for a mandate read as promotional? Is a forward-looking statement framed as fact? These checks depend on Rule 2241 semantics, the firm's own written supervisory procedures and the control room's live lists, and they are a precise, bounded language task that no generic tool is configured for. A pre-review pass that flags these specific failures, with the rule cited, lets the supervisory analyst spend the earnings-morning rush on the reports that actually need judgment.

## Impact If Solved
Report release is a bottleneck on the one morning per quarter when speed matters most, and the failure mode is a FINRA finding or a client receiving a report that should have been embargoed. A Rule-2241-aware pre-review layer shortens release time and makes the supervisory review auditable at the level of the specific check.
