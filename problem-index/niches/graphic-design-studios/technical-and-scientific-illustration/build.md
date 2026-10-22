# Change-Linked Assembly Illustrations

**Niche:** [[niches/graphic-design-studios/technical-and-scientific-illustration/profile|Technical, Medical & Scientific Illustration]]
**Industry:** [[industries/graphic-design-studios|Graphic Design Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** When an engineering change order alters a part, nobody tells the outside illustrator which of the hundreds of assembly and service figures show it, so manuals ship with drawings of parts that no longer exist.
**Tags:** #cnns #transformers #large-language-models #data-integration #workflow-orchestration #automation
**Contested on:** Every serious competitor in this niche is fighting to turn CAD models, specimens and source literature into figures that a subject expert — a technical publications manager, a clinician, a journal art editor — signs off without a correction round, and whoever gets expert sign-off first time at volume takes the account.

## The Problem
A technical illustration studio maintains assembly, exploded-view and service figures for a manufacturer's manuals, often several hundred per product line. Engineering change orders arrive from the client's PLM system as PDFs or spreadsheets listing changed part numbers, sometimes weeks after the change. The illustrator has to work out which figures show each part, redraw them and update callouts and parts lists. Figures that are missed ship in the next manual revision, and a field technician finds out at the machine.

## Why Nobody Has Built This
PLM systems link CAD models to the bill of materials, not to the illustrator's vector files outside the firewall. Component content management systems version the manual's text and treat figures as opaque images. The studios are small and the client's technical publications team owns the relationship, so no vendor has seen a market in the link between the two.

## What to Build
A service that reads each figure's callouts and parts-list tables (vector text or OCR) into a register of part numbers per figure, ingests each change order or BOM diff, and returns the list of affected figures with the changed callouts highlighted. It tracks which figures have been revised against which change, so the studio can show the client that every change reached the drawings, and it flags figures whose part numbers no longer exist in the current BOM.

## Target Customer
Technical illustration studios serving manufacturers of machinery, vehicles and equipment, and the technical publications managers who commission them.

## Impact If Built
Change orders reach every affected figure instead of the ones the illustrator remembers, manual revisions stop carrying obsolete drawings, and the studio can sell revision tracking as part of its retainer.
