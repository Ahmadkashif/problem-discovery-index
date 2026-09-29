# Fix: Nobody Knows Which Template Version Was Used

**Niche:** [[niches/remote-work-infrastructure/onboarding-and-contracts/profile|Onboarding, Contracts & Documentation]]
**Industry:** [[industries/remote-work-infrastructure|Remote Work Infrastructure]]
**Type:** Fix (Pain Point)
**One-liner:** A template defect is discovered and nobody can say which engagements were created from the broken version.
**Tags:** #compliance #data-integration #descriptive-statistics #evaluation-metrics #workflow-orchestration #quick-win #confidence-intervals #automation
**Contested on:** Whether the template version will be recorded on the engagement.

## The Problem

A template for a country turns out to have a defect — a notice provision that no longer matches the statute, a clause that a court has since found unenforceable, a missing mandatory term.

The next question is which engagements are affected, and it cannot be answered. The executed contracts are stored, but the template version used to generate each one was not recorded, and the template itself has been edited several times since with no version history. Determining which of four hundred engagements in that country carry the defect means opening and reading contracts.

So remediation either does not happen, or happens as an expensive manual review, or happens partially. And the same is true in reverse: when a rule changes, nobody can identify the engagements whose documents implement the old rule.

## Why It's Still Broken

The templates live in a document library or a CLM configured for simple versioning, and the generation step records the output rather than the inputs. Nobody asked for the input to be recorded because nobody anticipated needing to reverse the question.

Template editing is also treated as content maintenance rather than as a versioned release, so edits are made in place and the history is a document version list without effective dates or change descriptions.

And the need only arises when something is wrong, which is infrequent and urgent — exactly the conditions under which the absence is discovered and not fixed.

## What a Fix Looks Like

Record the version. It is a field.

Stamp every generated contract with the template identifier and version, the clause versions where conditional, and the date. Stored on the engagement, immutable. This is the whole fix and it takes a sprint.

Version templates properly. Numbered versions with effective dates, a change description, and the previous versions retained. Editing in place is what makes the history unrecoverable.

Link each template version to the rules it implements. When a rule version changes, the templates that depended on it are flagged for review and the engagements generated under them are identifiable. This is what turns a defect discovery into a query.

Backfill where you can. Matching existing executed contracts to template versions by content comparison is imperfect and is far better than nothing, and it establishes the baseline for everything created afterwards.

Build the remediation query. Given a template version and a date range, the affected engagements, their clients and their workers. Having the query ready before it is needed is the difference between a bounded remediation and a project.

And report template age. Which templates have not been reviewed within their cadence, per jurisdiction. It is the same currency problem as the rule base and the same dashboard should show both.

## Who Feels the Pain

Workers engaged under a defective contract who do not know, and whose entitlements or protections may be understated in the document a tribunal would read. Clients, carrying an exposure across an unknown number of engagements. Legal operations, facing a remediation they cannot scope. And the platform, whose highest-multiplier error becomes unbounded because the inputs were not recorded.

## Impact If Fixed

A template defect becomes a query rather than a manual review of four hundred contracts. Rule changes flag the templates and the engagements that depend on them. And the highest-multiplier error in this industry — a defect embedded in a template and propagated silently — becomes bounded and remediable.
