# Machine Learning Opportunities — Interior Design Firms

**Industry:** [[interior-design-firms|Interior Design Firms]]
**Derived from:** [[problems/interior-design-firms/high-impact|High Impact]], [[problems/interior-design-firms/low-impact-1|Low Impact 1]], [[problems/interior-design-firms/low-impact-2|Low Impact 2]], [[problems/interior-design-firms/worker-life-1|Worker Life 1]], [[problems/interior-design-firms/worker-life-2|Worker Life 2]]

---

## 1. Learning the Designer's Read of a Client's Taste
#tacit-knowledge-ml #contrastive-learning #transformers #k-nearest-neighbors #evaluation-metrics #feature-engineering #worker-facing #revenue-impact

**Problem statement:** Senior designers predict which products, finishes and schemes a client will approve from a few reference images and early reactions, a judgement they cannot specify. The ML problem is to learn that read from the firm's own history of shown-versus-approved items, so that a new client's first presentation is ranked by predicted approval and the items most likely to be rejected are flagged.

**ML task:** Contrastive representation learning over product images, swatches and room photographs, plus client-conditioned learning-to-rank of the firm's trade catalogue by approval probability
**Input data:** Product images and attributes from the trade catalogues the firm buys from; fabric, finish and colour swatch images; the client's reference boards and site photographs; every presentation's shown items with outcome (approved, rejected, questioned) and the designer's short reason; project metadata (room, budget band, existing pieces).
**Target:** For a client and a room, a ranking of candidate items by probability of approval; at item level, approved or rejected in the context of the other items in the scheme; a set of client taste descriptors in the designer's vocabulary with supporting evidence.
**Evaluation metric:** Ranking quality (recall at 10 and NDCG) of eventually approved items among the catalogue, measured on held-out clients rather than held-out items, since leakage through the same client inflates results badly. The practical headline is presentation rounds to approval in a controlled comparison. Agreement with designers is reported against the designers' own test-retest agreement on repeated client files, which is the ceiling. A false "likely approved" costs a round; a missed good candidate costs little, so precision at the top of the list matters more than recall deep in it.
**Scope:** The data collection challenge dominates: rejections are the most informative signal and are almost never stored, so the first deliverable is a capture surface that logs shown items and reactions during or immediately after a presentation in under a minute, plus a reconstruction of past projects from presentation decks and final proposals. The labelling challenge is that designers disagree with themselves and clients approve to end meetings, so a sample of client files must be re-judged by several designers to measure agreement, and later returns and complaints must be joined back as delayed labels. The deployment challenge is speed: ranking must run inside the tool the designer already clips from and be faster than flipping a catalogue, presented as the client's own history ("rejected sheen three times") rather than as machine taste. Two ML engineers and a product designer embedded with two or three studios, 6–9 months, starting with pretrained image-text embeddings and adding firm-specific fine-tuning once a few hundred presentations are logged.
**Data availability:** Catalogue images are available from manufacturers and Material Bank. Approved selections exist in studio software. Shown-and-rejected items and reasons do not exist anywhere and must be captured going forward; a pooled dataset across firms would require consent and is the strategic asset.

---

## 2. Acknowledgement and Invoice Discrepancy Detection
#large-language-models #transformers #feature-engineering #evaluation-metrics #automation #data-integration #workflow-orchestration

**Problem statement:** Extract line items from vendor order acknowledgements, invoices and shipping notices in arbitrary formats and match them to purchase order lines, flagging differences in item, fabric or finish code, dimensions, quantity, sidemark, price and ship date.

**ML task:** Document information extraction plus line-level entity matching and discrepancy classification
**Input data:** PDF and email acknowledgements, pro forma invoices and shipping notices from hundreds of to-the-trade vendors; the firm's purchase orders with line detail; vendor product catalogues for code normalisation.
**Target:** Structured line items; a match to each PO line; per-field discrepancy flags with severity (wrong fabric is critical, a one-cent price variance is not).
**Evaluation metric:** Recall on critical discrepancies (finish, fabric, dimension, quantity) is the binding metric, because a missed wrong-fabric acknowledgement becomes a custom sofa that cannot be returned. Precision is tracked as designer review minutes per acknowledgement. Field-level extraction accuracy is reported per vendor so a new vendor format is caught early.
**Scope:** General-purpose document models now extract tables from PDFs well; the work is normalisation of vendor codes and finish nomenclature, and a matching layer that understands sidemarks and partial shipments. One ML engineer and one integration engineer, 3–4 months to a production tool for a single studio-software platform.
**Data availability:** Every firm holds years of acknowledgements and POs in email and studio software; labels come from the corrections designers already made. Studio-software vendors hold the largest pooled corpus.

---

## 3. Realistic Arrival-Date Prediction for To-the-Trade Orders
#survival-analysis #gradient-boosting #time-series-forecasting #feature-engineering #evaluation-metrics #data-integration

**Problem statement:** Vendors quote lead times that slip often and unevenly. Predict, for each open order line, the distribution of the actual ship and delivery dates, so install dates are planned on evidence rather than on the quote.

**ML task:** Time-to-event modelling with censoring (orders still open) plus gradient-boosted quantile regression on lead-time overrun
**Input data:** Historical POs with order date, quoted lead time, acknowledged ship date, actual ship and delivery dates; vendor, product category, custom versus stock, fabric source (customer's own material versus vendor stock), season, freight mode and receiving warehouse; vendor-wide disruption signals.
**Target:** Probability of delivery by each week from order; median and 80th-percentile delivery date per line; project-level probability of being install-ready by a target date.
**Evaluation metric:** Calibration of the predicted delivery distribution (does the 80th percentile cover 80% of outcomes) and mean absolute error of the median against actual dates, both against a quoted-lead-time baseline. Under-prediction is costlier than over-prediction: an install scheduled too early wastes a crew day and a client's patience.
**Scope:** Statistically modest; the hard part is clean history, because actual delivery dates are often recorded only as a receiving-warehouse email. One data scientist, 3 months, once item 2 above has structured the paperwork.
**Data availability:** Each firm's history is small and vendor-skewed; studio-software platforms and receiving warehouses hold multi-firm histories that make the model useful for vendors a single firm rarely uses.

---

## 4. Code-Compliant Alternate Matching
#cnns #contrastive-learning #k-nearest-neighbors #bert #evaluation-metrics #compliance #automation

**Problem statement:** When a specified product is discontinued, back-ordered or value-engineered, find alternates that match the look of the basis-of-design product and also meet its performance and code attributes for the occupancy where it will be installed.

**ML task:** Visual similarity retrieval over product and swatch images, constrained by extracted attributes (flammability test, flame-spread class, abrasion double rubs, cleanability, dimensions, weight rating)
**Input data:** Manufacturer product images and swatch scans; spec sheets and test reports from which attributes are extracted; the project's basis-of-design item and occupancy and location requirements; past approved alternates.
**Target:** A ranked list of alternates with a pass, fail or unknown per required attribute and a visual similarity score.
**Evaluation metric:** Share of top-five alternates a specifier accepts, and, separately, zero tolerance for alternates marked as passing a required attribute they fail; a false pass is a code violation, so attributes not found in source documents are reported as unknown, never inferred.
**Scope:** Image retrieval is mature; attribute extraction from spec sheets and test reports is the bulk of the work. Two engineers, 4–6 months for a contract-textile and seating vertical first, where attribute data is most structured.
**Data availability:** Manufacturer data is public but inconsistent; test reports are often supplied only on request. Purchasing agents and commercial interiors teams hold approved-alternate histories.

---

## 5. Design-Hours Estimation for Fee Proposals
#gradient-boosting #linear-regression #regularization #feature-engineering #evaluation-metrics #revenue-impact

**Problem statement:** Firms quote flat or capped fees and routinely under-estimate design hours, absorbing overruns. Predict total design and procurement hours for a proposed project from its scope and client signals.

**ML task:** Regression on project hours with prediction intervals
**Input data:** Past projects' scope (rooms, square footage, new build versus refresh, number of FF&E lines, custom millwork), client attributes captured at intake (decision-makers, prior design experience, stated budget versus final spend), presentation rounds and change orders, and logged hours by phase.
**Target:** Total hours by phase and an 80% interval; a flag for scopes likely to exceed the quoted fee.
**Evaluation metric:** Mean absolute percentage error against logged hours on held-out projects, plus interval coverage; the cost asymmetry favours not under-estimating, since overruns on a fixed fee come straight out of profit.
**Scope:** Simple models suffice; the constraint is that many small firms do not log hours at all. One data scientist, 2 months per firm, or a pooled model inside a studio platform.
**Data availability:** Time and project data exist in studio software for firms that bill hourly; firms on flat fees need light-touch time capture first.
