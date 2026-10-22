# The Senior Officer's Red-Lines as a Training Record

**Niche:** [[niches/community-banks/the-commercial-credit-analyst/profile|The Commercial Credit Analyst]]
**Industry:** [[industries/community-banks|Community Banks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every credit memo an analyst writes is corrected by a senior credit officer, and those corrections, the bank's most concentrated teaching of credit judgement, are deleted when the final version is saved.
**Tags:** #tacit-knowledge-ml #large-language-models #transformers #evaluation-metrics #worker-facing #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to get an analyst from a borrower's raw returns to a credit memo the chief credit officer trusts in hours rather than days, and whoever makes every number traceable to its source and every senior edit reusable takes the account.

## The Problem
A junior analyst drafts a memo: the spread, the global cash flow, a strengths-and-weaknesses section, a recommended grade. The chief credit officer marks it up: this add-back is not recurring, the guarantor's other entity is losing money, the collateral is special-use and the appraisal ignores it, this grade is a notch too generous. The analyst fixes it and learns one lesson. The next analyst makes the same mistake, because the red-lines live in a Word document's tracked changes that are accepted and discarded.

## Why Nobody Has Built This
Memo tools store finished memos, not the edit history. The edits are small and scattered, and their value is only visible when collected across hundreds of memos. Nobody sells "credit training data" to a community bank.

## What to Build
Capture every draft and every senior edit in the memo workflow. Classify edits by type (add-back challenged, guarantor exposure missed, collateral valuation questioned, grade changed and why). Surface the patterns: which mistakes each analyst repeats, which borrower situations draw the most corrections. Use them to prompt the next analyst while drafting ("memos on special-use collateral are usually challenged on the appraisal") and as a dataset of the senior officer's reasoning that survives their retirement.

## Target Customer
Chief credit officers at community banks with two or more analysts and a retiring senior credit generation.

## Impact If Built
Analysts reach independence faster, senior review time falls as repeat mistakes disappear, and the bank keeps a written record of how its best credit people think.
