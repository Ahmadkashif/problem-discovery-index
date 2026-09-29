# Investigation Capture Adapted to Evidentiary Standards

**Niche:** [[niches/engineering-consultants/forensic-engineering-firms/profile|Forensic Engineering Firms]]
**Industry:** [[industries/engineering-consultants|Engineering Consultants]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Field data collection apps capture photographs and notes reliably; a forensic scene needs a record whose chain of custody and completeness will be attacked by someone whose job is finding the gap.
**Tags:** #object-detection #cnns #bert #transformers #evaluation-metrics #feature-engineering #automation #compliance #worker-facing #data-integration

## The Problem
Site investigation is the one irreproducible step — the scene is cleared, the failed component is repaired, the evidence is gone. What the expert captures in those hours determines what can be concluded and defended years later. In practice capture is a mixture of photographs, handwritten notes, measurements, and samples, assembled by an engineer who is simultaneously investigating and documenting, with completeness judged against their own mental checklist. Gaps are discovered during report writing or, worse, during deposition, and by then the scene no longer exists.

## What Already Exists
Field capture tooling is mature and cheap. The mobile data collection platforms handle structured forms, photographs with metadata, GPS, and offline operation; evidence management systems handle chain of custody; reality capture and photogrammetry tools produce dimensioned site models from a phone.

## The Customization Gap
All of it captures what the user chooses to capture. What the workflow needs is completeness against an evidentiary standard — a scene-type-specific model of what must be documented for a conclusion to be defensible, checked while the expert is still on site. That model is domain knowledge the firm has, distributed across its senior experts and encoded nowhere. The adaptation is investigation capture organized around hypotheses rather than around forms: as the expert records observations, the system tracks which candidate failure mechanisms remain live and what evidence each would require to support or exclude, and prompts for the observations that are missing. Chain of custody and metadata integrity have to be built for adversarial scrutiny rather than for internal record-keeping, since an attack on the record's provenance is a standard tactic. And the capture record should carry forward into the report as cited evidence, so that every assertion traces to something recorded on site rather than to recollection.

## Target Customer
Practice leaders and technical directors at forensic firms, and the field experts who currently investigate and document simultaneously and learn what they missed weeks later.

## Impact If Solved
Protects the only irreproducible step in the work. Hypothesis-driven prompting also raises the floor on less experienced investigators, which is where evidentiary gaps concentrate, and encodes senior judgment about what a defensible scene record contains.
