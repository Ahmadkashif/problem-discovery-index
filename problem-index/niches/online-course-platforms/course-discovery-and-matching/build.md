# Matching on Fit Rather Than Popularity

**Niche:** [[niches/online-course-platforms/course-discovery-and-matching/profile|Course Discovery & Matching]]
**Industry:** [[industries/online-course-platforms|Online Course Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The bestselling course is recommended to someone who will not get past week two, and the sale is recorded as a success.
**Tags:** #gradient-boosting #matrix-decompositions #evaluation-metrics #confidence-intervals #causal-inference #survival-analysis #revenue-impact #k-nearest-neighbors
**Contested on:** Every serious competitor in this niche is fighting to match a learner to a course they will finish and benefit from rather than to the one most people bought — and whoever ranks on fit rather than on popularity changes what the marketplace rewards.

## The Problem
Ranking is driven by rating and enrolment. Both measure popularity, both lag reality by years, and neither knows anything about the learner in front of them. A beginner is shown an advanced course because it sells well; a practitioner is shown an introduction because it has more reviews. The mismatched learner buys, stalls, does not complete, and does not return — and the platform records a successful transaction and a rating collected before the stall.

## Why Nobody Has Built This
Enrolment is the revenue event, so ranking optimises it and everything downstream is somebody else's concern — a marketplace paid at purchase will rank on purchase probability unless something forces otherwise. The learner's level is unknown because nobody asks. Outcome signals do not exist to rank on, which connects this to the measurement work. And ratings are what learners expect to see.

## What to Build
Rank on whether the match worked. Assess the learner's current level with a short diagnostic or from their history, which is the core and is the input ranking has never had. Model prerequisite fit between a learner and a course, since the most common failure is not a bad course but a wrong one. Rank on completion and outcome rather than on rating, which is what changes the catalogue because instructors build toward whatever ranks. Detect and downweight decayed courses, as ranking currently rewards a course that was excellent three years ago. Show the learner why a course is being recommended, because an unexplained recommendation cannot be corrected by someone who knows their own level. Recommend a path rather than a course, since most goals require a sequence and the learner is left to assemble it. Predict the likelihood this learner completes this course and say so, which is honest and would prevent a large share of wasted purchases. Use refund and early-abandonment data as a negative signal, as it is available and is currently ignored. Measure match quality rather than conversion, which is the metric that would make all of this stick. And give instructors the fit data, so they can position their course correctly rather than broadly.

## Target Customer
Product and marketplace leadership, learners buying the wrong course, instructors whose good courses rank behind popular ones, and recommendation vendors.

## Impact If Built
A marketplace paid at purchase will rank on purchase probability unless something forces otherwise. Assessing the learner's level and ranking on completion rather than rating changes what sells, and therefore what gets built.
