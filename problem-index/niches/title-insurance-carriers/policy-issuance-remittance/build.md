# Continuous CPL-to-Policy Reconciliation

**Niche:** [[niches/title-insurance-carriers/policy-issuance-remittance/profile|Policy Issuance, CPLs & Premium Remittance]]
**Industry:** [[industries/title-insurance-carriers|Title Insurance Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Underwriters find unreported policies by periodic chase, when every CPL issued is a promise that a policy and a remittance should follow within weeks.
**Tags:** #large-language-models #seq2seq #decision-trees #survival-analysis #evaluation-metrics #automation #data-integration
**Contested on:** Every serious competitor in this niche is fighting to make every policy and closing protection letter an agent issues arrive reported, correctly rated and remitted without rekeying, and whoever closes the gap between CPLs issued and policies remitted fastest takes the account.

## The Problem
A CPL is issued before closing. If the deal closes, a policy should be reported and premium remitted within the agent's reporting cycle. When the policy is never reported, through error or intent, the underwriter learns of it at audit or when a claim arrives on a policy it never booked.

## Why Nobody Has Built This
CPL systems, policy registers and remittance ledgers were built separately. Smaller agents report in free-form files, and matching depends on addresses and names that vary between documents.

## What to Build
Extract every remittance report into structured policy lines. Link each policy to its CPL and commitment by parcel, parties and dates. Model the expected time from CPL to reported policy by agent and transaction type, and flag CPLs past their expected window, ranked by liability. Recalculate premium with a rules engine per state manual and classify each discrepancy by cause.

## Target Customer
Agency operations and finance at underwriters with large independent-agent networks.

## Impact If Built
Unreported policies caught within weeks, premium leakage recovered, and the agency risk team given a clean behavioural signal per agent.
