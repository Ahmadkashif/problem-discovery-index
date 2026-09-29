# Fix: The Parent Gets a Receipt and Nothing Else

**Niche:** [[niches/online-tutoring-platforms/progress-reporting/profile|Progress Reporting to Parents]]
**Industry:** [[industries/online-tutoring-platforms|Online Tutoring Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** After eight sessions and several hundred dollars, the only record a parent has is eight charges and eight one-word topic labels.
**Tags:** #descriptive-statistics #evaluation-metrics #workflow-orchestration #data-integration #confidence-intervals #worker-facing #quick-win #compliance
**Contested on:** Whether the platform will show a parent the record of sessions it already holds.

## The Problem

A parent has paid for eight tutoring sessions. What they can see is a list of dates, durations and charges, plus whatever topic the tutor selected from a dropdown — "Algebra", "Algebra", "Fractions", "Algebra".

They do not know whether their child is doing the work, whether the same difficulty keeps recurring, whether the tutor has a plan, or whether anything has improved. They ask their child, who says it was fine. They ask the tutor, who is friendly and reassuring. And they decide whether to continue paying on the basis of almost nothing.

The platform holds the attendance record, the duration, the topics, the tutor's notes where they exist, and the full transcript. It shows the parent a billing history.

## Why It's Still Broken

The parent-facing surface was built around booking and payment, because those are the transactions. Reporting is not a transaction and was never scoped.

There is also a quiet reluctance to expose too much. A record showing that the same topic recurred for six weeks raises the question of whether the tutoring is working, and a platform whose revenue depends on continued booking has no urgency to prompt it.

And notes are inconsistent, which makes a reporting view look bad — half the sessions would show nothing. That is an argument for generating the content, not for hiding the view.

## What a Fix Looks Like

Show the parent what the platform already knows, and make the parts that are empty fill themselves.

Build the session history view: date, duration, attendance, topic, tutor notes, materials used, any homework set. This is the data the platform stores, rendered for the person paying. It is a screen, not a project.

Add the arc. Topics over time, so a parent can see the sequence and whether the same thing keeps recurring — which is genuinely informative in both directions, since sustained work on one gap is often exactly right and needs explaining rather than hiding.

Fill the notes automatically from the transcript, with tutor review, which is the build in this niche. Even a two-line generated summary per session transforms the view from a billing record into an account.

Ask the parent what they are trying to achieve, once, at the start, and show progress against it. Most parents have a specific goal — pass the exam, catch up to the class, stop the homework arguments — and nobody records it, so nothing can be reported against it.

Prompt a periodic check-in. After six sessions, a short message: here is what has been covered, here is what the tutor thinks, is this what you expected. That conversation happens too late or never, and when it happens late it is usually a cancellation.

And be willing to show a parent when it is not working. A platform that says "this has not moved in six weeks, let us try a different tutor or a different approach" loses a little revenue and earns the trust that keeps the family in the market at all.

## Who Feels the Pain

Parents, who spend substantial money on something they cannot see and decide whether to continue on faith. Students, whose parents cannot support them because they do not know what is being worked on. Conscientious tutors, whose careful work is invisible next to a tutor who writes nothing. And the platform, whose churn is driven substantially by parents who never found out whether it was working.

## Impact If Fixed

A parent can see what they are buying, which is the minimum condition for trusting a service delivered to their child by a stranger. The information is already stored, so the cost is a view plus the generated notes. And the conversation about whether it is working starts at session six rather than at cancellation.
