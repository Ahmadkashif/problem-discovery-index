# Fix: The Report Describes Code That No Longer Exists

**Niche:** Application Security Testing
**Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Type:** Fix (Pain Point)
**One-liner:** A two-week assessment of an application that deploys daily produces a document about a version that shipped past by the time anyone reads it.
**Tags:** #evaluation-metrics #change-point-detection #confidence-intervals #compliance #worker-facing #workflow-orchestration
**Contested on:** Whether assessment can keep pace with a codebase that ships daily, or whether a point-in-time test is obsolete before the report is written.

## The Problem

The engagement runs for two weeks. The report takes another one to two weeks to write and review. By the time it lands, the application has had perhaps sixty deployments. Some findings have been fixed incidentally by unrelated refactoring. Some are now unreachable because a flow changed. Some new endpoints exist that nobody has looked at. And the areas the tester examined most thoroughly are, statistically, the areas most likely to have changed since, because active development is where change concentrates.

Everyone accommodates this without naming it. The client treats the report as approximately current. The tester knows the reproduction steps may already fail. Remediation tickets get raised against a description of behaviour that may no longer match. Occasionally an engineer spends a day trying to reproduce a finding that was fixed three weeks ago by someone who never knew it existed.

The annual cadence makes it worse. An application assessed once a year is unassessed for eleven months of continuous change, and the single annual snapshot is presented — internally, to auditors, to customers — as the application's security posture.

Nobody is doing anything wrong. The engagement model was designed for software that shipped quarterly and has not changed for software that ships hourly.

## Why It's Still Broken

**Procurement and compliance are annual.** Budget cycles, audit requirements and customer security questionnaires all ask whether an annual penetration test was performed. The cadence is set by the paperwork rather than by the software.

**The business model is utilisation.** Firms sell booked days. Continuous or retainer engagements complicate scheduling, reduce the predictability of the pipeline, and are harder to staff, so they are offered without enthusiasm.

**Reports are slow because reporting is unpaid overhead.** The one-to-two-week write-up gap is itself a large part of the staleness, and it exists because testers are booked onto the next engagement immediately, as described in [[niches/penetration-testing-firms/the-tester/profile|🟣 The Tester]].

**Findings carry no version anchor.** Almost no report states the commit, build or deployment the testing was performed against, so nobody can tell later whether a finding predates a change that might have resolved it.

**Clients want the artefact.** For a meaningful share of buyers the deliverable is the point — a dated report satisfying a requirement — and staleness does not affect its usefulness for that purpose.

## What a Fix Looks Like

**Anchor every finding to a version.** Record the commit or build tested and the date of the specific observation. This costs nothing, and it immediately lets the client and the tester tell whether an intervening change might have affected a finding. Its absence is pure inertia.

**Deliver findings as they are found, not in a batch.** A high-severity issue discovered on day two should reach the client on day two, not in a report three weeks later. Most firms will do this informally on request; making it the default is a process change with no cost and a large effect on how quickly serious issues get fixed.

**Compress the reporting gap.** Every week between the last test day and delivery is a week of staleness. This is the cheapest available improvement and is mostly a scheduling problem — booking write-up time rather than expecting it to happen in the evenings.

**Shift to a change-triggered cadence.** Instead of one annual assessment, a smaller baseline plus focused engagements triggered by material change — a new authentication flow, a new payment integration, a permission model rework. This matches effort to risk and is a better product, though it requires the compliance buyer to accept something other than an annual date.

**Re-verify at delivery.** A short automated pass immediately before the report goes out, confirming each finding still reproduces. Cheap, and it removes the worst failure mode where an engineer burns a day on something already fixed.

**State the shelf life.** A plain sentence saying what this assessment is worth given the application's deployment rate, and when it stops meaning much. Clients deploying forty times a week should be told, in the document, that an annual snapshot is a weak form of assurance for them — which is honest and also the strongest argument for buying a better cadence.

## Who Feels the Pain

The engineer trying to reproduce a finding against code that has moved, which is a common and demoralising way to spend a day.

The security engineer, who has to defend the relevance of a document that is visibly out of date to developers who deploy daily and regard the annual test as theatre.

The tester, whose careful work is read weeks later against a system that has changed, and who knows the reproduction steps may no longer hold.

And the organisation, which believes it has an assessment of its application and has an assessment of a version of its application from some weeks ago.

## Impact If Fixed

Version anchoring and progressive delivery cost nothing and remove most of the practical damage. Serious findings reach engineers in days rather than weeks, and stale findings become identifiable instead of confusing.

Compressing the reporting gap is worth as much as anything else in this section and is entirely within the firm's control — it is a scheduling decision, not a capability.

And a change-triggered cadence would align testing with where risk actually enters the application, which is the only version of this service that makes sense for software that ships continuously.
