# Which Hearings Will Need a Record

**Niche:** [[niches/court-reporting-firms/litigants-without-a-record/profile|Litigants Without a Record]]
**Industry:** [[industries/court-reporting-firms|Court Reporting Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Legal aid programmes can afford a reporter for a few hearings a month and choose them by instinct, so the hearing that ends up on appeal is often the one nobody recorded.
**Tags:** #gradient-boosting #logistic-regression #evaluation-metrics #feature-engineering #worker-facing #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to give a litigant a record an appellate court will accept for a hearing the court does not staff, at a price a fee-waiver litigant or legal-aid budget can pay, and whoever gets low-income litigants a reviewable record before the appeal deadline takes the account.

## The Problem
A family-law clinic represents dozens of clients a week in custody, support and restraining-order hearings in courtrooms with no official reporter. Its reporter budget covers a fraction of them. Staff attorneys pick by feel: the contested custody trial, the hearing where opposing counsel is aggressive. Self-represented litigants pick nothing, because they do not know a record is their responsibility.

## Why Nobody Has Built This
Legal aid organisations are not technology buyers, reporting firms see only the hearings someone booked, and appellate outcomes are rarely joined back to whether a transcript existed.

## What to Build
A triage model trained on legal aid case histories and public appellate dockets. It predicts, per upcoming hearing, the chance the result will be appealed or need review, given case type, contested issues, opposing representation, judge and hearing type, and ranks where a reporter or an approved recording is worth the money. A booking link goes to partner reporting firms, with the paperwork for fee waivers and reimbursement funds pre-filled.

## Target Customer
Legal aid managing attorneys and court self-help centres in states where civil and family calendars go unreported; reporting firms building a reduced-rate practice.

## Impact If Built
Scarce reporter dollars spent on the hearings that matter, more appealable records for the people least able to recover from losing one, and better use of reimbursement funds that now pay out little.
