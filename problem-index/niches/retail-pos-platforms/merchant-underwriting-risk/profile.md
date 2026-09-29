# Merchant Underwriting & Risk

**Parent Industry:** [[industries/retail-pos-platforms|Retail POS Platforms]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in merchant onboarding is fighting to approve a merchant in minutes at the same loss rate a week of manual review would produce — and whoever holds that trade-off best takes the volume.

## Profile
**Market Size:** ~$1.9B US attributable to merchant underwriting, onboarding and risk within payments
**Share of Parent Industry:** ~19% of retail POS revenue
**Digital Adoption:** High — onboarding is instant for most merchants and the decisioning behind it is uneven
**Target Buyer:** Heads of underwriting and risk at POS platforms, acquirers and ISOs
**Automation Potential:** Very High — this is an adversarial classification problem with severe cost asymmetry and abundant outcome data

## What Makes This a Distinct Niche
Instant onboarding reset the competitive terms of payments. A merchant who once waited days for an underwriting decision now expects to accept a card the same afternoon, and any platform that cannot deliver that loses the account before the conversation starts. The entire contest is therefore a trade-off curve: approve faster and approve more, at what loss rate. Underwriting is adversarial — transaction laundering, merchants fronting for prohibited categories, synthetic businesses and merchants who are simply going to fail all try to look ordinary — and the cost of an error is asymmetric in both directions, because a false decline costs a customer the platform spent to acquire and a false approval costs money the platform pays out. The outcome data is unusually good: every approved merchant's subsequent behaviour is observed in full, which makes this one of the better-posed risk problems in the vault.

## Current Tools & Gaps
KYC and KYB verification, business registry checks, sanctions and adverse media screening, device and identity intelligence and consortium negative files are all available as commodity services and are widely deployed. Risk scoring at onboarding is standard. The gaps are in what happens with outcomes: declined merchants have no observed outcome, so the model learns only from those approved, and almost nobody runs the bounded approval of marginal applicants that would correct it; the merchant's own early behaviour — the first two weeks of transactions — is the strongest available signal and is generally used only for fraud alerting rather than fed back into the approval model; and website and business-presence evidence, which is where most category misrepresentation is visible, is checked manually when checked at all.

## Problems
- [[niches/retail-pos-platforms/merchant-underwriting-risk/build|🔨 Build: Underwriting That Learns From Its Own Declines]]
- [[niches/retail-pos-platforms/merchant-underwriting-risk/buy|🛒 Buy: Business Verification and Web Evidence Off the Shelf]]
- [[niches/retail-pos-platforms/merchant-underwriting-risk/fix|🔧 Fix: The First Two Weeks Nobody Feeds Back]]
