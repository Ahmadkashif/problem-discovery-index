# Wave 3 — The PC & the Spreadsheet (1979–1992)

**Trigger:** VisiCalc ships for the Apple II, Oct 17 1979 ($100); Lotus 1-2-3, Jan 26 1983 ($495); Excel for Mac Sept 30 1985; Excel for Windows Nov 19 1987
**What went to ~zero:** the cost of **building a model** — for the first time, without a programmer
**Failure class produced:** the missing join, self-inflicted and distributed across every desk in the building

> **This is the most important wave in this vault and the one it never mentions.** It created no industry of its own. It is the live incumbent in **1,405 files** here. An FDE is almost always replacing a spreadsheet, and the spreadsheet won for reasons that still hold.

## What Was True The Day Before

Computation belonged to the data-processing department. If a manager wanted to know what happened to margin when volume fell 8%, they filed a request and waited — days, sometimes weeks. The delay was not laziness; it was that the question had to be turned into a program by someone who wrote programs.

The consequence was that **most business questions were never asked.** Not answered wrongly — never asked, because the cost of asking exceeded the value of knowing.

## The Trigger

VisiCalc collapsed that cost to zero and put it on the desk of the person with the question. The grid is a programming environment that does not look like one: you describe relationships between cells and it recomputes the consequences instantly. Dan Bricklin built a tool for a finance class; he shipped a general-purpose modelling language that required no training.

The "killer app" effect is real — Apple II unit sales went from roughly 35,000 in 1979 to about 78,000 in 1980, dealers bundled the software with the machine, and VisiCalc sold 700,000–1,000,000 copies over its life. *(The widely-quoted "25% of Apple II buyers bought it for VisiCalc" traces to unsourced press retellings, not a study. Directionally right, spuriously precise — do not cite the number.)*

## The Competitive Fight

A three-round succession, and each round turned on the same thing: **being native to where the customer already was.**

- **VisiCalc → Lotus 1-2-3.** 1-2-3 was hand-written in assembly and ran fast, integrated spreadsheet, database and charting in one product, and targeted the IBM PC natively while VisiCalc shipped a port. Native beat ported.
- **Lotus → Excel.** Excel was GUI-native from birth (Mac 1985, Windows 1987). Lotus treated Windows as an afterthought — its first real Windows release came in 1991 and a competent one in 1993, by which point the market was gone. Lotus also spent its effort on integrated suites (Jazz, Symphony) the market did not want instead of hardening the core.

Both defeats are the same defeat. The incumbent optimised for the platform that was winning yesterday.

## Why the Spreadsheet Never Loses

This is the question the vault needs answered and never asks. The sources converge on three reasons:

1. **It is infrastructure, not an app.** Spreadsheets sit underneath certified, audited financial processes. Replacing one means re-verifying every formula for a regulator. The switching cost is compliance work, not training.
2. **It owns the ad-hoc.** BI and purpose-built tools report well on data that already exists. They are weak at exactly what the spreadsheet is for: entering data, restructuring a model mid-thought, and asking "what if."
3. **Zero training cost beats any efficiency gain.** Everyone already knows it. A specialised tool must beat not just the spreadsheet but the spreadsheet *plus* the absence of a learning curve.

**The FDE lesson:** when you propose replacing a spreadsheet, you are proposing to take away a general-purpose tool and hand back a special-purpose one. That trade is only worth it where the generality is actively harmful — which is precisely where it is.

## What It Broke

Business logic escaped into files nobody governs, and the error rate is not small.

Raymond Panko's synthesis of **13 field audits of real operational spreadsheets (1995–2004) found ~94% contained errors**, with an average cell error rate around **5.2%**. Lab studies (14 studies, 967 subjects working alone) show ~3.9%. Errors are rare per cell and near-certain somewhere in a large model, hard to detect, and their authors are systematically overconfident. *(The 94% figure applies to audited operational spreadsheets, not "all spreadsheets" — the distinction is routinely dropped.)*

The documented consequences:

| Case | Date | What happened |
|---|---|---|
| **JPMorgan "London Whale"** | 2012 | A manual copy-paste made a VaR model divide by a *sum* instead of an *average*, understating risk. $6.2B loss, $920M in fines. *(Regulators attribute the loss to a chain of modelling, risk-limit and oversight failures — the spreadsheet was one link, not the sole cause.)* |
| **Reinhart-Rogoff** | 2013 | **Three separate errors, not one** — a coding error (`AVERAGE(L30:L44)` should have read `L30:L49`, dropping five countries), selective country exclusion, and an unconventional weighting scheme. **The spreadsheet error was not necessarily the largest contributor.** Corrected, the headline growth figure moved from −0.1% to +2.2%. The original had been cited by policymakers arguing for austerity. *(Corrected at H5 — the single-formula telling is a simplification this vault previously repeated.)* |
| **Public Health England** | Oct 2020 | Legacy `.xls` caps at 65,536 rows. Overflow rows were silently dropped. **15,841 positive COVID cases** never reached contact tracing. |

Gartner formally named the resulting phenomenon **"shadow IT" in 2009**. The spreadsheet is the original shadow-IT artefact: ungoverned business logic, built outside IT's sight, load-bearing anyway.

## Children in This Vault

Wave 3 created no industry. These are industries whose *core working artefact* is still a spreadsheet model.

**Primary:**
- [[industries/general-contractors|General Contractors]]
- [[industries/energy-auditors|Energy Auditors]]
- [[industries/tax-prep-firms|Tax Prep Firms]]
- [[industries/public-adjusters|Public Adjusters]]
- [[industries/estate-planning|Estate Planning Law Firms]]
- [[industries/small-law-firms|Small Law Firms (Solo and 2-10 Attorney Practices)]]
- [[industries/printing-shops|Printing Shops]]
- [[industries/independent-publishers|Independent Publishers]]
- [[industries/video-production-smb|SMB Video Production]]
- [[industries/accounting-firms-smb|SMB Accounting Firms]]
- [[industries/engineering-consultants|Engineering Consultants]]
- [[industries/environmental-consultants|Environmental Consultants]]
- [[industries/grant-writers|Grant Writers]]
- [[industries/commercial-real-estate|Commercial Real Estate]]
- [[industries/real-estate-appraisers|Real Estate Appraisers]]
- [[industries/event-planning|Event Planning]]

**Secondary:**
- [[industries/electrical-contractors|Electrical Contractors]]
- [[industries/plumbing-contractors|Plumbing Contractors]]
- [[industries/developer-tools-vendors|Developer Tools Vendors]]
- [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
- [[industries/no-code-app-builders|No-Code App Builders]]
- [[industries/catering-companies|Catering Companies]]
- [[industries/insurance-restoration|Insurance Restoration]]
- [[industries/metal-fabrication|Metal Fabrication]]
- [[industries/hr-consultants|HR Consultants]]
- [[industries/land-surveyors|Land Surveyors]]
- [[industries/hoa-management|HOA Management]]
- [[industries/property-management|Property Management]]
- [[industries/data-analytics-consultants|Data Analytics Consultants]]
- [[industries/hvac-contractors|HVAC Contractors]]
- [[industries/painting-contractors|Painting Contractors]]
- [[industries/legal-practice-software|Legal Practice Software]]

**Sources:** Wikipedia, *VisiCalc*, *Lotus 1-2-3*, *Lotus Development*; The Register, *When Lotus met Excel*; Panko, *What We Know and Don't Know About Spreadsheet Errors* (arXiv 1602.02601 and ResearchGate); Henrico Dolfing and thekeycuts.com (JPMorgan London Whale); The Conversation and Retraction Watch (Reinhart-Rogoff); The Register and digitalhealth.net (Public Health England, Oct 2020); t2informatik.de (Gartner, "shadow IT", 2009).
