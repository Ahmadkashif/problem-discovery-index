# RFI Responses Grounded in the Contract Documents

**Niche:** [[niches/architecture-firms/construction-administration/profile|Construction Administration Services]]
**Industry:** [[industries/architecture-firms|Architecture Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Most RFIs are answered somewhere in the drawings, specs or earlier responses, and the architect searches for the answer by hand every time.
**Tags:** #large-language-models #transformers #k-nearest-neighbors #compliance #workflow-orchestration #worker-facing #automation
**Contested on:** Every serious competitor in this niche is fighting to turn around submittals and RFIs inside the contractual response period without taking on the contractor's means-and-methods liability, and whoever answers fastest with a defensible record takes the account.

## The Problem
A mid-size project produces several hundred RFIs (estimate). Many ask questions the documents already answer — a dimension on another sheet, a spec paragraph, an earlier RFI response — while others reveal genuine conflicts or omissions. The architect must classify each, find the relevant sheets and sections, write a response that answers without directing means and methods, and decide whether it changes cost or time.

## Why Nobody Has Built This
Construction platforms serve the contractor and treat the RFI as a workflow item; the answer is the architect's problem. Retrieval across a drawing set (sheets, details, schedules) plus specifications plus prior responses needed vision and language models that only recently became reliable.

## What to Build
A response assistant that indexes the issued set, specifications, addenda, bulletins and every prior RFI on the project; classifies each new RFI (answered in documents, conflict, omission, substitution, means-and-methods); retrieves the governing sheets and paragraphs; drafts a response in the firm's language with references; and flags likely cost or time impact for the project architect's decision. Every RFI tagged as conflict or omission feeds back to QA/QC.

## Target Customer
CA directors and project architects at firms of 20+ staff carrying several projects in construction at once.

## Impact If Built
RFI turnaround cut from days to hours on documented answers, and the design-attributable RFIs captured as data for the next project's review.
