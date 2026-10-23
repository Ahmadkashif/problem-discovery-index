# The Statutory Inspection Calendar and Its Deficiencies

**Industry:** [[facilities-management-firms|Facilities Management Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** A multi-site FM account must know, for every building, which code-required inspections are due and whether each deficiency an inspector found became a completed repair, and today that lives in a spreadsheet beside a folder of subcontractors' PDF reports.
**Tags:** #large-language-models #bert #transformers #evaluation-metrics #compliance #workflow-orchestration #automation

## The Problem
Every building an FM firm runs carries a calendar of inspections set by codes, insurers and regulators. Sprinkler systems are inspected and tested on NFPA 25 frequencies, fire alarms on NFPA 72, fire doors on NFPA 80 and emergency generators on NFPA 110. Elevators and boilers need state certificates renewed on their own cycles, backflow preventers need annual tests, and kitchens need hood cleaning. In hospitals the same work is audited against Joint Commission Life Safety and Environment of Care standards, whose fire-extinguishing-system standard was cited in nearly nine of ten hospital surveys in 2018 (the most recent figure found). Refrigeration and comfort-cooling equipment holding 15 lb or more of HFC has carried EPA leak-repair obligations since 1 January 2026.

Most inspections are performed by subcontractors, each of whom sends a PDF report in its own format. The deficiencies listed in it, such as a painted sprinkler head, an impaired valve, a failed battery or a door that does not latch, have to be read, turned into work orders, quoted, approved by the client, repaired and then documented as closed. On a portfolio of a few hundred sites that means thousands of deficiencies a year, tracked in a spreadsheet by a compliance coordinator who learns about an overdue inspection when the fire marshal, the insurer's surveyor or the client's auditor asks for it.

## What Already Exists
Inspection software for fire-protection contractors (Inspect Point, BuildingReports), general inspection and checklist apps (SafetyCulture), CMMS compliance modules that schedule recurring PMs, and the AHJ's own third-party report portals in some cities. Healthcare FM teams also buy compliance-document software for survey readiness.

## The Customisation Gap
The tools serve whoever performs the inspection. They do not serve the FM firm that has to govern dozens of inspection subcontractors across many jurisdictions. The industry-specific layer is a frequency library mapped to each site's systems, adopted code edition and jurisdiction; ingestion of every vendor's PDF report into structured deficiencies, each with a severity class (impairment versus housekeeping); automatic creation and tracking of the repair work order and client approval; insurer recommendations and Joint Commission evidence requirements alongside the code; and a portfolio view of overdue inspections and deficiencies left open past their allowed window.

## Impact If Solved
The compliance coordinator stops reconciling PDFs to a spreadsheet, and the FM firm can prove at any moment that every site is current. That turns a citation or an uninsured loss into something it sees weeks ahead, not on the day of the visit. On a 300-site portfolio the reading and re-keying alone is plausibly one to two full-time roles (estimate).
