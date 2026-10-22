# Tax and 911 Fees on the Phone Nobody Paid Full Price For

**Industry:** [[wireless-retail-agents|Wireless Retail Agents]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Sales-tax engines already sit inside every point-of-sale system, but none of them knows that a $25 phone sold with an activation is taxed in California on its $110 unbundled price, or that each state charges its own prepaid 911 fee per transaction.
**Tags:** #large-language-models #decision-trees #evaluation-metrics #compliance #data-integration #automation #quick-win

## The Problem
Wireless dealers sell phones at prices no other retailer uses. A flagship goes out for a dollar down with promotional credits over 36 months, a prepaid phone is discounted because the customer activated with it, and a trade-in credit lands on the carrier bill, not the receipt. Several states don't tax the price the customer paid. California's Regulation 1585 taxes a phone sold with a service contract on its unbundled sales price: CDTFA's own example taxes a $25 phone sold with a one-year activation on the $110 price charged without one. The Court of Appeal upheld the rule in Bekkerman v. CDTFA (2024). If the dealer can't show its own unbundled price from its records, the tax defaults to the device's fair retail price.

Prepaid adds a second layer. States require the seller to collect a prepaid wireless 911 charge on each retail transaction and remit it on their own schedule: $0.55 flat in Virginia, $1.95 in Pennsylvania, a percentage of the sale in Kansas, 2% of gross receipts in South Dakota, quarterly in Delaware, whose rate rises on October 1, 2026, with small-sale and Lifeline exemptions in some states and vendor allowances of 1.5–5% for filing on time. A multi-state prepaid dealer collects and files a different fee in every state it trades in.

## What Already Exists
Tax engines such as Avalara and Vertex, the tax tables inside iQmetrix RQ and other POS systems, and state revenue portals. They calculate sales tax on the transaction price and handle standard exemptions well.

## The Customisation Gap
The dealer-specific logic is: an unbundled-price record for every device and promotion, kept from the dealer's own non-activation sales so the California measure can be defended in an audit; rules that know when a sale counts as bundled (activation term longer than a month) and when a trade-in or carrier bill credit reduces the taxable amount; prepaid 911 rates, thresholds and exemptions by state and effective date, with filing calendars and vendor allowances; and an audit file linking each receipt to the rule applied. The rule changes come as statutes, regulations and agency notices, so maintenance means reading text, not just updating a rate table.

## Impact If Solved
Removing audit exposure on discounted-phone tax, which builds up on every activation in a multi-year audit period, and turning a monthly multi-state fee filing into a review. For a 20-store prepaid dealer that is several hours a month and a few hundred dollars of vendor allowances not forfeited (estimate).
