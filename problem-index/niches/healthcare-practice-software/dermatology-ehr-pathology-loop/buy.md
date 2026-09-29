# Lab Results Interface Adapted to Multi-Site Specimen Matching

**Niche:** [[niches/healthcare-practice-software/dermatology-ehr-pathology-loop/profile|Dermatology EHR — the Pathology Loop]]
**Industry:** [[industries/healthcare-practice-software|Healthcare Practice Software]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** HL7 lab result interfaces are a commodity every EHR ships, and they deliver a dermatopathology report attached to a patient rather than to the lesion it came from, which is the only attachment that matters when a patient has four.
**Tags:** #bert #large-language-models #word-embeddings #evaluation-metrics #confidence-intervals #data-integration #automation #worker-facing
**Contested on:** Every serious competitor in dermatology EHR is fighting to close the biopsy loop — specimen out, result back, matched to the exact lesion it came from, patient told, treatment scheduled — and whoever closes it with the fewest open ends takes the account.

## The Problem
A patient has four biopsies in one visit: left temple, right shoulder, mid-back, left calf. Four reports return, each carrying the site as free text written by whoever completed the requisition — "L temple", "left temporal scalp", "temple, left". The medical assistant reads each report, reads the chart, and assigns. Usually it is obvious. Occasionally two sites are similar enough that it is not, and the consequence of assigning a malignant result to the wrong lesion is an excision on the wrong part of a patient's face. The interface did its job perfectly; it delivered four correct reports to the correct patient.

## What Already Exists
HL7 v2 result interfaces are universal, reliable and cheap, and the large dermatopathology labs all support them. Some labs return structured site fields; most return the free text that was on the requisition, because that is what was written. Integration engines and interface vendors handle transport and patient matching well. Nothing in the bought stack attempts site matching, because site matching is dermatology-specific and the interface vendors are horizontal.

## The Customization Gap
The adaptation is a matching layer over the commodity interface. It requires: (1) normalising site descriptions from both sides — requisition text and chart lesion record — against an anatomical vocabulary that handles laterality, region, and the abbreviations clinicians actually write; (2) scoring candidate matches using site, procedure type, specimen count and collection date together rather than site alone, since the count constraint resolves most genuine ambiguity; (3) returning a confidence and auto-assigning only above a practice-set threshold, with everything else presented as a ranked choice to a human rather than as an empty field; (4) making the unmatched state visible and timed instead of silently pending; and (5) feeding every human correction back as a label, which is how the anatomical vocabulary becomes this practice's vocabulary rather than a textbook's.

## Target Customer
Dermatology practices with meaningful biopsy volume — multi-provider and Mohs-performing practices in particular — and the dermatology EHR vendors who currently ship the interface and stop there.

## Impact If Solved
Auto-matching the unambiguous majority removes a daily reconciliation task and, more importantly, makes the ambiguous minority explicit rather than resolved by assumption. Practices get a measurable match rate per lab, which is a number worth taking to a lab whose requisition practices are generating the ambiguity — the first lever any practice has ever had over that.
