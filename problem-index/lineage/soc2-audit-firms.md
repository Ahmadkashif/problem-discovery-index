# Lineage: SOC 2 & Attestation Audit Firms

**Industry:** [[industries/soc2-audit-firms|SOC 2 & Attestation Audit Firms]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** the CPA WebTrust seal and its Principles and Criteria (September 1997) — the failed consumer seal whose criteria, merged with SysTrust's, became the Trust Services Criteria every SOC 2 report is written against
**Builder:** AICPA
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

In 1997 the accounting profession had a product nobody on the web could buy.

A CPA's attestation was the one form of third-party assurance with a legal and professional apparatus behind it — independence rules, standards, liability. But it attached to financial statements, and the new question was not whether a company's books were right. It was whether a shopper could type a card number into a stranger's website. The profession wanted a way to sell assurance about **systems and conduct** rather than numbers, to a buyer who had never hired an auditor.

Some adjacent tooling existed. Auditors already reported on controls at service organisations, but as a document for another auditor, not for a customer. The web needed something a customer could see.

## What Got Built

A seal, and behind it a checklist.

WebTrust, launched in September 1997, let a CPA examine a website against published **Principles and Criteria** — business-practice disclosure, transaction integrity, information protection — and, on a clean opinion, license the site to display a clickable seal linking to the report. In 1999 SysTrust extended the same approach from websites to the reliability of whole IT systems.

The seal failed. Accounting Today, writing its obituary in 2009, reported that **no more than 50 companies ever displayed it at once**; the AICPA had quietly handed the programme to its Canadian partner and put a different vendor's seal on its own site.

The criteria did not fail. Around 2003 the AICPA and the Canadian Institute of Chartered Accountants merged the WebTrust and SysTrust principles into one set, the **Trust Services Principles and Criteria**. When the AICPA later built its SOC reports, those criteria became the benchmark for SOC 2 and SOC 3; the AICPA's Assurance Services Executive Committee reissued them as the 2017 Trust Services Criteria, TSP Section 100 — security, availability, processing integrity, confidentiality, privacy.

## Who Built It, And Why Them

The American Institute of Certified Public Accountants, jointly with the CICA.

The reason is a revenue problem shaped like a licence. Only a CPA could sign an attestation opinion, and the institute that writes attestation standards could define a new subject matter for one simply by publishing criteria. Accounting Today put the motive bluntly: the idea was that **CPAs could make money** annually certifying websites. No technology company could issue that kind of opinion; no standards body outside accounting could make it a CPA-only service.

The same obituary explained the failure. Card networks already capped a shopper's loss at $50, so the consumer had no problem the seal solved — and consumers did not think of CPAs as web-security judges. Yet the reusable part, criteria an accountant could attest against, found its real buyer later: not a shopper but a procurement team.

## What It Cost

**The report inherited the seal's economics.** WebTrust was paid for by the site being assessed and read by someone who could not see the work. SOC 2 kept that structure exactly: the audited company chooses and pays the firm; the relying customer sees an opinion and a list of exceptions, and cannot tell a searching engagement from a permissive one.

The criteria also inherited their generality. Written to cover any website, they specify outcomes, not tests — leaving scope, sampling and the system description largely to the client and the firm.

## What You Still Touch

The five trust services categories on a modern SOC 2 are WebTrust's principles, renamed and matured.

- [[problems/soc2-audit-firms/high-impact|🔴 The Report Cannot Tell a Searching Audit From a Permissive One]] — the seal's payer–reader split, carried into the report
- [[problems/soc2-audit-firms/low-impact-2|🟡 Scope and the Client's Own System Description]]
- [[niches/soc2-audit-firms/the-relying-customer/profile|The Relying Customer]]
- [[niches/soc2-audit-firms/rigour-expression/profile|Rigour Expression]]

**Sources:** Accounting Today, "Remembering WebTrust," 5 February 2009 (September 1997 launch, 1999 SysTrust, ≤50 seals, CPA revenue motive, $50 card-liability explanation, programme transferred to CICA); roosacpa.com and socreports.com practitioner histories (2003 AICPA/CICA harmonisation into Trust Services Principles; foundation for SOC 2 / SOC 3); Wikipedia, *System and Organization Controls* (2017 TSC established by the AICPA's ASEC); Cherry Bekaert and Linford & Co guides to TSP Section 100; CPA Canada, WebTrust programme pages (joint AICPA/CICA origin). Sibling note: `lineage/compliance-consulting.md` covers SAS 70, the separate auditor-to-auditor lineage, and is cited as vault material only. ⚠️ **Not established:** the year the AICPA first issued SOC 2 guidance (commonly given as 2010–2011 alongside SSAE 16's replacement of SAS 70; not confirmed against an AICPA primary source this session); whether the harmonisation was 2002 or 2003 (secondary sources differ); and which of the AICPA or CICA originated the WebTrust concept — keyed to AICPA as the party the contemporaneous US press credits, with CICA named as co-developer.
