# Serial Genealogy MES Extended to the Penetrant Booth

**Niche:** [[niches/aerospace-parts-suppliers/engine-components-rotating-parts/profile|Engine Components & Rotating Parts]]
**Industry:** [[industries/aerospace-parts-suppliers|Aerospace Parts Suppliers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Engine-part MES already tracks every serial from heat lot to shipment; it stops at the inspection booth door.
**Tags:** #data-integration #feature-engineering #evaluation-metrics #compliance #automation #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to turn more of the industry's scarce castings and forgings into accepted engine parts, and whoever proves the lowest scrap and re-process rate at final inspection with no rise in escapes takes the account.

## The Problem
Life-limited rotating parts need back-to-birth records: heat lot, forging, every machining and special-process operation, every inspection. MES systems hold this genealogy. Inspection enters as a pass or fail and a stamp, so the richest quality signal in the plant (what was seen, where, how big, and why it was accepted) never joins the genealogy.

## What Already Exists
Siemens Opcenter, SAP QM, Plex and Dassault's DELMIA run genealogy and nonconformance workflows at large engine-part plants; newer platforms such as First Resonance's ION serve quality-critical hardware makers. NDT systems store radiographs in their own archives.

## The Customization Gap
The MES needs an inspection-evidence object: indication images and annotations attached to serial and feature, penetrant-line parameters attached to the batch, disposition reasons from a controlled list, and re-process loops recorded as events. It needs analytics that join these to downstream findings (machining reveals, customer returns, shop-visit findings) by feature. All of it must sit inside an ITAR-compliant deployment and leave the certified inspector's workflow no slower.

## Target Customer
Plant IT and quality-systems leads at engine-part makers already running a genealogy MES.

## Impact If Solved
Extending an existing MES avoids a new system in a validated environment and turns inspection from a gate into a data source, enough to start finding the ~10–20% of rejects (estimate) that trace to process conditions rather than the part.
