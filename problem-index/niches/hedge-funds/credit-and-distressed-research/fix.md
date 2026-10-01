# The Amendment Nobody Re-Read

**Niche:** [[niches/hedge-funds/credit-and-distressed-research/profile|Credit & Distressed Research]]
**Industry:** [[industries/hedge-funds|Hedge Funds]]
**Type:** Fix (Pain Point)
**One-liner:** A borrower amends its credit agreement, the fund's summary stays as it was, and the position's risk changes without anyone noticing.
**Tags:** #large-language-models #change-point-detection #evaluation-metrics #compliance #quick-win #automation
**Contested on:** This niche is not terminal — reading the documents of a performing credit portfolio for what borrowers are permitted to do, and anticipating how a restructuring or liability management exercise will treat each tranche, are different contests with different winners, stated separately in the sub-niches.

## The Problem
Amendments arrive frequently and are often minor. Occasionally one loosens a basket or changes an amendment threshold in a way that enables a later transaction against the fund's interests. The analyst's summary on file reflects the original document; nobody re-reads the full chain when a small amendment lands.

## Why It's Still Broken
Re-reading is expensive and most amendments are innocuous, so triage is by intuition.

## What a Fix Looks Like
Diff every amendment against the structured current state, flag changes to the provisions that matter, and update the instrument record with the change and its source. Alert the analyst only when a material term moves.

## Who Feels the Pain
Credit analysts responsible for documents they cannot keep current; PMs surprised by transactions their documents allowed.

## Impact If Fixed
Material document changes are seen when they happen rather than when they are used against the fund.
