# Accounts-Payable Capture Retrained on Summonses

**Niche:** [[niches/legal-support-services/sop-receipt-forwarding/profile|Service-of-Process Receipt & Forwarding]]
**Industry:** [[industries/legal-support-services|Legal Support Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Invoice-capture platforms already classify and extract millions of varied documents a day with human review queues; summonses and subpoenas are a harder, smaller cousin of the invoice.
**Tags:** #transformers #large-language-models #feature-engineering #evaluation-metrics #automation
**Contested on:** Every serious competitor in this niche is fighting to read every served document correctly — entity, court, case type, answer date — and put it in front of the right lawyer the same day, and whoever never lets a served suit become a default takes the account.

## The Problem
SOP intake is a document-capture problem with legal stakes: varied layouts, scanned paper, multi-document bundles, and routing by entity.

## What Already Exists
Intelligent document processing platforms (ABBYY, Hyperscience, Rossum) with classification, extraction, confidence scoring and review queues, widely used for invoices and forms.

## The Customization Gap
SOP needs: a taxonomy of legal document types (summons, complaint, subpoena, garnishment, levy, agency notice); entity resolution against thousands of client subsidiaries and former names; jurisdiction-aware deadline computation; bundle splitting; and zero-silent-error controls, so low-confidence fields block forwarding rather than pass through.

## Target Customer
Registered agents and large corporate legal departments with central intake.

## Impact If Solved
Intake throughput rises without adding staff, and review effort concentrates on the documents that are genuinely unusual.
