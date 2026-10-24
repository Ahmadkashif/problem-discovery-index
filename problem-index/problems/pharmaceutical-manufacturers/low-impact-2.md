# The API Second Source and the Filing It Triggers

**Industry:** [[pharmaceutical-manufacturers|Pharmaceutical Manufacturers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Adding or switching an API supplier is routine supply-chain work, but deciding what filing each market requires, and what data the change needs, is done by hand by regulatory CMC staff for every product and every supplier.
**Tags:** #large-language-models #transformers #decision-trees #feature-engineering #data-integration #compliance #automation

## The Problem
Generic and CDMO-made products depend on API suppliers concentrated in India and China, whose shares of API manufacturing locations for US-based application products rose to 21.2% and 14.7% between 2020 and 2025 (FDA). When a supplier gets an OAI inspection or an import alert, raises prices, or lands on a policy list (the Section 232 proclamation of April 2026 left generics out "at this time" but ordered a review within a year, and the BIOSECURE Act's first OMB list is due by December 2026), the manufacturer wants a second source quickly. The supply decision takes a week. The regulatory consequence takes months: in the US the change is filed as a supplement whose category (annual report, CBE-30 or prior approval) depends on the route, site and data. The same change is a different variation type in Europe and a different notification in Canada, and each needs comparability data on impurities, including nitrosamine risk, stability batches and the new supplier's Drug Master File status.

## What Already Exists
Regulatory information management systems (Veeva Vault RIM, IQVIA RIM Smart, ArisGlobal) track registrations, submissions and commitments by product and market. QMS supplier modules hold supplier qualification and audit status. Public FDA data cover DMF lists, inspection classifications, import alerts and warning letters, and commercial databases (Clarivate's Cortellis Generics Intelligence, PharmaCompass) list API holders by molecule.

## The Customisation Gap
None of these tools answers the question regulatory CMC is actually asked: if we qualify supplier B for product X, what must we file in each market, with what data, and how long until we can ship? That requires mapping the change against FDA's post-approval change guidance and each authority's variation rules, reading the product's approved CMC section to see what is registered (route, specifications, the supplier's DMF reference), checking the new supplier's DMF and inspection history, and assembling the comparability package. Today a regulatory specialist does this from experience, product by product, in a spreadsheet. A portfolio of hundreds of ANDAs makes it a recurring bottleneck exactly when a sourcing shock hits many products at once.

## Impact If Solved
A change-impact assessment generated from the registered dossier and supplier data in hours instead of two to four weeks (estimate) would let a manufacturer move to a second source on many products in parallel, cut one to three months from the time a product is on backorder after a supplier failure (estimate), and give supply and regulatory teams one shared answer on when the new source can ship.
