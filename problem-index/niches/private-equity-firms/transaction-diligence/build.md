# Six Workstreams, No Shared Ledger of Findings

**Niche:** [[niches/private-equity-firms/transaction-diligence/profile|Transaction Diligence]]
**Industry:** [[industries/private-equity-firms|Private Equity Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Quality of earnings, commercial, legal, insurance, IT and environmental providers each deliver a report, and the deal team is the only place their findings meet.
**Tags:** #large-language-models #transformers #word-embeddings #evaluation-metrics #workflow-orchestration #data-integration
**Contested on:** This niche is not terminal — establishing what the earnings really are and establishing whether the revenue will persist are different contests with different providers, evidence and winners, and they are stated separately in the sub-niches below.

## The Problem
On a mid-market deal the sponsor engages four to seven diligence providers, each with its own request list, its own data room folder and its own report. Findings interact: a customer contract the lawyers flag for change-of-control affects the revenue the CDD provider is projecting and the add-back the QoE provider accepted. The only place these interactions are noticed is in the head of a vice president reading all the drafts in the final week.

## Why Nobody Has Built This
Each provider is paid for its own report and has no incentive to integrate with the others. VDR vendors move documents, not findings. And a findings ledger needs a schema that spans accounting, legal and commercial language, which nobody owns.

## What to Build
A shared findings ledger for each deal: every finding from every provider extracted into a common structure — what, which entity or contract, which financial line it touches, severity, status, and how it is being handled (price, structure, insurance, indemnity, post-close plan). LLM extraction from provider drafts populates it; links between findings are proposed by matching entities and affected line items. Each finding is tied to the model cell it changes. The IC memo's risk section is generated from the ledger, and the ledger survives close as the starting point for the hundred-day plan.

## Target Customer
Heads of diligence, deal partners and COOs at sponsors running ten or more processes a year past LOI.

## Impact If Built
The most expensive research effort in the deal cycle currently produces six disconnected reports. A shared ledger catches the cross-workstream interactions that cause post-close surprises and makes diligence output reusable after signing.
