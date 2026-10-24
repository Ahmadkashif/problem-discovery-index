# Machine Learning Opportunities — Land Developers

**Industry:** [[land-developers|Land Developers]]
**Derived from:** [[problems/land-developers/high-impact|High Impact]], [[problems/land-developers/low-impact-1|Low Impact 1]], [[problems/land-developers/low-impact-2|Low Impact 2]], [[problems/land-developers/worker-life-1|Worker Life 1]], [[problems/land-developers/worker-life-2|Worker Life 2]]

---

## 1. Learning the Land Manager's Entitlement Read
#tacit-knowledge-ml #gradient-boosting #survival-analysis #large-language-models #bert #evaluation-metrics #feature-engineering #revenue-impact

**Problem statement:** Experienced land and entitlement managers "know" whether a council will approve a rezoning, what it will cost in concessions, and how many months it will take. The judgement comes from years of watching the same commissions, staff and neighbourhood groups, and it leaves with them. The ML problem is to learn that read from public hearing records plus the manager's own recorded predictions, and give a calibrated approval probability and time-to-approval for a new case.

**ML task:** Case-level binary classification (approved / denied or withdrawn) with a calibrated probability, plus time-to-event modelling of months from application to final approval, with continuances and resubmittals as recurrent events; passage-level text classification of staff reports and minutes for the signals the manager reads (staff recommendation, conditions added, opposition speakers, density reductions)
**Input data:** Agendas, staff reports, minutes, votes and case histories from Legistar and similar systems (San Antonio's open Legistar API returns zoning cases with case numbers, districts, requested changes and "continued from" status in the title, though its records stop in 2021; Phoenix's and Austin's are current, and Phoenix's matter histories record the council action and pass flag); the zoning code and future land-use map; parcel attributes and neighbouring land uses; comparable cases in the same jurisdiction; the developer's deal ledger with the manager's predicted outcome, date and expected concessions at contract.
**Target:** Final outcome per case; months from filing to approval; number of continuances; whether the approved density or lot count fell below the request; agreement between model and manager.
**Evaluation metric:** Brier score and calibration of approval probability, and concordance index plus median absolute error in months for time-to-approval, all measured out of time and out of jurisdiction. A model that only learns "this city approves everything" is useless, so report skill against the jurisdiction's base rate. Under-predicting time is the costly error: a land committee that plans on a nine-month approval and gets eighteen pays a year of carry and may lose the builder's takedown, so penalise late errors more than early ones.
**Scope:** The data-collection challenge comes first. The expert's read must be captured at decision time, so the system needs a near-zero-effort prediction surface (the manager confirms a drafted forecast in the deal record), and historical predictions have to be reconstructed from committee memos. The labelling challenge is that outcomes are confounded by what the developer conceded, and managers disagree with themselves after a recent loss, so outcomes need decomposing (approved as filed, approved reduced, continued, denied) and a sample of cases double-labelled to estimate intra-rater reliability. The deployment challenge is speed: the forecast must arrive while the manager is deciding whether to tie up a tract, within minutes of an agenda posting, or it is ignored. 2 ML engineers and 1 data engineer for document ingestion, 6–9 months for a first set of metro areas. Value appears first as retrieval ("the last five cases like this before this commission") before any classifier is trusted.
**Data availability:** Hearing records are public but scattered: Legistar, Granicus and CivicClerk portals, PDFs and video. Coverage is uneven in smaller counties and in Texas ETJs where counties lack zoning. The manager's predictions exist only inside developers and builders and must be built going forward. Outcomes are public.

---

## 2. Jurisdictional Wetland and Stream Screening
#cnns #semantic-segmentation #gradient-boosting #feature-engineering #evaluation-metrics #compliance #quick-win

**Problem statement:** Before a developer spends money on a delineation, estimate which parts of a tract are likely wetlands or streams that a consultant will map, and which of those are likely federally jurisdictional after Sackett v. EPA (2023, recalled). Then estimate the acreage that would need a Section 404 permit or avoidance.

**ML task:** Pixel-level semantic segmentation of probable wetland and stream features, followed by feature-level classification of likely jurisdictional status
**Input data:** Aerial and satellite imagery across seasons, USGS 3DEP lidar elevation and derived wetness and flow-accumulation indices, NRCS soils (hydric ratings), USFWS National Wetlands Inventory, NHD hydrography, FEMA flood zones (all public, recalled); delineation reports and Corps approved jurisdictional determinations as labels where the developer holds them.
**Target:** Probability per pixel of wetland or stream; per feature, probability of jurisdiction and expected acreage affected.
**Evaluation metric:** Recall on delineated wetland acreage at the screening threshold, because a missed wetland found after closing can cost a phase, plus intersection-over-union against delineated boundaries. Precision matters less at screening, since the consultant's field delineation still happens.
**Scope:** A screening tool, never a delineation; the field delineation and Corps determination remain legally required where they apply. 1 ML engineer and 1 GIS engineer, 4–5 months for one region's soils and hydrology. Regional models will not transfer well between, say, Florida flatwoods and Texas blackland prairie.
**Data availability:** Imagery, lidar, soils and the wetlands inventory are free. Labels are the hard part. Delineations are client-owned consultant work (see [[niches/environmental-consultants/nepa-permitting-consultancies/profile|Environmental Permitting & NEPA Consultancies]]), so a developer can train on its own reports. Public approved jurisdictional determinations give a smaller, noisier set.

---

## 3. Horizontal Cost per Lot Estimating
#gradient-boosting #linear-regression #bayesian-inference #confidence-intervals #feature-engineering #evaluation-metrics #revenue-impact

**Problem statement:** Predict the horizontal development cost per lot (earthwork, storm and sanitary sewer, water, paving, detention, dry-utility contributions, fees) from a conceptual layout and site conditions, with an interval the land committee can underwrite.

**ML task:** Regression with quantile or Bayesian intervals on cost per lot and on major cost categories, hierarchical by region and year
**Input data:** The developer's historical pay applications and final costs by phase, mapped to cost codes; quantities from civil plans (cut and fill, linear feet of pipe by size, square yards of paving, lift stations); lot count, lot width and density; soils and slope; distance to utility tie-ins; jurisdiction (fee schedules, street standards); construction cost indices; municipal utility bid tabulations as public price points.
**Target:** Final cost per lot and per category at phase completion.
**Evaluation metric:** Mean absolute percentage error on cost per lot out of time, and interval coverage (does the 80% interval contain the outcome 80% of the time). Under-estimates matter more than over-estimates because they come out of margin after the land price is fixed.
**Scope:** The developer's own history is the core. Hierarchical pooling across phases and regions handles small samples. 1 data scientist and 1 engineer for cost-code mapping, 3–4 months to a first model for one developer. The most work goes into mapping inconsistent pay-application line items to a common taxonomy.
**Data availability:** Each developer holds its own costs. Unit prices from public utility and DOT bid tabs overlap with [[heavy-civil-contractors|Heavy Civil Contractors]] and the queued highway contractors build. The quantities sit in civil plans the developer owns.

---

## 4. Builder Takedown Pace and Walk-Away Risk
#time-series-forecasting #survival-analysis #gradient-boosting #temporal-fusion-transformers #evaluation-metrics #revenue-impact

**Problem statement:** Forecast how many lots each builder will take down per quarter in each community, and the probability that a builder misses its quota, renegotiates price or walks away from its deposit.

**ML task:** Hierarchical time-series forecasting of takedowns by builder and community, plus survival modelling of time to a missed quota or contract termination
**Input data:** Lot contracts and takedown history; builder sales and closings by community (the developer sees closings; licensed new-home data from vendors such as Zonda adds competitor communities); Census building permits by county; mortgage rates; builder backlog and cancellation rates from public filings; deposit size as a share of lot price; escalator terms.
**Target:** Lots taken down per builder per quarter; time to first missed quota; termination or repricing events.
**Evaluation metric:** Weighted absolute percentage error on quarterly takedowns over a one- to four-quarter horizon, and concordance plus calibration on default risk. The costly error is missing a slowdown: lots finished for a builder who stops taking them carry interest, taxes and district assessments.
**Scope:** Takedown events are sparse per community, so pooling across communities and builders matters more than model complexity. 1 data scientist, 3 months for a developer or land banker with a few dozen contracts. Value is highest for land-banking platforms holding hundreds of option contracts.
**Data availability:** Contracts and takedowns are the developer's or platform's own. Builder-level sales by community need a licensed data feed. Macro series are public.

---

## 5. Contract and Reimbursement Document Extraction
#large-language-models #transformers #seq2seq #bert #evaluation-metrics #automation #workflow-orchestration

**Problem statement:** Turn lot purchase and option agreements into a lot-level takedown ledger, and turn pay applications, invoices and lien waivers into district-eligible cost lines with their supporting documents.

**ML task:** Clause extraction and normalisation into a schema (quota, deposit, escalator, delivery conditions, remedies); line-item classification of invoice and pay-application rows into eligibility categories; document matching between invoice, waiver and payment
**Input data:** Executed contracts and amendments; pay applications, invoices, lien waivers and payment records; district creation documents and eligibility rules; engineer cost summaries from prior bond applications.
**Target:** Structured contract terms per lot and per phase; eligibility class and district or series per cost line; missing-support flags.
**Evaluation metric:** Field-level accuracy on contract terms at the confidence where fields are written without review, with zero tolerance for silent errors on price escalators and deposit credits. For reimbursement, recall on eligible dollars found, and precision on lines the auditor later disallows.
**Scope:** Prior bond applications and the developer's past takedown spreadsheets provide labelled examples. 1–2 engineers, 3–4 months. The hard tail is amended contracts and invoices that mix eligible and ineligible scope on one line.
**Data availability:** All documents are the developer's own. Reimbursement rules are public statute and district documents, but each district's creation documents vary.
