# Fix: The Record Is a Survey From Last Year

**Niche:** Data Discovery & Mapping
**Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The record of processing is assembled by questionnaire once a year, into an estate that changes weekly, and nobody knows how much of the estate it covers.
**Tags:** #evaluation-metrics #confidence-intervals #change-point-detection #compliance #worker-facing #data-integration
**Contested on:** Whether the record of where personal data lives and flows is observed from the systems or compiled by asking people.

## The Problem

Once a year, the privacy team sends a questionnaire to system owners. What personal data does your system hold, where does it come from, where does it go, how long is it kept, who has access.

The responses come back over several weeks, of varying quality, from people with varying knowledge of their own system's downstream integrations. They are assembled into a record of processing, reviewed, signed and filed. The exercise takes a quarter of the privacy team's year.

By the time it is signed it is already wrong. In the intervening weeks services were deployed, integrations added, vendors onboarded, pipelines changed. Over the following eleven months the estate diverges continuously, and nothing detects it.

The deeper problem is that nobody knows how wrong it is. The record covers the systems whose owners were asked and responded. It does not cover systems nobody registered, teams nobody surveyed, or the flows respondents did not know about. There is no completeness measure, so the record is presented to regulators, auditors and the organisation's own leadership as a description of the estate, when it is a description of the part of the estate that answered a questionnaire.

## Why It's Still Broken

**The survey is what the regulation seems to ask for.** A record of processing is a document, so producing a document satisfies the obligation. Accuracy is assumed rather than verified, and nothing in the assessment regime tests it.

**Observation requires access privacy teams do not have.** Deriving the map from systems needs network, cloud and database access that a legal function cannot obtain on its own authority.

**Nobody wants to know the answer.** A completeness measure showing the record covers sixty per cent of the estate creates an obligation to do something about the other forty, which is a large and unfunded programme.

**The annual cycle is a ritual.** It happens because it happened last year, consumes the budget allocated to it, and produces the artefact, which is the measure of its success.

**System owners cannot answer accurately.** They know their own system and not the downstream consequences of the events it emits, which is where most of the interesting flows are.

**Change has no trigger.** Nothing in the deployment or procurement process prompts a record update, so the record is only ever updated on the annual cycle.

## What a Fix Looks Like

**Verify a sample against reality.** Take ten systems from the record and check them technically — actual integrations, actual destinations, actual retention. The discrepancy rate is the record's accuracy, it takes a few days, and no organisation has ever measured it. That number is what makes every other change fundable.

**Trigger updates from change, not from the calendar.** New service deployed, new vendor contracted, new integration authorised — each should prompt a record entry as part of the existing process rather than being caught eleven months later. Hooking into deployment and procurement is where this has to happen.

**Use what can be observed now, even partially.** SaaS OAuth grants, cloud resource inventories, DNS and egress destinations and tag scans are all obtainable without a major programme and each reveals systems and flows the survey missed. Partial observation is strictly better than none.

**State coverage on the record.** What proportion of known systems the record covers, and which parts of the estate were not surveyed. A record that declares its own scope is far more defensible than one that implies completeness.

**Ask better questions of better people.** Surveying system owners about downstream flows asks them something they do not know. Asking about data received and data sent, separately, and reconciling the two sides across systems, catches a large share of the gaps at no extra cost.

**Keep it in the tooling teams already use.** A record maintained in the service catalogue, alongside ownership and dependencies, has a chance of staying current. One maintained in a privacy platform teams never open does not.

## Who Feels the Pain

The privacy officer, who signs a record they know is a best effort and is personally associated with its accuracy.

The engineer handling a deletion request scoped to a map that omits the three systems where the data also sits.

The incident response team, scoping a breach against a record that does not list the affected system.

And the organisation, which believes it knows where personal data is and knows where the responsive subset of its teams said it was a year ago.

## Impact If Fixed

Verifying a sample against reality costs a few days and produces the accuracy number that the entire privacy programme currently assumes and has never measured.

Triggering record updates from deployment and procurement is the only mechanism that keeps a map current in a changing estate, and it is a process change rather than a technology one.

And stating coverage explicitly converts an artefact that implies completeness into one that declares its own limits — which is both more honest and, in front of a regulator, considerably more defensible.
