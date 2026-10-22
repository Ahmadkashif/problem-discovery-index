# Niche Analysis — Notary & Signing Services

**Parent Industry:** [[industries/notary-signing-services|Notary & Signing Services]]

## Niche Selection

A notary's work is an identity decision made in about a minute under personal liability, wrapped in a production job — appointments, packages, journals, certifications — that runs against clocks set by lenders, courts, consulates and recorders. The eight niches below split the industry by what operators and the vendors serving them actually compete over. Market sizes are estimates of fees and tooling spend within each niche, against an industry of ~$2-3B a year in notary and signing fees (estimate), not of any wider closing or legal market.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Mortgage & Real Estate Signings | 🔵 High Market Share | ~$1.4B | Medium | Title and escrow operations managers |
| 2 | Estate & Legal Document Signings | 🔵 High Market Share | ~$250M | Low | Estate planning attorneys, families |
| 3 | Notary Journals & Records | 🟠 Low Digitized | ~$60M | Low | The individual notary |
| 4 | Apostille & Document Authentication | 🟠 Low Digitized | ~$150M | Low | Immigration, adoption and corporate filers |
| 5 | Hospital, Care-Facility & Jail Signers | 🟣 Underserved Audience | ~$120M | Very Low | Families, hospital social workers, defence lawyers |
| 6 | Limited-English Signers | 🟣 Underserved Audience | ~$100M | Low | Signers and community legal practices |
| 7 | Remote Online Notarization Sessions | ⚡ Highly Automatable | ~$300M | High | RON platform trust leads, title companies |
| 8 | Signing Order Dispatch | ⚡ Highly Automatable | ~$250M | Medium | Signing-service owners |

## Why These Niches

Mortgage and real estate signings take the largest share because ~5.4 million mortgage loans in 2025 (MBA) generate most of the paid notarial work, routed from title companies through signing services and Snapdocs to independent agents. Estate and legal signings are second: smaller in fees but the work where the notary's observation of the signer matters most and is tested years later. The two low-digitized niches are where paper still runs everything: the bound journal that is the notary's only legal record, and the chain of county, state and federal certifications behind an apostille. The two underserved audiences are the signers the industry avoids: people who cannot leave a hospital, care home or jail and often have no ID in hand, and people who do not read English and are exposed to "notario" fraud. The two automatable niches are the most mechanical: remote sessions, where identity proofing and recording are already software, and the signing service's dispatch desk, where assignment and confirmation are data problems handled by phone.

## Niches

- [[niches/notary-signing-services/mortgage-and-real-estate-signings/profile|🔵 Mortgage & Real Estate Signings]]
  - [[niches/notary-signing-services/borrower-loan-package-signings/profile|🎯 Borrower Loan Package Signings]]
  - [[niches/notary-signing-services/seller-and-deed-signings/profile|🎯 Seller & Deed Signings]]
- [[niches/notary-signing-services/estate-and-legal-document-signings/profile|🔵 Estate & Legal Document Signings]]
- [[niches/notary-signing-services/notary-journals-and-records/profile|🟠 Notary Journals & Records]]
- [[niches/notary-signing-services/apostille-and-authentication/profile|🟠 Apostille & Document Authentication]]
- [[niches/notary-signing-services/facility-bound-signers/profile|🟣 Hospital, Care-Facility & Jail Signers]]
- [[niches/notary-signing-services/limited-english-signers/profile|🟣 Limited-English Signers]]
- [[niches/notary-signing-services/remote-online-notarization-sessions/profile|⚡ Remote Online Notarization Sessions]]
- [[niches/notary-signing-services/signing-order-dispatch/profile|⚡ Signing Order Dispatch]]

## Filter Notes

Seven of the eight level-1 niches are terminal. **Mortgage & Real Estate Signings** is not: writing its contested sentence produced two contests with different winners. At a borrower signing the lender has already verified the borrower, so the agent wins on execution — a clean package back before the funding cutoff, measured in redraws per hundred signings. At a seller or deed signing the signer has not been underwritten and may be an impostor selling an absentee owner's land; ALTA's 2026 survey found ~59% of title firms saw an impersonation attempt in 2025 and named seller-chosen notaries and remote signings among the top red flags. That contest is won on identity judgement, and title companies route it to an approved panel; the title office's own file-level checks are analysed under [[industries/title-and-settlement-offices|Title & Settlement Offices]], and this sub-niche keeps the notary's side of the signing. Different skills, different risk owners, so it decomposes into **Borrower Loan Package Signings** and **Seller & Deed Signings**.

Two terminal calls were close. **Remote Online Notarization Sessions** could look like two contests, passing genuine signers and stopping impostors, but they are two ends of one decision threshold, judged on the same evidence by the same buyer, so one sentence governs. It is also kept distinct from [[niches/esignature-document-workflow/notarization-and-witnessing/profile|Notarization & Witnessing]] under E-Signature & Document Workflow, which owns whether the destination accepts a remote act; this niche owns the session's identity decision on the notary's side. **Hospital, Care-Facility & Jail Signers** overlaps with Estate & Legal Document Signings, since many bedside documents are powers of attorney; it stays separate because its contest is access and identity without an ID in hand, not the witnessed ceremony.

Three candidates were rejected. **Remote I-9 authorised-representative verifications** looked automatable and clock-driven, but a notary acting as an employer's representative is not performing a notarial act, E-Verify employers can now examine documents remotely under the DHS alternative procedure, and the work belongs with employment verification. **Civil-law notarial offices** in Louisiana and Puerto Rico are the closest fit to the Census definition of NAICS 541120 (drafting as well as executing documents), but in Puerto Rico notaries are attorneys (recalled, not checked) and the work sits inside law practice; the contest there is legal drafting, covered by [[industries/small-law-firms|Small Law Firms]]. **Retail walk-in notary counters** at shipping stores and bank branches were rejected because the contest is price and convenience — the generic statement fails the filter — and banks offer the service free to customers.

---

## Pass 2 — Insight-Layer Discovery

Second, orthogonal sweep. Pass 1 searched across the operator layer and found sole-proprietor agents and signing services of a few coordinators; research functions do not exist at that altitude. This pass sweeps seven positions in the value chain — aggregator/rollup, payer & intermediary, data & benchmark vendors, association research arms, specialist advisory & valuation, regulatory bodies, and suppliers selling into the industry — looking for a dedicated insight function of 10+ people whose analytical output is the billable deliverable. Full method in `_direction.md`.

| # | Pocket | Position | Insight Function | Score | Verdict |
|---|---|---|---|---|---|
| 9 | RON Platform Identity-Risk Teams | Supplier | ~10-50 | 37 | ⚠️ Kill switch |
| 10 | Notary Association Law & Guidance Content | Association | ~10-30 | 30 | Below threshold |
| 11 | Signing Marketplace & Closing Platform Analytics | Aggregator/rollup | ~10-30 | 27 | ⚠️ Kill switch |
| 12 | National Signing Services | Aggregator/rollup | <10 | — | Fails gate |
| 13 | Notary Bond & E&O Programs | Payer & intermediary | <10 | — | Fails gate |
| 14 | State Notary Commissioning & Enforcement Units | Regulatory | <10 analytical | — | Fails gate |
| 15 | County Recorder Notarial Review & Fraud Alerts | Regulatory | <10 | — | Fails gate |
| 16 | Forensic Document Examiners & Notary Expert Witnesses | Specialist advisory | 1-5 | — | Fails gate |
| 17 | Notary & Signing Agent Training Providers | Specialist advisory | <10 | — | Fails gate |
| 18 | Notary Seal, Journal & E-Journal Vendors | Supplier | <10 | — | Fails gate |

## Why These Pockets

Nothing qualifies, and that is the honest result. The operators fail the gate: a signing agent is a sole proprietor, and a signing service is a dispatch desk whose coordinators and QC reviewers are production staff, not analysts. The industry's most valuable judgement — whether the person at the table is the owner — produces no invoiced analysis anywhere in the chain. Where data about notarial acts accumulates, it belongs to someone else. The RON platforms (pocket 9) hold the richest corpus, millions of recorded sessions with identity evidence and notary decisions, but those recordings are retained as the notary's statutory record and state law limits their reuse, so the pocket carries a kill switch on top of a low Q1. Snapdocs (pocket 11) sees the whole loan-signing market's orders and fees, but the order data belongs to its lender and title customers under platform contracts, and it uses what it may use to rank agents inside its product: a second kill switch, scored consistently with [[niches/title-and-settlement-offices/production-software-vendors/profile|🔍 Title & Escrow Production Software Vendors]] under Title & Settlement Offices.

The only clean pocket is the NNA (pocket 10, 30), the one place where notary law knowledge is sold, through training and the hotline; but its inputs are public statutes, its team is small and the market is essentially one organisation. The strongest near-miss in this value chain sits next door. The vendors that verify sellers and wire instructions for title offices, CertifID among them, hold a fraud corpus spanning thousands of title offices and growing with impersonation attempts; they are profiled as [[niches/title-and-settlement-offices/wire-identity-verification-vendors/profile|🔍 Wire & Seller Identity Verification Vendors]] under [[industries/title-and-settlement-offices|Title & Settlement Offices]] (39, kill switch on consumers' GLBA-protected financial data) and get no second profile here.

Several other positions belong to other industries. The underwriters' agency audit and agent-risk teams, which hold the outcomes that would grade a notary's identity decisions, are profiled as [[niches/title-and-settlement-offices/underwriter-agency-audit-teams/profile|🔍 Underwriter Agency Audit Teams]] (31, below threshold); the title insurance carriers themselves are queued and not yet built. Mortgage post-closing quality control, which audits loan files including their notarial defects, is profiled as [[niches/mortgage-brokers/mortgage-qc-compliance-audit/profile|🔍 Mortgage Quality Control & Compliance Audit]] under Mortgage Brokers (52, kill switch). Title plants and search data are profiled under [[niches/land-surveyors/title-plant-search-operations/profile|🔍 Title Plant & Search Operations]] in Land Surveyors (55, indexed). Background screening of signing agents belongs to investigation and background screening firms, which are queued and left to that build. KBA and credential-analysis providers sit inside [[industries/identity-verification-vendors|Identity Verification Vendors]]. For a research-insight engine this industry is a map of where identity evidence is created and lost, not a market.

## Niches — Pass 2
- [[niches/notary-signing-services/ron-platform-identity-risk-teams/profile|🔍 RON Platform Identity-Risk Teams]]
- [[niches/notary-signing-services/notary-association-law-content/profile|🔍 Notary Association Law & Guidance Content]]
- [[niches/notary-signing-services/signing-marketplace-analytics/profile|🔍 Signing Marketplace & Closing Platform Analytics]]
- [[niches/notary-signing-services/national-signing-services/profile|🔍 National Signing Services]]
- [[niches/notary-signing-services/notary-bond-eo-programs/profile|🔍 Notary Bond & E&O Programs]]
- [[niches/notary-signing-services/state-notary-commissioning-units/profile|🔍 State Notary Commissioning & Enforcement Units]]
- [[niches/notary-signing-services/county-recorder-notary-review/profile|🔍 County Recorder Notarial Review & Fraud Alerts]]
- [[niches/notary-signing-services/forensic-document-examiners/profile|🔍 Forensic Document Examiners & Notary Expert Witnesses]]
- [[niches/notary-signing-services/signing-agent-training-providers/profile|🔍 Notary & Signing Agent Training Providers]]
- [[niches/notary-signing-services/notary-supply-journal-vendors/profile|🔍 Notary Seal, Journal & E-Journal Vendors]]
