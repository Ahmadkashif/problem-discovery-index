# The General Note Without a Balloon

**Niche:** [[niches/aerospace-parts-suppliers/drawing-ballooning-characteristics/profile|Drawing Ballooning & Characteristic Accountability]]
**Industry:** [[industries/aerospace-parts-suppliers|Aerospace Parts Suppliers]]
**Type:** Fix (Pain Point)
**One-liner:** FAI reports are often rejected not for a wrong measurement but for a requirement in a note that never got a balloon (practitioner experience, not a measured share).
**Tags:** #large-language-models #transformers #evaluation-metrics #compliance #quick-win #automation
**Contested on:** Every serious competitor in this sub-niche is fighting to extract every requirement on a drawing or model, notes included, into a ballooned Form 3, and whoever posts the highest characteristic recall on the shop's own scanned and model-based drawings takes the account.

## The Problem
General notes carry requirements: finishes, edge breaks, marking and identification, masking, cleanliness, the process specification for heat treatment or plating. Engineers balloon the dimensions on the field of the drawing and skim the notes. The customer's quality representative reads every note.

## Why It's Still Broken
Notes are prose; ballooning tools look for dimension text; and checking notes is the last step of a long task.

## What a Fix Looks Like
Before any report goes out, run every note through a requirement extractor that lists each verifiable requirement in the notes and compares it with the balloon list. Anything unballooned is flagged with the note text, for the engineer to balloon or mark as not applicable with a reason.

## Who Feels the Pain
Quality engineers whose reports bounce; shipping and finance, waiting on accepted FAIRs to ship and invoice.

## Impact If Fixed
A notes check takes minutes per drawing and could remove a frequent rejection cause, saving ~1–2 resubmissions a month at a typical supplier (estimate).
