# Lender Submission & Routing

**Parent Industry:** [[industries/mortgage-brokers|Mortgage Brokers]]
**Category:** Highly Automatable

## Profile
**Market Size:** $2-4B in annual embedded cost (pricing errors, re-submissions, rate lock losses)
**Share of Parent Industry:** Lender selection and submission is a core function affecting 100% of broker-originated volume
**Digital Adoption:** Low — lender selection is the most consequential decision a broker makes and it's done entirely from memory and spreadsheets, with no decision-support tooling
**Target Buyer:** Senior loan officer / brokerage owner
**Automation Potential:** High — lender rate sheets, overlays, and submission requirements are structured data that can be parsed, compared, and optimized algorithmically

## What Makes This a Distinct Niche
Lender submission routing is the single highest-value decision in mortgage brokerage — choosing which wholesale lender to submit a borrower's file to determines the rate, terms, approval probability, and close timeline. A broker with 30-50 lender relationships receives daily rate sheets from each, must cross-reference those rates against lender-specific overlays (credit score floors, LTV caps, property type restrictions, documentation requirements), and factor in soft knowledge (current turn times, underwriter tendencies, lender appetite for edge cases). This decision is currently made by experienced loan officers using intuition — it's the core tacit knowledge problem identified in the parent industry's high-impact analysis.

## Current Tools & Gaps
Optimal Blue and Mortech provide rate comparison engines that aggregate wholesale rate sheets, but they compare pricing without accounting for approval probability, lender overlays, or turn times. The rate you see may not be the rate you get if the lender kicks the file for an overlay violation. LOS platforms route submissions to specific lenders but don't advise on which lender to choose. No tool combines rate comparison + overlay compliance + historical approval patterns into a single recommendation.

## Problems
- [[niches/mortgage-brokers/lender-submission-routing/build|🔨 Build: Approval-Weighted Lender Recommendation Engine]]
- [[niches/mortgage-brokers/lender-submission-routing/buy|🛒 Buy: Rate Comparison Engine Adapted for Overlay-Aware Routing]]
- [[niches/mortgage-brokers/lender-submission-routing/fix|🔧 Fix: Rate Sheet Parsing & Overlay Tracking Fragmentation]]
