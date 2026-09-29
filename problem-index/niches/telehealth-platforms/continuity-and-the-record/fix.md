# Fix: The Primary Care Doctor Never Hears About It

**Niche:** [[niches/telehealth-platforms/continuity-and-the-record/profile|Continuity & the Fragmented Record]]
**Industry:** [[industries/telehealth-platforms|Telehealth Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A prescription was written and a diagnosis considered, and the doctor responsible for the patient's care will never know unless the patient remembers to mention it.
**Tags:** #data-integration #compliance #descriptive-statistics #evaluation-metrics #workflow-orchestration #quick-win #automation #confidence-intervals
**Contested on:** Whether the platform will send a record it has already created to a provider it can already reach.

## The Problem

A patient has a virtual visit, receives a diagnosis and a prescription, and goes home. Their primary care physician, who manages their other conditions and their other medications, is not told.

The next time that patient is seen in person, their chart shows nothing. A medication reconciliation misses the drug. A pattern of repeat presentations that would be obvious across both records is invisible in each. If the virtual clinician considered a serious diagnosis and decided against it, that reasoning is lost entirely.

The platform generated a complete clinical document. It has a network connection capable of delivering it. Most platforms send nothing.

## Why It's Still Broken

Mostly because nobody asked for it and it is not required. Regulation compels providers to share records on request; it does not compel proactive transmission, so the default is silence.

The practical obstacles are real and small. The platform frequently does not know who the patient's primary care provider is, because it never asked. Where it did ask, the answer is free text that cannot be routed. Delivery requires directory lookup and a transport the platform may not have configured, though it likely already participates in a framework for retrieval.

And there is a faint commercial reluctance. Routing encounters back to primary care reinforces a relationship that some virtual care businesses are positioned against, and nobody has had to argue the point because the feature was never proposed.

## What a Fix Looks Like

Ask, then send.

Ask for the primary care provider at registration and resolve it against a provider directory, so the answer is an addressable entity rather than a name. Two fields and a lookup. Where the patient has none, record that, because it is clinically important and identifies the population for whom the platform is the only care they have.

Get consent explicitly and plainly: we will send a summary of your visit to your doctor so they have a complete picture. Most patients assume this already happens and are surprised it does not. Allow opt-out and honour it.

Send after every encounter, automatically, via the interoperability framework or Direct messaging. Track delivery and failure, and handle the failures — an undeliverable summary that nobody notices is the same as not sending.

Keep the document useful. A concise summary — presentation, assessment, decision, prescription, plan, follow-up advice — rather than a full document dump. A receiving practice that gets a readable one-page summary will read it; one that gets a forty-page bundle will not.

Report on it. Share of encounters with an identified primary care provider, share transmitted, share delivered. This is the metric that tells the platform whether it is contributing to the record or fragmenting it, and no platform currently produces it.

And consider telling the patient it was sent, which closes the loop and prompts them to mention it too.

## Who Feels the Pain

Patients, whose records have holes in them that surface at the worst moments — a medication interaction, a missed pattern, a specialist working from incomplete information. Primary care physicians, who are responsible for care they cannot see and who complain about this consistently. And the health system, which absorbs the downstream cost of fragmentation that a document transmission would prevent.

## Impact If Fixed

The patient's record stops acquiring holes every time they use virtual care. Primary care physicians get the information they are accountable for having. And the platform moves from being a source of fragmentation to a contributor to the record — which is also, when payers start asking, a considerably better thing to be.
