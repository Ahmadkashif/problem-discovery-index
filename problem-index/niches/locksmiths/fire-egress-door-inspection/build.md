# From Inspection Photo to Repair Quote in One Pass

**Niche:** [[niches/locksmiths/fire-egress-door-inspection/profile|Fire & Egress Door Inspection and Deficiency Repair]]
**Industry:** [[industries/locksmiths|Locksmiths]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An inspector photographs 600 hospital fire doors in two days, then spends a week turning notes into a deficiency report and a quote, while the survey date gets closer.
**Tags:** #cnns #object-detection #large-language-models #transfer-learning #compliance #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn the annual NFPA 80 fire-door inspection into closed deficiencies before the fire marshal or accreditation surveyor arrives, and whoever converts the most findings into documented repairs inside that window takes the account.

## The Problem
An annual fire-door inspection checks each assembly against NFPA 80's list. Labels on door and frame must be present and legible. Clearances must be within limits. The door must self-close and positively latch, with no field modifications, holes or non-rated hardware. Inspectors work fast on site and slowly afterwards. They transcribe findings, look up hardware for replacement parts, price each repair and write a report the facility can show a surveyor. The lag between inspection and quote is where the account is lost, because the facility needs the doors fixed, not just found.

## Why Nobody Has Built This
Fire-protection inspection software grew up around sprinklers and alarms, where devices are standard. Doors are a mix of hardware brands, labels and conditions that needs visual judgement. Locksmith firms doing this work are mostly too small to build software, and the regulation does not prescribe a format.

## What to Build
A capture flow where the inspector photographs the label, hinge edge, latch edge and top of each door. Vision models read and grade the labels, estimate clearances against a reference, and identify closer, lock and exit-device models. A deficiency engine maps findings to NFPA 80 items and to a repair with parts and labour from the firm's price book. The output is a surveyor-ready report and a priced repair proposal on the same day. After repair, a re-inspection photo closes each item, so the facility holds an auditable trail per door.

## Target Customer
Locksmith and door-hardware firms with certified fire-door inspectors serving hospitals, nursing homes, schools and high-rise owners.

## Impact If Built
Turnaround from inspection to quote falls from days to hours. More findings convert to repair work before the survey, and the facility gets a defensible record. That combination wins the next year's inspection contract.
