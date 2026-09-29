# The Note Written for the Utilisation Reviewer

**Niche:** [[niches/healthcare-practice-software/behavioral-health-ehr/profile|Behavioral Health & SUD Practice Software]]
**Industry:** [[industries/healthcare-practice-software|Healthcare Practice Software]]
**Type:** Fix (Pain Point)
**One-liner:** Behavioral health progress notes are written to justify continued authorisation rather than to record clinical thinking, which makes them long, defensive, clinically thin, and the largest single consumer of a therapist's unpaid time.
**Tags:** #large-language-models #transformers #evaluation-metrics #descriptive-statistics #compliance #automation #worker-facing #tacit-knowledge-ml
**Contested on:** Every serious competitor in behavioral health software is fighting to share a patient record with a referring provider while withholding exactly the 42 CFR Part 2 material and proving it did so — and whoever makes that segmentation reliable takes the account.

## The Problem
A therapist finishes a session and writes a note. The note has to contain specific language — medical necessity, functional impairment, progress toward a treatment plan objective — because a utilisation reviewer will read it and an audit may sample it. The clinically useful content, what the therapist actually noticed and intends to do next, is two sentences. The rest is scaffolding. Therapists write these after hours, unpaid, at a rate of ten to fifteen minutes per session on top of a full caseload, and the profession's documentation burden is a well-documented contributor to its attrition. The notes are also, by design, worse clinical records than they would be if nobody were reading them for authorisation.

## Why It's Still Broken
The requirement is real and the vendor cannot remove it. Template-driven notes, the standard answer, make the problem worse in a specific way: identical structural language across a caseload is the pattern an auditor treats as evidence of cloned documentation, so the therapist gets both the burden and the exposure. Ambient documentation, which has reshaped note-writing in medical specialties, has moved into behavioral health far more slowly because recording a therapy session is a different consent and trust question, and vendors have been right to be cautious about it rather than simply slow.

## What a Fix Looks Like
Separate the two documents the note is currently trying to be. Let the clinician capture the clinical record briefly, in their own words, in whatever form is natural — dictated after the session, typed in two minutes, written on the treatment plan. Then generate the authorisation-facing narrative from that record plus the structured material the system already holds: the treatment plan objectives, the measurement-based care trajectory, attendance, and the prior notes' stated next steps. The generated narrative is presented for review and signature, with the clinician's own words preserved verbatim as the clinical core. Cloned-language detection runs before signature, not after audit. Where ambient capture is used, consent is explicit, per-session, revocable, and the default is off — anything else is unacceptable in this setting and will poison adoption.

## Who Feels the Pain
Therapists writing notes at nine at night for sessions that ended at five; clinical directors who know the notes are defensive documents and cannot say so to a payer; and patients, whose records are less useful to the next clinician than they should be.

## Impact If Fixed
Cutting note time from twelve minutes to four returns roughly an hour a day to a full-caseload clinician, which in a profession with this attrition rate is a retention intervention rather than a convenience. Generating the authorisation narrative from structured evidence also tends to produce stronger medical-necessity documentation than a tired human writing from memory, which reduces denial rates — the rare case where the fix serves the worker and the payer-facing metric at once.
