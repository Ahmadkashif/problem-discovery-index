# Fix: Lawful Basis Is a Dropdown Someone Filled In

**Niche:** Personal Data Classification
**Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The legal foundation for every processing activity is a field selected once by a privacy manager about a system they have not seen, and nothing has checked it since.
**Tags:** #evaluation-metrics #compliance #confidence-intervals #worker-facing #data-integration #hypothesis-testing
**Contested on:** Whether a system can determine that data is personal, whose it is and what category it falls into.

## The Problem

Every processing activity in the record has a lawful basis and a purpose. These are the fields on which the legal position rests — they determine what the organisation may do with the data, what rights the individual has, and whether a given use is permitted at all.

They were filled in by a privacy manager during the annual survey. The system owner said the system processes customer data for service delivery. The manager selected contract as the basis and typed a purpose description. It was plausible, it was recorded, and it has not been examined since.

Several things then go wrong quietly. The purpose as recorded is broad — service delivery covers a great deal — so any subsequent use appears to fall within it. The basis may be wrong: processing recorded under legitimate interests may never have had the balancing assessment that basis requires, and processing recorded under consent may be happening for users who never gave it. And the actual use drifts: data collected for service delivery starts feeding a recommendation model, then an advertising integration, and the record still says service delivery.

Nobody detects any of it, because the basis and purpose are text in a document and the actual processing is behaviour in systems, and the two are never compared.

## Why It's Still Broken

**They are genuinely legal determinations.** Basis and purpose depend on contracts, intentions and balancing judgements. No system can derive them, which has been taken to mean nothing can be done about them.

**Broad purposes are convenient for everyone.** A narrow purpose statement constrains what the business may do later. A broad one avoids returning to the privacy team every time a new use is proposed, which suits the business and reduces the privacy team's workload in the short term.

**The record is written once and reviewed annually.** Nothing triggers a re-examination when the processing changes, which is precisely when the basis should be revisited.

**Nobody compares declared purpose to observed use.** The comparison requires knowing where the data actually flows, which requires the observation layer most organisations do not have.

**Legitimate interests assessments are frequently missing.** The basis is selected and the assessment it requires is not performed, which is a documented and common finding and one that only surfaces under regulatory scrutiny.

**Consent records and processing are disconnected.** A system may process data for individuals who withdrew consent, because the consent record lives in one platform and the processing happens in another with no enforcement between them.

## What a Fix Looks Like

**Narrow the purposes and accept the consequence.** Purpose statements specific enough to exclude uses that were not contemplated. This makes new uses require a decision, which is the point — purpose limitation only works if the purpose limits something.

**Compare declared purpose against observed flows.** Where data declared as processed for service delivery flows to an advertising platform, that is a finding. This is the achievable automation in this layer and it catches the most common substantive failure.

**Enforce consent at the processing boundary, not at collection.** A withdrawal should propagate to the systems doing the processing, mechanically. Today consent is recorded in a consent platform and the processing systems frequently never learn about it, which makes the consent record an artefact rather than a control.

**Audit the assessments the basis requires.** Every legitimate interests basis should have a completed balancing assessment attached, and every consent basis should have a valid consent record for the individuals concerned. Checking that the required artefact exists is mechanical and routinely reveals gaps.

**Re-examine the basis when processing changes.** A new integration, a new destination or a new model trained on the data should trigger review of the basis for that activity — which requires the change detection the observation layer provides.

**Record the reasoning, not only the selection.** Why this basis was chosen, by whom, on what understanding of the processing. A dropdown selection with no reasoning cannot be defended or reviewed by a successor, and successors are frequent in this role.

## Who Feels the Pain

The privacy officer, personally associated with a record whose most legally significant fields were entered on the basis of a questionnaire answer.

The organisation, whose defence in a regulatory enquiry rests on a purpose statement that does not describe what the systems actually do.

The individual, whose data is processed for purposes they were not told about, under a basis that may not apply to them.

And the engineer, who is asked to stop processing for a user whose consent was withdrawn and finds no mechanism connecting the consent platform to their system.

## Impact If Fixed

Comparing declared purpose against observed flows is the one part of the legal layer that can be evidenced, and it catches the drift that purpose limitation exists to prevent.

Enforcing consent at the processing boundary rather than recording it at collection would turn the category's most visible product into an actual control rather than an audit artefact.

And auditing that the artefacts a basis requires actually exist — a balancing assessment, a valid consent record — is a mechanical check that would surface a large share of the gaps regulators find, before a regulator does.
