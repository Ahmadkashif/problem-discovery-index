# International Student Admissions-to-SEVIS Workflow Platform

**Niche:** [[niches/k12-private-schools/international-student-admissions/profile|International Student Admissions Programs]]
**Industry:** [[industries/k12-private-schools|K-12 Private Schools]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product connects the international admissions pipeline (inquiry, application, evaluation, acceptance) to the SEVIS compliance workflow (I-20 generation, registration, ongoing reporting) — schools manage these as disconnected processes.
**Tags:** #workflow-orchestration #automation #compliance #data-integration

## The Problem
When an international student is accepted, the school must generate an I-20 form (requiring financial documentation, enrollment verification, and program information), register the student in SEVIS, communicate visa interview guidance to the family (across time zones, often in a language the family barely reads in English), track visa issuance, and then manage ongoing SEVIS compliance (enrollment status changes, address updates, program extensions, transfers). This workflow involves 3 separate systems (admissions CRM, SEVIS portal, email) and 15-20 administrative touchpoints per student.

## Why Nobody Has Built This
The market is small — fewer than 2,000 US private K-12 schools enroll meaningful numbers of international students. SEVIS integration requires interfacing with a US government system (ICE/SEVP) that has limited API capabilities and strict data handling requirements. The compliance rules change with immigration policy shifts, requiring ongoing legal review and system updates. Higher education has tools for this (Terra Dotta, Sunapsis), but they are built for university-scale operations and priced accordingly.

## What to Build
An international student management platform that bridges admissions and SEVIS compliance: when an international applicant is accepted in the admissions CRM, the platform generates the I-20 from pre-populated enrollment and financial data, initiates SEVIS registration, sends multi-language visa preparation materials to the family, tracks visa issuance, and manages ongoing SEVIS reporting throughout the student's enrollment. The platform provides a compliance dashboard showing all international students' SEVIS status and upcoming reporting deadlines.

## Target Customer
International student coordinators at boarding schools and day schools enrolling 20-100+ international students per year who currently manage the workflow across 3-4 disconnected systems.

## Impact If Built
Reduces per-student administrative time from 3-4 hours to under 1 hour across the admissions-to-enrollment lifecycle. Prevents SEVIS compliance violations that can result in the school losing its SEVP certification — a catastrophic outcome that eliminates the school's ability to enroll any international students.
