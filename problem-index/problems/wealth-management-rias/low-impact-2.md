# SEC/State RIA Exam Compliance Documentation

**Industry:** [[wealth-management-rias|Wealth Management RIAs]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Compliance documentation tools exist for broker-dealers but don't map to the specific regulatory framework RIAs face under the Investment Advisers Act of 1940.
**Tags:** #large-language-models #bert #transfer-learning #attention-mechanisms #word-embeddings #evaluation-metrics #compliance

## The Problem
RIA firms face SEC examinations (for firms with >$100M AUM) or state regulatory exams (for smaller firms) every 3-7 years. Preparation requires assembling and organizing years of documentation: ADV Parts 1, 2A, and 2B filings, client agreements, trading records, advertising archives, email retention records, best execution analyses, and proxy voting records. A typical exam request list contains 40-80 line items. Firms spend 80-200 hours pulling, organizing, and cross-referencing these documents, often hiring outside compliance consultants at $200-400/hour.

## What Already Exists
Compliance platforms like ComplySci, NRS (National Regulatory Services), and RIA in a Box provide ongoing compliance calendars, template policies, and filing reminders. These tools are effective for routine compliance maintenance — annual ADV updates, code of ethics acknowledgments, and political contribution tracking. Generic document management systems (SharePoint, Google Drive) store the files but provide no regulatory intelligence about what's needed or what's missing.

## The Customisation Gap
What's missing is an intelligent document assembly engine that understands the specific regulatory requirements for RIAs (distinct from broker-dealer FINRA requirements), can map a firm's existing document corpus against a likely exam request list, identify gaps or stale documents, and auto-generate a structured exam-ready package. The system needs to understand that a "best execution" analysis for an RIA using model portfolios through a TAMP looks fundamentally different from one for an RIA doing direct trading through Schwab's institutional platform.

## Impact If Solved
Exam preparation time drops from 80-200 hours to 15-30 hours. Outside compliance consultant costs during exam years drop by $15,000-40,000 per firm. Deficiency findings decrease because documentation gaps are caught proactively rather than discovered by examiners.
