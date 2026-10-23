# All-In Price and Resale Rules by Jurisdiction

**Industry:** [[ticketing-agencies|Ticketing & Reservation Agencies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every ticket seller now has to show an all-in price, and in a growing number of states cap the resale price, block speculative listings and honour transfer rights, and each one keeps the rule table in a spreadsheet maintained by a lawyer.
**Tags:** #large-language-models #transformers #bert #evaluation-metrics #compliance #automation #data-integration

## The Problem
The FTC's Rule on Unfair or Deceptive Fees has applied to live-event tickets since May 12, 2025. Any business that shows a ticket price, whether the primary platform, a resale marketplace, a broker's own site or an affiliate, must show the total price including mandatory fees, disclose excluded charges before payment, and never misrepresent a fee. On top of the federal floor, states keep legislating. Vermont's Act 109 caps resale at 110% of the original price and bans speculative tickets from July 1, 2026. Maine passed a similar cap, North Carolina's budget added resale rules from October 1, and D.C. and California have bills pending. Older laws still apply: New York's resale and transferability provisions and the anti-bot and deceptive-URL statutes in many states.

The rule that applies depends on the venue's state, sometimes the buyer's state, the type of ticket and the original face price, which the reseller often cannot see. A broker listing a Burlington show on four marketplaces has to know the face value of each seat to stay under 110%. A marketplace has to suppress speculative listings in some states and allow them in others, and show a fee breakdown that varies by jurisdiction.

## What Already Exists
Tax engines such as Avalara and Vertex compute amusement and sales taxes by jurisdiction. Marketplaces maintain their own listing-policy rules, and law firms publish state-by-state surveys of ticket laws. General regulatory-change monitoring tools track bills.

## The Customisation Gap
None of these turns a statute into a listing-level control. The ticketing-specific logic is: a jurisdiction table keyed by venue location and event date, with effective and sunset dates (Vermont's subchapter is repealed on July 1, 2028); face-value capture or inference per seat so caps can be enforced on resale; detection of speculative listings, meaning seats the seller does not yet hold; fee display templates that satisfy both the FTC rule and state disclosure rules; and an audit trail that shows a state attorney general what was displayed to a buyer on a given day. Each marketplace and large broker rebuilds this by hand every time a legislature sits.

## Impact If Solved
A shared, maintained rule engine would let a mid-sized broker or marketplace list in every state without a lawyer reviewing each new statute. Today each new law costs a marketplace roughly 20-40 hours of counsel and engineering time to read, map and implement (estimate), and a session that adds several states multiplies that. Violations of an FTC trade regulation rule carry civil penalties of up to $53,088 per violation at the FTC's 2025 inflation-adjusted level, and every non-compliant listing shown to a buyer can count. A rule table tested before each effective date turns that exposure into a configuration task.
