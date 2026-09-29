# Build: Misconception-Level Diagnosis and Session Preparation

**Niche:** [[niches/online-tutoring-platforms/diagnostic-and-preparation/profile|Diagnostic & Session Preparation]]
**Industry:** [[industries/online-tutoring-platforms|Online Tutoring Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Identify the specific misconception blocking a student from their work and prior sessions, and hand the tutor a prepared plan before the session starts.
**Tags:** #large-language-models #bayesian-inference #transformers #evaluation-metrics #confidence-intervals #graph-theory #tacit-knowledge-ml #worker-facing
**Contested on:** Whether a student's specific misconception can be identified from their existing work without a skilled tutor asking questions live.

## The Problem

The first session is diagnostic and the family pays for it as teaching. A good tutor spends it finding the real problem, which is frequently several years upstream of the topic the parent booked for. A less experienced tutor teaches the booked topic to a student whose gap is elsewhere, and the sessions produce nothing.

The diagnosis is genuinely skilled work. It requires knowing the common misconceptions in the subject, knowing which prerequisite failures produce which surface errors, and asking the questions that separate them. It is also, importantly, the part of tutoring most amenable to support: misconceptions in school mathematics and reading are well catalogued, the prerequisite structure of school subjects is well understood, and student work carries diagnostic signal that a model can read.

Preparation between sessions is the same story — necessary, unpaid, and much of it reducible to assembling what the platform already has.

## Why Nobody Has Built This

Platforms sell sessions. Preparation happens between them, is unbilled, and therefore has no line in any product roadmap. The tutor absorbs it, which means the cost is invisible to the people who decide what to build.

Diagnosis specifically is hard in a way that has deterred attempts. Misconception-level inference needs a model of the subject's prerequisite structure and of the errors each gap produces, which is domain knowledge that has to be built subject by subject. It has existed in intelligent tutoring system research for decades without reaching this market, partly because the research systems were built to replace the tutor rather than to brief them.

## What to Build

A diagnosis and preparation layer that briefs the tutor before the session.

**Build the prerequisite structure.** A graph of concepts and their dependencies for each subject and level, with the common misconceptions attached to each node and the surface errors each misconception produces. This is curriculum knowledge, it exists in the education literature and in curriculum standards, and it is the foundation everything else stands on. Build it for one subject properly rather than five superficially.

**Diagnose from available evidence.** Student work — homework photos, uploaded assignments, the problems they got wrong — read by a model against the misconception catalogue. Prior session transcripts, which are the richest source and completely unused: a transcript where a student repeatedly stumbled on the same step is a diagnosis. A short adaptive diagnostic where nothing else is available, targeted at the prerequisite chain below the booked topic rather than at the topic itself.

**Express it as a posterior.** Not "the student does not understand fractions" but a distribution over candidate gaps with confidence, and the specific question that would distinguish the top two. This is the form a tutor can use: they will confirm or reject it in the first five minutes, which is what a tutor should be doing rather than starting from nothing.

**Prepare the session.** Given the diagnosis, a proposed sequence, two or three problems targeted at the suspected gap, a reminder of where the last session ended, and the student's recurring errors. Fifteen minutes of a tutor's unpaid preparation, done in advance and offered as a draft they can override.

**Carry it forward.** Every session updates the student model. A tutor picking up a student mid-stream gets the accumulated picture rather than starting over, which is where the largest waste currently sits.

**Keep the tutor in charge.** The brief is a hypothesis with evidence, not an instruction. Tutors will reject a system that tells them what to teach and will use one that tells them what it noticed — and the second framing is also the accurate one, given how uncertain any automated diagnosis will be.

## Target Customer

Platforms competing for tutors, for whom eliminating unpaid preparation is the strongest recruitment argument available. Also tutors directly, many of whom already pay for materials and would pay for preparation. And the district segment, where diagnostic rigour is expected.

## Impact If Built

The first session becomes teaching instead of investigation, which is an hour of value returned to every new family. The largest pool of unpaid skilled work in the industry shrinks substantially. And the diagnostic skill that currently separates experienced tutors from new ones becomes partly available to both, which raises the floor of the whole market.
