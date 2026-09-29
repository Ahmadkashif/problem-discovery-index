# Build: Automated Instructional Feedback from Session Recordings

**Niche:** [[niches/online-tutoring-platforms/session-instruction-analysis/profile|Session Instruction Analysis]]
**Industry:** [[industries/online-tutoring-platforms|Online Tutoring Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Transcribe and analyse sessions for the instructional behaviours the teaching research supports, and give every tutor specific feedback on their own teaching after every session.
**Tags:** #large-language-models #transformers #bert #evaluation-metrics #confidence-intervals #descriptive-statistics #worker-facing #tacit-knowledge-ml
**Contested on:** Whether instructional quality can be scored from a transcript reliably enough that tutors trust and act on the feedback.

## The Problem

A tutor teaches alone. Nobody observes them, nobody gives them feedback beyond a star rating, and they have no way to see what they actually do in a session. Habits form uncorrected over years — talking too much, answering their own questions two seconds after asking, correcting errors without ever finding out why the student made them, taking the pen when the student struggles.

Every one of these is visible in the recording, is well established in the teaching literature as consequential, and is fixable with feedback. The platform has the recordings and does nothing with them.

## Why Nobody Has Built This

It was not possible cheaply until recently. Analysing teaching discourse required a trained human rater and forty minutes per session, which is why classroom observation is sampled rather than universal. Automated analysis needed reliable transcription with speaker separation and a language model capable of judging pedagogical moves, and that combination is new.

It also sits in an organisational gap. Quality teams handle complaints, product teams build booking, and nobody owns tutor development — partly because tutors are contractors and a platform that trains and coaches them starts to look like an employer, which in this industry as in others has been a reason to do nothing.

And there is a credibility risk. Feedback that is wrong about teaching is worse than no feedback, because the tutor will reject the whole system after one bad call and tell every other tutor.

## What to Build

An analysis pipeline producing per-session, specific, evidence-anchored feedback.

**Transcribe with reliable speaker separation.** Two speakers in a video call is close to the easiest diarisation case there is, which makes the foundation solid. Retain timing, because the timing is where much of the signal lives.

**Compute the structural measures first**, because they need no judgement and are immediately meaningful. Student talk ratio. Number of questions asked by each party. Wait time after a tutor question — the pause before the tutor fills the silence, which the research identifies as one of the most consequential and most commonly violated teaching behaviours. Longest tutor monologue. Proportion of session on new material versus review. These are arithmetic on a timed transcript and a tutor seeing them for the first time usually finds at least one surprising.

**Then the judged measures**, with a language model working from a rubric grounded in the teaching literature and every judgement anchored to a specific exchange. Was the student's error diagnosed or corrected. Did the tutor ask what the student thought before explaining. Was the work handed back. Were connections made to prior sessions. Anchoring matters enormously: "at 14:20 the student said X and you responded Y — here the research suggests asking why" is feedback a tutor can evaluate and act on, while a score out of ten is something they argue with.

**Validate against human raters.** Have experienced teachers score a few hundred sessions on the same rubric and measure agreement. Publish it to the tutors. A system whose agreement with expert raters is stated is one tutors can calibrate their trust in; one that is silent about it will not be believed.

**Deliver it as development, not surveillance.** Private to the tutor by default, framed as coaching, with one or two specific suggestions rather than a scorecard. The distinction between a tool that helps tutors and a tool that ranks them determines whether the workforce cooperates, and cooperation is the whole thing.

**Handle consent and privacy properly.** Sessions involve minors. Recording, analysis, retention and access need explicit consent from families, a clear policy, and tutor consent separately — and the analysis should run on transcripts with student identity separated wherever possible.

## Target Customer

Platforms with a tutor quality function and no instrument, and platforms selling to districts where demonstrable instructional quality is part of the contract. Tutors are also a direct market: a tool that gives a professional working alone real feedback on their practice is something a meaningful share would pay for themselves.

## Impact If Built

Tutors see their own teaching for the first time, with specific and actionable feedback after every session — professional development that this workforce currently has no access to at all. The platform gets a quality signal computable on every session rather than a rating sampled from parents. And the corpus of what effective one-to-one teaching looks like starts being analysed instead of merely stored.
