# Medical Device EMS (ISO 13485)

**Parent Industry:** [[industries/electronics-contract-mfg|Electronics Contract Manufacturing]]
**Category:** Underserved Audience

## Profile
**Market Size:** $6-10B
**Share of Parent Industry:** ~10%
**Digital Adoption:** Medium-High — ISO 13485 QMS is mandatory, MES is standard, but the medical-specific quality overlay (DHR, risk management, design transfer) is managed through manual processes layered on top of standard EMS systems
**Target Buyer:** Quality Director or VP Manufacturing at ISO 13485-certified EMS providers (100-1,000 employees)
**Automation Potential:** High — DHR compilation, design transfer documentation, and FDA-specific quality records follow rigid formats with clear automation paths

## What Makes This a Distinct Niche
Medical device EMS providers (Jabil Healthcare, Plexus, Benchmark, and dozens of smaller specialists) manufacture PCBAs and electromechanical assemblies for medical device OEMs under ISO 13485 quality management systems. They face a dual challenge: meeting the OEM customer's specific quality requirements (which may exceed ISO 13485 baseline) while maintaining FDA registration and readiness for FDA inspection of their facility. The EMS provider must generate Device History Records (DHRs) for the OEM, manage design transfer documentation (receiving the OEM's design and translating it into manufacturing processes), and maintain risk management files (ISO 14971) that reference the OEM's design FMEA. This medical-specific quality overlay does not exist in standard EMS quality systems.

## Current Tools & Gaps
ISO 13485-certified EMS providers use QMS platforms (MasterControl, Greenlight Guru, ETQ) alongside standard MES (Aegis, Cogiscan) and ERP (SAP, Epicor). These tools handle generic quality management and production tracking. The gap is in the medical-specific intersection: no platform automates DHR compilation specific to the contract manufacturing context (where the EMS provider generates production records but the OEM owns the design records), manages design transfer workflows (translating OEM design documentation into EMS manufacturing documentation), or tracks risk management activities across the OEM-EMS interface.

## Problems
- [[niches/electronics-contract-mfg/medical-device-ems/build|🔨 Build: OEM-EMS Design Transfer Workflow Platform]]
- [[niches/electronics-contract-mfg/medical-device-ems/buy|🛒 Buy: Contract-Manufacturer DHR Engine]]
- [[niches/electronics-contract-mfg/medical-device-ems/fix|🔧 Fix: Multi-OEM Quality Requirement Conflicts]]
