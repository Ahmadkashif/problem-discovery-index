# Travel Nurse Tax Compliance and Stipend Documentation

**Niche:** [[niches/staffing-agencies/healthcare-travel-staffing/profile|Healthcare Travel & Per Diem Staffing]]
**Industry:** [[industries/staffing-agencies|Staffing Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** Travel staffing firms must document each nurse's tax home, stipend eligibility, and per diem compliance to avoid IRS reclassification that would cost the firm and the nurse thousands in back taxes.
**Tags:** #compliance #automation #worker-facing #data-integration

## The Problem
Travel nurses receive tax-free stipends for housing, meals, and incidentals — but only if they maintain a "tax home" and can document that they are duplicating living expenses while on assignment. The IRS requires that the nurse have a permanent residence they maintain while traveling, and the staffing firm must verify this to justify the tax-free status of stipends. If the IRS reclassifies stipends as taxable income (because the nurse does not maintain a true tax home), both the nurse and the agency face back-tax liability, penalties, and interest. Most staffing firms collect a tax home attestation at onboarding and never revisit it, even when the nurse's situation changes (they sell their home, move in with a partner at their assignment location, or take back-to-back assignments in the same city for 2+ years).

## Why It's Still Broken
Tax home determination is a facts-and-circumstances test with no bright-line IRS rule. The staffing firm is not the nurse's tax advisor but bears co-liability if stipends are improperly classified. Most firms use a one-time questionnaire at onboarding and assume the answers remain valid. No system tracks the ongoing indicators that a nurse's tax home status may have changed: extended assignment in the same metro area, mail forwarding to assignment address, driver's license change, or voter registration in the assignment state. The compliance risk accumulates silently until an IRS audit surfaces it.

## What a Fix Looks Like
A tax home compliance monitoring system integrated with the staffing firm's HR and assignment data. The system flags risk indicators: a nurse has worked in the same metro area for 12+ consecutive months, a nurse has no permanent address on file, a nurse's assignment history shows no return to their declared tax home between assignments. For flagged nurses, the system generates a re-verification questionnaire and documentation checklist. The system maintains an audit-ready file for each nurse with their tax home declaration, supporting documentation (lease/mortgage, utility bills), and assignment history — ready for IRS examination.

## Who Feels the Pain
Payroll and compliance teams at healthcare staffing firms who face $500K-$2M in potential liability from IRS reclassification of stipends across dozens of nurses, plus the nurses themselves who could owe $5K-$15K in back taxes per assignment year.

## Impact If Fixed
Eliminates IRS reclassification risk that can cost $500K-$2M per audit event, protects nurses from unexpected tax liability, and differentiates the staffing firm as a compliance-first employer in a market where nurses increasingly evaluate firms on tax home support.
