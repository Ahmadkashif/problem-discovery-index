# Remanufacturing Work Order Management

**Niche:** [[niches/medical-device-mfg/legacy-device-remanufacturers/profile|Legacy Device Remanufacturers]]
**Industry:** [[industries/medical-device-mfg|Medical Device Manufacturing]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Standard MES and ERP systems model forward-flow manufacturing (raw materials in, finished goods out) — remanufacturing reverses the flow (used device in, assessment, disassembly, component-level refurbishment, reassembly, testing), and no commercial platform handles this reverse workflow natively.
**Tags:** #workflow-orchestration #data-integration #compliance

## The Problem
A remanufacturing work order starts with an incoming used device of unknown condition, branches into multiple component-level refurbishment tasks (some components are replaced, some are refurbished, some pass through), converges at reassembly, and concludes with functional testing against original specifications. This branching-and-converging workflow does not fit the linear routing model of standard MES platforms. Remanufacturers who try to use standard MES (or ERP work orders) end up creating workarounds — multiple sub-work-orders per device, manual routing changes mid-process, and paper-based tracking for component-level work.

## What Already Exists
MES platforms (Plex, IQMS/DELMIAworks, Epicor Advanced MES) handle discrete and process manufacturing work orders. ERP platforms (SAP, Oracle, NetSuite) manage work orders with BOM-based routing. Aftermarket/MRO platforms (IFS, Maximo) handle maintenance and repair workflows for heavy equipment but are not designed for FDA-regulated medical device remanufacturing with its documentation and traceability requirements.

## The Customization Gap
The system must support: incoming device registration with condition-based routing (assessment determines the work order steps), component-level tracking (each component of a disassembled device follows its own refurbishment path), OEM-equivalent replacement part validation (documenting that the replacement part meets original specifications), reassembly verification (confirming all components are accounted for), and final functional testing with results compared to original device specifications. The traceability requirement — linking the remanufactured device to its original device identity, all replaced components, and all refurbishment records — is unique to this niche.

## Target Customer
Operations managers at remanufacturing facilities currently using paper or spreadsheets for work order tracking. Approximately 80-120 US facilities processing 20+ devices per week.

## Impact If Solved
Work-in-process visibility improves from "ask the technician" to real-time dashboard tracking. Device turnaround time decreases 15-25% by eliminating handoff delays between assessment, disassembly, refurbishment, and reassembly. FDA audit preparation drops from days to hours with complete electronic traceability records.
