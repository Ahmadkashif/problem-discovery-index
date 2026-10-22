# Sales Tax, Resale Certificates and Designer Accounting

**Industry:** [[interior-design-firms|Interior Design Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** A design firm is a reseller, a service business and a deposit-holder at once, and the general accounting and sales tax tools it runs on understand only one of those at a time.
**Tags:** #large-language-models #decision-trees #feature-engineering #compliance #automation #data-integration #quick-win

## The Problem
A residential design firm that buys a $9,000 sofa at trade price and sells it to the client with a markup is, for tax purposes, a retailer. It must give the vendor a resale certificate so the vendor does not charge sales tax, collect sales tax from the client instead, and remit it to the state where the sofa is delivered. Whether the design fee is taxable depends on the state and, in several, on whether the fee is bundled with the sale of goods. Freight, crating, receiving, storage and installation charges are taxed differently again. A client with a second home in another state turns one project into two tax jurisdictions, and since the 2018 Wayfair decision a growing firm can cross economic-nexus thresholds in states where it has no office.

At the same time the firm holds money that is not yet revenue. Clients pay deposits, often ~50–100% of product cost (estimate), before orders are placed; the firm pays vendor deposits; the balance moves when items ship, arrive, or are installed. A project that runs eighteen months can have hundreds of open deposits on both sides. Small firms track this in spreadsheets beside QuickBooks, and the reconciliation at project close regularly finds tax under-collected on one invoice, a vendor deposit never applied, or a markup applied to a freight line the client contests.

## What Already Exists
QuickBooks Online and Xero handle general ledgers; Avalara and TaxJar compute sales tax for retailers by ship-to address; Studio Designer, DesignManager and Houzz Pro include proposal-to-invoice modules with tax fields; vendor credit applications and resale certificates are managed by email and in folders. Bookkeepers who specialise in design firms fill the gap by hand.

## The Customisation Gap
The design-firm layer the generic tools lack is specific: line-level taxability rules for design fees, product, freight, receiving and installation by delivery state, including bundled-fee treatment; a resale-certificate register per vendor and per state that flags when a vendor invoice shows tax it should not, or when a certificate is about to lapse; deposit accounting that treats client deposits as liabilities and vendor deposits as prepaid assets, matched by purchase order line rather than by invoice; economic-nexus monitoring by state from the firm's own delivery addresses; and a markup policy engine that applies the firm's rules consistently (product but not freight, cost-plus versus discount-from-retail) so the client invoice matches the proposal. Most of this is configuration on top of existing tax engines and ledgers, which is why it is a customisation problem rather than a new product.

## Impact If Solved
A firm running ten residential projects stops losing a few points of product margin to tax errors, uncollected freight and misapplied deposits, and its bookkeeper's month-end close shrinks from days of spreadsheet reconciliation to an exception review, while the principal gains a real-time view of cash that is genuinely the firm's.
