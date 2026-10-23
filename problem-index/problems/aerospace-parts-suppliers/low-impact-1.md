# AS9102 First Articles Ballooned by Hand

**Industry:** [[aerospace-parts-suppliers|Aerospace Parts Suppliers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** First article software already exists, but it balloons clean vector drawings well and leaves the hard parts (scanned legacy prints, model-based definitions, flag notes, each prime's own FAI rules, and the material and special-process evidence on Form 2) to a quality engineer with a highlighter.
**Tags:** #object-detection #large-language-models #transformers #feature-engineering #evaluation-metrics #compliance #automation #quick-win

## The Problem
Before a supplier ships the first production part of a new part number, after a design change, after a change of sub-tier source or process, or after a production lapse (two years, recalled from AS9102), it must produce an AS9102 first article inspection report. Form 1 identifies the part and the reason for a full or partial FAI, which Revision C (June 2023, per vendor summaries of the standard) made mandatory on every report. Form 2 lists every raw material, special process and functional test with the certification behind it. Form 3 lists every characteristic on the drawing (dimensions, tolerances, GD&T callouts, surface finishes, and every requirement buried in general and flag notes) with a balloon number and a measured result.

Building Form 3 starts with ballooning: numbering every requirement on the drawing so nothing is missed. On a 50–300 characteristic part (estimate) that takes hours by hand, and the customer's quality representative rejects the report if one note ("break all sharp edges", "mask threads before plating per note 7") has no balloon. Then the inspector measures and transcribes, a step the vault already covers in [[niches/contract-manufacturing/aerospace-precision-machining/profile|Aerospace Precision Machining]] under contract manufacturing.

## What Already Exists
Net-Inspect, DISCUS, High QA, InspectionXpert and 1factory provide ballooning and AS9102 form generation, and GroundControl (YC) reports almost 1,000 reports a month across 70+ facilities on its platform. CMM software from Hexagon and Zeiss exports measurements. These tools work well on native vector PDFs from modern CAD.

## The Customisation Gap
The aerospace-specific layer is what the generic tools leave to people. Legacy drawings, including government technical data packages from decades ago, arrive as scanned rasters with hand revisions. Newer programmes ship model-based definitions with product manufacturing information in the 3D model and no drawing to balloon. Flag notes and general notes carry requirements that must become characteristics. Each prime adds its own FAI rules and forms through its supplier quality requirements (Boeing's D6-82479, GE Aerospace's S-1000, Pratt & Whitney's ASQR-01 and Rolls-Royce's SABRe, recalled). Form 2 must show that each special process was done by a processor the customer has approved, which means checking Nadcap status and the customer's approved-source list as well as reading the cert. A tool for this industry has to read all of that, propose the balloons and Form 2 lines, flag what it is unsure of, and know when a change to a sub-tier processor triggers a partial FAI.

## Impact If Solved
Cutting ballooning and Form 2 assembly from ~4–8 hours to under an hour per full FAI (estimate), and first-time customer acceptance from roughly four in five to above 95% (estimate), frees a quality engineer for ~1–2 days a week at a supplier running 20 FAIs a month and stops invoices being held for paperwork.
