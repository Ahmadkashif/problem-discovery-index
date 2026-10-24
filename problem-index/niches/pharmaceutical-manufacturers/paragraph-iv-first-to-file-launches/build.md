# Exclusivity Forfeiture Risk Tracked Before It Costs the Launch

**Niche:** [[niches/pharmaceutical-manufacturers/paragraph-iv-first-to-file-launches/profile|Paragraph IV & First-to-File Launches]]
**Industry:** [[industries/pharmaceutical-manufacturers|Pharmaceutical Manufacturers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A first-to-file position can be lost through forfeiture events nobody is watching together: approval timing, litigation outcomes, settlements and other filers' moves.
**Tags:** #large-language-models #survival-analysis #bayesian-inference #feature-engineering #compliance #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to file a substantially complete Paragraph IV ANDA first and clear the brand's patents, and whoever converts the most first-to-file positions into day-one launches takes the account.

## The Problem
Holding a first-to-file position is not the same as launching with exclusivity. The statute defines forfeiture events (failing to obtain approval in time, failing to market after a court decision or a patent's delisting, certain agreements), and each depends on dates spread across FDA actions, court dockets and other applicants' filings. The IP team, the regulatory team and outside counsel each watch part of it.

## Why Nobody Has Built This
Litigation analytics vendors sell to lawyers, pipeline databases to commercial teams. The forfeiture analysis is done by counsel as a memo when a question arises, and the inputs are scattered across public sources nobody joins per molecule.

## What to Build
A per-molecule exclusivity tracker that reads FDA's Paragraph IV list, approval letters, Orange Book changes and docket entries, maps them to the statutory forfeiture triggers, and estimates the probability and timing of launch with exclusivity, with time-to-event models fitted on past first-to-file molecules. It alerts when a docket event or another filer's approval changes the picture.

## Target Customer
IP and litigation heads and portfolio leads at generic makers holding ten or more first-to-file positions.

## Impact If Built
A single forfeited exclusivity on a large molecule can cost tens of millions of dollars of launch profit (estimate); catching one such event early pays for the system many times over.
