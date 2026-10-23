# Project SPAs Claimed Line by Line Through Ship-and-Debit

**Industry:** [[electrical-distributors|Electrical Distributors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Rebate platforms and EDI translators already move claims; neither knows that an electrical SPA belongs to one contractor on one job, and that the 849 rejection codes are where the money leaks.
**Tags:** #large-language-models #k-nearest-neighbors #logistic-regression #feature-engineering #compliance #revenue-impact #automation

## The Problem
In electrical distribution, the special pricing agreement is how projects are won. When a quote needs a lower price on gear, lighting or devices, the distributor asks the manufacturer, usually through its rep agency, for a job-specific price below the distributor's normal cost. The manufacturer issues an SPA number tied to a named contractor and job, a product list in the manufacturer's numbering, quantities and an expiry. The distributor buys at normal cost, sells at the SPA price, and claims the difference back through ship-and-debit: an EDI 844 claim per invoice line, answered by the manufacturer's 849 accepting, adjusting or rejecting each line with a reason code. For a mid-size distributor, a large share of project sales can run on SPAs (~20–40%, estimate), across dozens of manufacturers.

Each step leaks. The SPA number is keyed into the ERP by hand, sometimes under the wrong contractor or ship-to. The contractor buys the SPA-priced breakers for a different job. The quantity cap is consumed across branches without anyone noticing. A line ships after the expiry because the job slipped. The 849 comes back with rejection codes — wrong agreement number, expired contract, quantity exceeded, part not on agreement — and someone in accounting works them in a spreadsheet, if they work them at all. An older Electrical Wholesaling account counted 23 "touches" between distributor and manufacturer to settle SPA rebates (search summary), and every manufacturer runs the process differently.

## What Already Exists
Rebate and incentive platforms such as Enable and Vistex model programmes and accruals; EDI translators and value-added networks move 844 and 849 documents; Epicor Eclipse and other distributor ERPs hold contract-pricing tables; manufacturers run claim portals. The industrial side of the same contest is mapped under [[industrial-distributors|Industrial Distributors]], whose rebate niche leaves electrical SPAs to this industry.

## The Customisation Gap
Electrical SPAs need logic the generic tools don't carry: job and contractor matching on every invoice line (an SPA is not a customer price, it is a job price), quantity caps shared across branches and releases, expiry extensions requested before a slipped job ships, manufacturer-to-distributor part-number aliasing through IDEA data, and a reading of each manufacturer's 849 reason codes that turns rejections into corrective actions — rekey the agreement, request an extension, split the line, or write it off with a reason. The front end matters too: the SPA request at quote time should create the agreement record the claim will need, rather than leaving it to be keyed from a PDF weeks later.

## Impact If Solved
If ~3–10% of eligible SPA dollars go unclaimed or are written off after rejection (estimate), recovering most of them drops straight to net profit on the distributor's thinnest-margin business, and the controller sees leakage by manufacturer, branch and cause instead of a low-margin line on the P&L.
