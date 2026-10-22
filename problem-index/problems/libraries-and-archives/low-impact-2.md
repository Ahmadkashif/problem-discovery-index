# Screening Digitised Archives for What Must Stay Closed

**Industry:** [[libraries-and-archives|Libraries & Archives]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Before an archive puts a digitised collection online, someone has to read every page for social security numbers, student and medical records, donor restrictions and culturally sensitive material, and the redaction tools built for corporate documents cannot read a 1960s carbon copy.
**Tags:** #bert #transformers #large-language-models #cnns #evaluation-metrics #compliance #automation

## The Problem
A university archive digitises a collection — a former dean's correspondence, a civil rights organisation's files, a local newspaper's photo morgue — and wants it online for researchers. Before publication, an archivist has to screen it. Personnel files and student records may fall under FERPA, clinic records under HIPAA, and correspondence routinely contains social security numbers, home addresses and medical details about living people. Donor agreements may close parts of a collection for decades. Materials about Indigenous communities may call for consultation under the Protocols for Native American Archival Materials. The screening is done by reading, page by page, often by the same archivist who processed the collection.

Most digitisation projects are grant-funded on fixed timelines, so screening becomes the bottleneck: imaging runs at production speed, review at reading speed. The common result is either a delayed launch or a cautious decision to publish only the metadata, which defeats the purpose of digitising.

## What Already Exists
Enterprise redaction and data-loss-prevention tools (Microsoft Purview, AWS Comprehend PII detection, Google Cloud's Sensitive Data Protection), e-discovery review platforms (Relativity), OCR engines, and handwriting recognition services such as Transkribus. Archives management systems (ArchivesSpace) and digital repositories (Preservica, CONTENTdm) record access restrictions at collection, series or file level.

## The Customisation Gap
The corporate tools assume born-digital text, modern formats and a company's own data. Archival screening needs: recognition on degraded typescript, carbon copies, handwriting and mixed-language pages; detection of categories the regulations and the profession care about (student and patient records, social security and alien registration numbers, criminal records of private people, information about third parties in correspondence); awareness of the donor agreement and dates, since a restriction may lapse after a set term or on a person's death; and output at the level archivists work in — item, folder and series — written back as restrictions into the finding aid rather than black boxes on a PDF. Each archive improvises this with keyword searches and student workers.

## Impact If Solved
A screening pass tuned to archival material lets reviewers read only the flagged fraction of pages, cutting review time on a typical digitisation project by an estimated half or more (estimate), so grant-funded collections go online on schedule with a documented basis for every closure.
