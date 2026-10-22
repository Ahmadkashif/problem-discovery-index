# Correction Entry From Marked-Up Proofs

**Niche:** [[niches/graphic-design-studios/book-and-publication-layout/profile|Book & Publication Layout]]
**Industry:** [[industries/graphic-design-studios|Graphic Design Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every proof pass returns hundreds of corrections as PDF comments and handwritten marks that a typesetter keys in by hand, then re-reads every page to find what the corrections broke.
**Tags:** #cnns #transformers #seq2seq #large-language-models #automation #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to turn a manuscript into print and ebook pages that clear proof with the fewest correction passes at a per-page price, and whoever shortens the correction cycle takes the publisher's list.

## The Problem
A 320-page title comes back from first pass with corrections from the author (handwritten on printed pages, then scanned), the copyeditor (PDF strike-through and insert comments) and the proofreader (standard proof-correction marks). The typesetter works through them one at a time, finds the spot in InDesign, makes the change, and checks whether the paragraph now runs over, leaving a widow or pushing a heading to the foot of the page. Then the whole book is read again for collateral damage.

## Why Nobody Has Built This
Proof correction marks are a niche visual language, scanned handwriting is hard to read reliably, and the market is fragmented across small typesetting studios and offshore houses. Layout software vendors have focused on design features rather than the correction loop.

## What to Build
A correction pipeline: read PDF annotations directly, recognise handwritten proof marks and marginal text on scanned pages, anchor each correction to the exact text in the InDesign story, and apply it as a tracked change for one-click acceptance. After applying, report every page whose layout changed, with new widows, orphans, stacked hyphens, moved headings and shifted index or cross-reference targets highlighted.

## Target Customer
Typesetting studios and in-house production departments at trade, academic and educational publishers.

## Impact If Built
Correction entry drops from hours to minutes per pass, collateral reflow damage is caught by the system rather than a full re-read, and a studio can turn proofs around in a day — the speed contest publishers buy on.
