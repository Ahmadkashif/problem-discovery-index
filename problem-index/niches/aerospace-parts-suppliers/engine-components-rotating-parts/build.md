# A Disposition Ledger for Every Indication

**Niche:** [[niches/aerospace-parts-suppliers/engine-components-rotating-parts/profile|Engine Components & Rotating Parts]]
**Industry:** [[industries/aerospace-parts-suppliers|Aerospace Parts Suppliers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Engine-part plants record whether a part passed inspection but never what the inspector saw, so neither scrap nor escapes can be traced to the calls that caused them.
**Tags:** #tacit-knowledge-ml #cnns #object-detection #semantic-segmentation #evaluation-metrics #compliance #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to turn more of the industry's scarce castings and forgings into accepted engine parts, and whoever proves the lowest scrap and re-process rate at final inspection with no rise in escapes takes the account.

## The Problem
A disk or blade rejected at final penetrant inspection is scrapped or sent for engineering review with a note on the traveller. A part accepted with a borderline indication leaves no trace at all. When scrap at final inspection runs a few percent (estimate) on parts worth thousands of dollars each, the plant cannot tell how much of it is real defects, inspector variation or poor washing. When a crack is found later, it cannot see what the inspector saw.

## Why Nobody Has Built This
Imaging an FPI indication means changing a certified, Nadcap-audited process, and nobody wants to be the plant that explains a new camera to its auditor. NDT equipment makers sell lines and booths, not disposition data. Quality software stores results, not images. And the value only appears after months of capture.

## What to Build
UV-A-calibrated cameras at each booth that image an indication when the inspector marks it; a disposition record linking image, measured length, call, inspector, part serial, heat lot and penetrant-line parameters; digital radiograph annotation in the same ledger; and dashboards of reject and re-process rates by part feature, inspector and line condition. On top, a second-reader model per part family that flags unmarked indications and calls that differ from site history, routed to the Level III.

## Target Customer
VP Quality and Level III NDT managers at engine-component makers and their finishing subcontractors.

## Impact If Built
A plant that separates real defects from inspector and process variation can cut false rejects by a fraction of a point, worth ~$0.5–5M a year at a mid-size site (estimate), and can show customers a disposition record no competitor has.
