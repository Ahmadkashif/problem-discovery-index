# Lineage: Real Estate Appraisers

**Industry:** [[industries/real-estate-appraisers|Real Estate Appraisers]]
**Wave:** [[series/eras/wave-03-pc-spreadsheet|3 — PC & the Spreadsheet]]
**The tool:** the Uniform Residential Appraisal Report — Fannie Mae Form 1004, the same document as Freddie Mac Form 70 — and its sales comparison grid of three comparable sales adjusted line by line
**Builder:** Fannie Mae & Freddie Mac
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

The buyer of a mortgage never sees the house.

In 1970 Congress established Freddie Mac, through the Emergency Home Finance Act, "to expand the secondary market for mortgages … by buying mortgages made by savings and loan associations and other depository institutions." Fannie Mae, made private in 1968, was the other buyer. A loan bought from a thrift in another state is only as good as its collateral, and the buyer's only evidence of the collateral was a value opinion signed by an appraiser it had never met.

**The constraint was review at volume.** A purchaser of thousands of loans had to check each valuation's reasoning from paper, at a desk, without a site visit.

## What Got Built

A form, and inside it a grid.

The URAR's load-bearing section is the sales comparison approach. The March 2005 edition prints four columns — SUBJECT, COMPARABLE SALE # 1, # 2, # 3 — and a row for each feature, with a dollar adjustment in each comparable's cell. At the foot it prints a **Net Adjustment (Total)**, the **Adjusted Sale Price of Comparables**, and a **Net Adj. %** and **Gross Adj. %** for each sale.

The rules sit in Fannie Mae's Selling Guide: "A minimum of three closed comparables must be reported," sales closed within 12 months "should be used," and adjustments "must reflect the market's reaction," derived by "statistical analysis, modeling, paired sales, or other commonly accepted methods."

**An opinion of value became auditable arithmetic**: three sales that bracket the subject, each walked to the subject's features in plain dollars.

## Who Built It, And Why Them

The two government-sponsored enterprises, because they held the risk and set the terms.

A lender making a loan can send its own appraiser or drive past the house. A buyer of loans from thousands of lenders cannot. **The party that buys collateral sight unseen is the one that needs every report in one layout — and the one with the leverage to demand it**, since a loan written on another form is a loan it need not buy. The same logic explains the grid's shape: a human underwriter reading paper can check three bracketing sales in minutes, and cannot check a regression. Both readings are this note's inference, not a documented rationale.

Which of the two designed the first uniform version, and when, was **not established**. The form carries both numbers and both names, so this note keys both.

The PC layer came from the appraisers' side. a la mode says it was "begun in 1985" in Oklahoma City "with the simple idea that real estate appraisers could use new 'personal computer' technology to more quickly and efficiently complete appraisal reports" — a DOS form-filler. **The software filled in the GSEs' grid faster; it did not change the grid.**

## What It Cost

**The grid demands a dollar figure per feature and supplies no way to derive one.** The vault's own notes put a matched-pair derivation at one to two hours per adjustment, which is why junior appraisers fall back on "$1,500 per bathroom, $5,000 per garage." The form accepts either.

It also reduced a market to three rows, chosen from 15 to 25 candidates per the vault — the report's most consequential judgment, of which the form records only the result.

And it prints numbers the buyer disowns. Every comparable carries a net and gross adjustment percentage, yet Fannie Mae's guide states that it "does not have specific limitations or guidelines associated with net or gross adjustments."

## What You Still Touch

The grid is being rebuilt as data: from **November 2 2026**, every new submission to the GSEs' Uniform Collateral Data Portal must be in UAD 3.6, the redesigned report's format:

- [[problems/real-estate-appraisers/high-impact|🔴 Market-Calibrated Comparable Adjustment Development from Matched-Pair Sales]] — the dollar in each cell
- [[problems/real-estate-appraisers/low-impact-1|🟡 Comparable Sale Selection Assistance]] — "the best three comps for this subject"
- [[niches/real-estate-appraisers/comp-selection-and-adjustment/fix|Matched-Pair Adjustment Derivation from MLS Sales Data]]
- [[niches/real-estate-appraisers/comp-selection-and-adjustment/buy|One-Click Adjustment Grid Population from MLS Data]]
- [[niches/real-estate-appraisers/gse-collateral-policy-analytics/profile|Secondary Market Collateral Policy & Analytics]] — the policy layer above the form

**Sources:** Freddie Mac Form 70 / Fannie Mae Form 1004, March 2005 edition, PDF read directly (sf.freddiemac.com), for the four grid columns, the Net Adjustment (Total) and Adjusted Sale Price rows, and the Net Adj. % and Gross Adj. % fields. Fannie Mae Selling Guide B4-1.3-08, "Comparable Sales", and B4-1.3-09, "Adjustments to Comparable Sales" (both dated June 4 2025), fetched, for the three-comparable minimum, the 12-month guidance, "market's reaction", the list of accepted methods and the no-limits statement. Wikipedia, *Freddie Mac*, fetched, for the Emergency Home Finance Act of 1970 quotation and Fannie Mae's 1968 split. Freddie Mac, "UAD Redesign Timeline" fact sheet, PDF read directly, for broad production from January 26 2026, the November 2 2026 mandate and May 3 2027 retirement of UAD 2.6. a la mode company blog (July 30 2004), fetched, for 1985, Oklahoma City, the quotation and "DOS-based form filling software". This vault's appraiser problem and niche notes, and `history/real-estate-appraisers.md` (vault material, not independent corroboration). ⚠️ **Not established:** when the first uniform residential appraisal form was issued and whether Fannie Mae or Freddie Mac designed it — Wikipedia's *URAR* article gives no origin, and search summaries give only revisions of September 1986, July 1993 and March 2005 from a HUD page that did not resolve, so no origin year appears in the body. A search summary says one dynamic URAR replaces Form 1004 and its variants; not read at source, so not asserted. a la mode's founder is described only as "an appraiser" in a search summary and is not named. Freddie Mac's 1970 purpose statement is quoted via Wikipedia, not the statute.
