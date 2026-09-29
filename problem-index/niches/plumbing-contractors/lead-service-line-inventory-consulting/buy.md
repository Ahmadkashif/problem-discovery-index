# A Century of Tap Cards, Photographed and Read by People

**Niche:** [[niches/plumbing-contractors/lead-service-line-inventory-consulting/profile|Lead Service Line Inventory & Replacement Consulting]]
**Industry:** [[industries/plumbing-contractors|Plumbing Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The records that answer the question are handwritten index cards in a basement, and the extraction is staffed rather than solved.
**Tags:** #cnns #transformers #object-detection #transfer-learning #data-integration

## The Problem
The primary evidence for what a service line is made of is the utility's own historical record: tap cards recording the connection when it was made, service permits, meter set records, main installation ledgers, and marked-up plat maps. These span a century. They are handwritten, in varying hands, on cards and in bound ledgers, with abbreviations that meant something to a clerk in 1931. Many have been microfilmed, then scanned, so the image is a photograph of a photograph.

Reading them is the largest labour line in an inventory engagement. Staff work through digitised images, interpret the material notation, resolve the address to a modern parcel, and enter a determination. A mid-sized utility has tens of thousands of cards. The work is slow, hard to quality control, and the interpretations — this abbreviation in this era at this utility means lead — live in whoever did that project.

Address resolution is a second, equally manual problem. Historical addresses have been renumbered, streets renamed, parcels split and merged, and annexations have brought whole neighbourhoods into a system under different numbering. Joining a 1931 card to a 2026 parcel is genuine record linkage and it is done by eye.

## What Already Exists
Handwriting recognition has improved enormously and works well on historical documents, particularly with domain adaptation. Document layout analysis handles semi-structured forms competently. Genealogy and archive digitisation companies have industrialised exactly this pipeline — historical handwritten records at massive scale, extracted and indexed.

Off-the-shelf OCR fails on this material. Commercial document extraction is trained on modern printed and typed documents, and tap cards are handwritten, degraded, and formatted differently by every utility and every era within a utility. Generic handwriting models transcribe words; what is needed is a field-level extraction into a material determination with a confidence attached.

## The Customization Gap
**Every utility's cards are a different form.** Layout, field placement, notation and abbreviations vary by utility and by decade within a utility. The system must adapt to a new format from a small number of labelled examples at the start of each engagement — few-shot adaptation is the operational requirement, not a nice property.

**Notation carries local meaning.** A single letter in a material field may mean lead in one utility's 1920s cards and something else in a neighbouring system. The mapping from notation to material is engagement-specific knowledge currently held by whoever worked that project, and it belongs in a versioned, testable artefact.

**Confidence must survive to the output.** An uncertain transcription of a material field must arrive at the inventory as an uncertain classification, not as a guess. This is the opposite of how document extraction products behave, and it is what makes the extraction usable as model input rather than as a replacement for judgment.

**Historical address resolution is part of the pipeline.** Extraction is worthless if the record cannot be joined to a current parcel. Street renaming, renumbering, annexation and parcel splits are the norm, and the linkage needs to be probabilistic and auditable.

**Both ends of the line matter.** Records may describe the utility-side line, the customer-side line, or neither clearly, and the regulation treats them differently. An extraction that collapses this distinction produces an inventory that fails review.

**Every determination must be traceable to its image.** A resident, a state agency, or a lawyer can ask why an address was classified as it was, and the answer must be the source record with the field highlighted.

## Target Customer
Director of Water Data Services or the programme lead running inventory delivery across multiple utility engagements.

## Impact If Solved
Record extraction is the dominant labour cost and the pacing item on every inventory engagement, and the work recurs for years through annual updates and unknown-resolution obligations. Turning it from reading into reviewing extracted determinations — each with a confidence and a source image — is what lets a firm take on more systems without proportional headcount, and it produces the structured training data the material model needs.
