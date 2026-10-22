# AI Agents & Platform Opportunities — Mortgage Lenders

**Industry:** [[mortgage-lenders|Mortgage Lenders]]

---

## 1. Underwriting Second-Reader Agent
#ai-agent #large-language-models #gradient-boosting #tacit-knowledge-ml #evaluation-metrics #compliance

**Concept:** An agent that reads every file before the underwriter issues conditions: recomputes income from the source documents into the lender's worksheet, reconciles returns against IRS transcripts and deposits, compares the file with past files that drew income defects, and points at the specific lines a senior underwriter would question. It then drafts the conditions and records the underwriter's decision and reasoning as a structured income ledger, so every call can later be joined to QC findings and loan performance.
**Inputs:** Loan file documents, AUS findings, the lender's overlays and worksheet templates, historical files with QC and defect outcomes, underwriter notes.
**Outputs / Actions:** Recomputed income with source links; ranked flags with reasons; draft conditions; a structured decision record per file; turn-time and defect dashboards by income type and underwriter.
**Why now:** Language models now read returns, K-1s and bank statements well enough to recompute income with citations, and the agencies' validation programmes have made documented, traceable income the route to rep-and-warrant relief.
**Market:** Chief credit officers and underwriting managers at independent mortgage banks and bank mortgage divisions; competes with document-extraction vendors and LOS add-ons, and differentiates on capturing the decision, not just the data.

---

## 2. Secondary Marketing Desk Agent
#ai-agent #survival-analysis #gradient-boosting #time-series-forecasting #workflow-orchestration #revenue-impact

**Concept:** An agent for the lock desk and capital markets head that builds and checks the morning rate sheet, drafts reprices when MBS prices cross tolerance, forecasts pull-through loan by loan, prices every extension and renegotiation request against modelled fallout and hedge cost, and proposes commitment and best-execution decisions across agency cash windows, MBS pooling and aggregators.
**Inputs:** MBS and investor prices, pricing engine output, lock and status data from the origination system, hedge advisor position reports, lock policy, loan officer request history.
**Outputs / Actions:** Draft rate sheets and reprices with change explanations; lock-change recommendations with cost; pull-through forecasts; commitment and best-ex proposals; a record of every concession and what it bought.
**Why now:** Pricing engines and hedge advisors expose data through APIs, and lenders operating at $785 per loan of production profit (MBA, 2025) cannot afford margin leaking through ad hoc concessions.
**Market:** Capital markets heads at lenders hedging their own pipelines, a few hundred firms; overlaps with the hedge advisors profiled in Pass 2, who could also sell it.

---

## 3. Post-Close Delivery and Trailing Documents Agent
#ai-agent #large-language-models #transformers #feature-engineering #automation #workflow-orchestration

**Concept:** An agent that follows each loan from closing to final document: checks the closing package against investor purchase conditions before shipping, clears suspense items by routing them to the closer, title agent or settlement agent, tracks every trailing document against its investor deadline, checks county recorder and title agent sources automatically, verifies each document that arrives and uploads it to the investor.
**Inputs:** Closing packages, investor purchase conditions and suspense lists, custodian receipts, trailing-document requirements by investor, recorder and title agent sources, warehouse line terms.
**Outputs / Actions:** Pre-shipping exception list; routed and tracked fixes; verified trailing-document uploads; aging and deadline alerts; dwell-time and exception analytics by title agent and closer.
**Why now:** Document AI can verify recorded instruments and title policies against a closing package reliably, and most investor and custodian portals now accept electronic delivery.
**Market:** Post-closing and secondary operations at every lender that sells loans; adjacent to LOS vendors and outsourced post-closing providers; priced per loan.

---

## 4. Loan Quality and Repurchase Defence Platform
#ai-platform #large-language-models #random-forests #survival-analysis #compliance #workflow-orchestration

**Concept:** A platform that unifies prefunding QC, post-closing QC and agency defect management: risk-ranks discretionary QC samples, classifies findings to the agency taxonomy, receives agency notices and drafts rebuttals from the file evidence and the underwriter's recorded reasoning within the 30-day window, and joins every outcome back to the origination decision so the lender sees which income types, channels, underwriters and partners generate defects.
**Inputs:** QC samples and findings, agency defect notices and repurchase demands, loan files and decision records, payment histories, investor guidelines.
**Outputs / Actions:** Selection lists; classified findings; draft rebuttals with cited evidence; repurchase, fee-in-lieu or cure recommendations; root-cause dashboards for senior management and the 90-day QC report.
**Why now:** The agencies have formalised cure and fee-in-lieu options (Fannie Mae's Notice of Potential Defect in 2024, Freddie Mac's fee option from 2025), so a well-argued response now has more possible outcomes than repurchase, and language models can assemble that argument from the file in minutes.
**Market:** Chief credit officers, QC managers and secondary heads at agency sellers; QC software vendors and outsourcers are the natural incumbents but sell workflow and review hours, not the joined record.
