# Cross-Document Consistency Checker

**Niche:** [[niches/estate-planning/document-assembly/profile|Document Assembly & Plan Packaging]]
**Industry:** [[industries/estate-planning|Estate Planning]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Legal document review tools check individual documents for errors — but none verify consistency across a 6-8 document estate plan package where the same names, roles, and provisions must match across every document.
**Tags:** #bert #large-language-models #transformers #feature-engineering #evaluation-metrics #compliance #automation

## The Problem
An estate plan package has dozens of consistency requirements: the successor trustee named in Article 5 of the trust must match the personal representative named in the will; the healthcare agent in the healthcare POA must match the person authorized to make healthcare decisions in the trust's incapacity provisions; the trust's asset schedule must include the same assets referenced in the funding instructions; and conditional provisions must be logically consistent across documents (if the trust says "if my spouse predeceases me, distribute to my children in equal shares," the will must not say "if my spouse predeceases me, distribute to my sister"). When a paralegal generates documents individually, these consistency requirements are enforced by manual review — reading each document and comparing references. Attorneys catch errors during their review, but the error rate is high enough that some firms do a second paralegal review before attorney review.

## What Already Exists
Legal document review tools (Kira Systems, Luminance, ContractPodAi) use NLP to extract provisions, flag issues, and compare documents — but they target contract review for M&A due diligence, not estate planning document consistency. General-purpose document comparison tools (DeltaView, Workshare Compare) compare two versions of the same document but can't check consistency across different document types. WealthDocx maintains some consistency within its template system but doesn't validate cross-document references after documents are generated and potentially edited.

## The Customization Gap
The missing tool understands estate planning document structure well enough to extract and compare key elements across document types: named fiduciaries (trustee, executor, guardian, agents), beneficiary designations and distribution shares, conditional provisions and their triggers, asset references, and governing law provisions. It must know that "Successor Trustee" in the trust corresponds to "Personal Representative" in the will and "Agent" in the POA — these are different titles for what may be the same person in a coordinated plan. The checker should produce a consistency report: "14 cross-document references checked. 2 inconsistencies found: (1) Trust names Sarah Jones as successor trustee; Will names Sarah Smith as personal representative — possible name change or error. (2) Trust distributes to children per stirpes; Will distributes to children in equal shares — these produce different outcomes if a child predeceases."

## Target Customer
Paralegals and associate attorneys at estate planning firms who currently spend 30-60 minutes manually cross-checking each plan package for consistency before attorney review, and still miss errors 10-15% of the time.

## Impact If Solved
Eliminates consistency errors that currently reach clients in 5-8% of signed plan packages (after attorney review catches most but not all). Reduces paralegal cross-checking time from 30-60 minutes to 5-10 minutes per plan. Prevents malpractice exposure from inconsistent plans that produce unintended distribution outcomes at death.
