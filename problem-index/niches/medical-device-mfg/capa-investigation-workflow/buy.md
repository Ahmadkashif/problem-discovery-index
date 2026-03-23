# Cross-System CAPA Evidence Aggregator

**Niche:** [[niches/medical-device-mfg/capa-investigation-workflow/profile|CAPA Investigation Workflow]]
**Industry:** [[industries/medical-device-mfg|Medical Device Manufacturing]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** QMS platforms like MasterControl and Veeva manage the CAPA workflow, but the evidence that feeds the investigation — complaint records, production batch data, supplier COAs, equipment calibration history — lives in 4-6 other systems that the QMS cannot query, forcing quality engineers to manually search and copy-paste data from each system.
**Tags:** #data-integration #automation #compliance

## The Problem
A quality engineer investigating a CAPA must gather evidence from: the complaint management system (related complaints, complaint patterns), MES (production parameters for the suspect lot, equipment used, operators), ERP (component lot traceability, supplier history), LIMS (testing results for the suspect lot), calibration management (was the measurement equipment in calibration?), and previous CAPAs in the QMS (similar investigations, root causes found). The engineer manually logs into each system, searches by lot number or date range, exports or screenshots the relevant data, and pastes it into the CAPA investigation record. This evidence gathering consumes 30-50% of total CAPA investigation time.

## What Already Exists
QMS platforms (MasterControl, Veeva, ETQ) manage the CAPA record and workflow. Integration middleware (MuleSoft, Boomi) can move data between systems. Business intelligence tools (Power BI, Tableau) can create dashboards across data sources. None of these tools understand the CAPA investigation context — they do not know which data from which system is relevant to a specific CAPA based on its complaint type, suspect product, and time window.

## The Customization Gap
The aggregator must understand CAPA investigation context: given a CAPA triggered by a complaint about Device X, Lot Y, reported on Date Z, it should automatically pull complaint history for Device X (from complaint system), production parameters for Lot Y (from MES), component lots used in Lot Y (from ERP), testing results for Lot Y (from LIMS), equipment calibration status for equipment used on Lot Y (from calibration system), and similar historical CAPAs (from QMS). The relevance logic — which data to pull, how far back to look, which parameters matter — is specific to medical device quality investigation.

## Target Customer
Quality engineers and CAPA managers at device manufacturers running MasterControl, Veeva, or ETQ as their QMS. Approximately 400-600 US device manufacturers with formal CAPA programs.

## Impact If Solved
Evidence gathering time drops from 8-15 hours per CAPA to 1-2 hours. Quality engineers spend investigation time analyzing evidence rather than collecting it. CAPA closure rate increases by 30-40% as investigations are no longer bottlenecked by data collection.
