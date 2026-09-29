# Fix: The Student's History Does Not Follow Them

**Niche:** [[niches/online-tutoring-platforms/diagnostic-and-preparation/profile|Diagnostic & Session Preparation]]
**Industry:** [[industries/online-tutoring-platforms|Online Tutoring Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A student switches tutors and the new one starts from zero, though the platform holds every session the student has ever had.
**Tags:** #descriptive-statistics #large-language-models #evaluation-metrics #workflow-orchestration #data-integration #worker-facing #quick-win #compliance
**Contested on:** Whether what one tutor learned about a student is made available to the next one.

## The Problem

A student works with a tutor for two months. The tutor learns a great deal: that the student shuts down when they feel tested, that they are strong at procedure and weak at reasoning, that the real gap is in fractions, that they respond well to being asked to explain their thinking, that Thursdays after practice they are exhausted.

The tutor becomes unavailable. A new tutor picks the student up and starts from nothing. They spend a first session rediscovering what was already known, and they will not find all of it — some of that knowledge took the first tutor six sessions to accumulate.

The platform holds every session recording, every transcript and whatever notes were written. It passes none of it on.

## Why It's Still Broken

Tutor notes, where they exist, are private to the tutor or buried in a booking system nobody reads. Nothing prompts a structured handover, and a departing tutor — often leaving because they are busy or moving on — has no incentive to write one.

There are genuine concerns underneath: a previous tutor's characterisation of a student can be wrong, unfair, or prejudicial in a way that damages the new relationship, and passing on "this student does not try" would be worse than passing nothing. Student data about minors also needs handling carefully, and the consent basis for sharing session content between contractors is not obviously in place on most platforms.

But these are reasons to design the handover carefully, not to have none. Every school passes records between teachers under exactly these constraints.

## What a Fix Looks Like

Build the student record and hand it over deliberately.

Prompt a structured handover when a tutoring relationship ends: topics covered, what was working, what the student finds hard, the identified gap, and one thing the next tutor should know. Five fields, two minutes, prompted at the moment of ending — and paid for, because it is work.

Generate the draft automatically from what the platform already has. Session transcripts summarised into topics covered, recurring difficulties and the student's own language about what they find hard. The tutor reviews and corrects rather than composes, which is the difference between a handover that gets written and one that does not.

Separate observation from judgement in the format. "Struggled with three-step problems, solved single-step reliably" is useful and checkable. "Lazy" is neither, and the form should not have a place to put it. Design the fields so that what is passed on is behavioural and specific.

Show the student's arc to the new tutor. Sessions, topics, duration, frequency and any assessment data, as a timeline. This is a query, not a project, and it alone removes most of the rediscovery.

Get consent right. Families should be told that their child's tutoring record carries forward between tutors on the platform, what it contains, and be able to see it. Most will want this; a few will not; and the record is theirs in a meaningful sense.

Let the family see it too. A parent reading a clear summary of what their child has worked on and what the tutor identified is receiving something valuable, and it doubles as the progress reporting the family currently does not get.

## Who Feels the Pain

Students, who re-explain themselves and re-establish trust every time a tutor changes, and who are asked again about material they have already covered. Families, who pay for a rediscovery session they have paid for before. New tutors, who start blind and appear less competent than they are. And the platform, which holds the complete record and delivers a student to a new tutor as a stranger.

## Impact If Fixed

A tutor change stops costing a session and a relationship restart. The accumulated knowledge about a student becomes an asset that stays with them rather than leaving with whoever learned it. And the family gets, as a by-product, the first clear account of what their child has actually been working on.
