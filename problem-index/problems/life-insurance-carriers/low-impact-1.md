# Annuity Best-Interest Review at Volume

**Industry:** [[life-insurance-carriers|Life Insurance Carriers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every annuity application, and every replacement above all, must pass a carrier suitability review before issue, and carriers run it as a manual queue on top of document tools built for other jobs.
**Tags:** #large-language-models #bert #transformers #evaluation-metrics #compliance #workflow-orchestration #automation

## The Problem
Under the NAIC's best-interest revisions to the Suitability in Annuity Transactions Model Regulation, adopted in 49 jurisdictions by August 2025, and New York's Regulation 187, the carrier must keep a supervision system that reviews each recommended annuity before issue. A reviewer reads the application, the consumer profile form, the producer's disclosure and rationale, and for a replacement or 1035 exchange the comparison of the surrendered contract's values, surrender charges and lost benefits against the new one. With US retail annuity sales at a record $464.1B in 2025 (LIMRA), a mid-size annuity writer can face hundreds of these files a day (estimate). Most are clean. A small share, such as an 82-year-old moving most of her liquid assets into a ten-year surrender schedule, need real judgement. They wait in the same queue.

## What Already Exists
E-application and order-entry platforms (iPipeline, Hexure FireLight, DTCC's annuity processing) enforce required fields. Intelligent document processing tools (Hyperscience, ABBYY, the cloud providers' document AI) extract data from scanned forms. Broker-dealer supervision systems handle variable annuities sold through registered representatives under FINRA Rule 2330 and Reg BI. Carriers' own rules engines flag age, liquidity and surrender-charge thresholds.

## The Customisation Gap
None of these tools knows the suitability rule. The carrier-specific layer has five parts. First, the regulation's elements by state, including the consumer profile factors, the replacement rules and the documentation the producer must give. Second, replacement analysis that reads the surrendered contract's statement, which arrives in a different format from each issuing carrier, and computes what the client gives up. Third, the carrier's own supervision procedures and escalation thresholds. Fourth, the producer's rationale read against the profile: does the stated reason actually fit this client? Fifth, an examination-ready record of why each case was approved. Generic document AI extracts fields. It does not decide whether a rationale is boilerplate pasted into forty files from the same producer.

## Impact If Solved
Clean files clear in minutes rather than days, so suitability stops holding up premium. Reviewer time moves to the few cases with real consumer risk, and the carrier gains a consistent record to show a market conduct examiner. That matters because suitability findings in examinations, and replacement complaints, are among the most common sources of annuity market-conduct trouble (estimate).
