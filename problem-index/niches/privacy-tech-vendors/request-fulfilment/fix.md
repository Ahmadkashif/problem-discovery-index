# Fix: Confirmed Across the Systems That Answered

**Niche:** Data Subject Request Fulfilment
**Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The individual is told their data has been deleted, and what happened is that every system owner who replied said they had done it.
**Tags:** #evaluation-metrics #confidence-intervals #compliance #worker-facing #workflow-orchestration #data-integration
**Contested on:** Whether a deletion is verified across every system that holds the data, or confirmed across the systems someone remembered and could reach.

## The Problem

The confirmation letter is unqualified. Your personal data has been deleted from our systems.

Behind it: a list of systems drawn from a data map built by questionnaire, tasks sent to the owners of those systems, responses received from most of them within the statutory window, and one or two that did not respond and were closed anyway because the deadline arrived.

Nobody checked afterwards. The data may be soft-deleted with a flag rather than removed. It may persist in the warehouse that ingested it last week. It may be in logs nobody searched because logs were not on the map. It may be with a processor who confirmed by email. It is certainly in backups, which the organisation's position handles with a statement about eventual expiry that the individual is not told about.

The statement made to the individual is stronger than anything the organisation can substantiate. This is not usually deception — the people involved believe it — it is that the process produces a confirmation and nothing in it produces evidence.

## Why It's Still Broken

**The deadline drives closure.** A statutory window creates pressure to complete, and marking the request complete is what completes it. Accuracy has no deadline; the response does.

**Verification would produce contrary evidence.** Checking afterwards and finding remaining data creates a written record of a failed statutory obligation. The incentive not to look is direct.

**The map is the ceiling.** Fulfilment can only reach systems the organisation knows about, and the organisation knows about the systems that answered a survey.

**Backups have no good answer.** Deleting from immutable backups is genuinely impossible without compromising the security property they exist for. The accepted practice is a policy statement about retention expiry, which is defensible and is not what the individual is told.

**Soft deletion looks like deletion.** Many systems mark records deleted without removing them, which satisfies the task and leaves the data present. Nothing distinguishes the two in the confirmation.

**Nobody measures completeness.** There is no metric anywhere for what fraction of a subject's data a fulfilment actually removed, so the gap is invisible to the organisation as well as to the individual.

## What a Fix Looks Like

**Verify after the window and record the result.** Re-query every system for the identifiers. This is a query, it takes minutes, and it converts a confirmation into evidence. The discomfort about creating a record is precisely why it should be done — an organisation that verifies and remediates is in a far stronger position than one that never looked.

**Say what actually happened, accurately.** Tell the individual which categories of system the data was removed from, and state plainly that backups retain data until their expiry with the period named. This is honest, it is what regulators expect, and organisations consistently underestimate how acceptable it is.

**Distinguish soft deletion from removal.** Require system owners to state which they performed, and treat soft deletion as an interim state with a scheduled removal rather than as completion.

**Search beyond the map.** Logs, object storage, caches and non-production copies of production data, even where the map does not list them. These are the most common places data survives and the least likely to be on any survey-derived inventory.

**Chase non-responding systems rather than closing around them.** A request closed with two systems unanswered is not fulfilled. Track these explicitly rather than allowing the deadline to absorb them.

**Publish an internal completeness metric.** Across requests, the proportion of located data verifiably removed. This is the number that would drive improvement and it does not exist at any organisation.

**Handle derived data with a stated position.** Models trained on the data, aggregates, feature stores and search indexes. Each needs an answer — removed, will expire, retained on this basis — rather than silence.

## Who Feels the Pain

The individual, who exercised a right, received an unqualified confirmation, and whose data remains in several places.

The privacy officer, who signs confirmations they cannot substantiate and knows it.

The engineer, asked to delete from a system that has no deletion path, marking the task complete because the alternative is an escalation with no resolution.

And the organisation, whose exposure is a confirmation letter that overstates what it can prove — which in an enforcement action is worse than having stated the limitation honestly.

## Impact If Fixed

Verification after the window costs minutes per request and is the entire difference between a confirmation and evidence, in a domain where the confirmation is a statement to a regulator's likely complainant.

Telling the individual accurately what happened, including the backup position, is both more honest and more defensible than the current unqualified statement, and organisations consistently overestimate the cost of saying it.

And a completeness metric would reveal how much data actually survives fulfilment, which is the number this industry most needs and most assumes it already knows.
