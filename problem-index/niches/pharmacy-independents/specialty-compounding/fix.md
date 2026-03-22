# USP 797/800 Compliance Documentation Automation

**Niche:** [[niches/pharmacy-independents/specialty-compounding/profile|Specialty Compounding Pharmacy]]
**Industry:** [[industries/pharmacy-independents|Independent Pharmacies]]
**Type:** Fix (Pain Point)
**One-liner:** USP 797 (sterile compounding) and USP 800 (hazardous drug handling) require continuous environmental monitoring, cleaning logs, personnel competency records, and equipment maintenance documentation — all maintained on paper binders that consume 5-10 hours per week and are the top source of inspection deficiencies.
**Tags:** #large-language-models #feature-engineering #compliance #automation #workflow-orchestration

## The Problem
Compounding pharmacies performing sterile preparations (IV admixtures, eye drops, injectable compounds) must comply with USP 797, which mandates: air quality monitoring with viable and non-viable particle counts, temperature and humidity logs for clean rooms, cleaning and sanitization records with frequencies and agents used, personnel garbing and hand hygiene competency assessments (gloved fingertip testing, media fill testing), and master cleaning schedules. USP 800 adds requirements for pharmacies handling hazardous drugs: containment primary engineering controls, closed-system drug transfer devices, spill management protocols, and personnel exposure monitoring. These documentation requirements generate 15-30 pages of records per week, maintained in physical binders. During state board inspections, the pharmacist must produce complete, organized records demonstrating continuous compliance — a scramble that can take 2-3 days of preparation.

## Why It's Still Broken
The requirements are complex and change frequently — USP 797 was significantly revised in 2023 with new categories (Category 1 and Category 2 replacing low/medium/high risk), new beyond-use date limits, and expanded environmental monitoring requirements. Most compounding pharmacies lack dedicated quality assurance staff; the pharmacist-owner handles compliance alongside clinical duties. Commercial compliance software exists for hospital pharmacies (e.g., Simplifi 797, BD Pyxis) but is priced for institutional budgets ($2,000-5,000/month) and designed for hospital-scale sterile compounding operations. Independent compounders need the same documentation rigor at a price point ($200-400/month) appropriate for a 5-person pharmacy.

## What a Fix Looks Like
A compliance management platform designed for independent compounding pharmacies that: (1) provides digital templates for all USP 797/800 documentation — cleaning logs, environmental monitoring records, personnel competency assessments — with auto-scheduling and completion reminders, (2) integrates with environmental monitoring equipment (particle counters, temperature/humidity sensors) to auto-populate readings, (3) tracks personnel training and competency assessment due dates with automated notifications, (4) generates inspection-ready compliance reports organized by USP chapter section, and (5) updates templates automatically when USP chapters are revised. The pharmacist transitions from maintaining paper binders to confirming digital entries and reviewing auto-generated compliance dashboards.

## Who Feels the Pain
The pharmacist-owner who spends 5-10 hours per week on USP compliance documentation instead of compounding or patient care, and the lead technician responsible for daily cleaning logs and environmental monitoring entries who risks the pharmacy's license if any record is missed.

## Impact If Fixed
Reduces weekly compliance documentation time from 5-10 hours to 1-2 hours, reclaiming 3-8 hours per week for revenue-generating compounding activity. Eliminates the 2-3 day inspection preparation scramble by maintaining continuous inspection-readiness. Reduces the most common cause of pharmacy board citations — incomplete or disorganized USP compliance records — which carry fines of $5,000-25,000 and can trigger license suspension.
