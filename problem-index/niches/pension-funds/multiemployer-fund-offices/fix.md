# Remittance Reports Keyed by Hand Every Month

**Niche:** [[niches/pension-funds/multiemployer-fund-offices/profile|Multiemployer Pension Fund Offices]]
**Industry:** [[industries/pension-funds|Pension Funds]]
**Type:** Fix (Pain Point)
**One-liner:** Small contractors send monthly remittance reports as spreadsheets, PDFs and handwritten forms, and fund office clerks key them line by line.
**Tags:** #large-language-models #transformers #k-nearest-neighbors #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to post every contributing employer's monthly remittance to the right participant's hours and pension credit, and whoever credits every reported hour correctly with the fewest delinquencies and credited-service disputes takes the account.

## The Problem
Large employers use the fund's online portal. The long tail of small contractors does not. Their reports arrive in many formats, often with a single cheque covering several funds (pension, health, annuity, training). Clerks key, allocate and match them, and errors in keying become errors in members' pension credit.

## Why It's Still Broken
Fund offices cannot force small employers onto a portal, and the reports are too varied for template-based OCR. The fund pays clerks instead.

## What a Fix Looks Like
Document extraction that reads any remittance format and splits it across funds by the bargaining agreement's rates. It matches members by name and ID history and posts confident lines automatically. Unclear lines go to a clerk with the likely match shown.

## Who Feels the Pain
Fund office clerks in the monthly crunch; members whose hours are mis-keyed; trustees paying for manual processing.

## Impact If Fixed
Most remittance lines are posted without keying, and the clerks' time goes to the exceptions that affect members' credit.
