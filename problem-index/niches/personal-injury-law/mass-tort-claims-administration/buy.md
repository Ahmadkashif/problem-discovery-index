# Every Settlement Rebuilds the Rules Engine, Because a Court Rewrote the Rules

**Niche:** [[niches/personal-injury-law/mass-tort-claims-administration/profile|Mass Tort & Class Action Claims Administration]]
**Industry:** [[industries/personal-injury-law|Personal Injury Law Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Intake, document review, identity verification, case management and disbursement are all mature bought components, and the eligibility matrix at the centre of every settlement is a bespoke legal document that has to be reimplemented from scratch on a court deadline.
**Tags:** #bert #large-language-models #feature-engineering #workflow-orchestration #compliance

## The Problem
A claims administration platform assembles from recognisable parts. Web and paper intake. Document capture and extraction. Identity verification and deduplication. Case management with audit trail. Correspondence and notice delivery at scale. Contact centre. Payment disbursement across cheque, card and digital rails. Reporting to counsel and the court.

Administrators have bought most of this and it works. What does not transfer between settlements is the part that determines every outcome: the allocation matrix. It is negotiated by counsel, approved by a judge, written in legal prose, and different every time. Points for a diagnosis. Multipliers for exposure duration. Tiers by product purchased or years employed. Caps, floors, pro rata adjustment if the fund is oversubscribed, derivative claims for spouses.

That document has to become executable code, correctly, under a court-ordered schedule, with money moving at the end of it.

## What Already Exists
Case and claims management platforms handle workflow, correspondence and audit. Document AI extracts fields from uploaded proof. Identity verification and address hygiene services are mature. Deduplication and entity resolution products exist. Contact centre and mass correspondence platforms scale. Disbursement platforms handle multi-rail payment and tax reporting. Rules engines let non-developers encode decision logic. E-discovery and legal review tooling handles large document populations.

## The Customization Gap
**The matrix is a new specification every time, with legal consequence.** A configurable rules engine assumes rules that resemble each other across deployments. Here the rule set is unique, drafted by lawyers in prose that was negotiated rather than specified, contains genuine ambiguity, and cannot be got wrong — a misapplied multiplier is money delivered to the wrong people under a court order. Translating that document into logic, and validating the translation against counsel's intent, is the central engineering task of every engagement and no vendor addresses it.

**Oversubscription changes the arithmetic globally.** Most matrices contain a pro rata mechanism that adjusts every award once the claim population is known. Awards are therefore not independent — they cannot be computed and finalised claim by claim, which is exactly what claims platforms are built to do.

**Proof documents are whatever the claimant found.** A faded receipt, a decades-old employment record, a medical summary, a photograph of a product label. Document AI is strong on structured forms and much weaker here, and the reviewer's actual question — does this document support this eligibility element under this matrix — is a matter of judgment against a bespoke standard, not field extraction.

**Deduplication runs without an identifier.** Class members are consumers or workers with no shared key. Matching across variant names, old addresses, and household relationships is genuinely uncertain, and both errors are serious: a duplicate pays twice out of a fixed fund, and a false match denies a legitimate claimant. Vendor matching thresholds encode neither of those costs.

**Fraud here is organised and settlement-specific.** Large funds attract coordinated filing, and each settlement's fraud pattern adapts to that settlement's claim form. Vendor fraud tools are built for consumer credit and payments and do not represent the relevant structure, which is similarity among claims and relationships between filers.

**The deadline is a court order.** Claim volume arrives overwhelmingly in the final days of a claim period and the date cannot move. Ordinary workforce management assumes a manageable curve and a negotiable service level; here the curve is a spike and the deadline is judicial.

**Auditability is to a judge's standard.** Every determination may have to be explained in court. That constrains how decisions may be made and rules out anything that cannot be traced end to end — a requirement most bought analytics layers were not designed against.

## Target Customer
Chief Operating Officer or Chief Technology Officer at a settlement administration firm. The realistic build is narrow and high-value: keep intake, correspondence, contact centre and disbursement as bought, and build the matrix implementation and validation layer plus deduplication calibrated for asymmetric harm — the two places where every engagement currently starts from nothing.

## Impact If Solved
The gap between a settlement being approved and the money reaching people is an implementation project run against a judicial deadline, rebuilt from scratch each time, on tooling designed for organisations whose rules stay the same.
