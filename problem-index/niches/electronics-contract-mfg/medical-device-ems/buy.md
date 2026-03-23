# Contract-Manufacturer DHR Engine

**Niche:** [[niches/electronics-contract-mfg/medical-device-ems/profile|Medical Device EMS (ISO 13485)]]
**Industry:** [[industries/electronics-contract-mfg|Electronics Contract Manufacturing]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** QMS-based DHR tools (MasterControl, Greenlight Guru) assume the manufacturer owns both design and production records — but an EMS provider generates only the production records while the OEM owns the design records, creating a DHR assembly workflow that spans two organizations' quality systems and no tool handles natively.
**Tags:** #data-integration #automation #compliance

## The Problem
In the EMS model, the DHR is a shared responsibility: the EMS provider generates production batch records (from MES), inspection results (from quality system), component traceability (from ERP), and process parameter records, while the OEM owns design specifications, approved drawings, and risk management files that the DHR must reference. The EMS quality team assembles their portion of the DHR and ships it to the OEM, who combines it with their design records for the complete DHR. The formatting, content requirements, and delivery method differ by OEM — one OEM wants a PDF package, another wants records uploaded to their QMS portal, another wants raw data files. Managing 10-30 OEM-specific DHR formats is a significant quality team burden.

## What Already Exists
MasterControl and Greenlight Guru provide DHR workflow management for single-organization manufacturers. They handle document routing, review, and approval within one quality system. EMS-focused MES platforms (Aegis, 42Q) generate production records. Neither bridges the cross-organization DHR gap.

## The Customization Gap
The system must: (1) maintain OEM-specific DHR templates (format, content, delivery method per OEM customer), (2) automatically compile the EMS-generated records (production, inspection, traceability, process parameters) from MES and QMS, (3) format the package to each OEM's specifications, (4) generate the cover documentation linking EMS production records to OEM design records by reference, and (5) deliver via each OEM's preferred channel (portal upload, secure file transfer, PDF shipment). The per-OEM template management and multi-format output are the key customization needs.

## Target Customer
Quality managers and DHR coordinators at medical device EMS providers serving 5+ OEM customers. Approximately 80-120 US medical device EMS providers.

## Impact If Solved
DHR assembly time drops from 2-4 hours to 30-60 minutes per lot across OEM customers. OEM-specific formatting errors decrease by 80-90%. Quality team capacity is freed from document formatting to focus on actual quality improvement.
