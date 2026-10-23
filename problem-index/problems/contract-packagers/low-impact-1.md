# Reconciling Someone Else's Components

**Industry:** [[contract-packagers|Contract Packagers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Inventory software can count stock, but a co-packer has to account to each brand for every carton, label and tray the brand shipped in, and most do it with tally sheets and a spreadsheet sent weeks after the job.
**Tags:** #descriptive-statistics #bayesian-inference #time-series-forecasting #feature-engineering #data-integration #automation #revenue-impact

## The Problem
A co-packer rarely owns what it packs. The brand ships finished product from its own plant and components from its printers and converters: printed cartons, labels, blister cards, display corrugate, inserts. Each arrives against the brand's purchase order rather than the packager's, often short, early, late or in a different count than the packing slip. During the run, components are scrapped for misprints, damaged in handling, or used up faster than planned when a machine mis-feeds. At the end of the job the packager owes the brand a reconciliation: units received, units used, units scrapped with reasons, units returned or held. Brands set allowances for overage and scrap. Variances beyond them get charged back, and printed components are expensive and slow to reorder.

The work is done by hand. Receiving counts go on paper, line usage is estimated from finished-goods counts multiplied by the bill of materials, and scrap is whatever is left over. When the numbers do not tie, the reconciliation turns into an email argument about whether the printer under-shipped or the line over-used. In drug packaging the same arithmetic is a regulatory duty: labelling issued, used and returned must reconcile within preset limits, and discrepancies are investigated (estimate, recalled from 21 CFR 211.125).

## What Already Exists
Warehouse and ERP systems track lots, locations and bills of materials: Nulogy Shop Floor for co-packers, food ERPs such as Deacom and NutraSoft, and general systems such as Business Central or MRPeasy, which can issue components to a job and receive finished goods back. Brands track what they sent through their own ERP and their printers' advance ship notices.

## The Customisation Gap
The generic systems assume the operator owns the stock. A packager needs separate client-owned pools by brand and by purchase order. Many food ERPs keep lots in the plant's own inventory instead. It also needs receiving variance recorded against the brand's supplier's shipment, not just the brand's order, and expected usage computed from each job's actual bill of materials with per-component scrap allowances learned from past runs. Mid-run, it needs to flag when a component is being consumed faster than the finished count explains. The output that matters is the reconciliation report in the brand's own format, produced the day the job closes, with each variance tied to a cause the brand will accept: printer short-ship, line damage, misprint, or count error.

## Impact If Solved
Closing a job's component reconciliation on the day it finishes, rather than weeks later, removes most chargeback disputes and the hours spent on them. It also gives the estimator real scrap rates by component type for the next quote. For a mid-sized co-packer running hundreds of jobs a year, that is a full-time administrative role recovered and a recurring source of margin leakage closed (estimate).
