# Incoming Document Classification and File Organization

**Industry:** [[immigration-law|Immigration Law Firms]]
**Type:** Worker Life Changing
**One-liner:** Paralegals who receive 20-50 documents per client per case — government notices, passports, diplomas, employment records, tax documents — and manually read, classify, and file each one get an automated intake system that classifies and routes every incoming document without human review except for exceptions.
**Tags:** #bert #text-classification #ocr #nlp #automation #worker-facing

## The Problem
Immigration case files are document-intensive in a way that few legal practices match. A single employment-based green card case may involve: passport biographical pages, prior visa stamps, I-94 arrival/departure records, employer support letters, educational credentials and evaluations, tax returns, pay stubs, prior immigration approvals, and government-generated notices — all arriving at different times via email attachments, fax, and physical mail. Each document must be read, identified, matched to the correct case and case phase, and filed in the case management system. This intake and classification task consumes 20-30% of paralegal time and is a bottleneck for case readiness: cases cannot move forward until all required documents are confirmed received and filed.

## Why It Matters to the Worker
Manually reading and classifying incoming documents is low-complexity work that doesn't engage the paralegal's immigration knowledge or judgment — but it must be done carefully because misfiled documents or missed required documents cause downstream case delays. It's an ideal candidate for automation that would free paralegals to focus on case strategy, client counseling, and form preparation — the work that benefits from their domain expertise and that they find professionally meaningful. The current situation traps skilled staff in document filing tasks that a well-trained classifier could handle.

## What a Solution Looks Like
An email and scan intake pipeline that receives incoming documents, OCRs image-based documents, classifies each document by type (government notice, personal identification, educational credential, employment record, financial document), extracts key entities (client name, case number, date, issuing authority), matches the document to the correct case in the case management system, and files it in the appropriate folder. Documents with low classification confidence or that don't match a known document type are flagged for human review. The paralegal's document intake task shifts from reading-and-filing to reviewing-exceptions.

## Impact If Solved
Reduces document intake time by 70-80% — from 20-30% of daily paralegal time to 5-8%. For a case manager handling 150 active files, this recovers 1-1.5 hours daily. Eliminates misfiled documents as a source of case delays. Allows the firm to handle higher case volumes with existing staff.
