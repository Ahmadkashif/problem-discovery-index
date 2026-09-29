# Machine Learning Opportunities — Virtual Economy Operators

**Industry:** [[virtual-economy-operators|Virtual Economy Operators]]
**Derived from:** [[problems/virtual-economy-operators/high-impact|High Impact]], [[problems/virtual-economy-operators/low-impact-1|Low Impact 1]], [[problems/virtual-economy-operators/low-impact-2|Low Impact 2]], [[problems/virtual-economy-operators/worker-life-1|Worker Life 1]], [[problems/virtual-economy-operators/worker-life-2|Worker Life 2]]

---

## 1. Supply Policy Price Impact Forecasting
#monte-carlo-methods #time-series-forecasting #markov-chains #bayesian-inference #confidence-intervals #causal-inference #evaluation-metrics #revenue-impact

**Problem statement:** Drop rates, limited releases, sinks and rarity changes are money supply decisions made by designers on engagement grounds, with no forecast of the effect on prices that players pay real money at — and in several large economies without even looking at the secondary market where most trading happens.

**ML task:** Forecast the price response of circulating items to proposed supply changes, treating the item economy as an asset market rather than an inventory system
**Input data:** Circulating supply per item with issuance and sink rates; complete trade history with prices and volumes, including third-party venues where observable; holder concentration; item utility and its changes through balance patches; historical supply events and the price paths that followed.
**Target:** Price path of affected items over the following weeks and months.
**Evaluation metric:** Backtest against the operator's own history of supply events — project forward from before each and compare. The bar should be stated honestly: this need not be precise, it needs to reliably distinguish a change that will halve a widely-held item's value from one that will not, which is the decision it exists to inform. Report interval width, and treat the speculative component explicitly, since a substantial share of holdings are held for resale and behave differently from used inventory.
**Scope:** This is closer to asset pricing than to inventory planning and game economy teams are not staffed for it. The critical product decision is where the output goes: a forecast in a design review, attached to the supply proposal, is what prevents the incident class; a report published afterwards changes nothing. Third-party venue coverage is essential in the economies where most trading happens off the operator's marketplace. 2-3 ML engineers plus an economist, 9-12 months.
**Data availability:** First-party trade data is complete. Third-party venue data requires scraping or partnership and is the gap that matters most in several of the largest economies.

---

## 2. Relational Manipulation Detection in Thin Markets
#graph-neural-networks #dbscan #change-point-detection #k-means-clustering #gradient-boosting #confidence-intervals #evaluation-metrics #compliance

**Problem statement:** Wash trading, cornering, ramping and spoofed listings all appear in markets with real value, and detection is inherited from payment fraud — rules on velocity and account age that catch stolen-card abuse and miss manipulation entirely, because manipulation uses legitimate accounts and legitimate funds.

**ML task:** Detect coordinated trading from structure in the trade graph, with per-item baselines conditioned on liquidity
**Input data:** The full trade graph with account, item, price, timing and venue; funding sources and device characteristics where observable; item liquidity, trade counts and order book depth; listing and cancellation behaviour; confirmed manipulation cases as labels where they exist.
**Target:** Coordinated manipulation as confirmed by investigation, supplemented by unsupervised structure where labels are scarce.
**Evaluation metric:** Precision at the enforcement threshold, because an account restriction based on a false positive removes someone's property and their appeal route is a support ticket. The specific discrimination to measure is wash trading versus genuine repeat trading between acquainted players, which is common and benign. Liquidity conditioning must be validated separately: a detector calibrated on aggregate behaviour will either flood analysts with false positives on thin items or miss manipulation in liquid ones, and reporting a single performance number will hide both.
**Scope:** The relational structure is what rules cannot replicate. Cross-venue coverage is the largest gap — an operator surveilling only its own marketplace sees a minority of activity in several big economies and none of the cross-venue arbitrage schemes. A separate and much cheaper intervention: displaying liquidity and trade count alongside price, so a population that includes many young inexperienced traders can interpret a chart that currently invites misreading. 2 ML engineers, 6-9 months.
**Data availability:** First-party complete, third-party partial, confirmed labels scarce.

---

## 3. Theft Chain Detection and Value Transfer Patterns
#graph-neural-networks #gradient-boosting #dbscan #change-point-detection #k-nearest-neighbors #confidence-intervals #compliance #evaluation-metrics

**Problem statement:** A compromised inventory moves through intermediaries and is sold within minutes, after which recovery would require taking items from innocent buyers — so interruption before the final sale is the only point at which the outcome can change. Separately, item trades are a documented route for moving value, sitting between terms of service and unsettled financial regulation.

**ML task:** Recognise theft chains in progress from their structure in the trade graph, and identify flow patterns consistent with value transfer
**Input data:** Trade graph with timing, value and account relationships; session, device and location signals around account access; account history and gameplay relationship between trading parties; confirmed theft cases with their full chains; marketplace listing and sale events.
**Target:** Whether a trade sequence is part of a theft chain — labelled in hindsight from confirmed cases — and whether a flow pattern is consistent with value transfer rather than gameplay.
**Evaluation metric:** Detection latency measured from the initial compromise, because value is entirely determined by whether interruption occurs before the final sale — accuracy measured without a time dimension would miss the point completely. For risk-conditioned holds, the operative comparison is protection delivered against friction imposed, against the current fixed-delay approach which inconveniences everyone equally. For value transfer, the output is a measured pattern prevalence, not an accusation, and should be framed as the operator knowing its own exposure.
**Scope:** Risk-conditioned holds replacing fixed cooldowns are the practical application and require the graph model. On value transfer, the regulatory framing of virtual items is genuinely unsettled in most jurisdictions, which is an argument for having the measurement rather than against it. 2 ML engineers plus a financial crime specialist, 6-9 months.
**Data availability:** Complete within the operator. Confirmed theft chains exist in support records and are the label set.

---

## 4. Creator Income Decomposition and Forecasting
#time-series-forecasting #causal-inference #gradient-boosting #confidence-intervals #survival-analysis #evaluation-metrics #worker-facing #revenue-impact

**Problem statement:** Creator income inside a platform economy depends on engagement, ranking distribution, pool size, pool division, exchange rate and seasonality — all computable by the platform and none reported, so a creator whose income halved sees only a number that moved.

**ML task:** Decompose creator income movements into their causes and forecast forward income with uncertainty
**Input data:** Creator engagement and traffic by source; ranking and distribution changes with their timing; pool size and division mechanics; exchange rate and fee history; the creator's own content release history; seasonality and platform-wide trends.
**Target:** The attribution of an income change to each component, and the distribution of income over the following quarter.
**Evaluation metric:** Decomposition is validated by reconstruction — the components must sum to the observed movement, with a residual reported honestly rather than allocated. For forecasting, interval calibration, since the use case is a creator deciding whether they can afford to hire and an overconfident forecast is worse than a wide one. The measure that matters operationally is whether creators can distinguish a ranking change from their own performance, which is the question the current opacity makes unanswerable.
**Scope:** The modelling is straightforward; the obstacle is that publishing the decomposition means disclosing ranking and pool mechanics the platform currently keeps opaque. The largest items here — published exchange rate mechanics, advance notice of changes, honest earnings distributions rather than the top of them — are policy decisions with a model in a supporting role, and it is worth saying so rather than engineering around them. 1-2 ML engineers, 4-6 months.
**Data availability:** Complete on the platform side and invisible on the creator side, which is the entire problem.
