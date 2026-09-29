# Lineage: Compliance Consulting Firms

**Industry:** [[industries/compliance-consulting|Compliance Consulting Firms]]
**Wave:** [[series/eras/wave-04-client-server-erp|4 — Client–Server & ERP]]
**The tool:** SAS 70, *Service Organizations* — the 1992 auditing standard whose Type I and Type II reports became today's SOC 1 and SOC 2
**Builder:** AICPA
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A company's books were increasingly kept by somebody else.

Payroll went to a payroll bureau, transaction processing to a data-processing service, custody to a trust department. The company's financial statements still had to be audited — and the controls that decided whether those numbers were right now sat inside another firm's building, on another firm's computers.

So the auditor had a problem with no clean answer. It could not test controls it could not see. It could ask the service organisation to let it in, and so could the auditor of every other client that bureau served. **One service provider with hundreds of customers faced, in principle, hundreds of separate audit teams asking the same questions about the same controls.** Each customer's auditor paid to learn what the last one had already learned.

## What Got Built

A report written once and read by many.

The AICPA's Auditing Standards Board issued Statement on Auditing Standards No. 70, *Service Organizations*, in **April 1992**. It let a single independent auditor — the "service auditor" — examine a service organisation's controls and issue a report that each customer's own auditor could use as evidence.

It came in two forms. A **Type I** report described the controls in place at a point in time and whether they were suitably designed. A **Type II** report added tests of whether they actually operated effectively across a period — one practitioner history says a minimum of six months. **That split — design at a moment versus operation over time — is the structure every SOC report still has.**

## Who Built It, And Why Them

The American Institute of Certified Public Accountants, because it owned the rules on what counts as audit evidence.

The binding constraint was not technical. It was whether a customer's auditor was *allowed* to rely on another auditor's work about a third party's controls. Only the body that set generally accepted auditing standards in the US could make that reliance legitimate. A software vendor could build a control checklist; it could not make that checklist acceptable to an audit partner signing an opinion.

The AICPA also answered a problem its own members felt on both sides. Service auditors gained a new engagement to sell; user auditors gained a document that replaced a site visit. One secondary account describes the standard as a response to a "huge market shift toward outsourcing data processing." SAS 70 replaced an earlier standard, SAS 44, *Special-Purpose Reports on Internal Accounting Control at Service Organizations*; I could not confirm SAS 44's date.

## What It Cost

**It was built for financial reporting and was used for everything else.** The AICPA's own journal, writing in 2010, said many CPAs had used SAS 70 to report on controls "unrelated to user entities' internal control over financial reporting," such as privacy — and that it was never applicable to them. SAS 70 had become a marketing credential for any outsourced service, carrying authority it had not been designed to carry.

The AICPA's fix was to split it. SSAE 16, issued in **April 2010** and effective for reports on periods ending on or after **15 June 2011**, took over the financial-reporting case as SOC 1, and the framework added SOC 2 for security, availability, processing integrity, confidentiality and privacy. SSAE 18 followed in 2017.

The deeper cost survived the split: **the report covers the controls the service organisation chooses to describe**, tested by an auditor it hires. Customers receive an opinion on a system boundary drawn by the party being audited — and a consulting market grew up to help draw it.

## What You Still Touch

Every SOC 2 readiness engagement is a 1992 audit-evidence rule, extended to subjects it was never written for:

- [[problems/compliance-consulting/low-impact-2|🟡 Audit Evidence Collection Coordination]] — the months of screenshots a Type II period requires
- [[problems/compliance-consulting/low-impact-1|🟡 Gap Analysis Report Generation from Client Evidence]]
- [[niches/compliance-consulting/soc2-attestation-audit-firms/profile|Attestation & Certification Audit Practices]] — the descendants of the service auditor
- [[niches/compliance-consulting/audit-readiness-automation/profile|Audit Readiness & Evidence Automation]]
- [[niches/compliance-consulting/tprm-assessment-exchanges/profile|Third-Party Risk Assessment Exchanges]] — the questionnaires that persist alongside the reports

**Sources:** Ami Sherinsky, "Replacing SAS 70," *Journal of Accountancy* (August 2010, fetched), for "since 1992," the misuse for non-financial controls such as privacy, and SSAE 16's effective date; search summaries of practitioner histories (Kaufman Rossin, CliftonLarsonAllen, Linford & Co) for April 1992 publication, the "market shift toward outsourcing" phrase, SSAE 16's April 2010 issue and SAS 44 as predecessor; PKF AvantEdge, "A Brief History of SOC and SAS" (fetched), for Type I/Type II definitions, the six-month Type II minimum, SOC 2's five categories and SSAE 18 in 2017 — practitioner marketing, attributed. ⚠️ **Not established:** SAS 44's issue year (search suggested 1982; unconfirmed); which firms or bureaus pressed the Auditing Standards Board for SAS 70 — the *CPA Journal* archive article that may say so returned a connection reset; the claim that the six-month minimum was a formal requirement rather than practice. The two-sided member benefit is inference.
