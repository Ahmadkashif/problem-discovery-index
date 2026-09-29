# Everyone Gets the Same Sequence

**Niche:** [[niches/online-course-platforms/knowledge-state-estimation/profile|Knowledge State Estimation]]
**Industry:** [[industries/online-course-platforms|Online Course Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The experienced learner sits through the basics and the beginner is dropped into a section they have no chance with, and both are shown the same next video.
**Tags:** #quick-win #descriptive-statistics #evaluation-metrics #automation #confidence-intervals #worker-facing #gradient-boosting #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to infer what a learner currently knows from pauses, attempts, abandonments and returns — and whoever estimates mastery accurately can tell each learner what to do next instead of what to watch next.

## The Problem
A course is a fixed sequence. A learner who already knows the first three hours watches them anyway or skips blindly. A learner missing a prerequisite reaches section four, understands nothing, and concludes they are not capable. Both experiences are visible in the data — one is skipping and accelerating, the other is rewinding and failing — and the next-video button behaves identically for both.

## Why It's Still Broken
A course is authored and sold as a linear artefact, so the player is a playlist — a product shaped like a video series cannot branch without changing what it is. Adaptivity requires a concept structure nobody authored. Instructors design for a single imagined learner. And nobody measures how many learners are in the wrong place.

## What a Fix Looks Like
Use the signals that are already unambiguous. Detect the learner who is skipping and accelerating and offer to jump ahead, which is the fix and requires no model at all. Detect the learner who is rewinding repeatedly and failing and offer the prerequisite, since that pattern is unmistakable and currently produces nothing. Ask a short diagnostic at the start rather than assuming, as most learners will answer five questions and it places them correctly. Let the learner mark what they already know, because they usually know and are never asked. Report where in a course learners systematically stall, which is the instructor's most useful feedback and is one query. Surface the prerequisite explicitly at the point of struggle rather than in a course description nobody reads at that moment. Show a concept-level progress view rather than a video-position bar, so progress means something. Allow non-linear navigation with guidance, since learners already skip and are doing it blindly. Track whether learners who jumped ahead succeeded, which validates the feature cheaply. And measure abandonment by position, as the cliff will be obvious and specific.

## Who Feels the Pain
Experienced learners bored into abandonment; beginners who conclude they cannot learn the subject; instructors whose course fails for structural reasons they cannot see; and platforms whose completion statistic has an obvious partial explanation nobody acts on.

## Impact If Fixed
A product shaped like a video series cannot branch without changing what it is, so everyone gets the playlist. Detecting the accelerating and the stalling learner needs no model, and the abandonment cliff is one query away.
