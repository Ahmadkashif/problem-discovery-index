# Document Extraction Applied to Rate Manuals

**Niche:** [[niches/insurtech-platforms/rate-filing-to-configuration/profile|Rate Filing to Configuration]]
**Industry:** [[industries/insurtech-platforms|Insurtech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Table and structure extraction from technical documents is a commodity capability, rate manuals are mostly tables with rules around them, and the tables are retyped.
**Tags:** #cnns #bert #large-language-models #transformers #evaluation-metrics #confidence-intervals #compliance #automation
**Contested on:** Every serious competitor in rating technology is fighting to turn an approved filing into working, verified configuration across fifty states without a specialist retyping it — and whoever shortens filing-to-production most takes the account.

## The Problem
A rate manual's substance is largely tabular: base rates by territory and class, factor tables by limit and deductible, increased limit factors, schedule rating ranges. Those tables are in a PDF, sometimes a scanned one, frequently spanning pages with headers that repeat and footnotes that modify. A specialist retypes them or copies them imperfectly, and a transcription error in a factor table is a mispriced segment that may go unnoticed for a year.

## What Already Exists
Table extraction from PDFs, including scanned and multi-page tables with complex headers, is a mature capability from multiple vendors and in open implementations. Document layout analysis handles the structure. Long-context language models handle the surrounding rules text. Filing documents are publicly available through SERFF for many lines and states, which provides both a corpus and a verification source. Every component is available.

## The Customization Gap
The adaptation is to rate manual conventions and to a correctness bar that is unusually high. It requires: (1) table semantics rather than table structure — a factor table's meaning depends on what its axes are and how it composes with the others, and extracting the grid without the semantics produces numbers with no meaning; (2) footnote and exception resolution, since a table's applicability is routinely modified by text elsewhere in the manual and ignoring that is how a plausible-looking extraction becomes wrong; (3) cross-checking against the previous filing's extraction, because most filings are amendments and the diff is both the interesting content and a strong error check; (4) arithmetic verification where the manual provides examples, since rate manuals frequently include worked examples that constitute a free test suite for the extraction; and (5) confidence per element with mandatory human review below a high threshold, because the tolerance for error here is close to zero and the product should be honest about that rather than optimistic.

## Target Customer
Carriers, rating engine vendors, rate filing consultancies, and the competitive intelligence functions that already read competitors' public filings by hand.

## Impact If Solved
Table extraction removes the transcription and, with it, the transcription errors — which are the quiet failure mode of the current process. The worked-example verification is the elegant part: rate manuals contain their own test cases, and using them turns extraction from something to be trusted into something that is checked.
