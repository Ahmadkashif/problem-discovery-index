# Machine Learning Opportunities — Freight Brokerage

**Industry:** [[freight-brokerage|Freight Brokerage]]
**Derived from:** [[problems/freight-brokerage/high-impact|High Impact]], [[problems/freight-brokerage/low-impact-1|Low Impact 1]], [[problems/freight-brokerage/low-impact-2|Low Impact 2]], [[problems/freight-brokerage/worker-life-1|Worker Life 1]], [[problems/freight-brokerage/worker-life-2|Worker Life 2]]

---

## 1. Lane Rate Prediction and Margin Optimization
#gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #time-series-forecasting #bias-variance-tradeoff #entropy-cross-entropy-kl-divergence #gradient-descent #revenue-impact

**Problem statement:** Predict the optimal shipper quote and target carrier buy rate for each load to maximize expected margin while maintaining acceptable win rate.

**ML task:** Regression — optimal all-in shipper rate and target carrier cost from lane and market features
**Input data:** Historical load transactions: origin/destination lane, equipment type, weight, pickup date, shipper rate quoted, carrier rate paid, load won (yes/no). Market data: DAT spot rate for the lane and week, capacity signal (carrier-to-load ratio on DAT), fuel surcharge index, seasonal indicator.
**Target:** Recommended shipper quote with expected win probability at that price; target carrier cost with expected coverage probability; expected margin
**Evaluation metric:** Actual margin vs. model-recommended margin on out-of-sample loads; shipper quote win rate at model-recommended prices vs. historical win rate; margin uplift on loads priced by model vs. broker judgment
**Scope:** Any brokerage with 10,000+ annual loads has training data. Gradient boosting on 10-15 lane + market features: 4-6 week project. The temporal component (rate trends) improves with an ensemble that includes a time-series forecast for the lane. McLeod or Mercury Gate TMS integration. C.H. Robinson and Echo have built this internally; it's now accessible to mid-market brokerages with off-the-shelf ML.
**Data availability:** The broker's own TMS has historical transaction data. DAT provides spot rate API data. FreightWaves SONAR provides granular capacity and demand signal data (subscription required).

---

## 2. Carrier Double-Broker Fraud Detection
#gradient-boosting #logistic-regression #feature-engineering #cross-validation #evaluation-metrics #conditional-probability-and-bayes-theorem #descriptive-statistics #probability-distributions

**Problem statement:** Detect behavioral signals of double-brokering fraud and carrier service failure risk at booking time, before the load is dispatched.

**ML task:** Anomaly detection — carrier booking behavior deviation from established pattern; binary classification (fraud risk: yes/no) from carrier and booking features
**Input data:** Carrier transaction history: load acceptance rate, on-time delivery rate, check-call compliance, rate negotiation pattern (accepting vs. pushing back, accepting then backing out), MC authority age vs. equipment profile, GPS tracking compliance. Labeled fraud incidents from the broker's own cargo claim history.
**Target:** Fraud risk score per carrier per booking; specific red flag indicators; recommended action (proceed / increase monitoring / decline)
**Evaluation metric:** Recall on bookings that resulted in double-broker fraud or load abandonment; false positive rate on legitimate carriers; cargo claim reduction for loads using fraud screening
**Scope:** Isolation forest for anomaly detection on carrier behavior signals + gradient boosting on labeled fraud incidents: 4-6 week project. Training signal requires cargo claim records with carrier identification. Industry-shared carrier fraud data (FMCSA watch list, load board fraud flags) supplements the broker's own incident history.
**Data availability:** Broker's TMS has per-carrier transaction history. FMCSA SAFER has regulatory actions and authority history. DAT and Truckstop have carrier fraud flagging systems that provide partial labels. Cargo claim records are in the broker's claims management system.

---

## 3. Shipper Demand Forecasting by Lane
#lstms-and-grus #time-series-forecasting #gradient-boosting #autoregressive-models #feature-engineering #cross-validation #evaluation-metrics #backpropagation #revenue-impact

**Problem statement:** Forecast per-shipper, per-lane weekly load volume 4-8 weeks ahead to enable proactive capacity pre-procurement before market tightening.

**ML task:** Time-series forecasting — weekly load volume per shipper-lane pair; confidence interval for capacity pre-commitment planning
**Input data:** Historical shipper tender data from TMS by lane and week. External signals: retail sales indices (Census Bureau), agricultural USDA reports for produce lanes, fuel price trend, holiday and seasonal calendars.
**Target:** Weekly volume forecast per shipper per lane for next 4-8 weeks; high-confidence vs. uncertain periods; recommended capacity pre-commitment quantity per week
**Evaluation metric:** Forecast MAPE (mean absolute percentage error) on held-out weeks; revenue from pre-committed capacity at below-peak rates vs. spot-purchased capacity; carrier capacity availability for pre-committed loads
**Scope:** LSTM or Prophet model for per-shipper lane time series: 6-8 week project. External signal integration (retail, agricultural) adds predictive value. TMS transaction data is the primary training input.
**Data availability:** TMS contains shipper tender history by lane and week. USDA agricultural reports are public. Census Bureau retail sales data is public. Fuel price indices are public.

---

## 4. Carrier Capacity Matching for Lane Coverage
#gradient-boosting #logistic-regression #feature-engineering #cross-validation #evaluation-metrics #conditional-probability-and-bayes-theorem #quick-win

**Problem statement:** Rank carrier outreach candidates for a specific load by their predicted probability of accepting at the target buy rate, enabling the system to contact the most likely carriers first.

**ML task:** Ranking — carrier ordered by acceptance probability given load details and current carrier state
**Input data:** Historical carrier outreach records: carrier contacted for load → accepted/declined. Features: carrier's lane history, current known capacity (recently declined vs. accepted on nearby lanes), day-of-week and equipment type match, rate offered vs. carrier's historical rate for this lane.
**Target:** Ranked carrier outreach list per load; predicted acceptance probability per carrier; recommended rate per carrier based on their historical rate sensitivity
**Evaluation metric:** Coverage speed improvement (time to accepted load with ranked vs. random outreach order); number of outreach attempts per covered load; carrier acceptance rate at first vs. subsequent contact
**Scope:** Quick win — any TMS with outreach logging has the training data. Gradient boosting on carrier + load features: 3-4 week project. Parade and Newtrul have built versions of this; the broker's own transaction history with specific carriers is the proprietary differentiator.
**Data availability:** TMS carrier outreach logs. Carrier profile data (lane preferences, equipment type, historical rates) from transaction history. DAT carrier data provides supplemental signal.

---

## 5. Late Shipment Early Warning
#gradient-boosting #logistic-regression #feature-engineering #cross-validation #evaluation-metrics #time-series-forecasting #quick-win

**Problem statement:** Predict which in-transit shipments are at risk of missing their delivery appointment before the driver's ETA becomes critical, enabling proactive shipper communication and contingency planning.

**ML task:** Binary classification (will miss delivery appointment: yes/no) from current shipment state features
**Input data:** Real-time shipment tracking data: current location, remaining miles, available driver hours (ELD), historical transit time for this lane and carrier, weather data on route, traffic forecast
**Target:** Late probability score per in-transit shipment; ETA range with confidence; alert threshold for broker notification
**Evaluation metric:** Recall on shipments that missed their delivery appointment; false positive rate (alerts that turned out on-time); lead time between first warning and actual late delivery
**Scope:** Quick win — ELD data provides the real-time position and HOS (hours of service) remaining. Weather and traffic APIs are standard integrations. Gradient boosting or logistic regression on transit features: 2-3 week project. TMS integration with ELD APIs is the technical work.
**Data availability:** ELD providers (Samsara, Motive, KeepTruckin) provide real-time GPS and HOS data via API. Historical transit times are in the TMS. Weather and traffic APIs are commodity.
