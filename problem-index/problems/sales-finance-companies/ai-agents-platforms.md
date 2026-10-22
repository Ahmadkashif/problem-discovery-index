# AI Agents & Platform Opportunities — Sales Finance Companies

**Industry:** [[sales-finance-companies|Sales Finance Companies]]

---

## 1. Funding Desk Agent
#ai-agent #large-language-models #transformers #automation #workflow-orchestration #compliance

**Concept:** An agent that takes every contract in transit from the dealer networks or the scanning queue, reads the full package, checks it against the approval, the state's contract and fee rules and the dealer agreement, verifies the stipulations, and either funds the deal within policy or returns every defect to the dealer at once with the rule cited. It tracks the kickback until it clears and keeps a funding audit trail for the warehouse bank.
**Inputs:** eContracts and scanned packages; LOS approval terms; state rule library; dealer agreements; stipulation documents; title and lien status.
**Outputs / Actions:** Auto-funding of clean packages within limits; consolidated defect notices to dealers; exception queue for funders with the issue highlighted; days-to-fund and defect-rate reporting by dealer.
**Why now:** Layout-aware language models can read state-specific contract forms and pay stubs reliably enough to verify rather than merely extract, and California's CARS Act (operative October 1, 2026) has added dealer obligations a funder must now check.
**Market:** Every indirect lender — captives, independent finance companies, banks and credit unions buying dealer paper. Competes with origination-system vendors and stipulation-verification vendors; differentiates on carrying the rules and the dealer agreement, not just the fields.

---

## 2. Collateral Integrity Registry
#ai-platform #graph-theory #large-language-models #data-integration #compliance #revenue-impact

**Concept:** A platform warehouse banks, ABS trustees and forward-flow buyers use to confirm that every contract pledged to them exists, matches its loan-level data, has a perfected lien and is not pledged to anyone else. It matches contract images and title records to the tape, and — with participants' consent — fingerprints each contract by VIN and borrower so the same collateral appearing in two facilities is caught.
**Inputs:** Loan tapes and borrowing base files; contract images; electronic lien and title records; custodian files; participating lenders' pledged-collateral fingerprints.
**Outputs / Actions:** Per-pool integrity reports; exceptions for missing contracts, unperfected liens and data mismatches; alerts on duplicate pledges; evidence packs for credit committees.
**Why now:** Tricolor's collapse in September 2025, with executives charged with double-pledging collateral and falsifying loan data, showed that warehouse lenders were trusting tapes they could not verify, and banks are now asking for exactly this proof.
**Market:** Warehouse lenders, ABS trustees and custodians, private credit buyers of auto and equipment loans; paid per pool or per facility. A new category beside existing custody and backup-servicing services.

---

## 3. Recovery Orchestration Agent
#ai-agent #large-language-models #gradient-boosting #workflow-orchestration #compliance #automation

**Concept:** An agent that runs the recovery file from charge-off decision to deficiency: assigns the repossession through the lender's agent network, sends each state's required notices on time, handles personal property and redemption requests, routes the vehicle to the auction or retail channel expected to net the most, triggers add-on cancellations and refunds, and computes the deficiency with the documentation a collection agency or court will need.
**Inputs:** Servicing status; state notice rules; repossession assignments and condition reports; auction and wholesale values; add-on product contracts; borrower communications.
**Outputs / Actions:** Assignment and notice generation; channel recommendation; refund requests; deficiency statements; a compliance file per recovery.
**Why now:** Repossessions are at their highest since 2009 (Cox Automotive estimated ~1.73M in 2024), recovery steps are rule-bound but vary by state, and language models can now read condition reports and borrower correspondence well enough to keep the file moving.
**Market:** Recovery departments at finance companies and indirect lenders; repossession forwarders such as those on the RDN network are adjacent sellers. Hands off to [[collections-agencies|Collections Agencies]] at the deficiency stage.

---

## 4. Non-Prime Deal Structuring Copilot
#ai-agent #gradient-boosting #tacit-knowledge-ml #optimization-fundamentals #worker-facing #revenue-impact

**Concept:** A copilot inside the credit analyst's queue that proposes counteroffers on non-prime deals — advance, term, down payment, stipulations — that a senior buyer would have proposed, each with its expected early-default rate and probability of the dealer closing it, and that drafts the adverse-action reasons the counter implies.
**Inputs:** The deal as submitted; bureau and application data; the dealer's history and the lender's program rules; senior buyers' past counteroffers and outcomes.
**Outputs / Actions:** Ranked counteroffer structures; cue flags; reason codes; a record of which suggestion the analyst took.
**Why now:** Lenders now hold years of structured counteroffer history in their origination systems, and decision-support models can be explained and tested for disparate impact to the standard examiners expect.
**Market:** Non-prime auto, powersports and equipment lenders whose manual-review queues decide most of their margin; sold as a module to lenders or embedded by origination-system vendors.
