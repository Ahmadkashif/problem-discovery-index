# Fix: The Cap Is Renegotiated Three Times Mid-Incident

**Niche:** Engagement & Retainer Operations
**Industry:** [[industries/digital-forensics-firms|Digital Forensics Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The engagement is authorised to an initial cap set before anyone knew the size of the incident, and every extension is negotiated while the investigation waits.
**Tags:** #evaluation-metrics #confidence-intervals #compliance #workflow-orchestration #revenue-impact #worker-facing
**Contested on:** Whether the commercial and administrative shell around an activation runs itself, or consumes hours of the first day.

## The Problem

The engagement is authorised with an initial cap, set in the first hours by people who have no idea yet how large the incident is. It is a reasonable figure for a contained incident and is frequently far too small for what this turns out to be.

So the cap is reached on day six. The firm must stop or continue at risk. An extension is requested, which goes to the claims handler, who may need approval, who may want a scoping call, which requires the lead responder to leave the investigation and explain what has been found and what remains. Approval comes through on day seven or eight.

Then it happens again on day fourteen.

Each cycle costs the lead responder hours at a point where their attention is the scarcest resource on the engagement, introduces uncertainty into the work, and occasionally pauses collection while telemetry expires.

Nobody is behaving unreasonably. The insurer must control exposure on a claim whose size is unknown. The firm cannot work unbounded. And the cap must be set before the information that would size it exists. The structure guarantees repeated renegotiation and nothing has been done to make it cheaper.

## Why It's Still Broken

**The cap exists to control exposure and does so bluntly.** A single number reviewed on exhaustion is the simplest mechanism and the most disruptive.

**Nobody knows the size at the outset.** The information that would set a correct cap is produced by the work the cap authorises, which is genuinely circular.

**Extensions require the person who cannot spare the time.** Justifying an extension needs the lead responder, whose attention is precisely what should not be interrupted.

**Claims handlers are managing many claims.** An extension request competes with everything else on their desk and moves at that pace, not at the incident's.

**The pause is invisible in the claim.** Time lost to authorisation appears nowhere, so its cost — expired telemetry, prolonged attacker access — is not attributed to the mechanism causing it.

**No incident-shape data informs the cap.** Insurers have claims history that would predict engagement cost from early characteristics, and set caps by convention instead.

## What a Fix Looks Like

**Set the initial cap from historical incident shapes.** Insurers hold the data relating early incident characteristics to eventual engagement cost. A cap derived from it would be right far more often than one set by convention, and this is a straightforward analysis on existing claims data.

**Use staged authority rather than a single cap.** Defined tranches released automatically on stated triggers — scope exceeding a threshold, systems count exceeding a threshold — rather than on exhaustion and a negotiation. This is standard authority-limit practice in other claim lines.

**Make extension requests structured and cheap.** A short defined format the engagement manager completes from the engagement record, without requiring the lead responder. Most of the cost is the interruption, not the approval.

**Never pause collection for authorisation.** A standing agreement that evidence collection continues while an extension is considered, because collection is cheap relative to an engagement and evidence that expires cannot be recovered.

**Give extensions a service level.** Hours, not days, with an escalation path. An extension request during an active intrusion is not a routine claims decision.

**Track time lost to authorisation.** Measured and reported, so the cost of the mechanism becomes visible to the party operating it.

**Pre-agree the escalation ladder in panel terms.** What triggers a larger authority, who approves it and in what time, agreed once with the panel rather than negotiated per incident.

## Who Feels the Pain

The lead responder, pulled out of the investigation to justify continuing it, repeatedly, at the worst moments.

The client, whose investigation slows or pauses for commercial reasons they are frequently not told about.

The insurer, whose own claim costs rise when evidence expires and containment is delayed during an authorisation gap — a cost caused by the control that was meant to contain it.

And the investigation, which loses days at the points where days matter most.

## Impact If Fixed

Staged authority released on triggers rather than on exhaustion removes the renegotiation cycle entirely, using a mechanism insurers already operate in other lines.

Setting the initial cap from historical incident-shape data is an analysis on claims data insurers already hold, and would make the first number right far more often.

And a standing agreement that collection never pauses for authorisation protects the evidence that cannot be recovered, at a cost that is trivial next to the engagement it sits inside.
