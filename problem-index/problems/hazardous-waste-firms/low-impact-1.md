# Generator Status and the Biennial Report Built From Manifests

**Industry:** [[hazardous-waste-firms|Hazardous Waste Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every manifest a generator signs is now in EPA's e-Manifest system, yet multi-site generators still work out each site's monthly status and rebuild their Biennial Report by hand from spreadsheets that never match it.
**Tags:** #change-point-detection #large-language-models #descriptive-statistics #data-integration #compliance #automation #quick-win

## The Problem
A generator's obligations depend on how much hazardous waste each site makes each calendar month. At 100 kg or less a site is a very small quantity generator (40 CFR 260.10), above 100 and below 1,000 kg a small quantity generator, and at 1,000 kg or more a large quantity generator, with different accumulation limits, training, contingency planning and reporting. A plant that cleans out a tank or a lab that clears a stockroom can jump a level for a month. The Generator Improvements Rule lets a site manage one planned or unplanned episodic event a year without changing status, if it notifies first (estimate). Large generators then file a Biennial Report by 1 March of each even-numbered year, describing every waste stream by source, form and management method, and small generators re-notify every four years (1 September 2025, then 2029) (search summary).

An EHS manager covering 20–50 sites (estimate) assembles this from accumulation logs, invoices from three or four waste vendors, the vendors' own reports and whatever the plants kept. Status mistakes surface at inspection, as a small generator site that should have been running large-generator controls. Biennial Report mistakes surface when the state compares the report with the receiving facilities' reports and the manifests.

## What Already Exists
EHS platforms (Enablon, Cority, Sphera, VelocityEHS) store waste records and offer report templates. EPA's RCRAInfo takes Biennial Report and site notification filings, and many states use its myRCRAid module. Waste vendors give customers portals with their own shipment history, and the third e-Manifest rule now requires small and large generators to register so they receive their final signed manifests electronically.

## The Customisation Gap
The tools count what someone types in. The industry-specific logic is: monthly status computed per site from generation records and every manifest across every vendor, not one vendor's portal; state rules layered on federal ones, such as state-only waste codes and stricter thresholds; episodic-event tracking against the one-a-year allowance; Biennial Report source, form and management-method codes taken from the receiving facility's own records instead of re-keyed; and a reconciliation that flags every waste stream where the draft report, the e-Manifest record and the receiving facility's report disagree before the state does. Public e-Manifest data, released 90 days after receipt (search summary), lets a vendor or consultant run the same check from the outside.

## Impact If Solved
A Biennial Report cycle costs a multi-site EHS manager ~40–80 hours per large-generator site (estimate). Building it from the manifest record would cut that by more than half, saving ~1,000 hours a cycle for a 30-site generator (estimate), and would catch status errors before an inspector does.
