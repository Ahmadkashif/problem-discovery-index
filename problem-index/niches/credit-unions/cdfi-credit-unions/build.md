# CDFI Community Impact Analytics Platform

**Niche:** [[niches/credit-unions/cdfi-credit-unions/profile|CDFI-Designated Credit Unions]]
**Industry:** [[industries/credit-unions|Credit Unions]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** CDFI credit unions must prove community impact to retain certification and win grants — but no tool measures whether their lending actually improved economic outcomes in target communities versus simply processing loans at the right addresses.
**Tags:** #gradient-boosting #regression #tabular-ml #causal-inference #compliance

## The Problem
A CDFI CU receives $1M in CDFI Fund award and must demonstrate that its lending activity produced measurable community impact — job creation, homeownership increases, small business growth — in target markets. Current impact reporting counts loans in census tracts without measuring outcomes. "We made 200 loans in low-income tracts" satisfies minimum compliance but doesn't answer: did those loans lead to sustained homeownership? Did small business borrowers grow revenue and hire locally? Did consumer loan access reduce reliance on predatory lenders? Without outcome measurement, CDFIs can't optimize their lending strategy for impact or compete effectively for CDFI Fund awards that increasingly prioritize demonstrated outcomes over activity volume.

## Why Nobody Has Built This
Impact measurement requires linking loan origination data to downstream economic outcomes — homeownership retention, business revenue growth, neighborhood economic indicators — over multi-year timeframes. This requires joining CU lending data with external datasets (census, HMDA, SBA, local tax records) at the individual and community level, a complex data integration challenge. The CDFI CU market is small (~350 institutions) with limited budgets, making it unattractive for enterprise analytics vendors. Academic researchers study CDFI impact but don't build operational tools.

## What to Build
An analytics platform that connects CU lending data to community outcome metrics: (1) loan-level outcome tracking — did the mortgage borrower retain homeownership at 3/5 years? Did the small business borrower grow payroll? (2) Community-level impact measurement — how did CU lending activity correlate with census tract economic improvement over time? (3) Comparative analysis — how does this CU's impact per dollar deployed compare to peer CDFIs? (4) Award application support — generate narrative and data for CDFI Fund award applications demonstrating outcome-based impact. Uses causal inference methods to distinguish CU lending impact from broader economic trends.

## Target Customer
CEOs and development officers at CDFI-certified credit unions applying for CDFI Fund Financial Assistance awards ($500K-$2M), Community Development Financial Institutions capital, or CDFIs reporting to foundations and impact investors.

## Impact If Built
Strengthens CDFI Fund award applications with outcome-based evidence — the difference between a $500K and $2M award. Enables CDFIs to optimize lending strategy for maximum community impact per dollar deployed. Provides boards and funders with quantitative impact reporting that goes beyond activity counts to demonstrate actual community improvement.
