# UST Compliance Portfolio Manager

**Niche:** [[niches/environmental-consultants/underground-storage-tank-specialists/profile|Underground Storage Tank Specialists]]
**Industry:** [[industries/environmental-consultants|Environmental Consultants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A portfolio management platform for UST consultants that tracks every tank, test, notification, and compliance deadline across 50-200 client facilities — replacing the spreadsheet-and-calendar approach that lets deadlines slip through.
**Tags:** #automation #workflow-orchestration #compliance #data-integration #revenue-impact

## The Problem
A UST compliance consultant managing 100 client facilities with 400 tanks must track: annual tank tightness test dates, monthly leak detection records, triennial cathodic protection surveys, operator training certifications (Class A/B/C per EPA 2018 regulations), financial assurance documentation renewals, and state-specific notification deadlines (new tank installation, temporary/permanent closure, suspected release reporting). These deadlines are tracked in a combination of Excel spreadsheets, Outlook calendar reminders, and the consultant's memory. When a deadline is missed — a tank tightness test expires, a notification isn't filed — the client receives a violation notice that can result in $10,000-$37,500/day civil penalties under federal UST regulations. The consultant's reputation and E&O exposure ride on never missing a deadline.

## Why Nobody Has Built This
The UST market is small (3,000-5,000 active UST consulting firms in the US) and the per-customer revenue potential is modest ($100-300/month). State UST programs have different data formats, reporting requirements, and compliance intervals, making a 50-state product expensive to build and maintain. The consultants themselves are often solo practitioners or 2-5 person firms with minimal technology budgets. But the pain is acute: a single missed deadline can result in a violation that costs the client $10,000+ and the consultant their biggest account.

## What to Build
A cloud-based portfolio manager where each client facility has a structured profile: tank inventory (type, capacity, installation date, product stored), compliance calendar (all required tests, notifications, and certifications with due dates), document library (test reports, notifications, financial assurance certificates), and compliance scorecard (green/yellow/red per tank per requirement). The system sends automated alerts 60/30/7 days before each deadline, generates compliance status reports for client meetings, and produces the audit-ready compliance file that state inspectors request during inspections. Integration with state UST databases (where APIs exist) to auto-populate tank registration data.

## Target Customer
UST compliance consultants managing 30+ client facilities, currently tracking deadlines in spreadsheets and dreading the day they miss a notification.

## Impact If Built
Eliminates missed compliance deadlines — each prevented violation saves the client $10,000-50,000 and preserves the consultant's relationship. Reduces administrative overhead by 10-15 hours/week for a consultant managing 100 facilities, freeing capacity for additional client acquisition.
