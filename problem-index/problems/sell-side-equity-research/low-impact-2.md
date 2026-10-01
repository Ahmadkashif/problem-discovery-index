# Spreading the Print Into the Analyst's Own Model

**Industry:** [[sell-side-equity-research|Sell-Side Equity Research]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Reported results can now be bought as clean structured data, but every analyst's model has its own layout, its own segment definitions and its own non-GAAP adjustments, so the last mile is still typed by an associate at 7 a.m.
**Tags:** #large-language-models #transformers #feature-engineering #evaluation-metrics #data-integration #automation #quick-win

## The Problem
When a company reports, the press release, the supplementary data sheet and later the 10-Q contain the numbers the model needs: segment revenue, margins, KPIs, share count, cash flow lines, guidance. An associate copies them into the analyst's model — a workbook built over years in the analyst's own layout, with segment splits that may not match the company's current presentation, adjusted EPS bridges reflecting the analyst's view of what is "one-off", and KPIs the company reports in a slide deck rather than a table. Every company in coverage reports in the same few weeks.

## What Already Exists
Daloopa and Canalyst (now part of AlphaSense through Tegus) sell fundamental datasets and standardised models extracted from filings and decks, with links back to source. S&P Capital IQ, FactSet and Bloomberg provide standardised financials. Excel add-ins pull those values into cells.

## The Customisation Gap
The standardised model is not the analyst's model. The gap is the mapping from the vendor's (or the filing's) line items to the analyst's rows: a company re-segments and the analyst keeps the old split for continuity; the analyst's "adjusted EBITDA" excludes items the company includes; a KPI changes definition mid-year. That mapping lives in the associate's head and breaks silently. What is needed is a per-model mapping layer that learns the analyst's layout and adjustments from prior quarters' fills, proposes this quarter's fill with source links, and flags every cell where the company's presentation changed — rather than another standardised dataset.

## Impact If Solved
The first hour after the print is the hour the department is paid for, and it is spent copying numbers. Moving the fill to a reviewed, sourced proposal leaves the associate checking exceptions and the analyst reading the quarter instead of waiting for the model.
