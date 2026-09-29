# Fix: The Crosswalk Is a Spreadsheet From 2022

**Niche:** Framework Mapping & Crosswalks
**Industry:** [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The mapping between frameworks is a file someone made once, it has no owner and no version, and a framework revised last quarter.
**Tags:** #evaluation-metrics #compliance #confidence-intervals #data-integration #worker-facing #workflow-orchestration
**Contested on:** Whether an organisation pursuing several frameworks implements one control set once, or implements substantially the same things repeatedly.

## The Problem

An organisation running four frameworks has a crosswalk. It came from a consultant, a standards body or a platform, arrived as a spreadsheet, and was adapted to the organisation's own control numbering by someone who has since changed roles.

It has no version, no owner and no review date. It records which of this organisation's controls satisfy which requirements in each framework, which was accurate when it was built.

Since then two frameworks have revised. Requirements were reworded, merged, split and renumbered. The organisation's own control set has changed as systems were replaced and processes adjusted. Nothing propagated to the spreadsheet, because the spreadsheet is a file rather than a system and nobody's job includes maintaining it.

The failure surfaces at the worst moment. Preparing for an audit against the revised framework, the team discovers that mapped requirements no longer exist, new ones have no mapping, and the evidence they planned to present was mapped to a requirement that has changed its meaning. What follows is several weeks of reconstruction against a deadline, performed by the compliance manager and an increasingly irritated engineering team.

## Why It's Still Broken

**Nobody owns it.** The crosswalk sits between whoever bought the consulting engagement, the compliance manager who inherited it, and the platform that has its own internal mapping. Unowned artefacts do not get maintained.

**It is a file, not a system.** A spreadsheet has no revision awareness, no notification, no validation and no link to the frameworks it maps. Its staleness is structurally invisible.

**Framework revisions arrive without a delta.** Standards bodies publish a new version and sometimes a change summary written for readers rather than for mapping maintainers. Working out what changed for a specific organisation is a manual comparison every time.

**Maintenance has no deadline until the audit.** The cost of staleness is deferred entirely to audit preparation, which means it loses every allocation argument until it becomes urgent.

**Platform mappings are internal and unexplained.** Where a platform maintains its own mapping, the customer cannot see it, cannot reconcile it against their own crosswalk, and discovers the disagreement during the audit.

**Compliance teams are small.** The person who would maintain it is the same person running four certification programmes, handling questionnaires and chasing engineers for evidence.

## What a Fix Looks Like

**Give it a version, an owner and a review date.** The minimum viable fix, available immediately, and its absence is why everything else fails. A crosswalk with a named owner and a quarterly review is a different artefact from a file in a shared drive.

**Subscribe to framework revisions.** Standards bodies announce revisions. Someone should be receiving those notifications and treating each as a trigger for a mapping review — currently revisions are discovered when someone happens to mention them.

**Ask the platform for its mapping.** Where a platform maintains its own control mapping, the customer should be able to see it and reconcile. Discovering a disagreement during the audit is entirely avoidable and is purely a disclosure decision.

**Record mapping strength and rationale.** Not just that a control maps to a requirement, but whether it fully satisfies it and why. This is what makes a mapping reviewable rather than a matter of trusting whoever built it, and it identifies the entries that most need checking at revision.

**Review at framework revision and at control change.** Both directions matter — the mapping breaks when the framework changes and when the organisation's own controls change, and only the first is ever noticed.

**Do the revision review before the audit, not during.** A scheduled review within a month of any framework revision converts a pre-audit emergency into routine work, and it is the single scheduling change that would remove most of the pain.

## Who Feels the Pain

The compliance manager, who inherits an unowned spreadsheet, discovers it is wrong under deadline, and reconstructs it while running everything else.

The engineering team, hit with an urgent and apparently arbitrary evidence request weeks before an audit because a mapping turned out to be stale.

The organisation, which does duplicated implementation work it did not need to do and misses reuse it could have had, because the artefact that would have shown the overlap is unreliable.

And the auditor, working from a mapping that does not reflect the current framework, which wastes their time and the organisation's.

## Impact If Fixed

Versioning and ownership are free and address the root cause, which is that an important artefact is treated as a file rather than as maintained content.

Reviewing at framework revision rather than at audit preparation moves the work from a deadline emergency to routine maintenance, which is where most of the cost actually is.

And recording mapping strength and rationale makes the crosswalk something a successor can maintain, rather than something they must rebuild because they cannot tell what the previous person was thinking.
