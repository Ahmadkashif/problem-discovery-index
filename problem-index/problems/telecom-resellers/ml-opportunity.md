# Machine Learning Opportunities — Telecom Resellers

**Industry:** [[telecom-resellers|Telecom Resellers]]
**Derived from:** [[problems/telecom-resellers/high-impact|High Impact]], [[problems/telecom-resellers/low-impact-1|Low Impact 1]], [[problems/telecom-resellers/low-impact-2|Low Impact 2]], [[problems/telecom-resellers/worker-life-1|Worker Life 1]], [[problems/telecom-resellers/worker-life-2|Worker Life 2]]

---

## 1. Learning the Onboarding Engineer's Read of a Bad Account
#tacit-knowledge-ml #gradient-boosting #survival-analysis #graph-theory #feature-engineering #evaluation-metrics #compliance

**Problem statement:** Experienced onboarding and NOC staff at SIP-trunk and wholesale voice providers can tell from a sign-up and a first day of traffic that an account will turn into an illegal robocall source, a judgement they can't specify. The ML problem is to learn that read from their recorded decisions and later outcomes, score every new account before its first call, and update the score as traffic arrives.

**ML task:** Binary risk classification at sign-up plus time-to-event modelling of "account produces a traceback, carrier abuse notice or abuse termination" over the first 90 days, with graph features over shared identifiers
**Input data:** Onboarding records (business registration, domain age, payment instrument, stated use, requested calls per second, requested caller IDs and proof of ownership); reviewer decisions, limits set and confidence; daily traffic statistics per account (call attempts, answer-seizure ratio, average duration, share of calls under 6 seconds, caller-ID churn, sequential dialling, destination spread); complaints, carrier notices, ITG traceback requests and termination reasons; a graph linking accounts by contacts, IPs, payment instruments and upstream carriers.
**Target:** Adjudicated bad-actor label per account and time to first adverse event, plus agreement with the reviewer's own decision.
**Evaluation metric:** Recall of eventual bad accounts at a fixed review budget (for example, the riskiest 10% of new accounts) and time-dependent concordance for the hazard model, measured strictly forward in time by signup cohort. Missing a bad account risks the provider's RMD certification, and declining a good one costs one customer, so recall outweighs precision at sign-up. Precision matters for the traffic-stage alerts, which interrupt live revenue. Report model-reviewer agreement against each reviewer's own consistency on re-reviewed cases as the ceiling.
**Scope:** The data collection challenge is first and hardest: reviewers decide in their heads and in chat, so the system needs a near-zero-effort capture surface (a structured decision with a drafted reason, confirmed in a click) and must backfill history from tickets and softswitch logs. The labelling challenge is that tracebacks are sparse, late and name the provider rather than the account, while many bad accounts are terminated quietly and some terminated accounts were legitimate. Labels need adjudication by two reviewers on a sample, and reviewer self-consistency must be measured, because the same person grades borderline lead-generation traffic differently after a recent traceback. The deployment challenge is speed: the sign-up score must return in seconds or sales routes around it, and traffic alerts must fire within the first hour of a campaign. 2 ML engineers and a compliance lead at a provider with thousands of accounts, 6–9 months. Value appears first as a ledger and look-alike retrieval ("this account shares a payment card with two terminated accounts") before any score is trusted to gate activation.
**Data availability:** Traffic statistics and onboarding records sit in the provider's softswitch, billing and CRM. Reviewer reasoning mostly doesn't exist and has to be captured going forward. Traceback requests are held by each provider. Pooling across providers would help most and is constrained by CPNI rules and competition.

---

## 2. Port Order Pre-Validation and Rejection Prediction
#large-language-models #transformers #logistic-regression #feature-engineering #evaluation-metrics #worker-facing #automation

**Problem statement:** Predict before submission whether a number port order will be rejected by the losing carrier, and why, by comparing the letter of authorisation and bill with the customer service record under that carrier's known rules.

**ML task:** Document extraction and field matching, then multi-label classification of rejection reasons with a calibrated rejection probability
**Input data:** LOAs, bills and CSRs as PDFs and images; order fields; losing carrier and number type; historical orders with outcomes, rejection codes and free-text remarks; carrier-specific formatting rules learned from past rejections.
**Target:** Rejected or accepted on first submission; the rejection reason set (name, address, authorised contact, missing numbers, billing-number conflict, pending order, PIN or account number).
**Evaluation metric:** Precision and recall per rejection reason, and the first-submission acceptance rate after the tool's fixes against a held-out period before it. A missed rejection costs weeks of the customer's time and a false flag costs a specialist a minute, so recall matters more.
**Scope:** Extraction from carrier bills and CSRs is the hard tail, with hundreds of carrier formats. Rejection remarks are terse codes plus free text and need normalising. 1 ML engineer and a porting lead, 4 months to a pre-submission checker for the top carriers by volume.
**Data availability:** Every provider holds its own order history with outcomes in a ticketing system or carrier portal exports. Labels are free; only the free-text remarks need cleaning.

---

## 3. Call-Quality Fault Localisation From SIP and RTCP
#random-forests #lstms-and-grus #feature-engineering #evaluation-metrics #worker-facing #automation

**Problem statement:** Given a reported bad call, classify the fault domain (customer premises, provider platform, underlying carrier) and the specific pattern, from the call's signalling ladder and media statistics.

**ML task:** Multi-class classification over engineered features from SIP message sequences and RTCP quality reports, with a sequence model over the ordered message ladder as a comparison
**Input data:** SIP traces from session border controllers (methods, response codes, headers, SDP offers and answers, timers); RTCP and quality metrics (jitter, loss, round-trip time, MOS estimates); call detail records; endpoint and firewall make where known; the underlying carrier and route.
**Target:** Fault domain and pattern label (NAT one-way audio, header rewriting by a firewall SIP helper, session-timer expiry, codec mismatch, carrier re-INVITE failure, uplink congestion), taken from resolved tickets.
**Evaluation metric:** Macro-F1 across patterns and accuracy on fault domain, plus time-to-resolution and escalation rate on assisted tickets against a control group. Wrongly blaming the customer's network costs the most, because it delays the fix and damages trust, so precision on "customer premises" matters most.
**Scope:** The common patterns have clear signatures a senior engineer could write as rules, so a rules-plus-model hybrid is realistic. The intermittent and carrier-side faults are harder. 1 ML engineer and a senior voice engineer, 4–5 months.
**Data availability:** Traces and tickets are held by the provider. Resolution codes on tickets are inconsistent and need relabelling on a few thousand cases.

---

## 4. Toll Fraud and IRSF Detection on Live Call Records
#change-point-detection #gaussian-mixture-models #time-series-forecasting #feature-engineering #evaluation-metrics #revenue-impact

**Problem statement:** Detect within minutes when a customer's SIP account or PBX has been compromised and is pumping calls to premium or international revenue-share destinations, before the weekend's traffic becomes a five-figure wholesale bill the provider can't collect.

**ML task:** Per-account streaming change-point detection on call volume, cost and destination mix, with a mixture model of each account's normal calling profile and a destination-risk score
**Input data:** Real-time call detail records (account, origination IP, destination prefix, duration, rated cost); account history; known high-risk number ranges and destination lists; time of day and day of week; registration events and authentication failures.
**Target:** Fraud onset time per incident, taken from confirmed fraud cases and credit-dispute records.
**Evaluation metric:** Dollars of fraudulent cost incurred before detection, the business metric, and alert precision at the operating threshold. Detection latency matters more than any classification score, because cost accrues by the minute.
**Scope:** Detection is well understood. The difficulty is per-account baselines for thousands of small accounts with sparse history, and a response path (auto-block international, notify the customer) that doesn't cut off a legitimate surge. 1 ML engineer, 3 months.
**Data availability:** CDRs are the provider's own. Confirmed fraud incidents are few per provider, so labels are scarce and synthetic attack injection is useful for testing.

---

## 5. Product-to-Regime Revenue Classification
#large-language-models #bert #k-nearest-neighbors #evaluation-metrics #compliance #automation

**Problem statement:** Classify each billed product and bundle component into its communications tax category, Form 499 revenue line and jurisdictional treatment consistently, and flag when a product change breaks an existing classification.

**ML task:** Multi-output text classification of product descriptions and plan configurations, with nearest-neighbour retrieval of previously classified products and the reasoning behind them
**Input data:** Product catalogue and SKU descriptions, bundle structures, historical tax codes and 499 mappings, consultant-prepared filings, Form 499 instructions, and audit findings where available.
**Target:** Tax category, 499 line, interstate allocation method and end-user versus reseller treatment per SKU and customer type.
**Evaluation metric:** Agreement with a regulatory specialist's classification on a held-out set, and the dollar value of revenue whose classification changes on review. Any proposal that reduces contribution owed must be reviewed by a person, because under-reporting is the costly error.
**Scope:** Catalogues are small, a few hundred SKUs for most providers, so this is retrieval-heavy and human-confirmed rather than a large model. 1 engineer and a regulatory specialist, 3 months.
**Data availability:** Each provider's catalogue and past filings are internal. Classification reasoning is rarely written down and must be captured as it is confirmed.
