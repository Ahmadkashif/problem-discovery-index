# Public Adjusters

## Profile
**Category:** Insurance
**Market Size:** ~$2B US public adjusting market — highly cyclical, surging after major catastrophic events (hurricanes, wildfires, hailstorms)
**Tech Maturity:** Very Low — the industry runs on Xactimate for damage estimation, generic CRM for client tracking, and spreadsheets for everything else. No purpose-built public adjuster workflow platform exists at scale
**Workforce:** Licensed public adjusters (independent advocates who represent policyholders against insurance carriers), field inspectors, estimators, office managers, and marketing/intake staff

## Key Pain Themes
Public adjusters work on contingency fees (typically 10-20% of the claim settlement), meaning cash flow is entirely dependent on settlement speed and amount — a $100,000 claim that takes 9 months to settle generates $15,000 in revenue, but the adjuster has funded 9 months of inspection, documentation, and negotiation costs out of pocket. Damage documentation thoroughness determines claim value: the adjuster who documents hidden water damage behind walls, secondary smoke damage in HVAC systems, and code-upgrade requirements recovers 40-60% more than one who only photographs visible surface damage. This pattern recognition — seeing visible damage and knowing what hidden damage it implies — is the industry's most valuable tacit knowledge. Carrier negotiation is adversarial: insurance company adjusters are trained to minimize payouts, and public adjusters must build irrefutable documentation packages that justify every line item. Catastrophic events create feast-or-famine workload swings — a hurricane generates 6-12 months of overwhelming demand followed by a year of drought.

## Current Tech Landscape
Xactimate (by Verisk) is the universal language of property damage estimation — both carrier adjusters and public adjusters use it, and estimates that deviate from Xactimate's pricing database face automatic rejection. Symbility (CoreLogic) is an alternative estimation platform used by some carriers. ClaimWizard provides basic public adjuster CRM and workflow. Matterport and similar 3D scanning tools are used by some adjusters for documentation. No platform addresses the core challenge: ensuring documentation thoroughness, predicting hidden damage from visible indicators, or optimizing carrier negotiation strategy.

## Problems
- [[problems/public-adjusters/high-impact|🔴 High Impact: Damage Documentation Thoroughness and Claim Maximization]]
- [[problems/public-adjusters/low-impact-1|🟡 Low Impact: Policy Coverage Analysis for Complex Commercial Claims]]
- [[problems/public-adjusters/low-impact-2|🟡 Low Impact: Client Intake and Case Pipeline Management]]
- [[problems/public-adjusters/worker-life-1|🟢 Worker Life: Adjuster Disaster Deployment Burnout]]
- [[problems/public-adjusters/worker-life-2|🟢 Worker Life: Cash Flow Stress from Contingency-Fee Model]]
- [[problems/public-adjusters/ml-opportunity|🔵 ML Opportunities]]
- [[problems/public-adjusters/ai-agents-platforms|🤖 AI Agents & Platforms]]
