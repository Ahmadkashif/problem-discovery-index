# Exhibit-to-Docket Linking for Hearing Transcripts

**Niche:** [[niches/court-reporting-firms/administrative-arbitration-hearings/profile|Administrative, Arbitration & Public Hearings]]
**Industry:** [[industries/court-reporting-firms|Court Reporting Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A rate-case transcript mentions hundreds of exhibits by number and witness, and every lawyer writing a post-hearing brief rebuilds the map from transcript to docket by hand.
**Tags:** #large-language-models #bert #k-nearest-neighbors #feature-engineering #evaluation-metrics #automation
**Contested on:** Every serious competitor in this niche is fighting to be the reporter of record under a forum's or agency's master contract, delivering transcripts in its format with exhibits tied to its docket before post-hearing briefs are due, and whoever meets the forum's turnaround at the contract rate takes the account.

## The Problem
In a multi-week utility rate case or regulatory proceeding, witnesses adopt pre-filed testimony, exhibits are marked, admitted, withdrawn and renumbered, and cross-examination refers to "page 14 of Staff Exhibit 22". Briefs are due weeks after the hearing closes, and every party's associates spend days building an index from transcript references to docket filings.

## Why Nobody Has Built This
Reporters deliver transcripts with a word index and an exhibit list, which is all the contract asks for. Agency e-docket systems are separate, often old, and expose filings only as PDFs.

## What to Build
A post-processing step on the certified transcript that extracts every exhibit reference, admission ruling and witness adoption. It resolves each to the docket filing and page, matching on exhibit numbers, titles and filing dates, and delivers a linked transcript and an admitted-exhibits table with uncertain matches flagged for the reporter to confirm. Admission rulings come from the reporter's own record, so the product stays neutral: identical for every party who orders it.

## Target Customer
Reporting firms holding utility commission and regulatory-agency contracts; commission docket offices that want the record linked at the source.

## Impact If Built
Days of associate time saved per party per proceeding, fewer citation errors in briefs and orders, and a contract differentiator that turns a commodity transcript into the forum's working record.
