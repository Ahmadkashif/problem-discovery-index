# Continuity & the Fragmented Record

**Parent Industry:** [[industries/telehealth-platforms|Telehealth Platforms]]
**Category:** Low Digitized
**Contested on:** Whether anything connects one virtual encounter to the next, or to the rest of the patient's care.

## Profile
**Market Size:** ~$3.6B — 12% of US virtual care delivery
**Share of Parent Industry:** ~12%
**Digital Adoption:** Low — episodes with no thread between them
**Target Buyer:** Platform product leadership; payers; primary care organisations
**Automation Potential:** High — the linkage is integration work rather than invention

## What Makes This a Distinct Niche

A patient may see a different clinician each visit, on a platform that does not connect to their primary care record, for a problem that has a history the clinician cannot see. Continuity is the thing virtual care is worst at and the thing most conditions require.

The fragmentation runs in three directions. Within the platform, successive encounters are frequently handled by different clinicians with no thread between them. Outward, the encounter record usually never reaches the patient's primary care provider, so the person responsible for their overall care does not know it happened. Inward, the platform sees none of what the patient's other providers have done.

The niche is distinct because it is an integration and product problem rather than a clinical one, and because it is the failure that most limits what virtual care can responsibly treat. Episodic care handles episodic problems; the chronic and the complex require a thread.

## Current Tools & Gaps

Platform-internal records holding all encounters, usually accessible in principle and rarely surfaced to the clinician in a usable form. Continuity models at some platforms — assigning a patient a named clinician — which work well and are used mostly in behavioural health and chronic care. Interoperability frameworks and FHIR APIs that could carry the record both ways.

The gaps are within and outward. Within, the clinician's default view is the current encounter, and prior visits require deliberate navigation nobody has time for. Outward, most platforms send nothing to the patient's primary care provider — the integration is the same one used for retrieval and is simply not run in reverse, which is the single largest way virtual care adds to the fragmentation it complains about.

## Problems
- [[niches/telehealth-platforms/continuity-and-the-record/build|🔨 Build: A Longitudinal Thread and a Write-Back to Primary Care]]
- [[niches/telehealth-platforms/continuity-and-the-record/buy|🛒 Buy: EHR and Interoperability Products Adapted to a Platform With No Panel]]
- [[niches/telehealth-platforms/continuity-and-the-record/fix|🔧 Fix: The Primary Care Doctor Never Hears About It]]
