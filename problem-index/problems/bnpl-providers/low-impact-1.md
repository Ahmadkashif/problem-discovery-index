# Merchant Integration and Checkout Placement

**Industry:** [[bnpl-providers|BNPL Providers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Conversion depends on where and how the offer appears in a merchant's checkout, every merchant's checkout is different, and the integration is tuned by account managers reading dashboards.
**Tags:** #gradient-boosting #causal-inference #bert #large-language-models #evaluation-metrics #feature-engineering #data-integration #revenue-impact

## The Problem
A BNPL provider earns on volume, and volume depends on whether the consumer sees the offer at a moment when it changes their decision. That moment is not at checkout — it is on the product page, where the instalment price reframes a $200 item as $50. Placement on the product page, in the cart, in search results, and in the checkout itself each perform differently and each require merchant engineering work.

Every merchant's storefront is different. Shopify and BigCommerce apps cover the long tail with a standard widget. Larger merchants build custom, and the resulting implementation may render the messaging in the wrong place, in the wrong currency, on items that are not eligible, or not at all on mobile. Nobody notices until someone looks.

Eligibility complicates it. Not every item or basket qualifies — amount thresholds, category exclusions, shipping timelines — and a merchant whose widget advertises instalments on an ineligible basket produces a decline at checkout, which is worse than no offer.

Then there is the negotiation. Merchant discount rates are set commercially, and the provider's case is incremental revenue: consumers who would not have bought, or would have bought less. That claim is asserted from a dashboard comparing BNPL and non-BNPL orders, which is not a comparison of like with like and every sophisticated merchant knows it.

## What Already Exists
All major providers ship SDKs, platform apps and messaging components. Shopify, BigCommerce, Magento and Salesforce Commerce Cloud have supported integrations. Providers offer merchant dashboards with conversion and average-order-value reporting. A/B testing frameworks exist on the merchant side.

## The Customisation Gap
Nothing verifies the integration from the outside. Whether the messaging actually renders on the product page, in the right place, on mobile, on the categories it should and not on the ones it should not, is checkable by fetching the merchant's own pages and looking. Providers discover broken placements when volume drops.

Eligibility-aware messaging is inconsistently implemented. Showing an instalment price on a basket that will be declined is a conversion loss and a support ticket, and the check is available at render time.

Incrementality is asserted rather than measured. The honest version requires randomised exposure — withholding the offer from a small share of sessions — which merchants resist and which is the only thing that turns the provider's commercial claim into a fact. Providers with sufficient volume can run this and largely do not.

And placement optimisation is generic. The best placement differs by merchant category, basket size distribution and device mix, and the provider has thousands of merchants' worth of evidence about what works where. That evidence is used to write a best-practice guide.

## Impact If Solved
Placement is the provider's main conversion lever and its main commercial argument to merchants, and both are currently handled by assertion. Verifying integrations automatically, making messaging eligibility-aware, and measuring incrementality with real randomisation turns account management into engineering and gives the merchant negotiation a number that survives scrutiny.
