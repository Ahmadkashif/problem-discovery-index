# Recommended Because It Is Popular

**Niche:** [[niches/online-course-platforms/course-discovery-and-matching/profile|Course Discovery & Matching]]
**Industry:** [[industries/online-course-platforms|Online Course Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The learner is shown a course with two hundred thousand students and no indication that all of them already knew how to program.
**Tags:** #quick-win #descriptive-statistics #evaluation-metrics #automation #confidence-intervals #worker-facing #revenue-impact #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to match a learner to a course they will finish and benefit from rather than to the one most people bought — and whoever ranks on fit rather than on popularity changes what the marketplace rewards.

## The Problem
Course listings state a level — beginner, intermediate — chosen by the instructor, often optimistically, because a beginner label widens the market. There is no indication of what the course actually assumes, who succeeds in it, or how learners like this one fared. The learner buys on the enrolment count and the rating, discovers in week two that they lack something the course never mentioned, and stops. The information that would have prevented it is in the platform's data.

## Why It's Still Broken
The level field is self-declared because nobody verifies it, so the incentive is to claim the widest audience — a metadata field with a commercial incentive and no verification is unreliable by construction. Completion rates by learner background are not computed. Listings are marketing surfaces. And nobody measures how many purchases end in week two.

## What a Fix Looks Like
Show who actually succeeds. Report completion rate by learner background on every listing, which is the fix and is computable from existing data. Extract the course's real prerequisites from where learners stall, since the stall points reveal what is assumed and the description does not. State assumed knowledge explicitly, as most listings omit it entirely. Show early abandonment rate alongside the rating, because a course that loses half its learners in week two is a different product from one that does not. Verify the declared level against observed learner outcomes, which will find many miscategorised courses immediately. Warn a learner whose profile resembles those who abandon, since an honest warning before purchase is worth more than a refund after. Report refund rates, as they are a direct signal currently hidden. Recommend the prerequisite course when the fit is poor rather than declining to recommend anything. Give instructors their own stall data, because most would fix a bad opening if they could see it. And measure week-two abandonment as a listing quality metric, which nobody reports.

## Who Feels the Pain
Learners who conclude they cannot learn the subject; instructors whose courses are bought by the wrong people; platforms with a completion statistic they cannot explain; and good beginner courses outranked by advanced ones with a beginner label.

## Impact If Fixed
A metadata field with a commercial incentive and no verification is unreliable by construction, so declared level means little. Completion by background and stall-point analysis are computable today and tell a learner what the description will not.
