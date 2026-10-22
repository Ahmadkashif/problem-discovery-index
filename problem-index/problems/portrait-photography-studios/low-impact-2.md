# Sales Tax on Prints, Files and Packages

**Industry:** [[portrait-photography-studios|Portrait Photography Studios]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Sales-tax engines are a solved problem in general, but none of them knows that one print can make a photographer's whole package taxable, or that a sitting fee changes status depending on what the client buys later.
**Tags:** #decision-trees #large-language-models #feature-engineering #evaluation-metrics #compliance #automation #quick-win

## The Problem
A portrait photographer sells a mix that tax law treats very differently: a session or sitting fee, digital files delivered by download, proofs, prints, albums, framed wall art, and packages that combine them. Whether any of it is taxable depends on the state and, often, on the whole transaction rather than the line item. California's tax agency gives the canonical example: $1,000 of digitally uploaded images plus $100 of prints makes the entire $1,100 taxable, because the customer received tangible prints, and splitting the charges across two invoices does not change it. A sitting fee there is not taxable if the client buys no prints, and becomes taxable if they do. New York exempts photographs delivered only electronically but taxes the whole receipt once prints are included. Pennsylvania and Washington tax digital photographs. Minnesota exempts electronic delivery only if the invoice shows it clearly.

Most photographers price a package once, collect a retainer months ahead, add print orders weeks after delivery through a gallery store, and calculate tax at each step as if the items were independent. Volume studios add another layer: school commissions are often defined as a percentage of gross after tax, as in Albuquerque's contract terms, so the tax calculation feeds directly into what the school is owed.

## What Already Exists
General sales-tax engines such as Avalara and Stripe Tax calculate rates by address and product code; accounting packages such as QuickBooks apply them; gallery platforms (Pixieset, ShootProof, Pic-Time) and CRMs (HoneyBook, Dubsado) let the photographer set a tax rate per product or per order.

## The Customisation Gap
The generic engines classify items one at a time; photography taxability is a property of the whole client relationship across months. The gap is a photography-specific rules layer: state rules on whether tangible delivery taints the session and digital fees; how a retainer collected in March should be treated when prints are bought in October; product codes for prints, albums, files and proofs mapped per state; invoice wording that preserves an electronic-delivery exemption; and, for volume studios, a commission calculation that follows each district's contract definition. It belongs inside the gallery and CRM where packages are sold, not in a separate tax tool the photographer never opens.

## Impact If Solved
A solo photographer who now guesses, or pays a bookkeeper to reconstruct a year of orders, would charge the right tax at the moment of sale and keep an audit trail; a volume studio would calculate school commissions correctly the first time instead of reconciling them by hand at season's end.
