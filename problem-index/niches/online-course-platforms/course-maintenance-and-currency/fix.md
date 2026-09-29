# Last Updated Two Weeks Ago

**Niche:** [[niches/online-course-platforms/course-maintenance-and-currency/profile|Course Maintenance & Currency]]
**Industry:** [[industries/online-course-platforms|Online Course Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The course shows a recent update date because the instructor changed a slide, and the content is four years old.
**Tags:** #quick-win #descriptive-statistics #evaluation-metrics #compliance #automation #confidence-intervals #worker-facing #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to know which courses have gone materially wrong as the tools they teach changed — and whoever detects decay before a learner complains stops selling instruction that no longer matches reality.

## The Problem
The listing shows a last-updated date, which learners reasonably read as an indication of currency. The date moves when anything changes — a caption fixed, a resource file replaced, a single lecture re-recorded — so an instructor can refresh it in ten minutes on a course whose substance is years old. Learners use it to choose between courses, instructors know it affects ranking, and it therefore tells them nothing while looking authoritative.

## Why It's Still Broken
The field records the most recent edit because that is what an edit timestamp does, so a technical fact became a quality signal — a metadata value repurposed as a claim will be gamed the moment it affects ranking. Nobody defined what counts as an update. Verifying substance requires looking at content. And instructors respond rationally to what the ranking rewards.

## What a Fix Looks Like
Make the date mean something. Report what proportion of the course content was updated rather than a single date, which is the fix and is computable from the platform's own version history. Show the age distribution of the lectures, since a course with three recent lectures and forty old ones is legible that way and invisible as a date. Distinguish substantive updates from cosmetic ones, because the two are recorded identically today. Show the version of the tool taught where a course teaches one, as that is the actual question and is usually stated in the content. Weight recent reviews separately in the displayed rating, so currency is reflected in the signal learners actually use. Stop ranking on the update date, since rewarding a gameable field guarantees it is gamed. Prompt instructors with what specifically needs updating rather than encouraging a refresh, which turns an incentive to game into an instruction to fix. Let learners report outdated content in a structured way, as the Q&A already contains this and nobody extracts it. Report catalogue age honestly, which is uncomfortable and correct. And tell learners plainly when a course teaches a superseded version, because that is the disclosure they are owed.

## Who Feels the Pain
Learners choosing on a meaningless signal; instructors who genuinely maintain their courses and gain no advantage; platforms whose quality signal is gamed; and anyone following instructions for software that no longer works that way.

## Impact If Fixed
A metadata value repurposed as a claim will be gamed the moment it affects ranking. Reporting the proportion of content updated and the lecture age distribution is computable from version history and cannot be refreshed with a slide change.
