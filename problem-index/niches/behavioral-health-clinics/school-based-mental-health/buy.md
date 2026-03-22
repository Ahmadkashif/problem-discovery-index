# Medicaid School-Based Billing Connector

**Niche:** [[niches/behavioral-health-clinics/school-based-mental-health/profile|School-Based Mental Health Providers]]
**Industry:** [[industries/behavioral-health-clinics|Behavioral Health Clinics]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Medicaid billing vendors handle claim submission for school districts, but they can't connect to the therapist's clinical documentation — so session data is re-keyed manually, eligible sessions go unbilled, and reimbursement is left on the table.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #automation #compliance #data-integration

## The Problem
School districts can bill Medicaid for mental health services provided to eligible students by licensed clinicians — a revenue source worth $500K-$5M annually for mid-to-large districts. But the billing rules are state-specific nightmares: some states require specific provider credential types (LCSW but not LPC, or vice versa), specific CPT/HCPCS codes for school-based settings, documentation that the service occurred during the school day (or in some states, explicitly outside instructional time), and parental consent forms renewed annually. School-based Medicaid billing vendors (PCG, MAXIMUS, Cambrian) handle claim submission and state-specific rules, but they receive session data via manual spreadsheet uploads or batch files prepared by district staff. The therapist documents a session in their own system; someone (often an administrative assistant) re-enters that data into the billing vendor's portal weeks later. Sessions fall through the cracks. An estimated 25-40% of billable school-based mental health sessions go unclaimed.

## What Already Exists
Medicaid school-based billing vendors (PCG, MAXIMUS, Cambrian) have built state-specific rule engines for claim submission. They know which services are billable, which provider types qualify, and what documentation the state Medicaid agency requires. On the clinical side, therapists document sessions in EHRs (TherapyNotes, SimplePractice) or school-based systems. Both sides of the workflow exist — they just don't talk to each other.

## The Customization Gap
The missing piece is an integration layer between the therapist's clinical documentation and the billing vendor's submission platform. This connector would: (1) auto-extract billable session data from clinical notes (date, duration, CPT code, student Medicaid ID, provider NPI), (2) apply state-specific eligibility rules to flag non-billable sessions before submission (e.g., student's Medicaid lapsed, provider credential not covered in this state), (3) format and transmit claims to the billing vendor's system via API or structured file, and (4) use a classification model trained on historical claim outcomes to predict which sessions are likely to be denied and flag documentation gaps before submission. State-specific rule variation is the core complexity — each state connector is essentially a separate product.

## Target Customer
District CFOs and Medicaid billing coordinators in the ~3,000 school districts nationally that actively bill Medicaid for school-based services, plus the billing vendors themselves (PCG, MAXIMUS) who would benefit from cleaner upstream data.

## Impact If Solved
Districts capture 20-35% more Medicaid reimbursement by billing every eligible session instead of the subset that makes it through manual data entry. Administrative staff time spent on billing data prep drops by 70-80%. Denial rates decrease because documentation gaps are caught before claim submission, not after.
