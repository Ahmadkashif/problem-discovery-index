# SPA and Rebate Claims Matched by Spreadsheet

**Industry:** [[industrial-distributors|Industrial Distributors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Rebate software already tracks manufacturer programmes; what it doesn't do is match each industrial sale line to the special pricing agreement it was sold under, before the claim window closes.
**Tags:** #gradient-boosting #logistic-regression #large-language-models #feature-engineering #compliance #revenue-impact #automation #data-integration

## The Problem
A bearing, power transmission or fluid power manufacturer often lets a distributor sell to a named end customer below the normal price, then pays back the difference. That is a special pricing agreement (SPA): the distributor buys at its regular cost, sells at the agreed price, and claims the gap from the manufacturer line by line. On top sit volume rebates, growth incentives and buying-group programmes. Agreements arrive as PDFs and emails with their own part lists, quantities, end customers and expiry dates. Someone keys them into the ERP's contract tables, and someone else — often one person in accounting — exports the month's sales, matches lines to agreements in a spreadsheet and submits claims through each manufacturer's portal or template.

Money leaks at every step. A line sold at SPA price is never claimed because the agreement was keyed under a different part number. A claim is denied because the order was placed inside the agreement window but shipped after it, or because the end customer's ship-to address doesn't match the agreement's. The distributor sells below cost and recovers nothing. Enable's 2024 vendor survey found 52% of distributors believe they don't receive all the rebates they earn and only 43% know the amount each manufacturer owes them.

## What Already Exists
Rebate and incentive platforms such as Enable and Vistex manage programme terms and accruals, mostly from the manufacturer side, and newer tools (Band, Claro and others) target distributors directly. ERPs including Prophet 21, Infor CSD and Eclipse store contract pricing and can flag lines sold at a special price. Manufacturers run claim portals with their own file formats.

## The Customisation Gap
The generic tools assume a clean agreement and a clean sale. Industrial SPAs need four things they don't provide. First, extraction of agreement terms from manufacturer PDFs into structured records: part numbers in the manufacturer's format, end-customer identity, quantity caps, effective and expiry dates and claim deadlines. Second, part-number aliasing between the manufacturer's numbering, the distributor's SKU and interchangeable brands, because the line the rep sold may be an approved equivalent. Third, each manufacturer's denial rules — ship-date versus order-date, ship-to matching, minimum claim sizes, resubmission limits — encoded as checks before submission. Fourth, a model that learns from past denials which lines are at risk and what fixes them.

## Impact If Solved
A distributor that recovers even ~5–10% more of its earned claim dollars (estimate) adds margin directly to the bottom line in a business that nets low single digits on sales. It also removes the month-end crunch from the one accountant who knows every manufacturer's portal, and gives the branch a list of lines sold below cost that will never be recovered.
