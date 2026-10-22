# The Index That Breaks on Second Pass

**Niche:** [[niches/graphic-design-studios/book-and-publication-layout/profile|Book & Publication Layout]]
**Industry:** [[industries/graphic-design-studios|Graphic Design Studios]]
**Type:** Fix (Pain Point)
**One-liner:** The index is compiled against first-pass page numbers, late corrections reflow fifty pages, and the index is wrong in ways nobody finds until a reader does.
**Tags:** #large-language-models #automation #quick-win #data-integration #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to turn a manuscript into print and ebook pages that clear proof with the fewest correction passes at a per-page price, and whoever shortens the correction cycle takes the publisher's list.

## The Problem
Indexers often work from page proofs and deliver page-number entries. Second-pass corrections push text across page breaks, and every entry after the change may now point one page off. Checking means re-verifying entries by hand under deadline.

## Why It's Still Broken
The indexer and the typesetter are usually separate freelancers working from PDFs. Embedded index markers in InDesign solve it, but placing hundreds of markers from a page-number index is tedious, so it is skipped on tight budgets.

## What a Fix Looks Like
Convert the indexer's page-number entries into embedded anchors automatically, by matching each entry's term to its occurrence on the cited page, and flag the ambiguous matches for the indexer. Thereafter the index regenerates with every reflow, and a report lists any entry whose anchor moved or vanished in a correction.

## Who Feels the Pain
Typesetters re-checking indexes at midnight; indexers paid once for work that breaks; readers of reference books.

## Impact If Fixed
Late corrections stop corrupting the index, final-pass checking time drops, and publishers can accept late changes without dreading the index.
