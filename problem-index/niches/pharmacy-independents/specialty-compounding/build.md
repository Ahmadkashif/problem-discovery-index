# Compounding Workflow and Batch Record Platform with USP Compliance Automation

**Niche:** [[niches/pharmacy-independents/specialty-compounding/profile|Specialty Compounding Pharmacy]]
**Industry:** [[industries/pharmacy-independents|Independent Pharmacies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A platform that manages the entire compounding workflow — from master formulation record to batch compounding to quality testing to beyond-use dating — generating USP-compliant documentation automatically instead of requiring 10-15 minutes of manual paperwork per preparation.
**Tags:** #large-language-models #feature-engineering #data-integration #compliance #workflow-orchestration #automation #tacit-knowledge-ml

## The Problem
Compounding pharmacists manage a manufacturing-like workflow using retail pharmacy software and paper records. Each compounded preparation requires: selecting or creating a master formulation record, verifying ingredient lot numbers and certificates of analysis, documenting the compounding process step-by-step (weights, measurements, mixing times, equipment used), calculating beyond-use dating based on stability data and USP guidelines, and filing the completed batch record for inspection readiness. A busy compounding pharmacy produces 30-80 preparations per day, each generating 1-3 pages of documentation. Experienced compounding pharmacists develop tacit knowledge about formulation adjustments — knowing that a particular base cream needs 2% more emulsifier in humid conditions, or that a specific hormone compound requires lower mixing speed to maintain particle size — knowledge that lives in the pharmacist's head and is lost when they leave or retire.

## Why Nobody Has Built This
Compounding workflows vary significantly between pharmacies: a dermatology-focused compounder has different formulation libraries, equipment, and quality requirements than a sterile IV compounder or a veterinary compounder. Building a universal platform requires accommodating USP 795 (non-sterile), USP 797 (sterile), and USP 800 (hazardous) workflows in a single system. The market size (~3,000 active compounding pharmacies in the US) is small enough that enterprise software companies ignore it, and the regulatory complexity (USP chapters update regularly, state boards add requirements) means the compliance engine requires ongoing maintenance. Integration with the dispensing PMS is necessary for billing but each PMS has different APIs and data models.

## What to Build
A cloud-based compounding management platform with: (1) a master formulation record library with version control, ingredient substitution rules, and formulation-specific compounding instructions, (2) batch record automation that pre-fills ingredient lot numbers from barcode scans, calculates quantities based on prescription strength and volume, and timestamps each compounding step, (3) beyond-use dating calculation based on USP guidelines and available stability data, (4) quality testing workflow integration (potency, sterility, endotoxin) with result documentation, (5) USP compliance report generation for state board inspections. The tacit formulation knowledge of experienced compounders is captured through structured formulation notes, adjustment history, and outcome tracking — building an institutional knowledge base that survives staff turnover.

## Target Customer
Compounding pharmacy owners producing 20+ preparations per day who spend 3-5 hours daily on batch record documentation and face annual state board inspections requiring complete compounding records.

## Impact If Built
Reduces per-preparation documentation time from 10-15 minutes to 2-3 minutes, saving 3-5 hours per day for a pharmacy producing 40+ preparations. Eliminates the most common inspection findings — incomplete batch records, missing ingredient lot documentation, and improperly calculated beyond-use dates — which can result in $5,000-25,000 fines or license suspension. Captures formulation expertise that currently exists only in individual pharmacists' memories.
