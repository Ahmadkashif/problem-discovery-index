# A Recall-First Extractor for Hard Drawings

**Niche:** [[niches/aerospace-parts-suppliers/drawing-ballooning-characteristics/profile|Drawing Ballooning & Characteristic Accountability]]
**Industry:** [[industries/aerospace-parts-suppliers|Aerospace Parts Suppliers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Auto-ballooning tools are tuned for clean CAD output; the drawings that cost shops the most time are scans, revisions and note-heavy legacy prints.
**Tags:** #object-detection #cnns #transformers #large-language-models #evaluation-metrics #automation #compliance
**Contested on:** Every serious competitor in this sub-niche is fighting to extract every requirement on a drawing or model, notes included, into a ballooned Form 3, and whoever posts the highest characteristic recall on the shop's own scanned and model-based drawings takes the account.

## The Problem
A shop bidding government spares or legacy commercial parts receives technical data that was scanned from aperture cards or paper, with hand-lettered revisions, smudged feature control frames and pages of general notes. Auto-ballooning either fails or produces a partial list the engineer must check line by line, so the time saving disappears exactly where the work is hardest.

## Why Nobody Has Built This
Vendors demo on clean vector PDFs and sell to shops whose customers send modern CAD. Legacy scans are a long tail with no benchmark, and the supervision (years of a shop's accepted FAIRs) is export-controlled and customer-proprietary.

## What to Build
A pipeline of layout detection for annotations, OCR tuned to engineering lettering and GD&T symbols, structured parsing into nominal and limits, and an LLM pass over notes that turns sentences into requirements ("break sharp edges 0.005–0.015" becomes a characteristic). It reports confidence per item and ranks the engineer's review by risk of a miss, and it measures characteristic recall against the shop's own accepted FAIRs before it is trusted. Deploy on premises or in a US-only enclave for ITAR data.

## Target Customer
Quality managers at shops working government technical data packages and legacy commercial part numbers.

## Impact If Built
Bringing ballooning on hard drawings from ~4–8 hours to under an hour (estimate), with recall measured rather than assumed, makes legacy spares quotable and their first articles survivable.
