# Build: Automated Progress Reporting from Session Transcripts

**Niche:** [[niches/online-tutoring-platforms/progress-reporting/profile|Progress Reporting to Parents]]
**Industry:** [[industries/online-tutoring-platforms|Online Tutoring Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Generate a substantive progress report from the session transcript automatically, for the tutor to review and send, so parents get an account of what happened instead of a receipt.
**Tags:** #large-language-models #transformers #evaluation-metrics #descriptive-statistics #confidence-intervals #compliance #worker-facing #quick-win
**Contested on:** Whether a generated report can be substantive enough to be worth reading and accurate enough to be worth trusting.

## The Problem

Preparation, marking, parent messages and progress notes are what makes tutoring work and none of them are paid, so doing the job well costs the tutor money. Progress reporting is the clearest case: it takes fifteen minutes a week per student, it is the main thing that makes a parent feel the money is well spent, and it is entirely uncompensated.

The predictable result is that it is done inconsistently. Tutors with few students write good notes; tutors with full books write "we covered quadratics, good session". Parents therefore receive wildly varying amounts of information, mostly correlated with how busy their tutor is rather than with how their child is doing.

Meanwhile the transcript of the session contains everything needed to write the report.

## Why Nobody Has Built This

It was not feasible cheaply until recently — generating a substantive, accurate summary of a teaching session required a human who was in it. That constraint is gone and the products have not caught up.

The organisational reason is that progress reporting is not part of the transaction. The platform sells sessions; what happens around them is the tutor's business. That framing survives because the cost lands on the tutor rather than on the platform's margin.

And there is a real accuracy risk that has deterred attempts. A report that says the student mastered something they did not is worse than no report, because a parent will act on it and a tutor will be blamed. Tutor review in the loop handles this and requires designing the product so that review takes a minute rather than ten.

## What to Build

A per-session and per-period report generated from the transcript, reviewed by the tutor, sent to the parent.

**Generate from the transcript with the right structure.** What was worked on, specifically — not "algebra" but "solving two-step equations with negative coefficients". What the student did well. What they found difficult, with a concrete example from the session. What was agreed for next time. What the parent could do to help, if anything. Five short sections, in plain language, without jargon and without inflation.

**Anchor every claim in the session.** A report that says the student struggled with negatives should be traceable to the moment it happened, both so the tutor can verify it in seconds and so the claim is real. Generation that is not anchored will drift into generic educational language, which parents recognise immediately and discount.

**Make review a minute's work.** Present the draft with edits inline, a one-tap approve, and the ability to add a sentence. If review takes as long as writing, tutors will not use it and nothing has changed.

**Build the period view.** Sessions over a month with topics covered, a visible arc of what has been worked on and what has shifted from difficult to secure. Parents cannot see progress in a single session and can see it over eight, and nothing currently shows them.

**Connect it to school.** Where the family has shared grades or targets, place the tutoring work next to them. This is what the parent actually wants to know and is the reason they will share the grades in the first place — the exchange that also unlocks outcome measurement elsewhere in the platform.

**Handle it as child data.** Reports about a minor's learning, generated from a recording, sent to a parent. Consent, retention, access and accuracy all need explicit handling, and the tutor's review is part of the accuracy control rather than a formality.

## Target Customer

Platforms competing for tutors — removing fifteen minutes of unpaid weekly work per student is a stronger recruitment message than a commission change — and platforms competing for parents, for whom substantive reporting is the most visible quality differentiator in a market where everyone looks the same.

## Impact If Built

Parents get an account of what their money bought, consistently, rather than depending on how busy their tutor is. Tutors get back a meaningful share of their unpaid hours. And the report becomes the natural vehicle for asking families to share grades, which is the entry point to measuring whether any of this is working.
