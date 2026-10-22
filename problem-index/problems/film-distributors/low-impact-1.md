# Avails Answered From Prose Contracts

**Industry:** [[film-distributors|Film Distributors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Contract lifecycle tools store agreements and extract dates; none of them answers the distributor's only recurring question, which is whether a given right in a given territory and window is free to sell on a given date.
**Tags:** #large-language-models #transformers #bert #sets-and-logic #evaluation-metrics #compliance #data-integration #automation

## The Problem
A buyer from a Latin American pay-TV channel emails asking whether a distributor's 2019 thriller is available for pay-TV in Mexico and Colombia from next spring, exclusive, Spanish dubbed. To answer, a rights coordinator opens the original acquisition agreement, the sales agent's territory grants, a 2022 deal with a regional subscription service that may or may not include pay-TV under a broad "television" definition, a holdback in a free-TV licence, and an amendment that extended one term. The answer takes an afternoon and is still a judgement call. With a few hundred titles, each carrying grants across dozens of territories, media and windows, the rights grid runs to thousands of rows, and it is usually kept in a spreadsheet maintained by one person.

Errors are costly in both directions. Licensing a right that is already granted breaches a contract and can cost the deal and the relationship. Failing to notice that a right has reverted, or that a licence has expired, leaves money unsold. Missing a reversion date the distributor owes the producer creates a dispute.

## What Already Exists
Contract lifecycle management platforms (Ironclad, DocuSign CLM, Agiloft) store agreements, extract parties and dates, and send renewal alerts. Enterprise rights and royalties systems built for entertainment, now largely consolidated under Rightsline after its 2024 acquisitions of FilmTrack and RSG Media, model grants, windows and avails well. But they are priced and implemented for studios and broadcasters, and they assume someone has already keyed every contract into a structured form. Generic language models will summarise a contract on request.

## The Customisation Gap
Distribution rights have their own grammar, and generic extraction misses it. The layer needed includes:
- a rights taxonomy that maps each contract's media definitions ("pay television", "SVOD", "AVOD", "free video on demand", "all television") onto one controlled vocabulary, preserving the contract's wording where definitions conflict;
- territory definitions that resolve language rights, regional carve-outs and "the Benelux" into countries;
- window logic that handles sequential and overlapping windows, holdbacks keyed to another window's start, and terms that run from first exploitation rather than from signature;
- amendment chains, applied in order;
- a conflict check that, given a proposed grant, returns every existing grant it touches with the clause that creates the conflict.

The extraction has to cite the clause behind every row, because a coordinator will not sell on a model's say-so. It also has to work from the mixed PDFs, scans and emailed deal memos that independent distributors actually hold.

## Impact If Solved
An avails answer that takes minutes rather than an afternoon, with the clause attached, lets a small sales team respond to more buyers during markets and festivals, when the inquiries cluster. It also removes the double-grant and missed-reversion errors that cost far more than the coordinator's time. For a 300-title library that is a few hours a week back for the rights coordinator, and a defensible record when a licensee or producer disputes a grant.
