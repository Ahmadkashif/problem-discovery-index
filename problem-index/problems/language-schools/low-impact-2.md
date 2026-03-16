# Student Visa Compliance Tracking & SEVIS Automation

**Industry:** [[language-schools|Language Schools]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** SEVIS compliance is already software-managed for universities — but no tool addresses the specific reporting cadence, attendance-threshold rules, and program-extension workflows of intensive English programs and standalone language schools.
**Tags:** #llm #text-classification #nlp #compliance #data-integration

## The Problem
Schools enrolling international students on F-1 or M-1 visas must report to SEVP (Student and Exchange Visitor Program) through the SEVIS portal: initial I-20 issuance, quarterly enrollment verification, attendance threshold compliance (students must attend at least 80% of scheduled hours), program extension requests, authorized early withdrawal, and status terminations. Designated School Officials (DSOs) manage this manually — cross-referencing attendance spreadsheets against SEVIS deadlines, hand-entering records into the federal portal, and chasing students for supporting documents. A missed or late report can result in a student's SEVIS record being terminated, which triggers loss of legal immigration status — a catastrophic outcome for the student and a reputational and regulatory risk for the school.

## What Already Exists
University-scale Student Information Systems (Ellucian Banner, PeopleSoft Campus Solutions, Terra Dotta) include SEVIS batch-upload modules and compliance dashboards. Immigration-management platforms like Sunapsis and iStart are built for large university international student offices processing thousands of records. These tools assume a semester-based academic calendar, degree-program enrollment structures, and full-time IT staff to manage integrations — none of which apply to a 50-200 student language school running 4-8 week session cycles with rolling admissions.

## The Customisation Gap
A language-school-specific SEVIS compliance layer needs to: (1) ingest attendance data from whatever system the school uses (often just a Google Sheet or a basic SIS like STARS or SchoolAdmin) and automatically flag students approaching the 80% attendance threshold before they cross it; (2) map the school's session-based calendar (not semesters) to SEVIS reporting periods and generate deadline-aware task queues for the DSO; (3) auto-populate SEVIS batch files from existing student records, with LLM-assisted classification of event types (e.g., distinguishing "authorized early withdrawal" from "termination for attendance" based on the DSO's case notes); (4) track document expiration dates (I-20, passport, visa stamp) and trigger collection workflows before gaps cause compliance failures. The session-cycle calendar logic, rolling-admission enrollment patterns, and attendance-hour (not credit-hour) tracking are domain-specific requirements that university tools do not support.

## Impact If Solved
DSOs reclaim 8-12 hours per session cycle currently spent on manual SEVIS data entry and cross-referencing. Late or missed SEVIS reports — which currently affect an estimated 5-10% of records at small language schools — drop to near zero, protecting students from inadvertent status violations and protecting the school's SEVP certification.
