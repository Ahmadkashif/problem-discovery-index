# Specialty-Specific Patient Intake

**Industry:** [[healthcare-practice-software|Healthcare Practice Software]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Digital intake forms are a solved, crowded product category, and every specialty needs a different set of them, mapped into different discrete fields, which is why practices still hand out clipboards.
**Tags:** #large-language-models #transformers #word-embeddings #transfer-learning #feature-engineering #workflow-orchestration #quick-win

## The Problem
A new patient at a practice supplies demographics, insurance, medical history, medications, allergies, consents and a specialty-relevant history. Every practice management vendor ships digital intake. Adoption is patchy and clipboards persist, because generic intake collects generic information and the practice still has to ask the questions that matter.

An orthopaedic intake needs injury mechanism, prior imaging and functional scores. A behavioural health intake needs standardised screening instruments with scoring. An obstetric intake needs gravidity, parity and dating. A dermatology intake wants lesion history and photographs. Each field must land in the right discrete location in the chart, or the staff re-key it, which is worse than paper.

## What Already Exists
Intake and patient engagement products are numerous and capable — Phreesia, Klara, Luma, Yosi, plus the intake modules inside every EHR. Form builders are mature. E-signature and consent capture are commodity. Insurance card OCR and real-time eligibility verification work well. Standardised instruments like PHQ-9 and GAD-7 are widely implemented.

## The Customisation Gap
The gap is not form building, it is the mapping. Getting a specialty question into the correct discrete field of a specific EHR, so it flows into the note, the problem list and the claim, is bespoke integration work per specialty per vendor. That work is why most deployments collect a PDF that a staff member then reads and re-types.

Specialty content is the second half. Building and maintaining validated question sets across forty specialties is a content problem no single vendor has been willing to fund, and it is exactly the sort of content that could be assembled from what practices already ask — the vendor can observe which fields a specialty actually populates, in what order, and which are left blank across thousands of similar practices.

Language and reading level matter more here than anywhere else in the product. A form written at a twelfth-grade level and offered only in English silently excludes the patients most likely to have gaps in their history.

## Impact If Solved
Intake determines whether the visit starts with a complete chart or a staff member typing. It is also the first impression a practice's patients have of the software, which is why it is disproportionately cited in vendor switching decisions relative to its technical difficulty.
