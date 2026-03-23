# Real-Time Teller Cross-Sell Recommendations

**Niche:** [[niches/credit-unions/member-onboarding-automation/profile|Member Onboarding & Cross-Sell Automation]]
**Industry:** [[industries/credit-unions|Credit Unions]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Retail banking cross-sell platforms exist but are designed for large bank branch networks — CU tellers need product recommendations that fit a 90-second transaction window and reflect credit union product sets, not bank product catalogs.
**Tags:** #gradient-boosting #recommendation #tabular-ml #worker-facing #revenue-impact

## The Problem
CU tellers process 30-50 transactions per shift. Management pressures them to identify cross-sell opportunities during each interaction, but tellers have no data-driven guidance on what to recommend. They either suggest nothing (most common), suggest the same product to everyone ("are you interested in a credit card?"), or attempt awkward referrals based on training scripts rather than member context. Current cross-sell conversion rates are 1-3% — reflecting the mismatch between untargeted suggestions and member needs. Meanwhile, member transaction patterns contain strong signals about product readiness: a member making a large external mortgage payment is a refinance candidate; a member with growing savings balance is a certificate or investment candidate.

## What Already Exists
Retail banking cross-sell platforms (NCR Terafina, Engageware) provide product recommendation engines for bank branch staff. CU-specific tools like CU*Answers Member Reach and Trellance analytics provide member segmentation reports. Generic CRM platforms offer next-best-action recommendations. None of these deliver real-time, member-specific product recommendations within the teller workstation interface during a live transaction — the format required for a 90-second interaction window.

## The Customization Gap
CU tellers need a single product recommendation displayed prominently on their workstation screen when a member's transaction is processed — not a dashboard of analytics they must interpret. The recommendation must be: (1) specific ("Member is a strong candidate for auto loan refi — current external auto payment is $475/month, CU rate saves $80/month"); (2) contextual (based on the member's current product holdings and recent transaction patterns, not generic segments); (3) actionable in 15 seconds ("Would you like me to check what rate we could offer on your auto loan?"); and (4) CU-product-specific (credit union product names, rates, and eligibility criteria — not bank product catalogs). Integration must be with the teller workstation (Symitar teller module, KeyStone front-end) — not a separate browser tab.

## Target Customer
VP of Marketing and branch managers at CUs with 3+ branches and teller staff who are tasked with cross-selling but lack real-time, member-specific product recommendations during transactions.

## Impact If Solved
Increases teller cross-sell conversion from 1-3% to 5-10% by replacing generic suggestions with data-driven, member-specific recommendations. Generates $50-$150 in annual revenue per active branch member through incremental product adoption. Reduces teller stress by giving them confidence in what to recommend — replacing awkward scripted pitches with relevant, helpful suggestions.
