# Fix: There Is Nobody to Ask About a Difficult Case

**Niche:** [[niches/telehealth-platforms/the-contract-clinician/profile|The Contract Clinician]]
**Industry:** [[industries/telehealth-platforms|Telehealth Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A clinician facing an uncertain presentation at eleven at night has a queue, a protocol document and no colleague.
**Tags:** #workflow-orchestration #large-language-models #evaluation-metrics #descriptive-statistics #confidence-intervals #worker-facing #quick-win #compliance
**Contested on:** Whether the platform will provide the corridor conversation that every other clinical setting has.

## The Problem

In any clinic or hospital, a clinician who is unsure asks someone. They step next door, call a colleague, page the on-call specialist, or discuss it over coffee. This informal consultation is how medicine actually handles uncertainty and it happens dozens of times a day in every institution.

A virtual clinician working alone at eleven at night has none of it. They have a protocol document written for the common case, a queue with a target, and a decision to make. The available responses under that pressure are to treat the presenting complaint, to refer out, or to tell the patient to seek in-person care — and the middle path that a two-minute conversation with a colleague would have produced is unavailable.

Clinicians consistently name this as the hardest thing about the work, and it is not a clinical skill problem. It is an absence of a structure that every other setting provides.

## Why It's Still Broken

Contractors working independently have no team by construction, and building one costs money for something that does not appear in any throughput metric.

There is also a familiar structural caution: a platform that provides clinical consultation, supervision and peer support is doing things that look like employment, and legal advice in this industry has generally been to keep the relationship at arm's length. That advice has removed a professional support structure without removing any of the professional responsibility.

And the shifts make it hard. Clinicians work variable hours across time zones, so any on-call arrangement has to cover nights and weekends, which is where the need is greatest and the cost is highest.

## What a Fix Looks Like

Provide a route to another clinician, and the asynchronous alternatives when there is not one.

**Run a real on-call consultation line** staffed by experienced clinicians, available during all hours the platform operates, reachable inside the encounter interface in one action. This is the whole fix and it is an operating cost, not an engineering project. Platforms that have done it report it is used far more than expected, which is itself the evidence of the gap.

**Structure it so it does not stop the clock.** A consultation should extend the visit without counting against the clinician's throughput, or it will not be used. This is a metric definition and it determines whether the line works.

**Build the asynchronous layer for the rest.** A moderated clinical forum where a clinician can post a de-identified case and get responses, with an archive that becomes a searchable body of how this platform's clinicians handle ambiguous presentations. This is cheap, it accumulates value, and it partly substitutes for the corridor.

**Make the protocol documents answerable.** A retrieval interface over the platform's own clinical protocols, guidelines and prior case discussions, answering a specific question in the encounter rather than requiring someone to read a policy. This handles the large share of questions that are not really clinical uncertainty but "what does this platform expect me to do here".

**Get the employment framing right with counsel** — offered rather than required, consultation rather than direction, available rather than supervisory. It can be done; several structures exist in medicine for exactly this and the caution has been over-applied.

**And record the escalations.** What clinicians ask about is the best available map of where the protocols are inadequate and where the platform's scope is being stretched, and nobody currently collects it.

## Who Feels the Pain

Clinicians, who carry the licence and the liability for decisions made alone under time pressure, and who describe this as the reason people leave virtual platforms for institutional roles. Patients with atypical presentations, who get the safe-but-wrong answer or the unsafe-but-quick one. And the platform, whose clinical risk concentrates in exactly the encounters where nobody could be asked.

## Impact If Fixed

The clinician gets the conversation that every other clinical setting provides, at the moment they need it. Difficult presentations get handled properly rather than routed around. And the escalation record shows the platform where its protocols fall short — which is information it currently gets only from complaints.
