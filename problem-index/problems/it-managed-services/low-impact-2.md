# PSA/RMM Data Reconciliation for Accurate Billing

**Industry:** [[it-managed-services|IT Managed Services]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Device counts in ConnectWise never match device counts in Datto, and the gap is pure revenue leakage on per-device contracts.
**Tags:** #bert #transformers #word-embeddings #transfer-learning #attention-mechanisms #feature-engineering #evaluation-metrics #data-integration #automation

## The Problem
MSPs bill clients on per-device, per-user, or per-seat models, but the source-of-truth for device and user counts is split across PSA (ConnectWise Manage, Autotask) and RMM (Datto, ConnectWise Automate, NinjaRMM) platforms. These systems drift: a new workstation deployed by the client's internal IT shows up in RMM but not in the PSA agreement; a decommissioned server stays in the PSA billing configuration for months. The typical MSP under-bills by 5-12% due to unreconciled asset counts, representing $50-150K in annual revenue leakage for a 2,000-endpoint shop.

## What Already Exists
Gradient MSP and CloudRadial offer billing reconciliation features, and ConnectWise has built-in agreement reconciliation workflows. These tools compare device counts between systems but struggle with entity matching: the same device appears as "ACME-PC-042" in RMM and "John Smith Workstation" in PSA, or a single user has three different name formats across Microsoft 365, Active Directory, and the PSA contact record. Manual reconciliation typically requires a dedicated billing coordinator spending 10-15 hours per month.

## The Customisation Gap
The reconciliation engine needs NLP-based entity resolution that matches devices and users across systems despite inconsistent naming conventions, partial records, and stale data. It must understand MSP-specific billing logic: which agreement covers which devices, how bundled services map to individual assets, and when a "new device" is actually a reimaged existing device that shouldn't trigger a new billing line. The tool must also flag discrepancies by dollar impact rather than just count mismatch, so the billing coordinator focuses on the $500/month under-billed server agreement before the $15/month missing workstation.

## Impact If Solved
Recovering the typical 5-12% billing leakage adds $50-150K annually for a mid-size MSP, while reducing billing reconciliation time from 10-15 hours to 1-2 hours per month. Clean billing also reduces client disputes during invoice reviews, which are a leading source of friction in MSP-client relationships.
