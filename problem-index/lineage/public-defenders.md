# Lineage: Public Defenders

**Industry:** [[industries/public-defenders|Public Defenders]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** Standard 13.12 of the 1973 National Advisory Commission on Criminal Justice Standards and Goals — the caseload ceiling of 150 felonies, 400 misdemeanours, 200 juvenile, 200 mental-health cases or 25 appeals per attorney per year
**Builder:** Law Enforcement Assistance Administration
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

*Gideon v. Wainwright* (1963, 372 U.S. 335) made counsel for indigent felony defendants a constitutional requirement. It said nothing about how many clients one lawyer could carry.

That silence is the problem. A public defender office does not choose its intake: every arrest of a poor defendant in its jurisdiction is an appointment. Its budget is set by a county or state that also funds the prosecution and the police. So the only variable that absorbs growth is **time per case**, and without a number, there was no way to say that time had run out — to a judge, to a funding body, or to the lawyer herself.

The office could report cases handled. It could not report cases handled *badly*, because nothing defined too many.

## What Got Built

A number — five of them, in one line of a federal commission's report.

The National Advisory Commission's Task Force on Courts, in Chapter 13, "The Defense" (1973), included Standard 13.12 on public defender workload: the caseload of an office should not exceed, per attorney per year, **150 felonies; 400 misdemeanours, excluding traffic; 200 juvenile court cases; 200 Mental Health Act cases; or 25 appeals.**

Two design choices matter. The limits are **per case type, not per case** — a felony counts as a felony whether it is a shoplifting enhancement or a homicide. And they are written as an *office* average, not a ceiling on each individual lawyer.

The numbers became the benchmark almost everything else is measured against. When the Bureau of Justice Statistics surveyed county-based offices for 2007, it used the NAC figures as its yardstick and found that about **73% of those offices exceeded the maximum recommended caseload**, 15% had formal caseload limits, and 59% had neither limits nor authority to refuse appointments.

## Who Built It, And Why Them

A Justice Department commission, housed in the Law Enforcement Assistance Administration — the grant agency created by the Omnibus Crime Control and Safe Streets Act of 1968.

**Why a federal crime-control agency and not the defenders?** Because defenders had the problem and no standing. A number published by a defenders' association reads as a request for more staff. A number published by a national commission attached to the Justice Department reads as a standard. LEAA administered federal funding to state and local justice systems; a standard is the natural instrument of a funder describing what its money should buy — this note's inference, not a sourced statement of LEAA's intent.

That shaped the artefact. A grant agency needs something short, countable and auditable from a docket report. Five integers per attorney per year are exactly that: they can be checked from case-opening counts without anyone opening a file. What they could not do was weight complexity, because complexity is not in the docket report.

## What It Cost

**The standard counts cases, not work.** A felony in 1973 did not carry body-camera footage, phone extractions or digital discovery; the number never moved. Offices that complied on paper could still be drowning.

Its office-average framing let a jurisdiction meet it on paper while individual lawyers far exceeded it. And because it counted cases without weighting them, it gave funders a single ratio to argue with, rather than a measure of what adequate representation took.

The number was also advisory. Most offices never gained the power to refuse appointments above it.

## What You Still Touch

When a defender office tells its county it is "at three times the standard," the standard is almost always this 1973 table. The vault's caseload-triage problem is the direct descendant: a triage tool exists because the ceiling was published, exceeded and never enforced.

- [[problems/public-defenders/high-impact|🔴 Caseload Triage and Strategic Resource Allocation]]
- [[problems/public-defenders/worker-life-1|🟢 Defender Moral Injury from Systemic Inadequacy]]
- [[niches/public-defenders/indigent-defense-standards-commissions/profile|Indigent Defence Standards & Oversight Commissions]]
- [[niches/public-defenders/misdemeanor-volume/profile|Misdemeanor Volume Practice]]

**Sources:** NLADA, *National Advisory Commission — Black Letter* (text of Standard 13.12: "felonies per attorney per year: not more than 150; misdemeanors (excluding traffic) per attorney per year: not more than 400", plus 200 juvenile, 200 Mental Health Act, 25 appeals; 1973); Bureau of Justice Statistics, Farole & Langton, *County-based and Local Public Defender Offices, 2007* (NCJ 231175, September 2010) — attributes the NAC to the US Department of Justice, cites *Task Force on Courts, Chapter 13: The Defense* (1973), gives the 73% / 15% / 36% / 59% figures and notes the standards apply to the office, not each attorney; Wikipedia, *Law Enforcement Assistance Administration* (created by the Omnibus Crime Control and Safe Streets Act of 1968; "LEAA included the National Advisory Commission on Criminal Justice Standards and Goals"); Wikipedia, *Public defender (United States)* (*Gideon*, 1963, 372 U.S. 335). WebSearch was unavailable this session (session cap reached); research was by WebFetch on known URLs. RAND and the ABA pages for the 2023 National Public Defense Workload Study returned 403, so its findings are not used. ⚠️ **Not established:** how the NAC arrived at its figures — they are widely said to have come from an NLADA committee's experience rather than empirical time study, but NLADA's commentary is members-only and this was not confirmed; the commission's chair, members and appointing official; and whether LEAA or the Attorney General formally constituted it. The key uses LEAA because the fetched sources place the commission inside it; `US Department of Justice` would be the fallback key. The complexity argument in *Who Built It* is this note's inference.
