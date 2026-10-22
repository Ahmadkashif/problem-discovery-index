# Adverse Action & Regulatory Notices

**Parent Industry:** [[industries/credit-card-issuers|Credit Card Issuers]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to turn each model-driven decline, line decrease or rate increase into a notice whose stated reasons are the model's actual reasons and which goes out inside the Reg B and Reg Z clocks, and whoever makes reasons both faithful to the model and defensible to an examiner takes the account.

## Profile
**Market Size:** ~$1.5B a year in issuer spend on notice generation, reason-code mapping, explainability tooling, print and mail and the compliance testing around them (estimate)
**Share of Parent Industry:** ~2% of issuer spend on data, decisioning and operations (estimate)
**Digital Adoption:** Medium — generation is automated; the mapping from model to reasons is manual
**Target Buyer:** Head of Consumer Compliance / Model Risk Officer
**Automation Potential:** Very high for generation and testing

## What Makes This a Distinct Niche
Every declined application and every line decrease is an adverse action under ECOA and Reg B, which requires a notice with specific principal reasons, generally within 30 days; rate increases need 45 days' advance notice under the CARD Act, and increases must be re-reviewed every six months. With 89 million new accounts originated in 2024 (CFPB) and far more applications declined, these are millions of notices a year. The CFPB's position — recalled from its 2022 and 2023 circulars — is that reasons must be accurate even when the decision comes from a complex model, so a checklist reason that does not reflect the model's real drivers is a violation. That turns notice generation from mail-merge into an explainability problem.

## Current Tools & Gaps
Score-vendor reason codes, explainability libraries, decision-engine reason mappings, customer communications platforms for generation. Gaps: reasons mapped once at model launch and never re-tested; rate re-evaluations run as spreadsheet batches; and no single record of every notice and its clock.

## Problems
- [[niches/credit-card-issuers/adverse-action-and-consumer-notices/build|🔨 Build: Reason Codes Tested for Fidelity to the Model]]
- [[niches/credit-card-issuers/adverse-action-and-consumer-notices/buy|🛒 Buy: Communications Platforms Fitted to Credit Notice Rules]]
- [[niches/credit-card-issuers/adverse-action-and-consumer-notices/fix|🔧 Fix: The Six-Month Rate Review Run From a Spreadsheet]]
