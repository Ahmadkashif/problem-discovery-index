# Lineage: Personal Injury Law Firms

**Industry:** [[industries/personal-injury-law|Personal Injury Law Firms]]
**Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**The tool:** Colossus — the rules-based bodily-injury evaluation expert system that converts coded injuries into severity points and a recommended settlement range
**Builder:** Computations Pty Ltd
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

The tool that shapes a personal injury firm's work was built for the other side of the table.

Before it, the value of a bodily-injury claim — above all the "general damages" for pain and suffering, which have no invoice — was set by an adjuster's judgment. Experienced adjusters knew roughly what a whiplash or a fractured wrist settled for in their region. That judgment was expensive, inconsistent between adjusters, and impossible for head office to audit or move. An insurer losing money on injury claims had no lever to pull except hiring and training.

## What Got Built

An expert system that made the adjuster's judgment a lookup.

In the version later described by insiders, Colossus holds about **600 injury codes**, each carrying a severity value; the insurer assigns a dollar amount per severity point, with separate values for permanent impairment, configured by economic region. The adjuster enters the diagnosis, treatment, duration and prognosis from the medical records, and the system returns a recommended settlement range. Its values are set in a "benchmark session" in which the insurer's experienced adjusters value hypothetical claims, then tested against a "closed file study" of settled claims — and the insurer can **re-tune** the values, which is where most of the controversy lives. A 1992 academic account put its Australian knowledge base at around 15,000 rules and noted it excluded spinal cord injury, brain damage and nervous shock.

## Who Built It, And Why Them

**Computations Pty Ltd**, an Australian insurance-systems firm later renamed **Continuum**, at the request of **GIO**, the Australian government insurance office.

The Consumer Federation of America's 2012 report — written with a former Allstate Colossus tuning manager — dates the commission to **1988**: GIO was losing money and asked Computations to help build a system to reduce claims payments. A 1992 *Australian Law Journal* article by Graham Greenleaf reports it in use across GIO's funds-administration offices from **July 1989**. Why a claims insurer with a software house: GIO had the closed files and the adjusters whose judgment could be encoded; Computations had the means to package that judgment as a licensable product. After GIO reported lower payouts, other insurers asked to license it. The CFA report states Allstate was the first American insurer to test it and USF&G the first to use it, and that Continuum merged with **Computer Sciences Corporation in 1996**, which marketed it thereafter.

Its American scale came through **Allstate's Claims Core Process Redesign**, built with McKinsey from the mid-1990s. A McKinsey slide later released in litigation read: "Allstate gains, others must lose."

## What It Cost

**The evaluation became a function of what could be coded, not of what happened to the person.**

Colossus values what is entered: diagnoses, treatment types, visit counts, documented duration. Pain that is not in the records in a form an adjuster can code does not score. And because the insurer controls the tuning, a claimant's lawyer is arguing against a number whose parameters they cannot see. The system also replaced a negotiation between two people who could exercise judgment with a negotiation between a person and a range the adjuster may not be authorised to exceed.

## What You Still Touch

Every PI demand package that itemises ICD-coded diagnoses, lists every treatment date, and quotes the doctor's words on permanency is being written for Colossus's input screen — even at firms that never name it.

- [[problems/personal-injury-law/low-impact-1|🟡 Demand Letter Generation and Settlement Negotiation Preparation]] — a document shaped for a coder
- [[problems/personal-injury-law/high-impact|🔴 Medical Record AI — Automatic Chronology, Injury Extraction, and Causation Linking]] — extracting what the evaluator scores
- [[problems/personal-injury-law/worker-life-1|🟢 Medical Records Review and Chronology Compilation]]
- [[niches/personal-injury-law/auto-injury-claims-analytics-crossref/profile|Bodily Injury Claims Evaluation & Medical Review Analytics]]
- [[niches/personal-injury-law/demand-letter-settlement/profile|Demand Letter & Settlement Valuation]]

**Sources:** Consumer Federation of America, Romano & Hunter, *Low Ball: An Insider's Look at How Some Insurers Can Manipulate Computerized Systems to Broadly Underpay Injury Claims*, 4 June 2012, text read directly (1988 GIO request to Computations Pty Ltd, later Continuum; Allstate first to test, USF&G first to use; 1996 merger with CSC; ~600 injury codes, severity points, economic regions, benchmark session, closed file study, tuning; CCPR; McKinsey "Allstate gains, others must lose", quoted via Berardinelli et al., *From Good Hands to Boxing Gloves*, 2006). Graham Greenleaf, "A Colossus Come to Judgment: GIO's Expert System on General Damages", *Australian Law Journal*, 1992 — the July 1989 rollout, ~15,000 rules and exclusions are taken from a search-result summary of the AustLII copy; the page itself refused connection and SSRN returned 403, so these are **not read directly**. CLM Magazine, "Colossal Cleanup" (~600 injury profiles, adjuster data entry). ⚠️ **Not established:** the individuals who designed Colossus; whether GIO or Computations did the core design (sources say "jointly" and "asked … to assist") — keyed to Computations as the party that built and licensed it; the date Allstate went live with Colossus (commonly given as 1995 in plaintiff-side sources; I did not find a primary date). The CFA is an advocacy organisation and its co-author a former Allstate employee; its account is not neutral. The claim that demand packages are written for Colossus is inference from the input structure.
