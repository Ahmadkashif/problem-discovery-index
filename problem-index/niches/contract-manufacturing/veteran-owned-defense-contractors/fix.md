# ITAR Export Control Compliance for Small Shops

**Niche:** [[niches/contract-manufacturing/veteran-owned-defense-contractors/profile|Veteran-Owned Defense Contractors]]
**Industry:** [[industries/contract-manufacturing|Contract Manufacturing]]
**Type:** Fix (Pain Point)
**One-liner:** Small defense manufacturers manage ITAR compliance through written procedures that no one reads and access control lists maintained in spreadsheets — a compliance posture that creates serious legal exposure when a machinist emails a controlled drawing to a vendor without checking whether the vendor has the required export authorization.
**Tags:** #compliance #automation #worker-facing

## The Problem
ITAR (International Traffic in Arms Regulations) restricts access to defense-related technical data to US persons and authorized foreign nationals. A small machine shop manufacturing defense components must control who can access technical drawings, process specifications, and inspection data — and must track every export (including deemed exports to foreign national employees) with proper authorization. In practice, ITAR compliance at small shops consists of: a written Technology Control Plan (TCP) filed in a binder, an employee nationality verification log maintained in Excel, and a verbal reminder to "don't share drawings outside the company." When a machinist emails a controlled drawing to an outside finishing vendor, nobody checks whether the vendor's facility has foreign nationals with access. When a new employee who is a legal permanent resident (authorized under ITAR) starts work, the access control spreadsheet may not be updated for weeks.

## Why It's Still Broken
ITAR compliance software exists (EASE, SAP GTS) but is designed for large defense contractors with dedicated export control departments and costs $50,000-$200,000 to implement. Small shops cannot justify this investment. The result: ITAR compliance is theoretical (procedures exist on paper) rather than operational (procedures are followed in daily workflow). The consequences of ITAR violations are severe — civil penalties of $500,000 per violation and criminal penalties including imprisonment — but enforcement against small manufacturers has been rare enough that many shops treat compliance as a checkbox rather than an operational requirement.

## What a Fix Looks Like
A lightweight ITAR compliance tool integrated into the shop's daily workflow: employee access control management (nationality verification, authorization status, access rights per program), controlled document tracking (which drawings are ITAR-controlled, who has accessed them, who they've been shared with), visitor management (logging foreign national visitors per TCP requirements), and shipping compliance checks (verifying export authorization before technical data leaves the facility). Implemented as a layer on top of existing file sharing (marking controlled files, alerting on unauthorized sharing attempts) rather than requiring a separate document management system.

## Who Feels the Pain
Shop owners who are personally liable for ITAR violations, and office staff who are informally designated as "the ITAR person" without training, tools, or authority to enforce compliance procedures on the shop floor.

## Impact If Fixed
Transforms ITAR compliance from paper-based procedures to operational workflow controls. Prevents inadvertent ITAR violations that carry $500,000 civil penalties per incident. For a small defense manufacturer, a single ITAR violation investigation — even without a finding — can cost $50,000-$100,000 in legal fees and consume months of management attention. A $5,000-$10,000/year compliance tool is trivially justified against this exposure.
