# History: Real Estate Appraisers

**Industry:** [[industries/real-estate-appraisers|Real Estate Appraisers]]
**Primary Wave:** [[series/eras/wave-03-pc-spreadsheet|3 — PC & the Spreadsheet]]
**Secondary Wave:** [[series/eras/wave-07-big-data|7 — Big Data]]
**Origin Parent:** none — see note below
**Episode Tier:** 1
**Transferable Pattern:** When a statistical model and a licensed human can both produce the same output, the cheaper one is deployed for the routine case and the expensive one is kept only where liability requires a named, accountable signature.

> **Origin Parent note.** No origin among the eighteen fits. Insurance carriers' credibility-weighted pooled statistics and this industry's AVMs share a family resemblance — both blend a population-level model with an individual case — but insurance carriers' legacy file names no real-estate child, and the mortgage-secondary-market mechanism that actually drives appraisal policy (Fannie Mae, Freddie Mac, FHFA) is not one of the eighteen origins either. Treated as a direct Wave 3 child.

## Before

A residential appraiser's core artefact — the sales comparison grid — was always structurally a spreadsheet, decades before it ran on one. Rows for each comparable sale, columns for each adjustable feature (bedroom count, square footage, garage, condition, location), cells holding a dollar adjustment the appraiser derived from judgment and matched-pair analysis. Pre-PC, this was filled in by hand on a paper URAR (Uniform Residential Appraisal Report) form, with comps pulled from printed MLS books or a courthouse's paper deed records. The floor plan sketch was drawn with a ruler from tape-measured field dimensions. Every part of the job that is now software was, before the PC, a grid drawn by hand.

## The Origin Event — a voluntary standard, then a statute

This industry's origin event follows hospital systems' pattern more than dental's: **a law did the work, but it adopted something that already existed.**

| Date | What happened |
|---|---|
| **1986–87** | An ad hoc committee of US and Canadian appraisal organisations drafts what becomes USPAP — the Uniform Standards of Professional Appraisal Practice — as a **voluntary** industry standard. |
| **1987** | Copyright transfers to the newly formed **Appraisal Foundation**, established by eight founding valuation organisations. |
| **January 30 1989** | The Appraisal Foundation's Appraisal Standards Board formally adopts USPAP. |
| **August 9 1989** | **FIRREA** (Financial Institutions Reform, Recovery, and Enforcement Act) is signed. Title XI creates the **Appraisal Subcommittee** and makes state appraiser licensing federally mandatory for any transaction involving a federally regulated lender — converting the Foundation's voluntary standard into the statutory floor of an entire licensed profession. |

**The standard predates the statute by two and a half years.** FIRREA did not invent USPAP; it made compliance with an already-drafted voluntary standard a condition of doing federally backed mortgage business — the same mechanism, differently timed, that this vault's dental-practices file records for HITECH and EHRs, except here the industry itself wrote the standard the government later enforced.

## What Became Cheap

**Producing *a* valuation, for the routine case.** Two separate, later technologies did this, for two different customers:

- **Automated Valuation Models (AVMs)**, emerging in the **late 1990s** for institutional investors pricing collateralised mortgage loans, gave lenders a statistical alternative to a fee appraiser for straightforward assets.
- **Zillow's Zestimate**, launched with the site on **February 8 2006**, put a free consumer-facing AVM in front of every homeowner. Its own disclosed accuracy has moved over time — a median error around **$14,000 nationally by mid-2016**, tightening to roughly **2% for listed homes and 7% for unlisted homes** in Zillow's most recent published figures — good enough to anchor expectations, not good enough to replace a report a lender can rely on for an unusual property.

What did not get cheap: **the adjustment itself.** An AVM regresses against comparable transactions; it does not (per this vault's own hub note) replicate "the multi-attribute similarity judgment that experienced appraisers make intuitively" when choosing which three of twenty candidate comps actually represent the subject property.

## How It Was Actually Solved — for the parts that got solved

**Report-writing software** (TOTAL/WinTOTAL and predecessors from a la mode) replaced the paper URAR with a filled-in digital form, and **Apex Sketch** replaced the ruler-drawn floor plan — both straightforward digitisations of an existing paper object, not new capability.

**UAD and UCDP** — the Uniform Appraisal Dataset and Uniform Collateral Data Portal — standardised the *data fields* inside a report starting **around 2011–2012** *(the exact mandate date could not be independently re-verified in this session; treat as approximate)*, so that Fannie Mae and Freddie Mac's systems could parse a report programmatically rather than a human re-keying it. **Fannie Mae's Collateral Underwriter**, reported to have launched **around 2015**, then ran that standardised data against a risk model to flag adjustment patterns and comparable selections that looked statistically anomalous — automated second-guessing of the human grid, at the scale of every loan Fannie Mae touches. *(Launch year is the commonly reported figure in industry sources; not independently confirmed to a primary source here.)*

## The Trade-Off

**Independence was bought with a fee-extracting middle layer, and the appraiser paid for it.**

The 2008 crisis produced documented evidence of lenders pressuring appraisers to hit a target value to make a loan work. The response — the **Home Valuation Code of Conduct**, effective **May 1 2009**, developed by Freddie Mac, the FHFA and the New York Attorney General's office — barred loan officers from selecting or directly pressuring the appraiser. Dodd-Frank's **Appraiser Independence Requirements (2010)** made a version of that separation permanent federal rule.

**The practical effect was to require an intermediary between lender and appraiser — and that intermediary is the Appraisal Management Company.** AMCs proliferated in HVCC's wake, and this vault's own hub note records the resulting economics: AMCs "extract 30–40% of the appraisal fee, leaving appraisers $250–$350 for an assignment that takes 4–6 hours." *(That figure is this industry's own widely repeated claim, not an independently audited number — treat it as directional.)* Independence from lender pressure was real and worth having. It was purchased by inserting a fee layer between the appraiser and the money, and the appraiser's fee is what shrank to pay for it.

## The Binding Constraint

**The appraisal waiver threshold — a number set by Fannie Mae and Freddie Mac, not by the appraiser's software.** GSE automated underwriting (Desktop Underwriter, Loan Prospector, and now Collateral Underwriter's risk scoring) can determine that a given loan's collateral risk is low enough that **no appraisal is required at all**. Below that threshold, the assignment simply does not exist, regardless of how fast or accurate a human appraiser's grid is. This is dental's binding-constraint pattern with the sign flipped: dental's number caps what a patient gets *paid*; this number caps how many assignments the profession gets *offered*, and it is set by two GSEs and their regulator, not negotiated with the people it affects.

**A finding flagged, not asserted as settled:** reporting from 2020–2022 raised documented allegations of undervaluation in appraisals of Black-owned homes, prompting the federal government's **PAVE (Property Appraisal and Valuation Equity)** interagency task force. *(I could not independently verify the task force's founding date or specific study citations to a primary source in this session — this is a live, contested area and should be re-researched before it appears in a script.)*

## What's Still Open

- [[problems/real-estate-appraisers/high-impact|🔴 Market-calibrated adjustment modelling from MLS data]] — automating the grid, not replacing the judgment
- [[problems/real-estate-appraisers/low-impact-2|🟡 MLS comparable similarity ranking]]
- [[niches/real-estate-appraisers/comp-selection-and-adjustment/profile|Comp Selection & Adjustment]]
- [[niches/real-estate-appraisers/avm-collateral-valuation-analytics/profile|AVM & Collateral Valuation Analytics]]
- [[niches/real-estate-appraisers/gse-collateral-policy-analytics/profile|GSE Collateral Policy Analytics]] — where the waiver threshold actually lives
- [[niches/real-estate-appraisers/appraisal-management-review-crossref/profile|Appraisal Management Review]] — the AMC fee layer, as a business
- [[niches/real-estate-appraisers/desktop-and-hybrid-appraisers/profile|Desktop & Hybrid Appraisers]]

## The Transferable Pattern

> **Two different customers can be satisfied by two different qualities of answer to the same question. Find out who is allowed to accept the cheap one, and the software market splits along exactly that line — automatically, without anyone designing it to.**

A GSE buying a loan below a risk threshold will accept an AVM's number. A court, an estate, or a lender above that threshold will not — because somewhere downstream a human signature has to be defensible under USPAP and under oath. An FDE building appraisal AI should ask which side of that line their customer sits on before proposing to replace anything: automating the grid for a licensed appraiser is a different, much larger, and much less contested market than replacing the appraiser.

**Sources:** Wikipedia, *Uniform Standards of Professional Appraisal Practice*, *Zillow*; The Appraisal Foundation (founding 1987, USPAP adoption Jan 30 1989); FIRREA Title XI (Aug 9 1989); Wikipedia/HVCC summaries (effective May 1 2009; Freddie Mac, FHFA, NY AG); Dodd-Frank Act, Appraiser Independence Requirements (2010); this vault's `industries/real-estate-appraisers.md` (AMC fee compression, AVM competition) and `problems/real-estate-appraisers/*.md`. UAD/UCDP mandate timing, Collateral Underwriter launch year, and PAVE task force specifics are flagged above as approximate or unverified in this session and should be re-checked before use in a script.
