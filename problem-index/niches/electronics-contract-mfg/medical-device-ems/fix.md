# Multi-OEM Quality Requirement Conflicts

**Niche:** [[niches/electronics-contract-mfg/medical-device-ems/profile|Medical Device EMS (ISO 13485)]]
**Industry:** [[industries/electronics-contract-mfg|Electronics Contract Manufacturing]]
**Type:** Fix (Pain Point)
**One-liner:** When 10-30 OEM customers each impose their own quality requirements (IPC class, inspection frequency, SPC requirements, supplier qualification standards) on a shared production facility, conflicting requirements create confusion on the production floor and quality nonconformances when an operator applies OEM A's standards to OEM B's product.
**Tags:** #compliance #workflow-orchestration #worker-facing

## The Problem
Each medical device OEM specifies quality requirements for their products manufactured at the EMS facility: IPC class (Class 2 vs. Class 3), inspection type and frequency (100% visual vs. sampling), SPC charting requirements (which characteristics, what Cpk threshold), acceptance criteria for visual inspection (OEM-specific cosmetic standards beyond IPC), and supplier qualification standards (OEM-specific AVL restrictions). When a production line runs OEM A's product followed by OEM B's product, the operators and inspectors must switch between two different quality requirement sets. At a facility serving 10-30 OEMs, operators carry laminated cards or reference binders listing each OEM's requirements. Mix-ups are common — applying Class 2 inspection to a Class 3 product, or using the wrong cosmetic acceptance standard — generating nonconformances that damage the EMS provider's quality scorecard with the affected OEM.

## Why It's Still Broken
Quality requirements are documented in each OEM's quality agreement and translated into work instructions and inspection procedures by the EMS quality team. But the work instructions and inspection procedures are static documents that operators must actively consult. No system dynamically presents the correct quality requirements based on the product currently being run on the line. The EMS quality team updates these documents manually when OEM requirements change, and changes communicated by email may take weeks to propagate to the production floor.

## What a Fix Looks Like
A context-aware quality requirement system that links to the MES: when a work order for OEM A's product is loaded on a line, the operator's workstation displays OEM A's specific requirements — IPC class, inspection criteria, SPC charting requirements, cosmetic standards — without the operator needing to look up a binder. When the line changes over to OEM B's product, the requirements automatically update. Quality requirement changes from OEMs are entered once in the system and immediately reflected on the production floor. Alert the inspector if they are about to apply the wrong standard.

## Who Feels the Pain
Production operators and inspectors who must remember which OEM's standards apply to the product they are currently running. Quality engineers who investigate nonconformances caused by wrong-standard application. Quality directors who explain quality escapes to OEM customers during quarterly business reviews.

## Impact If Fixed
Quality nonconformances from incorrect standard application decrease by 70-90%. Operator training time for multi-OEM requirements drops by 50%. OEM quality scorecard performance improves, directly affecting contract renewal and new program awards.
