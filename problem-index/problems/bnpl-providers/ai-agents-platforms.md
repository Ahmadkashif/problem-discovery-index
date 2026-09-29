# AI Agents & Platform Opportunities — BNPL Providers

**Industry:** [[bnpl-providers|BNPL Providers]]

---

## 1. Consumer Capacity Platform
#ai-platform #gradient-boosting #survival-analysis #causal-inference #confidence-intervals #evaluation-metrics #compliance #revenue-impact

**Concept:** A platform that underwrites the consumer rather than the plan. It treats connected bank cashflow as the primary signal — income timing, recurring obligations, balance troughs, overdraft history — and reads competitors' instalment auto-debits directly out of the descriptor stream, which is the only way any single provider can see accumulation without waiting for the sector to agree on shared furnishing. It reports a two-sided outcome: loss rate at a given approval rate, and the rate at which approved plans were serviced through an overdraft or a further plan. A provider that improves the first while worsening the second has not improved, and no current system can tell it so.

**Inputs:** Connected account transaction feeds; descriptor patterns for competing providers; bureau and alternative file data; device and behavioural signals; internal plan, repayment and re-borrowing history; merchant and basket context; overdraft events observed in connected accounts.

**Outputs / Actions:** Approval decisions with an explicit capacity estimate and an inferred concurrent-obligation count. Two-metric performance reporting. Connection-prompt experiments measuring the conversion cost of asking for a bank link against the loss and harm it prevents. Portfolio-level accumulation exposure, which no provider currently reports to its own board.

**Why now:** The sector built one of the largest thin-file repayment datasets in existence in under a decade and has used it to score its next approval. The accumulation question will be answered by a regulator with worse data if it is not answered internally first, and cashflow-primary underwriting is available to any single provider unilaterally.

**Market:** BNPL providers, instalment lenders, thin-file consumer lenders and the cashflow-data vendors serving them. The commercial argument is loss reduction; the durable argument is that the harm metric is the one that will eventually be asked for.

---

## 2. Collections Treatment Agent
#ai-agent #gradient-boosting #survival-analysis #bert #large-language-models #causal-inference #worker-facing #compliance

**Concept:** An agent that tells a collections agent what situation they are in before the call. It builds a distress signal from decline patterns, balance and payroll timing where an account is connected, competing instalment debits, and the consumer's own words, and separates a temporary shortfall from a structural one. It selects retry timing against observed payroll cycles instead of a fixed schedule, and refuses to retry into a balance it can see is negative. It recommends a treatment — retry, plan, hardship, hold — with the measured outcomes of that treatment on similar consumers attached, and it surfaces hardship candidates before they call, since the consumers most at risk are the least likely to.

**Inputs:** Retry and decline histories; connected balances and income timing; competitor debit patterns; message text and responsiveness; plan and purchase history; prior arrangements and whether they held; recovery and re-delinquency outcomes.

**Outputs / Actions:** A capacity state per delinquent consumer. Payroll-aligned retry scheduling with an overdraft guardrail. Treatment recommendations with outcome distributions rather than a script. Proactive hardship offers. Outcome feedback returned to the individual agent on arrangements they set up, which is the only closure the role currently offers.

**Why now:** The signals that distinguish temporary from structural difficulty are present in data the provider already holds, and the current alternative is an agent guessing under a recovery target. Retrying into an empty account generates an overdraft fee larger than the instalment, which is the provider actively worsening the situation it is trying to resolve, and it is a scheduling default rather than a decision anyone made.

**Market:** BNPL providers, instalment and small-dollar lenders, and collections platforms. The efficiency case and the consumer-outcome case point the same direction here, which is unusual in collections and is worth stating plainly to a buyer.

---

## 3. Merchant Dispute and Placement Agent
#ai-agent #bert #large-language-models #k-nearest-neighbors #gradient-boosting #evaluation-metrics #workflow-orchestration #revenue-impact

**Concept:** An agent covering both sides of the merchant relationship. On disputes it classifies the consumer's claim from their own message, assembles tracking, delivery scans, return windows, merchant policy and prior interactions into one view, names the evidentiary gap, and retrieves similar prior cases with their decisions and what happened afterwards. It surfaces merchant-level patterns — a tripling of non-delivery claims tied to a carrier change is a merchant problem, not three hundred consumer problems. On placement it fetches the merchant's own storefront across devices, verifies that the offer renders where it should and not on ineligible baskets, and runs randomised exposure holdouts so the provider's incrementality claim is a measurement rather than an assertion.

**Inputs:** Consumer claim text; order, tracking and delivery records; merchant return policies and processing latency; refund files; historical dispute decisions and their aftermath; storefront pages across device types; session exposure and conversion data.

**Outputs / Actions:** Pre-assembled dispute cases with evidence gaps named and precedent attached. Merchant-level claim anomaly alerts. Decision consistency monitoring, including whether outcomes on identical fact patterns vary with merchant size — a number the organisation should hold rather than leave to individual conscience. Verified placement reports. Holdout-measured incrementality per merchant.

**Why now:** Disputes are the point where the provider's two customers collide and are currently resolved case by case under unstated commercial pressure, while the merchant conversation turns on a revenue claim that sophisticated merchants already discount. Both problems are evidentiary, and the evidence is available.

**Market:** BNPL providers, marketplaces and payment platforms carrying merchant disputes. The dispute half sells on cost and consistency; the placement half sells on winning rate negotiations with a number that survives the merchant's own analytics team.
