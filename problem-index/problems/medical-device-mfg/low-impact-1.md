# DHR Assembly from Disconnected Systems

**Industry:** [[medical-device-mfg|Medical Device Manufacturing]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Device History Records — the complete production documentation package that FDA requires for every manufactured lot — are assembled by quality technicians who manually pull records from MES, ERP, LIMS, and quality systems and compile them into a single document, a 2-4 hour task per lot that generic document management cannot automate because it doesn't understand the DHR structure or the cross-system record linkages.
**Tags:** #llm #named-entity-recognition #nlp #data-integration #compliance

## The Problem
21 CFR Part 820.184 requires a Device History Record for each batch or lot of finished medical devices, containing: production dates, quantities, acceptance records, component traceability, labeling records, and any deviations or nonconformances. In practice, this means pulling production batch records from MES, component lot traceability from ERP, inspection and test results from QMS or LIMS, sterilization records from sterilization monitoring systems, labeling verification records, and any deviation or nonconformance reports associated with the lot. A quality technician assembles this package manually — logging into 4-6 systems, locating records by lot number, exporting or printing each record, and compiling them into the DHR folder. For a device manufacturer releasing 20-50 lots per week, this represents 40-200 hours per week of skilled quality technician time spent on document assembly rather than quality analysis.

## What Already Exists
Quality management platforms (MasterControl, ETQ, Veeva Vault Quality) provide document control and can store the assembled DHR. ERP systems generate component traceability reports. MES platforms log production batch records. Each system produces its own reports, but none of them can reach into the other systems to pull the complete record set. Enterprise integration platforms (MuleSoft, Boomi) can connect systems but require custom development for each data linkage and don't understand the DHR completeness requirements — they can move data but cannot verify that all required records are present for a given lot.

## The Customisation Gap
A DHR assembly automation system needs: (1) a cross-system query engine that can locate records by lot number across MES, ERP, LIMS, QMS, and sterilization monitoring systems — using each system's API or database; (2) a DHR completeness model that knows which record types are required for each device type based on the device master record and production routing; (3) a gap detection layer that identifies missing records (e.g., inspection result not found for this lot, sterilization record missing) and alerts the quality team before the DHR is finalized; (4) a compilation engine that assembles retrieved records into the DHR structure the quality team expects, with index and cross-references. The device-type-specific completeness rules and the cross-system record linkage logic are the domain-specific components that no generic integration platform provides.

## Impact If Solved
Reduces DHR assembly time from 2-4 hours per lot to 15-30 minutes of review and approval. Eliminates incomplete DHRs — a common FDA audit finding. For a manufacturer releasing 30 lots per week, recovering 60-120 hours per week of quality technician time redirects skilled personnel from document assembly to quality engineering and process improvement.
