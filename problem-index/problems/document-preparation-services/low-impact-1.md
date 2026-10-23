# From Intake Call to Accomplishment Bank

**Industry:** [[document-preparation-services|Document Preparation Services]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every resume writer runs the same hour-long discovery interview and then spends another hour turning their notes into quantified accomplishments, and the general-purpose transcription and writing tools they use know nothing about what makes a resume bullet work.
**Tags:** #large-language-models #transformers #feature-engineering #evaluation-metrics #automation #worker-facing #quick-win

## The Problem
A professional resume order starts with an old resume, a questionnaire the client half-completes, and a phone or video call of roughly an hour (estimate). On the call the writer digs for what the old resume leaves out: the size of the team, the budget, the before-and-after number, the problem nobody else could solve, the reason the client was promoted. Good writers are relentless interviewers. Clients understate their work, and the accomplishment that wins the interview is usually buried in a story the client tells as an aside.

Then the writer works from notes. They replay the recording or reread scribbles, pull out each achievement, find or estimate the metric, recast it in an action-result form (the CAR or STAR pattern every resume course teaches), choose which ones fit the target role, and match vocabulary to the postings the client is aiming at. The same raw material later feeds a cover letter, a LinkedIn About section and, for senior clients, a bio. At platform rates (independent contractors at volume services are reportedly paid a flat ~$20–35 per resume, estimate) this second hour is the difference between a living and a loss. For a boutique charging several hundred dollars or more (estimate), it is the part the client is actually paying for.

## What Already Exists
Meeting transcription (Otter, Zoom and Teams transcripts, Fathom) turns the call into text. General chatbots will rewrite a paragraph as bullets. Resume builders such as Resume.io, Teal and Kickresume generate bullets from a job title, and keyword matchers such as Jobscan compare a resume against a posting. Writers also keep their own swipe files of verbs and phrasings. Customer tools like HoneyBook or Dubsado handle the order, the questionnaire and payment.

## The Customisation Gap
None of these tools knows what a resume accomplishment is. Transcripts are a wall of conversation. Generic rewriting invents metrics, flattens a client's voice into the same "spearheaded cross-functional initiatives", and cannot tell a responsibility from an achievement. The resume-specific logic is: extract candidate accomplishments from the interview with the evidence for each (who, what, how much, compared with what) and flag the ones missing a number, so the writer can ask a follow-up before the draft rather than after. Bank each accomplishment once, tagged by skill, scale, industry and seniority, so the resume, cover letter, LinkedIn profile and future updates draw from the same verified record. Map the bank against the target postings, and for federal clients against OPM's qualification language, showing which requirements have evidence and which don't. And keep the client's own phrasing available, because hiring managers and recruiters increasingly see machine-written sameness as a red flag.

## Impact If Solved
An accomplishment bank built straight from the intake call could cut the writer's post-interview hour roughly in half (estimate). It would also catch missing metrics while the client is still on the phone and give every later document and update a single source of truth. For a solo writer turning out a few resumes a week, that is capacity for one or two more clients without lowering the quality that earns their referrals.
