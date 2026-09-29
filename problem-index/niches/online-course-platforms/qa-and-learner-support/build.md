# The Same Twenty Questions

**Niche:** [[niches/online-course-platforms/qa-and-learner-support/profile|Q&A and Learner Support]]
**Industry:** [[industries/online-course-platforms|Online Course Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Thousands of questions, twenty distinct ones, and an instructor answering them individually until they stop.
**Tags:** #large-language-models #bert #k-means-clustering #evaluation-metrics #automation #confidence-intervals #worker-facing #word-embeddings
**Contested on:** Every serious competitor in this niche is fighting to answer the same twenty questions once instead of forever — and whoever does it removes an unbounded obligation that makes instructors abandon their own courses.

## The Problem
Learners hit the same confusions at the same points, because the course explains the same things in the same way to everyone. The Q&A therefore contains the same questions repeatedly, already answered, sometimes many times, buried in a chronological thread. The instructor answers them again or stops answering, at which point the course displays an unanswered queue and looks abandoned — which affects its ranking and its sales, so the obligation is real and permanent.

## Why Nobody Has Built This
The Q&A was built as a discussion feature, so it is chronological and unstructured — a forum optimised for conversation accumulates rather than resolves. Deduplication was never applied. The question corpus was never read as course feedback. And the burden falls on the instructor rather than on the platform, which means nobody with the ability to fix it experiences the problem.

## What to Build
Answer once, surface always, and fix the cause. Cluster questions by meaning and identify the recurring ones, which is the core and immediately reveals that thousands of questions are twenty. Surface the existing answer before a learner posts, since most would accept it and the asking is a search failure. Draft answers from the course content and prior responses for the instructor to approve, which removes the typing without removing their voice. Attach answers to the point in the course where the confusion occurs rather than to a separate thread, as that is where the learner is. Feed the recurring questions back as course feedback, because twenty recurring questions are twenty things the course does not explain and fixing them removes the questions permanently. Distinguish a content gap from an individual difficulty, since they need different responses. Escalate the genuinely novel to the instructor, which is the part worth their time. Bound the obligation with a stated response policy, as an open-ended commitment attached to a single sale is why instructors disengage. Show the instructor which questions cost them the most time, so the highest-value fix is obvious. And measure question volume per enrolment as a course quality signal, which is informative and unreported.

## Target Customer
Support and community leadership, instructors carrying an unbounded obligation, learners waiting for answers, and community platform vendors.

## Impact If Built
A forum optimised for conversation accumulates rather than resolves, and the burden falls on someone who cannot change the product. Clustering the questions shows that thousands are twenty, and those twenty are a list of what the course fails to explain.
