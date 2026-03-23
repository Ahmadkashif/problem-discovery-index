# Manual First Article Inspection Data Transcription

**Niche:** [[niches/contract-manufacturing/aerospace-precision-machining/profile|Aerospace Precision Machining]]
**Industry:** [[industries/contract-manufacturing|Contract Manufacturing]]
**Type:** Fix (Pain Point)
**One-liner:** Quality inspectors spend 4-16 hours per First Article Inspection manually transcribing CMM measurement values into AS9102 report templates — copying numbers one by one from the CMM printout into an Excel or PDF form, a mind-numbing process that introduces transcription errors in 5-10% of reports.
**Tags:** #automation #compliance #worker-facing

## The Problem
An AS9102 FAI report for a typical aerospace machined component requires populating 50-300 rows of measured values, each matched to a drawing characteristic number with its nominal, tolerance, and measured value. The CMM captures all measurements digitally, but the output format (DMIS results, Hexagon PC-DMIS report, Zeiss Calypso report) doesn't match the FAI template format. Quality inspectors print the CMM report, then manually type each measurement into the corresponding row of the FAI Excel or PDF template. For a 200-characteristic part, this is 200 individual data entry operations — a 4-16 hour transcription task that requires intense focus to avoid transposing digits or misaligning measurement-to-characteristic mappings.

## Why It's Still Broken
Three factors perpetuate manual transcription. First, CMM output formats vary by machine brand (Hexagon, Zeiss, Mitutoyo) and CMM program structure — there is no universal CMM output standard. Second, the mapping between CMM measurement sequence and drawing characteristic numbers is not standardized — measurement #1 on the CMM may correspond to characteristic #47 on the drawing. Third, FAI management software (Net-Inspect, 1factory) accepts data entry but doesn't import CMM files natively for most machine brands, so the integration gap between CMM output and FAI software remains unresolved.

## What a Fix Looks Like
A CMM output parser that reads the most common output formats (PC-DMIS, Calypso, Polyworks) and presents measurements in a mappable list. The inspector creates a one-time mapping between CMM measurements and drawing characteristics (using a visual drag-and-match interface). For subsequent inspections of the same part, the mapping is applied automatically — CMM file in, populated FAI template out. The system validates that all characteristics are populated (no missing measurements) and flags any out-of-tolerance values before the inspector reviews the completed report.

## Who Feels the Pain
CMM operators and quality inspectors who spend days per month on data transcription — work that adds no quality value and is purely a format translation exercise. Quality managers who find transcription errors during report review, triggering re-inspection and re-documentation.

## Impact If Fixed
Reduces FAI report assembly from 4-16 hours to under 30 minutes for repeat part numbers. Eliminates transcription errors that currently cause 5-10% of FAI reports to require correction after customer review. For a shop producing 10 FAI reports/month, saves 40-160 inspector hours monthly and accelerates part qualification timelines by days per report.
