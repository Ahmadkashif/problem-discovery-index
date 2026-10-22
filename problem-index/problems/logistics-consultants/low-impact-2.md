# Inventory Policy Studies on Uncleaned Demand History

**Industry:** [[logistics-consultants|Logistics Consultants]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Inventory optimisation software assumes clean demand and a long implementation; a consultant has eight weeks and an ERP extract in which stockouts look like low demand and lead times have to be reverse-engineered from purchase order receipts.
**Tags:** #exponential-smoothing #expectation-maximization #monte-carlo-methods #probability-distributions #survival-analysis #feature-engineering #revenue-impact

## The Problem
A distributor's CFO wants to know how much working capital is tied up in excess inventory and what safety stock policy would release it without hurting fill rate. The consultant receives two or three years of sales order lines, purchase orders and receipts, and on-hand snapshots from the ERP. The study is a fixed-fee diagnostic — commonly six to ten weeks (estimate) — ending in a working-capital release figure and a policy table: service target, safety stock, reorder point and order quantity by SKU and location.

The data fights the method. Sales history records what shipped, not what was wanted, so every stockout week looks like a week of low demand and the policy built on it under-stocks the SKUs that most need stock. Lead time is not recorded as a field; it has to be reconstructed from purchase order dates and partial receipts, and its variability — the input safety stock depends on most — is buried in split deliveries and expedites. Slow movers sell in lumps that normal-distribution formulas mis-size. And the client's planners will only use the result if it arrives as min/max values their ERP can load.

## What Already Exists
Inventory optimisation software — ToolsGroup, Slimstock, Netstock, Lokad, and the planning modules of Kinaxis, o9 and Blue Yonder — models demand probabilistically and computes multi-echelon safety stock well. These products are sold as continuous planning systems with months of integration and data hygiene work, priced as annual subscriptions. They are not built for a consultant who needs to run a one-off, defensible study on an extract and hand it back.

## The Customisation Gap
A study-mode tool needs: ingestion of raw ERP extracts with no integration project; demand de-censoring that estimates true demand during stockout periods from on-hand history and lost-sales signals; lead-time distributions reconstructed from purchase order and receipt history, including split shipments; intermittent-demand handling for the long tail; simulation of fill rate and inventory under the proposed policy against the actual history, so the client can see how the policy would have performed last year; and output formatted to the client ERP's replenishment fields. The output the CFO signs is a working-capital figure with an honest confidence range, not a point estimate.

## Impact If Solved
The analyst's four to five weeks of data reconstruction (estimate) compresses to days, and the working-capital figure stops being built on censored demand, which is the usual reason a study's projected release fails to appear and its policy causes stockouts in the first quarter after go-live.
