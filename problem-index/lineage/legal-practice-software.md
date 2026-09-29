# Lineage: Legal Practice Software

**Industry:** [[industries/legal-practice-software|Legal Practice Software]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** LEDES 1998B — the pipe-delimited, 24-field ASCII invoice file in which a law firm bills a corporate client or insurer, each time entry carrying a UTBMS task code and activity code
**Builder:** LEDES Oversight Committee
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

The problem belonged to the buyer of legal work.

By the mid-1990s large US law departments and liability insurers were spending heavily on outside counsel and could not see what they were paying for. A law firm's bill was a narrative. The UTBMS project's own account of the period is blunt: paper bills were "virtually impossible to digest," and a single timekeeper's description of one day's work could run for "multiple paragraphs or pages."

That made the client's controls unenforceable at scale. A law department could write billing guidelines — no block billing, no partner time on document review — but checking every invoice against them meant a human reading every line. The time entry existed; nothing could *test* it.

## What Got Built

Two linked artefacts: a vocabulary and a file.

The vocabulary is the **Uniform Task-Based Management System (UTBMS)** — a three-tier code set that tags each time entry with *what phase of the matter* (litigation L-codes, from case assessment through appeal), *what kind of act* (A-codes: research, drafting, communicating), and, for disbursements, *what kind of cost* (E-codes: travel, transcripts, experts).

The file is **LEDES 1998B**: an ASCII, pipe-delimited format of 24 fields, one line per time or expense entry, each line carrying invoice, matter, timekeeper and code identifiers. It dates to 1998 and remains, in its steward's words, the most widely used e-billing standard in the US legal industry. Later XML versions (2000, 2.0 in 2006, 2.1 in 2008, 2.2 in 2020) and an international variant, 1998BI (ratified 2006), never displaced it.

Put together, a bill became something a receiving system could **reject automatically** — an entry with the wrong task code, a rate above the agreed one, a timekeeper not approved for the matter.

## Who Built It, And Why Them

A buyer-side coalition, coordinated by an accountancy.

UTBMS came out of a joint effort of the **American Bar Association Section of Litigation, the American Corporate Counsel Association**, and a group of major corporate clients and law firms coordinated by **Price Waterhouse LLP**. LEDES began in 1995 as an informal industry project led by Price Waterhouse's Law Firm and Law Department Services Group, and was incorporated as the LEDES Oversight Committee — a California mutual-benefit nonprofit — in 2001. The Committee now maintains both LEDES and UTBMS, and so is keyed here as the standard's owner.

**Why them and not the practice-software vendors?** Because no vendor gained by standardising the bill. A proprietary billing export locked a firm in; a standard one let the client dictate terms to every firm at once. The people with the motive were the payers — law departments and insurers who wanted to audit hundreds of firms with one rule set — and the neutral party with both audit culture and access to firms on each side was a Big Six accountancy.

That shaped the artefact. It is a flat, one-row-per-entry file because its purpose is line-by-line rule checking, not presentation. The codes describe the *task*, not the outcome, because what the client was policing was time.

## What It Cost

**The code set turned judgement into a classification exercise.** A lawyer now does the work and then decides which of a few dozen codes it was, and the answer determines whether the line is paid. Codes built for litigation fit transactional, IP or regulatory work badly, which is why patent and trademark codes (2007), eDiscovery (2011) and governance, risk and compliance (2015) had to be bolted on.

It also entrenched the hour. By making time entries machine-auditable, the standard made the timesheet the unit of trust between firm and client.

## What You Still Touch

Every practice-management product sold to firms with corporate or insurance clients must emit a LEDES file; an insurance-defence lawyer's rejected line item is a UTBMS rule firing. And the unbilled hour the industry now chases exists partly because a coded, audited entry costs more effort to create than the narrative it replaced.

- [[problems/legal-practice-software/high-impact|🔴 Time Capture & the Unbilled Hour]]
- [[niches/legal-practice-software/insurance-defense-platforms/profile|Insurance Defense & Panel Counsel Platforms]]
- [[niches/legal-practice-software/passive-timekeeping-reconstruction/profile|Passive Timekeeping & Billable Reconstruction]]

**Sources:** ledes.org home page (Committee "first formed in 1995 as an informal group"; website established 1998) and *LEDES 98B Format* page ("ASCII, pipe delimited format containing 24 fields"; "most-widely used ebilling standard in the legal industry in the US"; documentation revised August 2014); Wikipedia, *Legal Electronic Data Exchange Standard* (1995 start led by PricewaterhouseCoopers' Law Firm and Law Department Services Group; 2001 incorporation as a California mutual-benefit nonprofit; format dates 1998, 1998B, XML 2000, 1998BI 2006, XML 2.0/2.1/2.2); utbms.com history (mid-1990s; ABA, Association of Corporate Counsel and PricewaterhouseCoopers joint group; "virtually impossible to digest" and "multiple paragraphs or pages" quotations); Wikipedia, *Uniform Task-Based Management System* (ABA Section of Litigation, American Corporate Counsel Association, Price Waterhouse LLP; IP codes 2007, eDiscovery 2011, GRC 2015). WebSearch was unavailable this session (session cap reached); research was by WebFetch on known URLs. ⚠️ **Not established:** the exact year the UTBMS litigation code set was first published (sources say only "mid-1990s"); the names of the individuals at Price Waterhouse who led the project; and the specific field names of the 24 LEDES 1998B fields, which are in a downloadable spreadsheet not fetched. The inference that vendors lacked a motive to standardise is this note's argument, not a sourced claim.
