# Dermatology EHR — the Pathology Loop

**Parent Industry:** [[industries/healthcare-practice-software|Healthcare Practice Software]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in dermatology EHR is fighting to close the biopsy loop — specimen out, result back, matched to the exact lesion it came from, patient told, treatment scheduled — and whoever closes it with the fewest open ends takes the account.

## Profile
**Market Size:** $550M US dermatology practice software
**Share of Parent Industry:** ~14% of the specialty EHR block
**Digital Adoption:** High — dermatology digitised early and is heavily concentrated in private-equity-backed groups with real IT capacity
**Target Buyer:** Physician-owners, and increasingly the central operations teams of multi-site dermatology groups
**Automation Potential:** Very High — the loop is a state machine that is currently run on paper logs and memory

## What Makes This a Distinct Niche
Dermatology's central risk is not an image or a measurement: it is an open loop. A visit produces specimens — often several, from several sites on one patient, on one day. Each goes to a lab, comes back days later as a report, must be matched to the lesion it came from, communicated to the patient, and converted into a treatment plan if malignant. Every step is a place a result can stall, and the failure is asymmetric in a way that defines the specialty: a melanoma result sitting unreviewed in a queue is the specialty's malpractice archetype and its most common one. Practices manage this with a paper or spreadsheet log maintained by a medical assistant. That log is the real system of record for the loop, and it is not in the EHR.

## Current Tools & Gaps
ModMed's dermatology product, Nextech, EZDERM and Practice Fusion all ship lab interfaces and a results inbox. The interfaces deliver the report; they do not close the loop. Two specific gaps recur across every vendor. Specimen-to-lesion matching is manual, because the requisition carries a site description in free text and the chart carries a lesion map, and nothing joins them — so a patient with four biopsies produces four reports that a medical assistant assigns by reading. And there is no state model: the product knows a result arrived and does not know whether the patient was told, whether the recommended excision was scheduled, or whether an ordered specimen never came back at all. The missing-result case is the dangerous one and is precisely the one a results inbox cannot represent, because it is defined by absence.

## Problems
- [[niches/healthcare-practice-software/dermatology-ehr-pathology-loop/build|🔨 Build: The Specimen Loop as a Tracked State Machine]]
- [[niches/healthcare-practice-software/dermatology-ehr-pathology-loop/buy|🛒 Buy: Lab Results Interface Adapted to Multi-Site Specimen Matching]]
- [[niches/healthcare-practice-software/dermatology-ehr-pathology-loop/fix|🔧 Fix: The Result Nobody Told the Patient About]]
