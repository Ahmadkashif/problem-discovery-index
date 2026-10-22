# Payment Policy Turned Into Claim Edits by Hand

**Industry:** [[health-insurance-carriers|Health Insurance Carriers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Commercial claim-editing engines ship national coding edits, but each plan's own reimbursement policies, contract terms and line-of-business rules are still read by analysts and turned into edit configuration by hand.
**Tags:** #large-language-models #transformers #feature-engineering #evaluation-metrics #automation #compliance #revenue-impact

## The Problem
Every health plan publishes reimbursement policies: when an assistant surgeon is paid, how modifiers 25 and 59 are treated, which services bundle into a global surgical package, how often a lab panel is payable. It also signs provider contracts whose terms vary by product and region. Medicare Advantage claims must follow traditional Medicare's national and local coverage determinations, and Medicaid MCOs must follow each state's fee schedule and policy manual. When a policy changes, a payment integrity or configuration analyst reads it, decides which claim fields and codes it touches, writes requirements, has the edit built in the claim editing engine or core platform, tests it on sample claims, and estimates its dollar effect. Then the provider notice goes out, typically 30 to 90 days ahead (estimate).

Translation errors are expensive in both directions. An edit that is too broad denies legitimate claims, triggers appeals and provider complaints, and can breach prompt-pay statutes. An edit that is too narrow pays claims the policy says should not be paid, and the money is recovered later, if at all, through a contingency-fee post-payment audit.

## What Already Exists
Commercial claim-editing engines and content libraries (Lyric, the former ClaimsXten; Optum; Cotiviti) apply national correct coding initiative edits, medically unlikely edits and their vendors' clinical edit logic. Core platforms such as HealthEdge and Facets hold configurable benefit and pricing rules. Outsourced payment integrity vendors propose new "concepts" from their cross-client experience.

## The Customisation Gap
The national content covers national rules. What each plan needs on top is a set of plan-specific steps. Reading its own policy prose and contract language and generating candidate edit logic in the engine's rule syntax. Mapping that logic to the plan's line-of-business distinctions (commercial versus MA versus each state's Medicaid). Simulating the edit against a year of the plan's paid claims to show which providers and dollars it would touch before it goes live. Checking it against existing edits for conflicts. And keeping a link from every configured edit back to the paragraph of policy that justifies it, which is what an appeal reviewer, a provider dispute or a state regulator will ask to see.

## Impact If Solved
Cutting policy-to-edit cycles from ~3–6 months to ~3–6 weeks (estimate) would let plans enforce their own policies from the effective date instead of recovering overpayments after the fact. Pre-launch simulation would catch the over-broad edits that generate denial waves and provider abrasion. And a policy-to-edit trace would make every denial defensible on appeal.
