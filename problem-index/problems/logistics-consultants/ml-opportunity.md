# Machine Learning Opportunities — Logistics Consultants

**Industry:** [[logistics-consultants|Logistics Consultants]]
**Derived from:** [[problems/logistics-consultants/high-impact|High Impact]], [[problems/logistics-consultants/low-impact-1|Low Impact 1]], [[problems/logistics-consultants/low-impact-2|Low Impact 2]], [[problems/logistics-consultants/worker-life-1|Worker Life 1]], [[problems/logistics-consultants/worker-life-2|Worker Life 2]]

---

## 1. Capturing the Senior Consultant's Read of Scenario Assumptions
#tacit-knowledge-ml #gradient-boosting #bayesian-inference #causal-inference #confidence-intervals #evaluation-metrics #revenue-impact

**Problem statement:** Senior consultants set the assumptions every scenario depends on — first-year productivity of a new building, rates on lanes with no bid history, transition cost, and the share of the modelled saving the client will actually capture — from pattern recognition across dozens of engagements they cannot specify, and the projected saving built on them is never compared with what the client realised. The ML problem is to learn those calls, and how far each kind has historically missed, from the firm's past engagements, and surface both while the next scenario is being built.

**ML task:** Per-assumption regression with prediction intervals for the value a senior consultant would set, conditioned on engagement features, with hierarchical (Bayesian) shrinkage across assumption types and clients; plus estimation of each assumption's realised error from post-implementation outcomes restated at matched volumes and market rates
**Input data:** Assumption registers reconstructed from past network design model files, scenario workbooks and readout decks; engagement metadata (industry, channel mix, labour market, client sponsor, implementation scope); where follow-up was contracted, post-go-live freight invoices, labour hours, transition cost and the implementation record; public freight rate indices and wage data for the restatement.
**Target:** The assumption value a senior consultant chose, with a confidence range; and, where outcomes exist, the realised value and the restated projection error per assumption.
**Evaluation metric:** Agreement with held-out senior consultant assumptions, reported against the consultants' own consistency on near-identical cases, which is the ceiling. For the outcome model, calibration: the share of restated realised values falling inside the stated interval, with confidence intervals honest about the small number of engagements per assumption type. Under-predicting ramp time or over-predicting capture costs the client money and the firm its credibility, so optimistic misses are weighted more heavily than pessimistic ones.
**Scope:** The data collection challenge is first and hardest: the expert's reasoning must be captured as the assumption is set, inside a scenario deadline, so the first deliverable is a register that drafts each record from the model file and asks the consultant to confirm value, precedent and confidence in seconds. The labelling challenge is twofold: consultants disagree with themselves, so a sample of assumptions needs repeated assessment to estimate intra-rater reliability; and realised outcomes are noisy and selected — only the recommended scenario is implemented, often partly — so labels must be restated counterfactually rather than read off the P&L. The deployment challenge is timing and authority: precedent must appear in the scenario-building surface faster than the consultant's own recall, and must inform rather than override, because the partner signs. Two data scientists and one senior consultant at a quarter of their time, 6–9 months to the register and a precedent view; outcome-calibrated conclusions need tens of followed-up engagements, so two to three years of disciplined capture at a mid-size firm.
**Data availability:** Model files and decks exist on firm drives for engagements whose letters did not require deletion; reconstructing assumption registers from them is most of the early work. Post-implementation data belongs to the client and is available only where a follow-up is contracted — more common in gainshare and managed-service engagements, rare in fixed-fee studies.

---

## 2. Ship-To Entity Resolution and Baseline Variance Attribution
#k-nearest-neighbors #word-embeddings #dbscan #gradient-boosting #evaluation-metrics #worker-facing #data-integration

**Problem statement:** In the data month of every network study an analyst resolves hand-typed ship-to and customer variants across TMS, ERP and freight audit files, fixes geocodes that land on billing offices, and hunts the gap when the baseline model does not tie to the ledger. Cluster record variants into physical receiving locations, flag implausible geocodes, and rank the likely causes of a baseline variance by cost bucket.

**ML task:** Entity resolution (embedding-based candidate matching plus density clustering of name and address variants); binary classification of geocodes as receiving versus non-receiving locations; ranked attribution of baseline variance to candidate causes (unallocated accessorials, missing invoice months, intercompany moves)
**Input data:** Ship-to names and addresses from TMS, ERP and freight audit extracts; geocodes and land-use data; past engagements' confirmed matches and corrected geocodes; baseline-versus-ledger variances by bucket with the causes analysts eventually found.
**Target:** Location clusters with confidence; receiving-location flags; a ranked list of variance causes per bucket.
**Evaluation metric:** Pairwise precision and recall of matches against analyst-confirmed clusters — false merges are worse than missed merges, because a wrong merge moves volume to the wrong place in the model — plus top-3 hit rate on variance causes, and analyst hours from data receipt to accepted baseline.
**Scope:** One ML engineer and one analyst, 4 months; matching quality improves with every engagement's confirmed clusters.
**Data availability:** Every engagement supplies the raw extracts; confirmed matches and variance causes are rarely saved and should be logged from now on.

---

## 3. LTL Shipment Density Imputation for Re-Rating
#gradient-boosting #word-embeddings #transformers #feature-engineering #evaluation-metrics #data-integration #automation

**Problem statement:** Since NMFC Docket 2025-1 (19 July 2025) moved many items to density-based classes, re-rating a client's LTL history under carrier proposals needs each shipment's density, and most historical records lack dimensions. Predict handling-unit dimensions and density for each shipment, with a calibrated interval, so the history can be re-classified and re-rated.

**ML task:** Regression with prediction intervals on density per shipment; classification of the resulting density subprovision
**Input data:** Shipment records (weight, piece and handling-unit count, commodity description, item numbers, origin and destination), item master dimensions where present, carrier re-weigh and inspection corrections (which carry measured dimensions), and dimensioner data from the minority of shipments that pass through measured terminals.
**Target:** Density in pounds per cubic foot and the corresponding class; flag for items whose class depends on handling or stowability rather than density.
**Evaluation metric:** Class-level accuracy (the rated outcome) rather than raw density error, with the cost asymmetry stated: under-estimating density over-states cost and biases carrier comparison; reporting each proposal's saving with the share coming from imputed shipments is part of the metric. Prediction-interval coverage on held-out measured shipments.
**Scope:** One ML engineer, 3 months, given re-weigh and inspection data for training labels. Commodity text varies widely and benefits from text embeddings over a vocabulary of LTL descriptions.
**Data availability:** Carrier inspection corrections are on the client's freight invoices and in freight audit files; item masters are internal; measured density at scale sits with carriers and dimensioner vendors rather than consultants.

---

## 4. Censored Demand and Lead-Time Reconstruction for Inventory Studies
#expectation-maximization #survival-analysis #exponential-smoothing #monte-carlo-methods #probability-distributions #revenue-impact

**Problem statement:** Inventory policy studies size safety stock from sales history that records shipments, not demand, and from lead times that are not recorded as a field. Estimate true demand distributions through stockout periods and lead-time distributions from purchase order and receipt history, then simulate proposed policies against last year's actuals.

**ML task:** Censored-demand estimation (demand is observed only up to available stock) with intermittent-demand models for the tail; time-to-receipt modelling of lead time with partial deliveries; Monte Carlo simulation of fill rate and inventory under candidate policies
**Input data:** Order lines with requested and shipped quantities, daily or weekly on-hand snapshots, purchase orders with order, promise and receipt dates (including splits), supplier and lane identifiers.
**Target:** Per-SKU-location demand distribution and lead-time distribution; simulated fill rate and average inventory under each policy.
**Evaluation metric:** Backtest the recommended policy against a held-out final quarter: realised fill rate against the policy's stated target, and inventory against projection. A policy that releases the projected working capital and misses its fill rate has failed — the client's sales team will blame the study — so fill-rate shortfall is weighted more heavily than excess inventory.
**Scope:** One data scientist, 3–4 months, to a reusable study harness; each later study in days rather than weeks.
**Data availability:** ERP extracts every study already receives; the gap is that on-hand snapshots are often not retained historically, which limits de-censoring to periods with snapshots.

---

## 5. Order-Profile-Driven Layout and Slotting Generation
#k-means-clustering #graph-theory #monte-carlo-methods #optimization-fundamentals #worker-facing #automation

**Problem statement:** A facility designer redraws the block layout and slotting for every scenario by hand. Generate candidate layouts and slotting plans from the order profile and building constraints, and score each by simulating last year's orders through it.

**ML task:** SKU clustering by velocity, cube and co-order affinity (affinity as a weighted graph); constrained layout generation; simulation-based scoring of travel distance and throughput
**Input data:** Order lines with timestamps, SKU dimensions and handling class, building drawing (column grid, clear height, docks), equipment catalogue and the designer's stated rules.
**Target:** Ranked candidate layouts with slotting, travel distance per line, throughput at peak hour and equipment count.
**Evaluation metric:** Simulated travel and throughput against the designer's own layout for the same scenario on past projects, and designer acceptance rate of generated candidates; where go-live data exists, simulated against achieved throughput.
**Scope:** Two engineers, 6 months; the hard part is encoding building constraints and rules, not the clustering.
**Data availability:** Order history and drawings are supplied on every engagement; achieved-throughput data after go-live is rare and held by the operator.
