# Fix: The Objection Was Verbal and Left No Record

**Niche:** [[niches/talent-assessment-platforms/the-io-psychologist/profile|The I-O Psychologist]]
**Industry:** [[industries/talent-assessment-platforms|Talent Assessment Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The psychologist says the configuration is outside the validated range, the meeting moves on, and nothing anywhere records that the objection was made.
**Tags:** #compliance #workflow-orchestration #descriptive-statistics #evaluation-metrics #confidence-intervals #quick-win #worker-facing #hypothesis-testing
**Contested on:** Whether a professional objection will be written down.

## The Problem

An implementation call. The client wants the instrument configured for a role it was not validated for, or a cut score higher than the validation supports. The psychologist on the call says so. The implementation lead notes the client's requirement and the timeline. The configuration ships.

Nothing records that the objection happened. There is no field in the configuration record, no note in the project file, no register. So the professional judgement exists only in the memory of the people on the call, and if the instrument is later challenged, the psychologist who advised against it has no evidence they did.

The pattern is invisible too. If a particular client, product or implementation team generates overrides repeatedly, nobody can see it, because there is nothing to count.

## Why It's Still Broken

Recording an objection is uncomfortable and nobody's job. It creates a document that says the vendor knowingly deployed an instrument outside its validated range, which is precisely the document that would be damaging in a challenge — which is also precisely why it should exist as a control rather than not exist as a convenience.

The psychologist raising it is usually junior to the commercial lead in the room and asking for it in writing is socially costly in a way that a form removes.

And the configuration system has no field for it, so even a willing team has nowhere to put it.

## What a Fix Looks Like

Add the field, make it routine, and count what accumulates.

Put a scientific review field on every configuration record. Reviewed, not reviewed, reviewed with concerns, with the concerns stated and the reviewer named. Two fields and a text box, filled in as part of the standard configuration workflow so it is routine rather than an escalation.

Require the client's acknowledgement where a concern was raised. A configuration deployed over a stated scientific concern should carry the client's written acceptance. This is uncomfortable, it takes one email, and it transforms who carries the risk.

Keep the register and report it. Configurations with concerns, by client, by instrument, by reviewer, monthly. A count is enough; the pattern will be visible immediately and is currently invisible entirely.

Give the psychologist a copy. The professional carrying the judgement should hold the record of having made it, which is a matter of their own standing and is currently entirely absent.

Define the small set of matters where a concern blocks rather than records — a narrow, published list, agreed in advance, so that the routine case is documentation and the severe case is a stop. Making the list short is what makes it respected.

And review the register when an instrument is challenged, which is the moment it exists for.

## Who Feels the Pain

I-O psychologists, whose professional judgement is overridden without trace and who carry the reputational and occasionally licensure risk for deployments they advised against. Vendors, who cannot see a pattern of overrides accumulating in one account until it becomes an incident. Employers, receiving configurations whose scientific concerns were never conveyed to them. And candidates assessed by an instrument used outside its range.

## Impact If Fixed

The objection gets written down, which costs two fields and changes who carries the risk. The pattern of overrides becomes countable and therefore governable. And the person whose professional standing depends on having advised correctly has the record that they did.
