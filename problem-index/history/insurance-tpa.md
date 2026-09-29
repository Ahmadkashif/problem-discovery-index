# History: Insurance Third-Party Administrators (TPAs)

**Industry:** [[industries/insurance-tpa|Insurance Third-Party Administrators (TPAs)]]
**Primary Wave:** [[series/eras/wave-01-mainframe-batch|1 — Mainframe & Batch]]
**Secondary Wave:** [[series/eras/wave-04-client-server-erp|4 — Client–Server & ERP]]
**Origin Parent:** [[origins/insurance-carriers/profile|Insurance Carriers]]
**Episode Tier:** 1
**Transferable Pattern:** An industry can be created by a statute that changes who bears a risk, not by an invention that changes how anyone computes it — and when that is how an industry starts, it organises its trade body years before it spends real money on software.

> **Template note.** There is no origin computer here, and no founding company to point to. This industry exists because a 1974 law changed who was legally permitted to bear insurance risk directly. The computing arrived afterward, gradually, on top of a market structure the statute had already created. That absence is the finding.

## Before

Before 1974, an employer or a municipality that wanted to provide health or workers' compensation benefits had, in practice, one real option: buy a policy from a licensed insurance carrier, which priced the risk using the credibility-weighted, pooled-loss-cost machinery [[origins/insurance-carriers/the-mechanism|insurance carriers' own mechanism file]] describes, and which administered every claim itself, in-house, as part of the premium the employer paid. A large employer bore no risk directly. It also had no visibility into, and no control over, how its own workforce's claims were actually being adjudicated — that judgement belonged entirely to the carrier.

## The Origin Event — a Statute, Not a Computer

**The Employee Retirement Income Security Act was signed by President Gerald Ford on 2 September 1974.** ERISA is primarily remembered as pension regulation, and that is a fair characterisation of most of the statute. The provision that created this industry is narrower and easy to miss: **Section 514**, the federal preemption clause, holds that ERISA preempts state laws "relating to" an employee benefit plan — with the specific and consequential effect that a **self-funded** employee benefit plan is exempt from state insurance regulation and state premium taxes, in a way an insured plan is not.

That single clause made it legally and financially attractive, for the first time, for a large employer to **bear its own claims risk directly** rather than transfer it to a carrier — paying claims out of its own funds as they arise, instead of paying a premium calibrated to cover them. By 2017, per federal survey data, roughly **60% of Americans with employer health coverage were in self-funded, ERISA-governed plans.**

Self-funding solved the risk-bearing question. It created an immediate operational one: an employer that wants to bear its own risk still has no in-house capability, and usually no desire to build one, to process claims, apply plan rules, negotiate provider networks, and comply with state workers' compensation law in every jurisdiction where it has employees. **That gap — self-funded risk with no in-house claims capability — is the entire reason this industry exists.** A TPA is, structurally, the claims-administration department a self-insured employer chose not to build.

## What Became Cheap

**Bearing your own risk without becoming an insurance company.** ERISA preemption made that legally straightforward for the first time; the market that grew in the gap made it operationally straightforward too. Neither of those is a computing achievement, and this file will not pretend otherwise. What is genuinely notable is how slowly the industry organised even after the legal door opened: the **Self-Insurance Institute of America** — the sector's trade body for self-insured payers and the TPAs serving them — was founded in **1981**, seven years after ERISA, and its trade publication *The Self-Insurer* dates from 1984. This is the same gradual, multi-actor formation this series' research has already flagged for pharma CROs: **an industry assembling itself slowly around a legal opening, with no single founding company or founding computer to anchor an episode to.**

## How It Was Actually Solved — and How Little of It Was

Claims platforms arrived much later than the legal and organisational structure they run on, and arrived piecemeal by line of business rather than as a single wave: ClaimVantage for group disability and absence, FINEOS dominant in life, accident and health for large carriers, Origami Risk and BriteCore in P&C-adjacent risk management, Guidewire priced out of reach of all but the largest TPAs. This vault's own hub note is blunt about what that produced: *"many TPAs use legacy systems customized over decades with brittle integrations,"* frequently COBOL-based, with **60–70% of claim volume still requiring full manual review** because auto-adjudication only reliably handles the simplest cases.

The reason this matters as history and not just as a current-state complaint: **there was never a forcing function comparable to HITECH.** [[origins/hospital-systems/profile|Hospital systems]] went from 9% to 96% EHR adoption in seven years because a federal subsidy and a penalty schedule made slow adoption expensive. No equivalent programme ever existed for TPA claims platforms. Modernisation here has been funded entirely out of each TPA's own margin, against SLA penalties that punish slow claims but never subsidised the system that would make them faster. That absence of a subsidy is as load-bearing, in its own quiet way, as HITECH's presence was for hospitals.

## The Binding Constraint

**There is no federal workers' compensation system for private-sector employers.** Each of the fifty states runs its own — its own benefit schedules, its own filing deadlines, its own fee schedules for medical treatment, its own definition of what an employer must report and when. A TPA administering workers' compensation claims for an employer with operations in a dozen states is not solving one adjudication problem twelve times faster. It is satisfying twelve separate, independently amended regulatory regimes simultaneously, none of which any single piece of software can assume away.

This is a rule-shaped constraint in the same sense [[history/dental-practices|dental practices' annual maximum]] is: no amount of modelling makes Ohio's workers' compensation fee schedule compatible with Texas's by making the model better. The best a TPA's technology can do is track fifty moving targets accurately and flag the exceptions — which is exactly what this vault's own `regulatory-reporting` and `state-workers-comp-boards` niches describe as a business, not a technical inconvenience to be engineered away.

## Why There Is No Fight

Unlike Epic against Cerner, or American Airlines against People Express, this industry has no comparable contest, and it is worth saying plainly why.

TPAs do not compete for a single national account the way EHR vendors competed for HITECH dollars. The market is fragmented by line of business (workers' compensation, group health, municipal self-insurance pools, specialty P&C) and further fragmented by the fifty-state regulatory patchwork just described — an insurance-adjacent restatement of the same absence [[origins/insurance-carriers/legacy|insurance carriers' own legacy file]] notes about this industry directly: it inherited *"the claims-adjudication layer downstream of a pricing decision it did not make."* There was no single prize large enough, arriving on a single deadline, to produce a two-company race for it. What exists instead is a large number of regional and specialty TPAs, each competing on service quality, SLA performance and network breadth within a fragment of the market too small to consolidate the way hospital EHRs or credit bureaus did.

## What's Still Open

- [[problems/insurance-tpa/high-impact|🔴 Claims Adjudication Speed and Accuracy]] — the SLA penalty this file traces to a market with no HITECH-style subsidy
- [[problems/insurance-tpa/worker-life-1|🟢 Claims Examiner Decision Fatigue]]
- [[niches/insurance-tpa/auto-adjudication-engine/profile|Auto-Adjudication Engine]] — closing the 60–70% manual-review gap
- [[niches/insurance-tpa/self-insured-employers/profile|Self-Insured Employers]] — the ERISA-created buyer this whole industry serves
- [[niches/insurance-tpa/workers-comp-claims/profile|Workers' Comp Claims]]
- [[niches/insurance-tpa/state-workers-comp-boards/profile|State Workers' Comp Boards]] — the fifty-regime constraint, as a business
- [[niches/insurance-tpa/regulatory-reporting/profile|Regulatory Reporting]]
- [[niches/insurance-tpa/nurse-case-management-services/profile|Nurse Case Management Services]]

## The Transferable Pattern

> **Before looking for the founding computer, check whether the industry was created by a change in who is legally permitted to bear a risk. If it was, expect a slow, trade-association-shaped formation instead of a launch date, expect the technology to arrive underfunded relative to industries a regulator actively subsidised, and expect the real constraint to be a patchwork of jurisdictions rather than a single number.**

An FDE meeting a TPA should not go looking for this industry's SABRE. It does not have one. What it has instead is a statute that moved a risk from one balance sheet to another, and forty years of software built to administer the consequence — mostly after the fact, mostly per state, mostly without the subsidy that compressed a comparable transition elsewhere in this vault into seven years.

**Sources:** ERISA, Pub. L. 93-406 (signed 2 Sept 1974), 29 U.S.C. § 1144 (Section 514 preemption); Wikipedia, *Employee Retirement Income Security Act of 1974*, *Third-party administrator*; KFF, Employer Health Benefits Survey (self-funded plan share, 2017 estimate); Self-Insurance Institute of America (SIIA), organisational history (founded 1981) and *The Self-Insurer* (1984); this vault's `industries/insurance-tpa.md`, `origins/insurance-carriers/the-mechanism.md`, `origins/insurance-carriers/legacy.md`, `origins/hospital-systems/profile.md` (HITECH comparison), `history/dental-practices.md` (binding-constraint parallel).
