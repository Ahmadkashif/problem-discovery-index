# Submittal Review Against the Specification

**Industry:** [[architecture-firms|Architecture Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Submittal platforms route every shop drawing and product data package to the architect on time; none of them check it against the specification section the architect wrote.
**Tags:** #large-language-models #transformers #seq2seq #feature-engineering #compliance #automation #workflow-orchestration

## The Problem
During construction, the contractor submits product data, shop drawings and samples for everything from curtain wall to door hardware to roofing membranes — a few hundred packages on a mid-size building (estimate). Each must be reviewed against the relevant specification section and drawings within a contractual period, typically ~10–14 days (estimate), and returned stamped "No exceptions taken", "Make corrections noted", "Revise and resubmit" or "Rejected". The reviewer opens the PDF, opens the spec section, and checks line by line: the manufacturer is listed or a substitution request was approved, the performance values (air and water infiltration ratings, fire ratings, STC, wind load) meet the stated criteria, the finishes match the schedule, required certifications and warranties are attached.

It is detailed, repetitive reading, done by a construction administrator or project architect who is often also producing another project's documents. Late responses delay procurement and invite delay claims; careless ones let a non-compliant product into the building with the architect's stamp on it.

## What Already Exists
Procore, Autodesk Construction Cloud and Newforma manage submittal logs, routing, due dates and stamps well. Specification tools — Deltek Specpoint with AIA MasterSpec, SpecLink — produce the sections. Some platforms generate a submittal register from the specification automatically. General LLM assistants can summarise a product data sheet.

## The Customisation Gap
The generic tools move the package; the review is still a person comparing two documents. The architect-specific logic is: extracting the requirements of the project's own spec section (Part 2 products, performance criteria, Part 1 submittal requirements) into a checklist; pulling the corresponding values from manufacturer data sheets and shop drawings, which use inconsistent units, test standards and naming; comparing against the drawings' schedules and details; distinguishing a true deviation from an approved equal or an accepted substitution; and drafting review comments in the firm's stamp language that note exceptions without taking responsibility for the contractor's means, methods or dimensions — the liability boundary every architect's review stamp exists to protect.

## Impact If Solved
If the first pass of every submittal is an automated requirement-by-requirement comparison, a construction administrator's review time per package could fall from an hour or more to minutes on routine items, response times stay inside the contract period, and the review record shows exactly which requirements were checked — a better position than a stamp alone if a product later fails.
