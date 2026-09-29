# Fix: A Tutor Has Never Seen Their Own Teaching

**Niche:** [[niches/online-tutoring-platforms/session-instruction-analysis/profile|Session Instruction Analysis]]
**Industry:** [[industries/online-tutoring-platforms|Online Tutoring Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Sessions are recorded and stored, and the tutor who taught them has no way to watch one back.
**Tags:** #descriptive-statistics #evaluation-metrics #workflow-orchestration #compliance #large-language-models #worker-facing #quick-win #automation
**Contested on:** Whether a tutor gets access to a recording of their own teaching.

## The Problem

Platforms record sessions, usually for safeguarding and dispute purposes. The recordings sit in storage. On most platforms the tutor cannot watch them.

This is a strange situation. The most basic professional development tool available to anyone who teaches is watching themselves teach, it costs nothing because the recording already exists, and the person who did the teaching is the one party denied access. Tutors ask for this and are told the recordings are for safeguarding purposes only.

The consequence is a workforce of hundreds of thousands of people, many of them serious about their craft, who have never once observed their own practice and have no mechanism by which to improve except accumulated guesswork.

## Why It's Still Broken

Safeguarding recordings are governed by a policy written for a different purpose, and extending access to tutors requires revisiting the consent basis on which they were made. That is real work involving legal review and probably re-consenting families, and nobody has had a reason to start it.

There is also an unstated worry that giving tutors access creates risk — that a recording could be extracted, shared or used to contest a complaint. The first is a technical control problem with known solutions; the second is a feature rather than a bug, since a tutor accused of something should be able to see the evidence.

And tutors are contractors. A platform that provides professional development is doing something employer-shaped, which in this industry is a familiar reason for inaction.

## What a Fix Looks Like

Give the tutor their own sessions back, under controls.

Streaming-only access to their own recordings, within the platform, for a defined window, with no download and with access logged. The controls are standard and the engineering is modest.

Get the consent basis right. Update the recording consent to cover tutor review for professional development, explain it plainly to families, and allow opt-out — most will not, because a parent who thinks about it wants their child's tutor to be improving. Where a family opts out, the session is excluded.

Add the cheap automated layer alongside it, because most tutors will not rewatch an hour-long session. A short summary with the structural measures — you spoke 71% of the time, you asked six questions, your average wait time was 1.2 seconds, your longest uninterrupted explanation was four minutes — plus timestamps into the two or three moments worth rewatching. That converts an hour of review into five minutes and is what makes the access actually used.

Let tutors share a session for feedback, with consent, into a peer review or mentoring arrangement. Peer observation is among the most effective professional development that exists and is completely unavailable to this workforce.

And make it available to the tutor when a complaint concerns a session. A tutor defending themselves against an allegation should be able to see the recording the platform is deciding on, which is a due process matter as much as a development one.

## Who Feels the Pain

Tutors, who cannot improve at a craft they practise for years because they have never seen it from outside, and who face complaints about sessions they cannot review. Students, taught by people whose uncorrected habits have compounded. And the platform, which stores an enormous professional development asset and uses it only for disputes.

## Impact If Fixed

A workforce that has never observed its own practice gets the most basic tool of the teaching profession, at essentially zero marginal cost because the recordings already exist. The structural summary makes it usable in five minutes rather than an hour. And a tutor facing a complaint can see what they are accused of.
