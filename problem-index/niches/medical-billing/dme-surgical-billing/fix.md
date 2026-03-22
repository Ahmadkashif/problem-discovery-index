# CMN Expiration Tracking to Prevent Auto-Denials

**Niche:** [[niches/medical-billing/dme-surgical-billing/profile|DME & Surgical Billing]]
**Industry:** [[industries/medical-billing|Medical Billing]]
**Type:** Fix (Pain Point)
**One-liner:** Every DME item requires a Certificate of Medical Necessity with an expiration date — when a CMN expires without renewal, all subsequent claims for that item and patient are automatically denied, and most small DME companies track expirations in spreadsheets or not at all.
**Tags:** #decision-trees #feature-engineering #automation #compliance #revenue-impact #worker-facing

## The Problem
A CMN (Certificate of Medical Necessity) is a document signed by the ordering physician certifying that a patient has a medical need for a specific DME item. CMNs have defined validity periods — typically 12 months for most items, though some categories (oxygen, CPAP) have different intervals tied to recertification requirements. When a CMN expires, the DME supplier cannot bill for continued use of the equipment until a new CMN is obtained from the physician. Claims submitted without a valid CMN are automatically denied. The challenge: obtaining a new CMN requires contacting the ordering physician's office, sending the recertification form, waiting for the physician to complete and sign it, and tracking the return. Physician offices treat CMN renewals as low-priority paperwork — average turnaround is 2-4 weeks, and 20-30% require multiple follow-up contacts. During this renewal gap, the supplier provides the equipment but cannot bill. A DME company with 200 active patients may have 15-20 CMN expirations per month, each requiring proactive outreach 30-60 days in advance.

## Why It's Still Broken
No standard PM system tracks CMN expiration dates because CMN management is DME-specific. Small DME companies track expirations in Excel spreadsheets, wall calendars, or Outlook reminders — methods that work when the owner remembers to check them and fail when they're busy, on vacation, or when the spreadsheet hasn't been updated. Enterprise DME platforms (Brightree) have CMN tracking modules, but their $500-1,000+/month pricing excludes small suppliers. The failure mode is silent — a missed CMN renewal doesn't trigger an alert until the first claim is denied, at which point 1-3 months of claims may be affected. The denial is easily resolved (obtain the CMN and resubmit), but the cash flow gap and rework cost are significant.

## What a Fix Looks Like
A standalone CMN tracking tool (web-based, $50-100/month) designed for small DME companies: (1) CMN registry — stores every active CMN with patient, physician, item category, issue date, and expiration date. Data entry is simple: scan or upload the CMN document, and the tool extracts key dates. (2) Renewal timeline — displays all CMNs expiring in the next 90 days, color-coded by urgency (green: 60+ days, yellow: 30-60 days, red: under 30 days). (3) Automated physician outreach — generates pre-populated recertification request forms and sends them to the ordering physician's office via fax or electronic portal at the 60-day mark, with automatic follow-up reminders at 45 days and 30 days. (4) Renewal status tracking — tracks each CMN renewal through the process (requested → sent to physician → received → filed), with escalation alerts when the physician hasn't responded within 2 weeks. (5) Claims integration — flags any claim being prepared for an item whose CMN is expired or expiring within 30 days.

## Who Feels the Pain
The DME company billing manager who manually tracks 150-300 CMN expiration dates and spends 8-12 hours/month managing the renewal process, and the company owner who loses revenue during CMN renewal gaps and faces audit risk when claims are submitted with expired CMNs.

## Impact If Fixed
Eliminates CMN-related denials (estimated 8-15% of all denials at small DME companies) by ensuring renewals are initiated 60 days before expiration rather than discovered after denial. For a DME company billing $100,000/month with 10% CMN-related denials, this recovers $10,000/month and eliminates the 2-4 week cash flow gap per affected patient. The billing manager reclaims 8-12 hours/month of manual CMN tracking time. At $75/month, the tool pays for itself if it prevents a single CMN-related denial per month.
