# Portfolio Company Reporting Normalisation

**Industry:** [[private-equity-firms|Private Equity Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Portfolio monitoring software stores KPIs beautifully once someone has turned twelve CFOs' monthly packages into one consistent definition of revenue, EBITDA and churn.
**Tags:** #large-language-models #bert #feature-engineering #change-point-detection #evaluation-metrics #data-integration #automation

## The Problem
A mid-market fund holds 8–25 portfolio companies, each sending a monthly reporting package: P&L, balance sheet, cash flow, covenant calculations, and a KPI page whose contents depend on the business — bookings and net revenue retention for software, same-store sales for multi-site services, backlog and gross margin by job for contractors. The packages arrive as Excel and PDF in each company's own format, with each company's own definition of adjusted EBITDA, its own chart of accounts and its own idea of what a pro forma add-on contribution means. A fund finance analyst or associate rekeys them into the portfolio monitoring tool, chases late submissions, and rebuilds the quarterly portfolio review.

## What Already Exists
S&P iLEVEL, Chronograph, Cobalt (FactSet), Allvue and Dynamo provide portfolio monitoring with templated data collection portals, KPI storage and LP reporting outputs. Fund administrators produce fund-level accounting. Generic data ingestion tools and LLM extraction can read spreadsheets and PDFs.

## The Customisation Gap
The monitoring platforms assume clean input through a portal template; the reality is that portfolio CFOs send their own packages and the template is filled by someone at the sponsor. The gap is a mapping layer that learns each company's chart of accounts and KPI definitions, maps them to the fund's standard definitions with the adjustments made explicit, detects when a company quietly changes a definition (a restated churn calculation, a reclassified expense moving into "one-time"), reconciles covenant EBITDA to management EBITDA to the lender's definition, and handles add-on acquisitions that change the comparable base mid-year. This is industry logic — credit-agreement definitions, pro forma conventions, ILPA reporting expectations — that a generic extraction tool does not carry.

## Impact If Solved
Portfolio problems surface in the monthly numbers weeks before they surface at the board, but only if the numbers are comparable and on time. Removing manual normalisation shortens the close-to-insight cycle from weeks to days and makes definition drift — a common precursor to bad news — visible when it happens.
