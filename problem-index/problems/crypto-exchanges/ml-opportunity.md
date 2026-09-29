# Machine Learning Opportunities — Crypto Exchanges

**Industry:** [[crypto-exchanges|Crypto Exchanges]]
**Derived from:** [[problems/crypto-exchanges/high-impact|High Impact]], [[problems/crypto-exchanges/low-impact-1|Low Impact 1]], [[problems/crypto-exchanges/low-impact-2|Low Impact 2]], [[problems/crypto-exchanges/worker-life-1|Worker Life 1]], [[problems/crypto-exchanges/worker-life-2|Worker Life 2]]

---

## 1. Screening Precision Estimation Under Scarce Ground Truth
#graph-neural-networks #graph-theory #gradient-boosting #causal-inference #confidence-intervals #hypothesis-testing #evaluation-metrics #compliance

**Problem statement:** Exchanges freeze deposits on a vendor's address risk score and almost never learn whether the funds were criminal. The control has run for years at real cost to customers and analysts without a precision estimate in either direction, and the propagation model that decides how far taint travels is chosen by the vendor rather than by the exchange.

**ML task:** Precision and recall estimation for existing screening thresholds against a small confirmed-outcome set, with sensitivity analysis across taint propagation models
**Input data:** Every screening decision with the vendor score, the direct and indirect exposure breakdown, and the hop distance at which exposure was found; analyst dispositions; source-of-funds documentation and whether it was verified or merely accepted; law enforcement confirmations and subpoena correlations; subsequent customer behaviour; cases where the same customer was later confirmed in either direction.
**Target:** The estimated proportion of flagged deposits that represented actual illicit proceeds, at each threshold and under each propagation rule.
**Evaluation metric:** This is an estimation problem with a tiny, non-random label set, so the deliverable is an interval with the selection bias stated, not a point estimate. Cases resolve disproportionately when a customer had the resources to contest, which biases the confirmed set toward legitimate funds; the honest presentation reports the estimate under explicit assumptions about the unresolved majority rather than quietly conditioning on resolution.
**Scope:** The first deliverable is a curated outcome register treating the few genuinely confirmed cases as the scarce asset they are — most exchanges hold these scattered across legal, compliance and support systems and have never assembled them. Comparing vendors on the exchange's own population, and measuring what fraction of flag volume comes from indirect exposure at three or more hops versus direct exposure, are both immediately available and usually reframe the internal conversation on their own. Re-running screening under proportional, poison and haircut propagation on historical data shows how much of the flagged population is an artefact of a modelling choice nobody made deliberately. 2 ML engineers and 1 analyst, 6 months.
**Data availability:** Screening decisions and dispositions are complete internally. Confirmed outcomes are scarce, scattered and the entire point of the exercise. Vendor internals are proprietary, which is why measurement must be black-box.

---

## 2. Automated Fund Tracing and Typology Classification
#graph-neural-networks #graph-theory #k-means-clustering #large-language-models #bert #evaluation-metrics #worker-facing #compliance

**Problem statement:** Analysts trace funds backwards through a public ledger hop by hop in a vendor interface, deciding manually which branches matter, then write formulaic suspicious activity narratives by hand. The underlying patterns repeat in a few dozen recognisable typologies.

**ML task:** Ranked path discovery to known entities over the transaction graph, motif classification into laundering typologies, and narrative generation from structured trace evidence
**Input data:** Full chain transaction graphs; vendor entity attributions and cluster assignments; the exchange's own address-to-identity knowledge at deposit and withdrawal points; historical investigations with their traced paths, typology conclusions and filed narratives; sanctions lists.
**Target:** Ranked candidate paths from the deposit address to attributed entities; a named typology; and a drafted narrative.
**Evaluation metric:** For path discovery, agreement with the paths experienced analysts actually chose on historical cases, plus time to reach the same conclusion. For typology classification, accuracy against analyst labels with abstention permitted — an unnamed pattern is a correct output, and a confidently wrong typology sends an investigation in the wrong direction. Narrative quality is judged by analyst edit distance and by whether a compliance reviewer accepts the draft.
**Scope:** Narrative generation is the largest immediate time saving and the least contentious, because the facts are already structured by the time drafting begins. Path ranking is the intellectually interesting half and must remain explorable — the analyst has to be able to disagree and expand manually. An internal case corpus with retrieval over prior investigations is the part that stops the institution losing what its investigators learn, and needs no modelling beyond embedding and search. 3 ML engineers, 7 months.
**Data availability:** Chain data is public and complete. Historical investigations are retained for regulatory reasons. The identity join at deposit and withdrawal is the exchange's unique asset and is subject to serious privacy constraints on how it may be used and retained.

---

## 3. Listing Risk Analysis and Wash Trading Detection
#graph-neural-networks #graph-theory #large-language-models #bert #gradient-boosting #evaluation-metrics #feature-engineering #compliance

**Problem statement:** Listing an asset requires assessing contract risk, supply distribution, unlock schedules, team history, legal characterisation and whether observed volume is genuine. The work is manual, redone at every exchange for every asset, and never graded against what happened to past listings.

**ML task:** Contract risk pattern detection from bytecode, holder and unlock analysis from chain state, and graph-based wash trading detection over trade and transfer flows
**Input data:** Contract bytecode and source where verified; token holder distributions and vesting contract state; transfer and trade graphs across venues; project documentation and social presence; the exchange's own listing decisions joined to subsequent outcomes — collapses, exploits, delistings, enforcement actions.
**Target:** A structured risk profile per asset, a wash trading likelihood for reported volume, and a graded assessment of the listing framework itself.
**Evaluation metric:** Contract pattern detection is largely deterministic and measured on recall of known dangerous constructs — mint authority, upgradeable proxy, blacklist function, fee-on-transfer. Wash trading detection should be measured on the subset where ground truth exists through enforcement actions and venue admissions, with the understanding that this subset is small; precision at a review threshold matters more than recall, since the output accuses a market participant. The framework grading uses the exchange's own listing history as labels.
**Scope:** Holder concentration and unlock scheduling are computable exactly from chain state and should replace reliance on projects' self-published schedules, which is the weakest current input. Wash trading detection on flow graphs is where the real money sits, since reported volume from other venues drives listing and market-making decisions. Continuous post-listing monitoring is the structural gap: the decision is a snapshot and the risks are dynamic. 2 ML engineers, 6 months.
**Data availability:** Chain and contract data are public. Cross-venue trade data is partially public and partially purchased. The exchange's own listing outcomes are internal and unexploited.

---

## 4. On-Chain Transaction Classification for Basis Reporting
#gradient-boosting #k-nearest-neighbors #graph-theory #bert #evaluation-metrics #feature-engineering #data-integration #compliance

**Problem statement:** Under the 1099-DA regime the exchange must report gains on assets that arrived from elsewhere with no basis attached. Determining what a customer's intermediate on-chain activity actually was — swap, liquidity provision, bridge, reward claim, wrap — requires decoding contract calls against a protocol taxonomy that changes monthly, and matching withdrawal legs to later deposit legs to carry basis is unautomated.

**ML task:** Classification of on-chain interactions into tax-relevant event types, plus graph matching of transfer legs across exchanges and wallets
**Input data:** Contract call data and event logs; protocol ABIs and known contract registries; historical labelled interactions; withdrawal and deposit records with addresses, amounts and timing; price history per asset; the exchange's own trade and transfer records.
**Target:** A tax event type per on-chain interaction, and a matched basis chain per disposed lot.
**Evaluation metric:** Classification accuracy per event type against a labelled sample, with abstention strongly preferred over a guess — an unclassified interaction becomes a flagged item for the customer, while a misclassified one becomes a wrong number on a tax form. For transfer matching, precision is decisive: attaching the wrong basis to a lot produces a confidently incorrect filing, which is worse than reporting basis as unknown.
**Scope:** The highest-value and least attempted piece is honest uncertainty. Where basis is genuinely unknown, a range with a stated method is the correct output and a zero is a confident assertion that the customer owes tax on the full proceeds. Transfer leg matching is mechanical graph work on data the exchange holds and is what the transfer statement regime is trying to achieve institutionally. Predicting which customers will receive a materially wrong form before the forms go out is a small addition with a large support effect. 2 ML engineers, 5 months.
**Data availability:** Chain data is public; the exchange's own records are complete. The protocol taxonomy requires continuous maintenance and lags new protocols, which is the durable difficulty rather than a one-time cost.
