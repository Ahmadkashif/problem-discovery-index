# Machine Learning Opportunities — Hazardous Waste Firms

**Industry:** [[hazardous-waste-firms|Hazardous Waste Firms]]
**Derived from:** [[problems/hazardous-waste-firms/high-impact|High Impact]], [[problems/hazardous-waste-firms/low-impact-1|Low Impact 1]], [[problems/hazardous-waste-firms/low-impact-2|Low Impact 2]], [[problems/hazardous-waste-firms/worker-life-1|Worker Life 1]], [[problems/hazardous-waste-firms/worker-life-2|Worker Life 2]]

---

## 1. Learning the Approval Chemist's Read of a Waste Profile
#tacit-knowledge-ml #gradient-boosting #large-language-models #transformers #evaluation-metrics #feature-engineering #compliance #revenue-impact

**Problem statement:** Senior approval chemists at TSDFs read a generator's waste profile and "know" that loads under it will not match: the plant under-describes water, the generator-knowledge claim is thin for that process, the recertified volume jumped. The ML problem is to learn that read from the facility's own history of profiles and what the receiving lab later found, and to rank the approval queue by the risk the senior chemist would have seen.

**ML task:** Binary classification (will loads under this profile be discrepant or rejected within 12 months) with calibrated probabilities, plus field-level attribution of which profile entries and history drive the score
**Input data:** Structured profile fields (claimed waste codes, constituents and ranges, physical state, generator-knowledge basis, process description, container, volume) and their change from the prior version; attached safety data sheets and analytical reports as text; generator and site history (prior profiles, discrepancy and rejection rate, re-profiles); approval decision, conditions and chemist; receiving-lab fingerprint and full-analysis results per load; e-Manifest discrepancy reports; treatment outcome flags (off-spec feed events, residues failing land-disposal standards).
**Target:** Load-level discrepancy or rejection under the profile, aggregated to the profile; secondary target is agreement with the senior chemist's conditions on a held-out review set.
**Evaluation metric:** Recall at the top decile of the ranked queue on profiles that later produced discrepancies, because a missed bad profile costs a held or rejected load and a possible permit deviation while a false flag costs a chemist a few minutes. Brier score and calibration by generator size, measured strictly forward in time. Model-to-chemist agreement is reported against the chemists' own test-retest agreement on re-reviewed profiles as the ceiling.
**Scope:** The data collection challenge comes first: the chemist's reasoning must be captured as she approves, so the approval screen needs a one-tap record of the concern acted on, and historical approvals must be joined to LIMS results and discrepancy records that sit in separate systems. The labelling challenge is that only fingerprinted containers are tested, rejected profiles never ship, and the same chemist conditions the same profile differently in a full week and a slack one, so labels need repeated blind review of a sample of profiles to estimate intra-rater reliability. The deployment challenge is speed: the Waste Analysis Plan fixes what is tested, so the model can only reorder the queue and draft generator questions, and it must surface its concern faster than the chemist's own recall of the generator or it will be ignored. Two ML engineers and one technical-services chemist, 6–9 months at one consolidator's facility, with value first appearing as retrieval ("every load under this generator's last three profiles") before any score is trusted.
**Data availability:** Every TSDF holds the profiles, LIMS results and discrepancy records; few have joined them. Generator data arrives under service terms, so models stay inside the facility that received the profiles. Outcomes are recorded for every shipped load.

---

## 2. Waste-Code and Shipping-Description Classification From Safety Data Sheets
#bert #transformers #large-language-models #k-nearest-neighbors #evaluation-metrics #compliance #automation

**Problem statement:** Given a product's safety data sheet, the generator's process context and the state, propose the RCRA waste codes and the DOT proper shipping description for the waste it becomes, so profiles, retail SKU classifications and lab-pack inventories start from a checked draft instead of a blank form.

**ML task:** Multi-label classification over federal characteristic and listed codes plus state-only codes, with retrieval of the nearest previously classified products as evidence; sequence-to-structure extraction of SDS sections into profile fields
**Input data:** Safety data sheets (sections on composition, physical properties, transport and disposal); prior approved profiles and SKU classifications with their codes; state code lists; process descriptions where available.
**Target:** Set of waste codes and a DOT description per product or stream, each with a cited SDS passage or precedent.
**Evaluation metric:** Recall on characteristic and listed codes per product, because a missed code is a mis-managed waste and a violation, while an extra code costs a reviewer's check. Exact-set accuracy and reviewer edit rate are reported alongside. Results are split by SDS quality, since old and foreign-language sheets are where errors concentrate.
**Scope:** The model drafts and a credentialed reviewer approves. The rules are written down, but applying them to mixtures and spent materials is the hard tail, and state codes multiply the label space. One ML engineer, one regulatory chemist and a labelling budget for ~20,000 reviewed products, 5 months to a usable drafting tool.
**Data availability:** SDS libraries are licensed by chemical data vendors and held by every TSDF; historical profiles and SKU classifications provide labels, under the data terms of whoever holds them.

---

## 3. Generator Status Shifts Detected From Public Manifest Data
#change-point-detection #hidden-markov-models #bayesian-inference #descriptive-statistics #data-integration #compliance

**Problem statement:** Infer each generator site's monthly status from the quantities it ships under manifests, detect status changes and episodic events, and flag sites whose notified status disagrees with what they ship, for the generator's own compliance team or a vendor serving it.

**ML task:** Latent-state inference of monthly generation status from noisy, lagged shipment quantities (generation is not shipment), with change-point detection for process changes and episodic events
**Input data:** Public e-Manifest records (generator site, quantities, units, waste codes, dates, receiving facility), released 90 days after receipt (search summary); RCRAInfo handler notifications and Biennial Report filings; the generator's own accumulation logs where it supplies them.
**Target:** Per site and month, the probability of each status; dated change points; a mismatch flag against the notified status.
**Evaluation metric:** Precision of mismatch flags confirmed by the generator's records or inspection outcomes, since each flag triggers a review; recall on known status changes in a labelled sample. Calibration matters because shipment timing smears generation across months.
**Scope:** Unit normalisation (kilograms, gallons, cubic yards, containers) and site identity resolution are most of the work. One data scientist and one regulatory specialist, 3–4 months on public data alone, which makes it a natural first product.
**Data availability:** Manifest and RCRAInfo data are public regulatory data. Accumulation logs belong to generators and stay with them.

---

## 4. Inbound Volume, Lab Load and Gate Slot Forecasting at TSDFs
#time-series-forecasting #temporal-fusion-transformers #gradient-boosting #optimization-fundamentals #workflow-orchestration #worker-facing

**Problem statement:** Forecast loads, tons and sampling work arriving at a TSDF by day and hour, by waste category and treatment train, so the facility can set gate appointment slots, staff the receiving lab and plan incinerator feed, and drivers stop waiting hours at the gate.

**ML task:** Multi-horizon hierarchical forecasting of arrivals and sample counts, then slot allocation subject to lab, bay and tank capacity
**Input data:** Approved profiles with scheduled pickups; transporter dispatch plans; historical gate arrivals, sample counts and lab cycle times; tank and storage inventory; incinerator feed plans and outages; calendar and weather.
**Target:** Hourly arrivals and sample counts by category for the next 1–14 days; a slot schedule.
**Evaluation metric:** Weighted absolute percentage error on daily tons by treatment train; for the slot plan, average gate dwell and the share of trucks waiting over two hours, against the current baseline. Under-forecasting the lab load is costlier than over-forecasting, because a short lab strands trucks.
**Scope:** Forecasting is standard; the gain comes from joining dispatch data the TSDF does not always see, especially third-party transporters. One data scientist and one operations engineer, 4 months for a single facility.
**Data availability:** Internal to each TSDF and its in-house transport; third-party transporters' plans need a data-sharing arrangement.

---

## 5. Lab-Pack Container Label Reading and Product Matching
#cnns #object-detection #transformers #large-language-models #worker-facing #automation

**Problem statement:** From a field chemist's phone photos of each container in a stockroom, read the label, identify the product and match it to a safety data sheet, so the drum inventory and manifest lines are drafted as the chemist packs.

**ML task:** Label region detection, text recognition on curved, faded and multilingual labels, then product entity matching against an SDS library, with a proposed hazard class and drum group for confirmation
**Input data:** Container photos; SDS library; historical lab-pack inventories with the chemist's final classifications; manufacturer catalogues.
**Target:** Product identity, size and quantity per container; proposed DOT hazard class and waste codes; an unknown flag when confidence is low.
**Evaluation metric:** Top-1 product match accuracy at the confidence where drafts are shown without warning, and zero tolerance for a confident wrong hazard class, because a misplaced container is a receiving discrepancy and a safety event. Chemist time per container before and after.
**Scope:** Label reading is mature; the long tail of old and hand-labelled stock is not, and unknowns must fall back to the existing procedure. Two engineers, 5 months, trained on the photo archive a lab-pack operator already keeps.
**Data availability:** Operators hold inventories and some photos; SDS libraries are licensed. Labels are produced by the chemist's own confirmations once the tool is in use.
