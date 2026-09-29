# Lineage: Talent Assessment Platforms

**Industry:** [[industries/talent-assessment-platforms|Talent Assessment Platforms]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** the four-fifths rule — the adverse-impact test that flags any group whose selection rate is below 80% of the highest group's, codified federally at 29 CFR 1607.4(D)
**Builder:** California Fair Employment Practice Commission
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

After 1971, a test could be illegal because of its results, not its intent.

In *Griggs v. Duke Power Co.*, decided **8 March 1971**, the Supreme Court held that employment tests with a disparate impact on minority applicants must be shown to be job-related, and that the burden of proof sits with the employer. Duke Power had introduced a high-school diploma requirement and two aptitude tests — the Wonderlic and the Bennett Mechanical Comprehension Test — on **2 July 1965**, the day Title VII took effect. At the cut-offs used, about 58% of white applicants passed against about 6% of Black applicants.

That created a question nobody had a procedure for: **how different do two pass rates have to be before an enforcement agency should look?** Statistical significance was one answer, but it depended on sample size, needed a statistician, and meant nothing to the personnel manager who had to decide on Monday whether to keep using a test.

## What Got Built

A ratio and a threshold. Take each group's selection rate; divide it by the rate of the group selected most often; if the result is below **four-fifths**, treat it as evidence of adverse impact.

It is arithmetic a clerk can do on the back of an applicant log. That is the whole design. It does not ask whether the difference is statistically reliable, and it does not ask whether the test predicts job performance — it only decides *when the second question must be asked.*

## Who Built It, And Why Them

A panel of 32 professionals, the **Technical Advisory Committee on Testing (TACT)**, convened in **1971** by the **State of California Fair Employment Practice Commission**. Its *State of California Guidelines on Employee Selection Procedures*, published in **October 1972**, is the first official document known to have used the 80% test in an adverse-impact context.

**Why a state commission rather than the federal agencies or the test publishers?** A state enforcement body was the party with the caseload and without a product to defend. Publishers had every reason to argue validity study by study; employers had every reason to avoid any bright line at all. A commission that had to triage complaints needed a screening rule its own investigators could apply without a psychometrician — so the rule's shape is an enforcement queue's shape: cheap, fast, deliberately blunt.

The federal agencies then took it over. The **Uniform Guidelines on Employee Selection Procedures** were issued on **25 August 1978** (43 FR 38295), effective **25 September 1978**; the EEOC's accompanying Questions and Answers list the adopting agencies as the EEOC, the Office of Personnel Management and the Departments of Justice, Labor and the Treasury. Under the vault's originator-over-inheritor precedent, the builder key is the California commission.

## What It Cost

**It is a rule of thumb that became a pass mark.** The federal Q&A say so directly: the "'4/5ths' or '80%' rule of thumb is not intended as a legal definition, but is a practical means of keeping the attention of the enforcement agencies on serious discrepancies." The same guidance warns that with small numbers one hiring decision can create or erase the disparity.

Those caveats did not travel. A test vendor can report that its instrument "passes the four-fifths rule" on a pooled sample, which says nothing about a given client's applicant pool — and nothing at all about whether the scores predict anything. The threshold was built to trigger a validity inquiry and is routinely used instead of one.

## What You Still Touch

The adverse-impact table in every assessment vendor's technical manual, and the impact ratios in the bias audits now required of automated hiring tools, are the 1972 California screening rule applied to software.

- [[problems/talent-assessment-platforms/low-impact-1|🟡 Adverse Impact Measurement and Audit]] — the rule itself, still the default metric
- [[problems/talent-assessment-platforms/high-impact|🔴 The Instrument's Validity Is Asserted by the Vendor and Established Nowhere]] — the question the rule was meant to trigger
- [[niches/talent-assessment-platforms/adverse-impact-auditing/profile|Adverse Impact Auditing]]
- [[niches/talent-assessment-platforms/validity-and-bias/profile|Validity & Bias Measurement]]

**Sources:** Wikipedia, *Disparate impact* (TACT, 32 members, convened 1971 by the California FEPC; October 1972 California Guidelines as the first official use of the 80% test; 1978 federal codification); Wikipedia, *Griggs v. Duke Power Co.* (decision date, the tests, the 2 July 1965 introduction, the 58%/6% pass rates); Cornell LII, 29 CFR § 1607.4(D) (text and the 43 FR 38295, 25 August 1978 citation); EEOC, *Questions and Answers to Clarify and Provide a Common Interpretation of the Uniform Guidelines* (rule-of-thumb passage quoted, adopting agencies, issue and effective dates). ⚠️ **Not established:** the names of TACT's members or who proposed the 80% figure; I could not open the 1972 California Guidelines themselves, so the origin rests on one secondary source. The bias-audit reference in the last section is from general knowledge (New York City's automated employment decision tool law) and was not re-verified this session. WebSearch was unavailable this session (session cap reached); research used WebFetch on known URLs only.
