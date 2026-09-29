# Merchant Onboarding and Underwriting

**Industry:** [[payment-processors|Payment Processors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every acquirer independently rebuilds business verification and risk underwriting against the same public registries, and grades it against fraud losses it never attributes back to the decision.
**Tags:** #gradient-boosting #bert #large-language-models #graph-neural-networks #evaluation-metrics #feature-engineering #compliance #data-integration

## The Problem
Before a merchant can process, the acquirer must verify that the business exists, identify who controls it, screen against sanctions and adverse media, assess the risk of the business model, and set exposure limits and reserve requirements. The regulatory floor is the card network rules plus the acquirer's own BSA obligations; everything above the floor is judgement.

The inputs are public and messy. Secretary of state registrations with inconsistent naming, EIN verification, beneficial ownership that is self-attested, a website that may or may not describe what is actually being sold, processing history at a prior acquirer that the merchant supplies selectively. The risk questions are qualitative: is this a drop-shipper, is the fulfilment timeline long enough to create chargeback exposure, is the product in a prohibited or high-brand-risk category, is this business a rebrand of one terminated last year.

Platform acquirers have compressed this to minutes for the easy cases and still route a meaningful share to manual review, where an underwriter reads a website and makes a call.

The outcome — whether this merchant generated fraud losses, excessive chargebacks, or a network fine — arrives six to eighteen months later and is recorded in a loss ledger that is not joined back to the underwriting decision.

## What Already Exists
Middesk, Persona, Alloy, Socure and Ekata cover business and beneficial-owner verification. Sanctions and adverse media screening is a mature vendor category. The card networks operate terminated merchant registries. Chargeback monitoring programmes define the thresholds. Most acquirers have internal risk scorecards and written underwriting policies.

## The Customisation Gap
The website is the richest signal and the least used. What a merchant actually sells, its fulfilment and refund terms, its pricing model, whether it is a subscription with a hard cancellation path, whether the storefront is a template used by a hundred other merchants — all of this is readable from the site and is currently read by a human when it is read at all. Classifying merchant category and risk model from site content is a well-shaped task on a corpus every acquirer holds.

Entity resolution across terminations is the second gap. A merchant terminated for excessive chargebacks reappears with a new legal entity, a new EIN, a different beneficial owner on paper, and the same website template, payment descriptor patterns, hosting fingerprint and bank account behaviour. Linking these is a graph problem and is largely handled by exact matching on fields that are trivially changed.

And nothing grades the underwriting. Approval decisions and their eventual loss outcomes are both recorded and are not joined, so acquirers tune their risk appetite by reacting to the last large loss rather than by measuring the tradeoff. It is the same missing join as the authorisation problem, in a different department.

## Impact If Solved
Onboarding friction is a direct competitive lever — merchants choose the acquirer that approves them the same day — and the cost of being wrong is concentrated in a small number of expensive failures. Reading the website, resolving entities across rebrands, and grading past decisions against realised losses lets an acquirer approve faster and decline more accurately at the same time, which is currently treated as a tradeoff because nobody measures it.
