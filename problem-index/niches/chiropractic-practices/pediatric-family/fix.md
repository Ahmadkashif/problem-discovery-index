# Pediatrician Referral Resistance

**Niche:** [[niches/chiropractic-practices/pediatric-family/profile|Pediatric & Family Chiropractic]]
**Industry:** [[industries/chiropractic-practices|Chiropractic Practices]]
**Type:** Fix (Pain Point)
**One-liner:** Pediatricians rarely refer to chiropractors because they lack confidence in chiropractic diagnostic rigor for children — and pediatric DCs have no standardized way to communicate clinical findings in a format pediatricians understand and trust.
**Tags:** #data-integration #compliance

## The Problem
Pediatric chiropractors and pediatricians serve overlapping populations but rarely collaborate. Pediatricians are skeptical of chiropractic care for children, citing lack of evidence and safety concerns. When a DC identifies a musculoskeletal issue in a child (torticollis, asymmetric crawling, scoliotic curvature), they want to communicate with the pediatrician — but their documentation uses chiropractic terminology (subluxation listings, motion palpation findings) that pediatricians don't recognize or trust. The DC sends a report saying "C1 subluxation with atlas laterality" — the pediatrician reads it as pseudoscience and doesn't refer.

## Why It's Still Broken
The language gap between chiropractic and medical documentation is a profession-wide issue, but it's most acute in pediatrics where pediatricians are protective of their young patients. Chiropractic EHRs generate reports in chiropractic terminology. There's no translation layer that converts chiropractic findings into medical-compatible language — "C1 subluxation with atlas laterality" mapped to "cervical segmental dysfunction with asymmetric atlantooccipital joint mobility" with relevant ICD-10 codes and standardized functional assessments that a pediatrician would recognize.

## What a Fix Looks Like
A inter-professional communication template that generates pediatrician-compatible reports from chiropractic findings: translates chiropractic terminology to medical terminology, includes standardized functional assessments (e.g., AIMS for infants, functional movement screens for children), references evidence-based literature supporting the clinical findings, and uses a format consistent with medical consultation reports (History, Findings, Assessment, Plan with ICD-10 codes). Designed to build trust through clinical rigor, not chiropractic philosophy.

## Who Feels the Pain
Pediatric DCs who want to build referral relationships with pediatricians but can't bridge the terminology and credibility gap. Parents who must choose between their chiropractor and their pediatrician when the two professionals can't communicate.

## Impact If Fixed
Enables pediatrician-chiropractor co-management relationships that increase pediatric referral volume by 20-40% for participating practices. Improves clinical outcomes through coordinated care. Positions pediatric chiropractic as a complementary service rather than an alternative, expanding the addressable market.
