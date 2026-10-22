# Renew, Cancel or Renegotiate the Big Deal

**Industry:** [[libraries-and-archives|Libraries & Archives]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every academic library runs the same renewal analysis on every journal package and database before the publisher's contract rolls over, and rebuilds it in a spreadsheet each year because no tool joins usage, cost, open access and interlibrary loan into one answer.
**Tags:** #linear-regression #time-series-forecasting #causal-inference #evaluation-metrics #feature-engineering #data-integration #automation

## The Problem
An electronic resources librarian at a university library manages dozens to hundreds of licences: journal packages from the large publishers, aggregator databases, ebook collections and streaming video. Each has a renewal date, often the calendar year-end, and multi-year packages carry price caps that reset when they expire. Before each renewal the library has to decide whether to renew as is, cancel, move to title-by-title subscriptions, or renegotiate, often through a consortium that needs the member's position weeks earlier.

The analysis is always the same shape and always rebuilt by hand. Download COUNTER usage reports from each publisher platform, de-duplicate titles across packages, compute cost per use, check which articles are already free through open-access copies or funder mandates (NIH's no-embargo policy took effect on 1 July 2025), estimate the interlibrary loan and document delivery cost after cancellation, and gather faculty opinion. The answer goes to a dean or a collections committee as a spreadsheet and a memo, and next year it starts again.

## What Already Exists
Library services platforms (Alma's ERM functions, FOLIO, OCLC WorldShare) store licences and harvest COUNTER reports through the SUSHI protocol. Usage-analysis tools such as Unsub model journal-level cancellation scenarios, and subscription agents (EBSCO, Harrassowitz) consolidate invoices and offer spend dashboards. General contract-lifecycle tools (Ironclad, DocuSign CLM) track contract dates and obligations for any industry.

## The Customisation Gap
The generic tools either store the licence or analyse one dimension. The library-specific logic is: matching titles across publisher, aggregator and package lists by ISSN and KBART title lists; separating usage that open-access copies or backfiles would satisfy from usage that only a subscription serves; estimating post-cancellation demand from past interlibrary loan behaviour and turnaways rather than raw downloads; honouring perpetual-access rights, text-and-data-mining and AI-use clauses, and consortium most-favoured terms; and modelling multi-year price caps against inflation. Contract-lifecycle software knows nothing about COUNTER or perpetual access, and the ERM modules hold the data without producing the recommendation. Each library rebuilds the join itself, and the result rarely survives the librarian who built it.

## Impact If Solved
A repeatable renewal harness turns a several-week spreadsheet exercise per major package into a few days, produces a recommendation a provost and a consortium can both read, and lets a library cancel or renegotiate with evidence of what the change will cost readers. For a research library spending millions a year on packages, even a few percent of better-targeted spend is a six-figure sum (estimate).
