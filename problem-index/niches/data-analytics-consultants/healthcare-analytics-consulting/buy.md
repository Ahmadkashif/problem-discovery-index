# Clinical Code Set Mapping for Cross-System Analytics

**Niche:** [[niches/data-analytics-consultants/healthcare-analytics-consulting/profile|Healthcare Analytics Consulting]]
**Industry:** [[industries/data-analytics-consultants|Data Analytics Consultants]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** UMLS and the NLM's code set mapping services provide standard crosswalks between ICD-10, SNOMED, LOINC, and RxNorm, but analytics consultants need client-specific mappings that account for local code usage patterns, custom local codes, and code set version mismatches.
**Tags:** #data-integration #nlp #automation #tabular-ml

## The Problem
A healthcare analytics consultant analyzing readmission rates across two hospitals in a health system discovers that Hospital A codes congestive heart failure as ICD-10-CM I50.9 while Hospital B codes it as I50.22. Both are clinically valid but represent different specificity levels, making cross-hospital comparison inaccurate. Lab results are coded to different LOINC versions — one hospital upgraded to LOINC 2.77, the other is on 2.73, and 200+ codes have changed between versions. Medication data uses NDC codes at one hospital and RxNorm CUIs at another. The consultant spends 2-3 weeks building custom code mappings for each cross-system analytics project.

## What Already Exists
The National Library of Medicine's UMLS provides standard crosswalks between medical terminologies. OHDSI's OMOP Common Data Model standardizes clinical data for research. Code set mapping tools like Apelon DTS and Clinical Architecture's Symedical provide terminology mapping services. But these tools provide generic mappings — they cannot account for a specific hospital's local coding practices (Hospital A always uses the less specific I50.9 because their coders follow a different coding guideline), custom local codes (many hospitals create local procedure codes for facility-specific workflows), or code set version mismatches across sites.

## The Customization Gap
The adaptation requires: (1) ingesting the client's actual code usage data (which codes appear in their data, at what frequency) rather than relying on standard crosswalks, (2) identifying client-specific coding patterns (Hospital A codes CHF at a lower specificity than Hospital B), (3) generating custom mapping tables that account for local codes and version differences, (4) validating mappings through clinical subject matter expert review (automated suggestions, human confirmation), and (5) producing a mapping documentation artifact for the client showing exactly how codes were harmonized and why. The tool should learn from previous mapping projects to suggest likely mappings for new engagements.

## Target Customer
Healthcare analytics consultants performing cross-facility, cross-system, or cross-payer analytics where code harmonization is a prerequisite for meaningful analysis.

## Impact If Solved
Reduces code mapping effort from 2-3 weeks to 2-3 days per engagement. Improves mapping accuracy by 20-30% through data-driven mapping suggestions rather than manual crosswalk lookup. Enables consultants to tackle cross-system analytics projects that were previously too expensive due to mapping overhead.
