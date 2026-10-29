# Machine Learning Opportunities — Consumer Goods Wholesalers

**Industry:** [[consumer-goods-wholesalers|Consumer Goods Wholesalers]]
**Derived from:** [[problems/consumer-goods-wholesalers/high-impact|High Impact]], [[problems/consumer-goods-wholesalers/low-impact-1|Low Impact 1]], [[problems/consumer-goods-wholesalers/low-impact-2|Low Impact 2]], [[problems/consumer-goods-wholesalers/worker-life-1|Worker Life 1]], [[problems/consumer-goods-wholesalers/worker-life-2|Worker Life 2]]

---

## 1. New-Item Sell-Through and Buy Depth From a Sample
#tacit-knowledge-ml #contrastive-learning #gradient-boosting #transformers #feature-engineering #revenue-impact

**Problem statement:** Given a sample an importer's merchant is considering (photo, attributes, factory quote, minimum, target retail and intended accounts), predict its 26-week sell-through by channel and recommend a buy quantity, making the experienced merchant's read of "what will sell" explicit, comparable and gradeable.

**ML task:** Image-and-attribute embedding with similarity retrieval, then quantile regression of rate of sale by channel, converted to a recommended buy range under the factory minimum.
**Input data:** Item photos and spec sheets; factory quotes and minimums; category, material, licence, colourway, price point and pack; intended accounts and retail price; for past items, units shipped by account, retailer sell-through where available (portal exports and EDI 852 product-activity data), markdown money and returns claimed, closeout recovery and stockout weeks; early signals (show orders, Faire orders, test-store results); the merchant's conviction score from the item ledger.
**Target:** P10/P50/P90 units sold per distributed store per week over 26 weeks by channel; a derived buy range; a binary flag for "ends in closeout above 20% of units" (estimate threshold).
**Evaluation metric:** Pinball loss on the quantiles and weighted MAPE on season units, scored on a held-out season rather than random items, because trends move season to season. Report realised margin of the recommended buy against the actual buy on back-test. Overbuys cost more than underbuys for most categories (closeout at a fraction of cost against a lost sale's margin), so evaluate at the asymmetric loss the finance team sets per category.
**Scope:** A team of 2–3 for 4–6 months for a first category. The collection challenge comes first: the item ledger has to capture samples considered and passed, with the merchant's intent, at the showroom, so the first two months are a capture app and back-filling three to five seasons of bought items from spec sheets and photos. The labelling challenge is that sell-through must be normalised for distribution, price and retailer cuts before it grades the item, and merchants re-rate the same sample differently season to season. The data is also selected, since only bought items have outcomes. The deployment challenge is speed: retrieval of comparables must return on a phone in seconds during a factory meeting, or the merchant's memory wins.
**Data availability:** Shipments, item masters and closeout sales are the importer's own. Retailer sell-through is furnished under each retailer's supplier terms (Walmart's and Target's portal terms were not read), so the model should use it for the importer's own planning only. Five seasons of history at a mid-size importer gives a few thousand items, enough for the retrieval model with transfer from a pretrained image encoder, and thin for rare categories.

---

## 2. Deduction Validity, Recovery and Supplier Pass-Back
#gradient-boosting #large-language-models #bert #feature-engineering #automation #revenue-impact

**Problem statement:** For every retailer deduction on a wholesaler's remittances, predict whether it is invalid (dispute it), valid and caused by a supplier (re-bill it), or valid and the wholesaler's own (accept it), and the expected recovery of each action, so analysts and agents work the dollars that come back.

**ML task:** Document parsing and entity extraction, then three-way classification plus regression of expected recovery per deduction.
**Input data:** X12 820 remittances and 812 credit and debit adjustments; retailer portal claim exports; 850 purchase orders (EDI or PDF), 856 ship notices, 810 invoices and proof of delivery; vendor agreements and promotion emails with allowance terms; supplier agreements with pass-back clauses; the history of disputes filed, won and lost by retailer, reason code and amount.
**Target:** Class (dispute / re-bill supplier / accept) with calibrated probabilities; expected dollars recovered net of handling cost; for re-bills, the supplier and SKU lines responsible.
**Evaluation metric:** Dollars recovered per analyst hour on a held-out period, with precision on "dispute" weighted heavily, because weak disputes burn credibility with the retailer's claims team and can delay payment on good invoices. Calibration matters because the triage threshold is set in expected dollars.
**Scope:** A first version fits a two-week MVP with 2 engineers. It parses 812 and 820 files into a queue, classifies reason codes with a fine-tuned BERT model plus rules, extracts PO prices and allowances from 850s and PDF purchase orders with an LLM, matches 856 and 810 records, and drafts the dispute packet or supplier debit memo for human approval. The gradient-boosted recovery model needs 6–12 months of labelled dispute outcomes; until then, rules and retailer-specific evidence templates carry it.
**Data availability:** Remittances, POs, invoices and agreements are the wholesaler's own. Dispute outcomes exist only if the AR team logged them, and many teams have only a spreadsheet, so outcome capture is the first build.

---

## 3. Retailer Reorder Forecasting From Product Activity Data
#time-series-forecasting #temporal-fusion-transformers #lstms-and-grus #exponential-smoothing #data-integration

**Problem statement:** Forecast each big-box retailer's replenishment purchase orders for each SKU and distribution centre 4–12 weeks ahead from the retailer's own store sales and inventory, so a wholesaler that holds the stock can buy, position and ship it complete.

**ML task:** Multi-horizon hierarchical time-series forecasting of retailer orders, conditioned on point-of-sale and inventory signals.
**Input data:** EDI 852 product activity data and portal exports (store sales, on-hand, on-order), the retailer's order history (850s), promotions and ad calendars, store counts and modular changes, price, weather for seasonal lines, and the wholesaler's own fill history.
**Target:** Units ordered per SKU per retailer DC per week for the next 4–12 weeks, with quantiles.
**Evaluation metric:** Weighted MAPE at SKU-DC-week, plus the share of ordered units that would ship short at a given inventory level in simulation. Under-forecasting costs a scorecard miss and possibly an on-time and in-full fine, so weight under-forecast errors higher.
**Scope:** 1–2 data scientists for 3 months per retailer feed. Exponential smoothing per series sets the baseline; a temporal fusion transformer or LSTM across series learns the order policy the retailer's replenishment system follows. The hard part is item and calendar mapping across retailers.
**Data availability:** The order history is the wholesaler's own. The 852 and portal data are the retailer's, furnished under its supplier terms (unread), and usable for the wholesaler's planning. Harmonisers such as Crisp, Alloy.ai and SPS Analytics already clean these feeds.

---

## 4. Independent-Store Credit Risk on Net Terms
#survival-analysis #gradient-boosting #logistic-regression #feature-engineering #revenue-impact

**Problem statement:** Predict which independent store accounts will go 60+ days past due, close or default within six months, so the credit manager can set terms and limits by store rather than by habit.

**ML task:** Time-to-event modelling of delinquency and default, with a gradient-boosted classifier for 6-month default probability.
**Input data:** The wholesaler's own receivables history (invoice dates, payment dates, partial payments, disputes, returns), order cadence and size by season, rep notes, credit applications, trade references, commercial credit bureau scores where licensed, and public signals such as closures, liens and changes of ownership.
**Target:** Hazard of reaching 60+ days past due; 6-month default probability; a recommended credit limit.
**Evaluation metric:** Concordance index for the survival model and AUC for the classifier, judged on the dollars written off per dollar of terms sales at the approval rate the business chooses. A missed default costs the whole balance, while a wrongly refused store costs one order's margin, so recall on defaults is weighted.
**Scope:** 1 data scientist for 2–3 months. Thousands of small accounts with years of payment history make this one of the cheapest wins in the industry. The labelling trap is that accounts put on cash-in-advance never default, so the history is censored by past credit decisions.
**Data availability:** Receivables history is the wholesaler's own. Bureau data comes under its licence terms. Industry credit-group information is membership data shared for the group's purposes, not for model training.

---

## 5. Landed-Cost Scenarios Under Pending Tariff Actions
#monte-carlo-methods #bayesian-inference #large-language-models #feature-engineering #compliance

**Problem statement:** For each SKU and each open purchase order, estimate the distribution of landed cost at receipt under pending tariff, freight and currency changes, and flag SKUs whose margin on each retailer programme will fall below floor, so cost-change requests and buy decisions are made before the duty lands.

**ML task:** Monte Carlo simulation over tariff, freight and currency scenarios, with Bayesian updating of scenario probabilities as notices and rulings appear, plus LLM extraction of notices into rate changes by HTS line and country.
**Input data:** Entry summaries (HTS lines, values, duty paid), the tariff schedule and pending actions (Federal Register notices, CBP messages, USTR determinations), freight quotes and index levels, currency rates, the SKU-to-HTS map, open purchase orders, and retailer cost files and programme margins.
**Target:** P10/P50/P90 landed cost per SKU at expected receipt date; probability of margin below floor per SKU and retailer.
**Evaluation metric:** Mean absolute percentage error of the P50 landed cost against the actual landed cost at receipt, and coverage of the P10–P90 band. Missing a cost spike costs a quarter of margin; a false alarm costs one unnecessary request.
**Scope:** 1–2 engineers for 2–3 months. The simulation is simple. The work is in keeping the SKU-to-HTS map clean, extracting notices into machine-readable rate changes, and linking costs to each retailer's cost file.
**Data availability:** Entry data is the importer's own, from its broker or ACE reports. Tariff notices are public. Freight indexes are licensed.
