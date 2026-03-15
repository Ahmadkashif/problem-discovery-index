# Engineering Change Order Impact Assessment

**Industry:** [[contract-manufacturing|Contract Manufacturing]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic document analysis tools can read engineering change orders, but don't understand BOM structures, process qualification requirements, or the downstream impact of a material substitution on production tooling, test fixtures, and quality specifications — the manufacturing-specific reasoning that determines whether an ECO is a simple update or a multi-week re-qualification event.
**Tags:** #llm #bert #named-entity-recognition #nlp #compliance #automation

## The Problem

Engineering change orders (ECOs) are the most disruptive operational event in contract manufacturing. An OEM issues an ECO — changing a component, material specification, or dimensional tolerance — and the CM must assess the impact across BOM, process documentation, test procedures, tooling, quality specifications, and regulatory qualification requirements. For a medical device CM, a material change may trigger a full IQ/OQ/PQ process re-qualification under 21 CFR Part 820. For an aerospace CM, a dimensional tolerance change may require new first article inspection and customer design review approval.

Current ECO impact assessment is a manual process: the engineering team reads the ECO, manually traces affected BOMs, consults process engineers on production implications, and generates an impact assessment document that may take 3-10 engineering days for a complex change. In a CM managing 20-50 concurrent programs, ECO volume can be 5-15 per week during active programs.

## What Already Exists

Windchill and Arena PLM provide BOM change tracking and ECO workflow routing. They do not assess manufacturing impact, identify which process steps are affected, flag regulatory re-qualification triggers, or estimate re-qualification timeline and cost.

## The Customisation Gap

An ECO impact assessment tool needs: (1) BOM traversal — linking the changed component or material to every process step and assembly level that uses it; (2) process impact classification — identifying whether the change affects tooling, test fixtures, process parameters, or incoming inspection criteria; (3) regulatory trigger detection — recognizing change descriptions that trigger re-qualification requirements under 21 CFR Part 820, AS9100, or IATF 16949; (4) impact effort estimation — predicting re-qualification timeline and engineering hours based on change type and affected process scope. The regulatory trigger library and effort estimation — requiring manufacturing-domain knowledge — are the gaps generic LLMs don't fill reliably.

## Impact If Solved

Reduces ECO impact assessment time from 3-10 engineering days to 4-8 hours of expert review of an AI-generated assessment. For a CM handling 10 ECOs per week, this recovers 20-40 engineering hours weekly. More importantly, ensures no regulatory re-qualification triggers are missed — a missed re-qualification on a medical device program creates FDA enforcement exposure and potential product recall.
