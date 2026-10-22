# Fifty Clients, Fifty CAD Standards

**Industry:** [[drafting-services|Drafting Services]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every client has its own layers, title blocks, text styles, line weights, Revit template and sheet naming, and a bureau serving dozens of clients conforms to each one by hand, then gets the set bounced for a wrong pen weight.
**Tags:** #k-nearest-neighbors #random-forests #word-embeddings #decision-trees #feature-engineering #automation #quick-win

## The Problem
An architecture firm's CAD standard specifies layer names (often its own variant of the US National CAD Standard), title block fields, text heights, dimension styles, hatch patterns, pen tables, keynote format and file naming. An engineering firm's is different. A steel fabricator wants its own title block, piece-mark convention and drawing numbering on the detailer's shop drawings. A Revit client sends a template and a list of view naming rules. A bureau with fifty active clients is working to fifty standards, documented in PDFs of varying age, sample drawings and the memory of whichever drafter last worked for that client.

Non-conformance is the most common avoidable rejection. A set that is technically right but on the wrong layers, with the wrong text style or a stale title block, gets returned, and the client's perception of the bureau drops even though nothing in the drawing was wrong. Offshore teams, working overnight without anyone to ask, are especially exposed.

## What Already Exists
AutoCAD's CAD Standards manager checks drawings against a .dws standards file; Revit templates, Ideate StyleManager and pyRevit scripts enforce some conventions; Bluebeam can compare sets; layer-translation utilities map one naming scheme to another. Large firms publish their standards and hand out templates.

## The Customisation Gap
These tools check a drawing against a standard someone has already encoded. The bureau's problem is the encoding: most client standards arrive as a PDF manual and a handful of sample sheets, not as a .dws file, and they are partly unwritten — the architect who always wants door tags in a particular style or details numbered from the top right. The bureau-specific logic is: learning a client's standard from its sample drawings (layer usage, text and dimension styles, title block content, sheet numbering, annotation habits); keeping one profile per client and per project; checking each outgoing set against the right profile before transmittal; and converting a drawing from the bureau's working conventions into the client's on the way out. It is one engine serving many standards, which no single-firm tool attempts.

## Impact If Solved
Automatic conformance would remove the most avoidable class of rejected deliverables and the hours drafters spend reformatting, and would let a bureau onboard a new client from a sample set in a day rather than a fortnight of trial and error.
