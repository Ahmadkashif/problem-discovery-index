# Spare-Parts RFQs Quoted From Thin Technical Data

**Industry:** [[aerospace-parts-suppliers|Aerospace Parts Suppliers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Quoting tools price a part from a good drawing; aerospace spare-parts RFQs, above all DLA solicitations on DIBBS, turn on things a generic quoting tool never checks: whether the shop is an approved source, whether the technical data exists, whether a first article test applies, and what the last award paid.
**Tags:** #gradient-boosting #logistic-regression #large-language-models #feature-engineering #revenue-impact #automation #compliance

## The Problem
A 30-person AS9100 machine shop that wants government work opens DLA's bid board every morning. DLA Aviation alone manages more than 1.8 million national stock numbers for 2,341 weapon systems (search summary of a DLA flyer), and many of its buys are small, quick-turn quotes for a bracket, a bushing, a fitting or a panel. For each RFQ the estimator has to work out, within days, whether the shop can legally and practically make the part, and only then what to charge. Most of the time goes on the first question. The same pattern holds for commercial spares and repair-part RFQs from tier-1s and distributors, with tighter windows and less data.

## What Already Exists
Quoting platforms such as Paperless Parts, ERP estimating modules and spreadsheets price machined parts from drawings and routings. Bid-board tools (SalesPatriot, SAM Search, BidPulsar, Starbridge, Cleat.ai) surface solicitations, summarise them and pull award history. Federal opportunity intelligence vendors cover large contract pursuits, profiled under contract research labs as [[niches/contract-research-labs/federal-opportunity-intelligence/profile|Federal R&D Opportunity Intelligence]].

## The Customisation Gap
An aerospace spare-parts quote needs checks that quoting software does not model. Is the item source-controlled, a critical safety item, or restricted to approved sources, and would the shop need a source approval request reviewed by the engineering support activity first? Is the technical data package available in cFolders, and does the shop hold the JCP certification (DD Form 2345) to download export-controlled drawings? Does the solicitation require a first article test, and can it be waived on prior production? Do specialty-metals and domestic-source clauses apply (DFARS 252.225-7009, recalled)? What did the last three awards for this NSN pay, in what quantity, to whom? Then comes the price itself, which depends on raw-material availability, outside special processing and the shop's own history on similar parts. A tool that answers the first five questions in minutes, and only then estimates, turns an estimator's morning of triage into a shortlist of quotes worth sending.

## Impact If Solved
If triage time per solicitation falls from ~30–60 minutes to ~5 (estimate), a shop can review three to five times more RFQs. Quoting only what it can win (SalesPatriot cites a 283% bid-volume increase at its customer Echelon Supply & Service, a vendor figure) can roughly double the shop's award count per estimator-hour (estimate).
