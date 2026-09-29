# Course Discovery and Readiness Matching

**Industry:** [[online-course-platforms|Online Course Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Search ranks courses by rating and enrolment, which recommends the popular course to a learner who lacks its prerequisites and will quietly give up in week two.
**Tags:** #bert #word-embeddings #contrastive-learning #graph-neural-networks #gradient-boosting #k-nearest-neighbors #evaluation-metrics #dimensionality-reduction

## The Problem
A learner searches for a topic and receives courses ranked mostly by popularity and rating. Both are lagging signals dominated by marketing, course age and the instructor's existing audience, and neither says anything about whether this particular learner is ready for this particular course.

Readiness is the actual determinant of whether a course works. A course labelled beginner assumes a set of prior concepts its description does not enumerate, and a learner missing two of them will struggle, blame themselves, and stop. The platform sees the abandonment and records it as churn. Conversely a learner placed in material they already know is bored out within a week.

Self-assessed level is the only input collected — beginner, intermediate, advanced — which learners are known to answer badly in both directions. Meanwhile the platform holds the data to do far better: what else this learner has completed, where they struggled, and how thousands of learners with similar histories fared in this specific course.

## What Already Exists
Every platform has search, filters and recommendations; Coursera and Udemy both run substantial recommendation systems. Learning paths and specialisations curate sequences manually. Skill taxonomies exist — Lightcast, ESCO, and each platform's internal version — and map courses to skills at a coarse grain. LinkedIn Learning connects courses to profile skills. Some platforms offer placement quizzes on a small number of subjects.

## The Customisation Gap
Recommendation optimises for enrolment, which is the wrong objective and is why the same popular courses dominate. The objective that would serve the learner is expected mastery gain given their current state, which requires a state estimate and a model of how prior knowledge interacts with a course's assumed prerequisites — both of which are derivable from the platform's own completion and struggle data and neither of which is built.

Prerequisites themselves are the concrete missing artefact. They are stated in prose when stated at all, and the real prerequisite structure of a course is observable: which prior concepts distinguish learners who succeed from those who abandon at a given point. Inferring that from behaviour, rather than asking instructors to declare it, is tractable and would let a platform tell a learner precisely what to learn first.

The second gap is content-level rather than course-level matching. Learners frequently need one module, not a forty-hour course, and search operates on course titles. Representing content at the lesson level lets a platform answer the question people actually have, which is how to do one specific thing.

And discovery needs to account for decay: a highly-rated course about a tool that has changed twice since should not outrank a current one because it accumulated ratings over four years.

## Impact If Solved
Mismatched placement is a substantial share of the sector's abandonment, and it is invisible because it looks like ordinary churn and the learner blames themselves. Readiness-aware matching with inferred prerequisites converts a portion of that into completion, and lesson-level retrieval serves the large population who want a specific answer rather than a course — which today leaves for a search engine or an assistant and does not come back.
