# Aerospace Precision Machining

**Parent Industry:** [[industries/contract-manufacturing|Contract Manufacturing]]
**Category:** Low Digitized

## Profile
**Market Size:** $30-40B
**Share of Parent Industry:** ~8-10%
**Digital Adoption:** Low-Medium — CNC machines are digitally controlled but quality documentation, AS9100 compliance, and First Article Inspection reports are assembled manually
**Target Buyer:** Quality Director or DCMA liaison at precision machining job shops serving aerospace primes
**Automation Potential:** Medium — First Article Inspection reporting, AS9100 documentation, and SPC compliance are highly automatable but require aerospace-specific domain logic

## What Makes This a Distinct Niche
Aerospace precision machining shops produce flight-critical components — turbine blades, landing gear fittings, structural brackets, engine housings — under AS9100 quality management standards with DCMA (Defense Contract Management Agency) oversight for defense programs. Every new part number requires a First Article Inspection (FAI) per AS9102 — a complete dimensional inspection of the first production unit with results documented in a standardized format that traces each dimension to the engineering drawing. Every production lot requires in-process SPC with documented process capability (Cpk) for critical dimensions. Non-conformances require formal Material Review Board (MRB) disposition. These documentation requirements create a paperwork burden that is disproportionate to shop size — a 30-person machine shop serving aerospace primes may dedicate 3-5 people to quality documentation alone.

## Current Tools & Gaps
QualityOne, Net-Inspect, and 1factory provide AS9102 FAI report management. CMM (Coordinate Measuring Machine) software from Hexagon and Zeiss captures dimensional data. ERP systems (JobBOSS, E2 Shop System) manage job scheduling. No platform connects CMM measurement data directly to FAI report templates and AS9100 quality records without manual data transcription — the quality inspector measures a dimension on the CMM, then manually enters the value into the FAI report template, a transcription step that introduces errors and consumes hours per report.

## Problems
- [[niches/contract-manufacturing/aerospace-precision-machining/build|🔨 Build: CMM-to-FAI Automated Report Generation]]
- [[niches/contract-manufacturing/aerospace-precision-machining/buy|🛒 Buy: AS9100-Aware SPC Module for Job Shop ERP]]
- [[niches/contract-manufacturing/aerospace-precision-machining/fix|🔧 Fix: Manual First Article Inspection Data Transcription]]
