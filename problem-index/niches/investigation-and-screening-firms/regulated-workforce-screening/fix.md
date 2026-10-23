# Monitoring Consent That Lapsed With the Job Change

**Niche:** [[niches/investigation-and-screening-firms/regulated-workforce-screening/profile|Regulated-Workforce Screening & Monitoring]]
**Industry:** [[industries/investigation-and-screening-firms|Investigation & Background Screening Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Continuous criminal monitoring needs a current FCRA authorisation for each employee, and nobody tracks whether the one signed at hire still covers the alert that just arrived.
**Tags:** #large-language-models #compliance #workflow-orchestration #quick-win #data-integration
**Contested on:** Every serious competitor in this niche is fighting to catch every disqualifying event on a workforce already hired — a new arrest, a lapsed or disciplined licence, an exclusion-list entry — and whoever raises the fewest false alerts while missing none that an auditor or surveyor later finds takes the account.

## The Problem
An employer enrols its workforce in post-hire criminal monitoring. Each alert is a new consumer report for employment purposes, which needs an authorisation that covers ongoing checks and, before any adverse decision, the full pre-adverse and adverse action sequence. Authorisations signed at hire years ago may not mention monitoring, may have been revoked, or may not meet the rules of a state where the employee now works remotely. When an alert arrives, HR acts on it without checking.

## Why It's Still Broken
Authorisations live as PDFs in the applicant tracking system from the hiring event; monitoring enrolment lives in the screener's platform; job and location changes live in the HR system. No one joins the three.

## What a Fix Looks Like
An authorisation registry per employee: what was signed, when, its scope and the jurisdiction rules applied, checked automatically against current role and location. Alerts for anyone without valid coverage are held and a re-authorisation request sent, and every alert carries its authorisation reference into the adverse action workflow.

## Who Feels the Pain
HR business partners acting on alerts; employment counsel facing claims that a monitoring report was obtained without authorisation; employees surprised by a termination based on a check they did not know continued.

## Impact If Fixed
A simple join removes a procedural defect that can void an otherwise sound decision, at almost no cost per employee.
