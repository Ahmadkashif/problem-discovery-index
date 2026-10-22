# Microfilm Scans With No Article Boundaries

**Niche:** [[niches/libraries-and-archives/local-history-digitisation/profile|Local History & Newspaper Digitisation]]
**Industry:** [[industries/libraries-and-archives|Libraries & Archives]]
**Type:** Fix (Pain Point)
**One-liner:** A newspaper run is scanned page by page, so a search hit lands the user on a whole page of tiny type with no idea which article matched.
**Tags:** #cnns #semantic-segmentation #object-detection #evaluation-metrics #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to turn a small institution's newspapers, photographs and records into searchable online collections at a per-page cost a grant can carry, and whoever does it with the fewest strings on the library's rights to its own content takes the collection.

## The Problem
Low-budget projects scan microfilm to page images with page-level OCR. Users get a page, not an article, and obituaries and notices are unfindable by headline.

## Why It's Still Broken
Article zoning was a manual, costly step that small grants skipped; the pages were delivered and the grant closed.

## What a Fix Looks Like
Re-process existing page images with layout detection that zones articles, headlines and advertisements, re-runs OCR per zone and writes article-level records to the repository, without rescanning.

## Who Feels the Pain
Genealogists and local researchers; the librarian who fields their calls.

## Impact If Fixed
Already-paid-for scans become article-searchable at a fraction of the original imaging cost.
