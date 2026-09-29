# Machine Learning Opportunities — Freight Tech Platforms

**Industry:** [[freight-tech-platforms|Freight Tech Platforms]]
**Derived from:** [[problems/freight-tech-platforms/high-impact|High Impact]], [[problems/freight-tech-platforms/low-impact-1|Low Impact 1]], [[problems/freight-tech-platforms/low-impact-2|Low Impact 2]], [[problems/freight-tech-platforms/worker-life-1|Worker Life 1]], [[problems/freight-tech-platforms/worker-life-2|Worker Life 2]]

---

## 1. Carrier Identity Graph and Fraud Detection
#graph-neural-networks #gradient-boosting #dbscan #change-point-detection #feature-engineering #evaluation-metrics #confidence-intervals #compliance

**Problem statement:** Brokers cannot reliably establish who is hauling a load. Double brokering and authority takeover defeat document-based vetting because the documents belong to real carriers. The fraud is visible in relationships — shared phone numbers, addresses and remittance accounts across supposedly unrelated authorities, and sudden attribute changes on established identities — and invisible in any single carrier's record.

**ML task:** Graph construction and node classification over a heterogeneous entity graph, combined with change point detection on identity attributes
**Input data:** Carrier authority records and their history; contact attributes (phone, email domain, address) and their change history; remittance and factoring details; insurance certificates and issuers; booking behaviour (lanes, rates, equipment, timing) across the platform's broker base; confirmed fraud and chargeback events; equipment identifiers where captured.
**Target:** A fraud or re-brokering event associated with a booking, with the specific carrier identity implicated.
**Evaluation metric:** Precision at the review threshold is the binding constraint, because the consequence of a false positive falls on a small legitimate business and carries defamation exposure. Report precision@k for a realistic analyst review capacity, plus lead time — how many days before the loss the signal was available. Detection recall on held-out confirmed fraud is the secondary measure.
**Scope:** Graph construction is most of the work: entity resolution across authority records, contact attributes and payment details, with the deliberate obfuscation that fraudsters apply. Attribute change detection on established identities is the highest-value single feature and requires no graph learning at all — it should ship first. Cross-broker data pooling raises real antitrust and defamation questions that must be designed around, most cleanly by outputting risk signals with evidence rather than shared negative assessments of named businesses. 3-4 ML engineers plus fraud investigators and counsel, 8-10 months.
**Data availability:** Public authority and insurance data is thin, slow and reflects registration rather than operational control. The valuable data is the platform's own interaction history, which is complete but siloed per broker. Confirmed fraud labels are scarce, late and under-reported, so semi-supervised and anomaly-based approaches carry most of the early weight.

---

## 2. Lane-Level Transit Time and Arrival Forecasting
#time-series-forecasting #gradient-boosting #survival-analysis #feature-engineering #confidence-intervals #evaluation-metrics #recurrent-forecasting

**Problem statement:** Appointments are committed days ahead as though transit time were deterministic. It is a distribution, and treating it as a point estimate produces missed windows, detention charges and disputes. Visibility platforms collect the position data that would characterise the distribution and report current ETA rather than modelling it.

**ML task:** Probabilistic arrival time forecasting, updated continuously in transit, with a pre-booking transit time distribution per lane
**Input data:** Historical GPS and ELD position traces by lane; hours-of-service state; dwell times at origin and destination facilities by facility and time of day; weather; traffic; day of week and seasonality; carrier and equipment type; facility-specific historical detention patterns.
**Target:** Actual arrival timestamp at each stop, and dwell duration at the facility.
**Evaluation metric:** Pinball loss across quantiles, because the operational question is what window can be committed to with a stated confidence, not a mean ETA. Report calibration separately for the tail — late arrivals are the only ones that cost anything, and average error is dominated by the ordinary cases.
**Scope:** Facility dwell is the most variable and least modelled component and frequently exceeds the variance in road transit. It is highly facility-specific and estimable from the platform's own arrival and departure traces across all carriers serving that facility, which is a genuinely proprietary asset. 2-3 ML engineers, 5-6 months.
**Data availability:** Excellent for carriers with telematics integration and absent for small carriers, which creates a coverage bias — the lanes served by small carriers are exactly the ones with the least data and the most variance. Facility identification from coordinates requires a geofence layer that must be built and maintained.

---

## 3. Carrier Acceptance Probability at a Given Rate
#logistic-regression #gradient-boosting #k-nearest-neighbors #feature-engineering #cross-validation #evaluation-metrics #confidence-intervals #revenue-impact

**Problem statement:** Covering a load is a search performed by cold calling, with a low hit rate, under time pressure. The brokerage's own history holds which carriers run which lanes at which rates and who accepted what recently, and it is used to populate a screen the rep scrolls past.

**ML task:** Binary classification of offer acceptance conditional on carrier, load and offered rate, producing a rate-response curve per carrier and lane
**Input data:** Historical offers with carrier, lane, equipment, commodity, pickup timing, offered rate, and accepted or declined outcome; carrier's recent lane activity and likely equipment position; market rate indices; seasonality; time remaining before pickup; carrier size and historical rate behaviour.
**Target:** Offer acceptance, and secondarily whether the accepted load was serviced without failure.
**Evaluation metric:** Calibration across the rate range is the whole point, since the model is used to choose a rate. Business metrics are loads covered per rep-hour and margin retained; report both against the rep's actual outcomes, and monitor for the failure mode where the model raises coverage by systematically recommending higher rates.
**Scope:** Declined offers are frequently not recorded — a rep calls, gets a no, and moves on — which removes the negative class. Instrumenting decline capture is a prerequisite product change and is where most of the effort will go. Time pressure matters: acceptance probability rises as pickup approaches and rate expectations move with it, so the model must be conditioned on time remaining. 2 ML engineers, 4-5 months.
**Data availability:** Booked loads are complete; offers and declines are not. Carrier equipment position is inferable from prior deliveries and is far better than nothing but is not a live truck location for most small carriers.

---

## 4. Accessorial Term Extraction from Transportation Agreements
#large-language-models #bert #transformers #word-embeddings #transfer-learning #evaluation-metrics #compliance #revenue-impact

**Problem statement:** Whether a detention or lumper charge gets paid depends on shipper-specific evidence and notification rules written in a master transportation agreement. Nothing extracts those terms, so billing clerks apply them from memory, charges are abandoned pre-emptively, and denials arrive weeks later with uninformative codes.

**ML task:** Clause extraction and structuring from contract text — identifying each accessorial type with its trigger conditions, free time, rate, evidence requirement and notification window
**Input data:** Master transportation agreements and their amendments; historical accessorial charges with submitted evidence and paid, short-paid or denied outcomes; denial reason codes; the platform's cross-customer billing history by shipper.
**Target:** A structured accessorial rule set per shipper contract; and separately, the payment outcome per submitted charge.
**Evaluation metric:** Field-level extraction accuracy against attorney-reviewed contracts, with free-time thresholds and notification windows weighted most heavily since those determine whether a charge is viable. For the outcome model, calibration of predicted payment probability, which is what makes the pursue-or-abandon decision.
**Scope:** Transportation agreements are reasonably standardised in structure and highly variable in terms, which suits retrieval-augmented extraction with clause-level review. The denial analysis needs no extraction at all and delivers value immediately — which shippers deny which charges at what rate is a query, not a model. 2 ML engineers plus a transportation attorney, 4-5 months.
**Data availability:** Contracts are held by the brokerage but stored as documents in shared drives rather than as a corpus. Charge and denial history is complete in the billing system. Evidence documents are captured but rarely linked to the specific charge they support, which is a data model gap.
