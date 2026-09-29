# Buy: Interoperability and CDS Products Adapted to Episodic Virtual Care

**Niche:** [[niches/telehealth-platforms/point-of-care-decision-support/profile|Point-of-Care Decision Support]]
**Industry:** [[industries/telehealth-platforms|Telehealth Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Health data exchange infrastructure exists and works; it was built to move records between institutions that hold them, not to brief a contractor clinician who will see the patient once.
**Tags:** #data-integration #large-language-models #compliance #evaluation-metrics #confidence-intervals #workflow-orchestration #automation #descriptive-statistics
**Contested on:** Whether institution-to-institution data exchange can serve an episodic encounter with no institution behind it.

## The Problem

Health information exchange is real and improving. National networks, state and regional exchanges, the interoperability frameworks mandated by federal rule, FHIR APIs on major EHRs, and commercial aggregators all move clinical data between organisations, and pharmacy benefit and fill data flows reliably through the e-prescribing network.

The infrastructure assumes participants who are healthcare organisations with a treatment relationship, an EHR to receive into, and a longitudinal record to merge with. A telehealth platform has an episodic relationship, frequently a lightweight record, contractor clinicians who are not employees of the participating entity in the ordinary sense, and no chart to merge into.

## What Already Exists

The national interoperability frameworks and their participants, Surescripts and the e-prescribing network for medication history, commercial data aggregators, FHIR-based APIs, and the CDS content vendors. Consent and identity-matching infrastructure. The plumbing is there and improving annually.

## The Customization Gap

**Patient matching is harder without an institutional record.** Exchange networks match on demographics that a health system holds with confidence. A telehealth platform has what the patient typed at signup, which produces both missed matches and, more seriously, wrong ones. A deliberate matching strategy with confidence thresholds and a review path for ambiguous cases is the platform's own work and is a patient safety issue rather than a data quality one.

**Participation terms have to be established for this model.** Framework participation assumes defined roles and permitted purposes; an episodic virtual provider with contractor clinicians fits the categories awkwardly, and getting the participation and consent posture right is a legal project that precedes any engineering.

**Retrieval must be asynchronous and pre-visit.** Exchange queries take seconds to minutes and are designed for a clinician who has the chart open. Here the retrieval has to complete before the encounter begins, triggered at booking, with graceful handling when it does not return.

**The output is documents and the need is a brief.** Exchange returns CCDs and document bundles. Condensation into a one-screen, source-linked summary is the whole usability question and is not something any exchange participant provides.

**The data flows one way and should not.** A telehealth encounter produces a record that the patient's actual primary care provider should receive, and most platforms send nothing. Publishing back into the exchange is technically the same integration and is routinely omitted, which is the single largest contributor to the fragmentation this industry creates.

## Target Customer

Platform engineering and clinical informatics teams undertaking interoperability work and needing to know what the frameworks do not cover. Also the data aggregators and exchange vendors, for whom telehealth is a large participant class their institutional model fits poorly.

## Impact If Solved

The exchange networks, medication history feeds and CDS content get used as designed, and the patient matching, participation posture, asynchronous retrieval, condensation and write-back get built. The concrete result is a clinician with the patient's real history and a primary care provider who receives the encounter — the second being the thing that stops virtual care fragmenting the record further.
