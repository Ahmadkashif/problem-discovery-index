# Fire Alarm ITM Reporting to the AHJ

**Industry:** [[security-alarm-integrators|Security Alarm Integrators]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Field-service software already schedules inspections and captures checklists, but NFPA 72 testing is recorded device by device, reported to each fire marshal in that jurisdiction's own way, and turned into repair quotes by hand.
**Tags:** #large-language-models #transformers #feature-engineering #evaluation-metrics #compliance #workflow-orchestration #automation

## The Problem
A fire alarm integrator's service department lives on inspection, testing and maintenance (ITM) contracts. NFPA 72 sets the frequencies. Initiating devices, notification appliances, control units, batteries, and the communicator that reports to the central station are each tested on their own schedule, most of them annually and some semi-annually or quarterly. A two-person crew walks a mid-size building testing several hundred smoke detectors, pull stations, duct detectors and horn-strobes. One technician activates devices while the other watches the panel and logs what came in. The result is a report that lists every device, its location, its result and every deficiency.

That report then goes three places. The building owner wants it for insurance. The integrator's sales team needs it to quote the repairs, which is where the margin is. And the fire marshal increasingly demands it through a third-party portal. Raleigh has required reports through Brycer's The Compliance Engine since 2015, and Gastonia and Charleston require fire alarm annual reports there too. Other jurisdictions want e-mail, paper or their own forms. Deficiencies sit in the PDF until someone reads it, prices the repair and chases approval. Meanwhile the building is out of compliance and the AHJ can cite it.

## What Already Exists
Fire and life-safety inspection software (Inspect Point, BuildingReports, ServiceTrade) and general field-service platforms (ServiceTitan, Salesforce Field Service) schedule recurring inspections, capture device lists with barcodes, produce NFPA-styled reports and generate quotes. Brycer and similar portals collect reports for AHJs, funded by per-report fees paid by contractors.

## The Customisation Gap
The fire-alarm-specific logic is thin in all of them. It starts with a device inventory that survives renovations, so that last year's device list reconciles to this year's after detectors are added or moved. Test results have to be keyed to the NFPA 72 edition the jurisdiction adopted, not the latest one. Each AHJ's submission rules need mapping, including which portal, which form, which deficiency categories and which deadlines for correction. Deficiencies need classing as impairments, deficiencies or recommendations, each with its own clock. And every deficiency should flow straight into a priced repair quote using the integrator's parts and labour book. Reports from other contractors, inherited when the integrator takes over a building, arrive as PDFs in every format and have to be re-keyed to start the inventory.

## Impact If Solved
A crew that finishes a building with a reconciled inventory, an AHJ-ready submission and draft repair quotes in hand saves an estimated one to three hours of office work per report. It also cuts the weeks deficiencies now sit unquoted, which is both the integrator's best margin and the building owner's largest compliance exposure.
