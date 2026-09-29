# Paying More Than Everybody Else

**Niche:** [[niches/ap-automation-vendors/cross-buyer-supplier-intelligence/profile|Cross-Buyer Supplier Intelligence]]
**Industry:** [[industries/ap-automation-vendors|AP Automation Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The buyer has no way of knowing whether their price for a routine item is normal, and the platform processing the invoice does.
**Tags:** #descriptive-statistics #quick-win #evaluation-metrics #automation #confidence-intervals #revenue-impact #compliance #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to turn the sight of one supplier invoicing hundreds of buyers into an assessment of that supplier nobody else can produce — and whoever builds it holds the most complete record of business-to-business commerce outside a bank.

## The Problem
A company has been buying the same service from the same supplier for six years at a price that has crept upward. Whether that price is competitive is unknowable to them without a sourcing exercise nobody has time for. The platform processes invoices for that supplier from two hundred other buyers and can see the distribution. It renders the invoice and says nothing.

## Why It's Still Broken
The product is scoped to the buyer's own tenant, so every view stops at their data — the tenancy boundary became the analytical boundary by default rather than by decision. Price comparison needs item normalisation nobody has done. Governance for cross-tenant comparison was never written. And nobody asked whether buyers would want it, which they obviously would.

## What a Fix Looks Like
Show the position, not the price. Start with categories where comparison is straightforward — standard services, common goods, recurring subscriptions — which is the fix and avoids the hard normalisation problem entirely. Show the buyer's position in a distribution rather than any other buyer's price, since that is both useful and safe. Set aggregation thresholds so no counterparty is identifiable, which is the governance minimum. Flag only material outliers, because a marginal difference is noise and a large one is a finding. Include payment terms as well as price, as terms are frequently where the real difference sits and are never compared. Alert on price increases that are out of line with the supplier's other buyers, which is the most actionable form and is entirely mechanical. Write the consent and use basis explicitly before shipping anything. Give procurement the list of biggest opportunities, since they are the audience and currently have nothing. Track whether flagged items were renegotiated and what was saved, which is the proof. And expand normalisation gradually as the value is demonstrated, rather than waiting for a complete taxonomy.

## Who Feels the Pain
Buyers overpaying with no way to know; procurement teams without benchmark data; suppliers whose pricing inconsistency is invisible; and platforms sitting on the answer.

## Impact If Fixed
The tenancy boundary became the analytical boundary by default rather than by decision. Showing a buyer their position in a distribution for straightforward categories is safe, mechanical, and something no competitor without the network can offer.
