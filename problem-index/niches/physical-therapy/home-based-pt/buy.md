# Mobile-First PT Documentation with Offline Capability

**Niche:** [[niches/physical-therapy/home-based-pt/profile|Home-Based PT Providers]]
**Industry:** [[industries/physical-therapy|Physical Therapy]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Home-based PTs get a documentation platform designed for the field — offline-capable, mobile-first, with GPS mileage tracking and homebound status templates — instead of wrestling clinic-designed EMRs on a laptop in a patient's living room.
**Tags:** #feature-engineering #data-integration #workflow-orchestration #worker-facing

## The Problem
Home-based PTs document care in patients' homes where Wi-Fi is unreliable or nonexistent, desk space doesn't exist, and the workflow is fundamentally different from a clinic. They need to document: clinical findings (ROM, strength, balance), treatment provided, home environment observations, homebound status justification, mileage for reimbursement, and time-in/time-out for productivity tracking. Current options force them into clinic-designed EMRs (WebPT on a laptop balanced on a kitchen counter) or home health agency EMRs (Axxess, WellSky) that handle nursing documentation well but lack PT-specific outcome measures, treatment plan templates, and exercise prescription workflows.

## What Already Exists
WebPT and Clinicient/Prompt provide excellent PT-specific documentation but require stable internet and are designed for clinic workflows (receptionist check-in, multiple treatment rooms, scheduled blocks). Home health EMRs (Axxess, WellSky, KanTime) handle mobile documentation and offline sync but are nursing-centric — their assessment templates, care plan structures, and billing modules are designed for skilled nursing, not physical therapy. General mobile documentation tools (DrChrono mobile, Practice Fusion mobile) lack PT-specific features entirely.

## The Customization Gap
The gap is PT-specific clinical logic running on a home-health-appropriate mobile platform. Requirements: (1) offline-first architecture that syncs when connectivity returns, (2) PT-specific outcome measure calculators (TUG, Berg Balance, Tinetti, 6MWT) with auto-populated trend charts, (3) homebound status documentation templates that satisfy Medicare's homebound criteria with structured data entry rather than free-text narratives, (4) integrated GPS mileage tracking that automatically logs drive distance between patient visits for reimbursement, (5) home environment assessment templates linked to the clinical note, and (6) treatment plan templates organized by home-based PT protocols (limited equipment progressions, caregiver training documentation, transfer training sequences). This requires combining the mobile/offline infrastructure of home health EMRs with the clinical depth of dedicated PT platforms.

## Target Customer
Independent home-based PT contractors and home health agency PT directors who need field-ready documentation that is PT-clinically specific, not nursing-adapted, and works without consistent internet.

## Impact If Solved
Reduces documentation time per home visit by 10-20 minutes by eliminating workarounds (writing notes on paper, re-entering in EMR later, manually calculating mileage). Improves homebound status documentation quality, reducing Medicare claim denials. Gives home-based PTs documentation tools comparable to what clinic-based PTs enjoy, addressing a persistent professional frustration.
