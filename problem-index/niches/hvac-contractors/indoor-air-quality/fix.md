# IAQ Testing Report Standardization

**Niche:** [[niches/hvac-contractors/indoor-air-quality/profile|Indoor Air Quality]]
**Industry:** [[industries/hvac-contractors|HVAC Contractors]]
**Type:** Fix (Pain Point)
**One-liner:** Every IAQ company generates assessment reports in its own format — Word documents, Excel spreadsheets, PDF exports from sensor dashboards — making it impossible for building owners, property managers, and health departments to compare reports or track IAQ improvements over time.
**Tags:** #automation #compliance #large-language-models

## The Problem
An IAQ assessment produces a report that a building owner or property manager uses to make remediation decisions and, in some jurisdictions, to satisfy regulatory or lease requirements. There is no standard format for these reports. One IAQ company produces a 30-page PDF with sensor data graphs, photos, and narrative analysis. Another produces a 2-page summary with numbers in a table. A third sends the raw sensor CSV with a cover email. The building owner who hires Company A for an initial assessment and Company B for post-remediation verification can't meaningfully compare the two reports because they measure different parameters, report in different units, reference different standards, and present data in different formats. Property managers with IAQ obligations across multiple buildings struggle to aggregate results. Health departments receiving IAQ reports from different companies can't assess whether the reports meet minimum documentation standards.

## Why It's Still Broken
There is no regulatory mandate for a standardized IAQ report format. ASHRAE 62.1 specifies ventilation requirements but not reporting formats. EPA provides IAQ guidelines but no report templates. Without a mandate, each IAQ company develops its own format based on its owner's preferences, the testing instruments used, and the level of effort the company is willing to invest in report presentation. Professional organizations (IAQA — Indoor Air Quality Association, ACCA) publish best practices but not enforceable templates. The result is a fragmented market where report quality ranges from excellent (experienced consultants with professional templates) to useless (sensor screenshots in an email).

## What a Fix Looks Like
A report generation platform that accepts IAQ test data from any instrument format (CSV, API, manual entry), building profile information, and testing conditions, and generates a standardized IAQ assessment report following IAQA/ACCA best practices. The report includes: executive summary, testing methodology, instrument specifications and calibration dates, measured values vs. applicable standards (EPA, ASHRAE, WHO) with clear pass/fail designations, trend data if previous assessments exist, recommended remediation actions prioritized by impact, and appendices with raw data and photos. An LLM layer generates the narrative sections — interpreting the data, explaining exceedances in non-technical language for building owners, and describing recommended actions with expected outcomes. The platform maintains a building history so subsequent assessments automatically show trends and improvement tracking.

## Who Feels the Pain
IAQ consultants who spend 2-4 hours per assessment writing reports from scratch, building owners and property managers who receive inconsistent reports and can't compare or track results, and the IAQ industry broadly — lack of report standardization undermines professional credibility and makes it easy for low-quality operators to compete on price without delivering meaningful assessments.

## Impact If Fixed
Reduces IAQ report generation time from 2-4 hours to 20-30 minutes through automated formatting and LLM-generated narrative. Creates a comparable assessment record across providers, enabling building owners to evaluate IAQ performance over time. Raises the professional standard for IAQ reporting, differentiating serious IAQ companies from sensor-resellers.
