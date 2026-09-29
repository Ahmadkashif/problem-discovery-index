# History: Online Course Platforms

**Industry:** [[industries/online-course-platforms|Online Course Platforms]]
**Primary Wave:** [[series/eras/wave-10-creator-platform|10 — The Creator Platform]]
**Secondary Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**Origin Parent:** none — see below
**Episode Tier:** 1
**Transferable Pattern:** When a business is paid for a proxy (enrolment, watch time) rather than the outcome it claims to produce (a learner who can now do the thing), the highest-value product is the instrument that measures the outcome, not more of the proxy.

> **Origin Parent — omitted.** No `origins/` industry has a claim here. Correspondence courses and broadcast-television education are the pre-digital analogue, and this file opens with them deliberately, because the completion-rate finding below only makes sense against that baseline.

## Before, Completion Was Already the Problem

Distance education did not begin with the internet. Correspondence courses and broadcast-based instruction existed for decades before any of this vault's Wave 10 platforms, and the honest historical baseline is unflattering to the category before a single MOOC existed: **fewer than five percent of enrollees in that older model typically completed a course.** This matters because it means the low-completion finding below is not a new failure the internet introduced. It is an old, unsolved problem that a much larger, much cheaper distribution layer inherited and has not fixed.

## The Origin Event — One Course, One Semester

**In autumn 2011, Stanford's "Introduction to Artificial Intelligence,"** taught by Sebastian Thrun and Peter Norvig and opened to anyone online rather than restricted to enrolled students, drew **roughly 160,000 registrants** — a scale no university course had approached. Within weeks, comparable open courses from Andrew Ng and Jennifer Widom followed. The direct consequence was fast and traceable: **Sebastian Thrun founded Udacity, and Daphne Koller and Andrew Ng founded Coursera, both in 2012; MIT's parallel MITx effort became edX that spring when Harvard joined.** *(The characterisation of 2012 as "the Year of the MOOC" is a widely repeated framing from contemporary press coverage; this session could not independently reverify the specific attribution and phrasing against a primary source, and it should be treated as a well-known contemporary label rather than a confirmed direct quotation.)*

## What Became Cheap

**Enrolling the next learner.** Once a course was recorded, the marginal cost of a 160,001st student was close to zero — the same cloud-infrastructure economics [[series/eras/wave-06-cloud-saas|Wave 6]] describes for vertical SaaS, applied to a lecture instead of a database. That is the entire founding insight of this industry, and it is worth being precise that it is a distribution insight, not a pedagogical one: nothing about the 2011 course changed how learning works. It changed how many people could be exposed to it for the same production cost.

## The Trade-Off — What Gets Measured Is What Gets Sold

The business model that resulted from that founding insight monetises enrolment, and in a marketplace context, completion is not the metric revenue depends on. That misalignment is not conspiratorial — a platform selling access to a library has a straightforward reason to report and optimise the number that correlates with revenue — but it produces exactly the gap this vault's own hub note names: "the business model monetises enrolment and the mission claims to produce capability, and nothing in the stack connects the two."

**The completion figures that exist are genuinely mixed, and the honest thing to do is present the range rather than a single number.** Harvard and MIT's early open courses in 2012 showed **completion rates averaging around 22%**. A separate Stanford-affiliated analysis of the same period found figures ranging from **5% (graduate-level enrollees) to 27% (high-school-level enrollees)**, depending heavily on who was enrolling and why. Both studies also flag a definitional problem worth stating directly: researchers distinguished "auditors," who watch material with no intention of finishing, from "completers," meaning a single reported completion rate conflates two entirely different populations with different goals. **A course's completion rate depends heavily on what denominator you choose, and the sector has never agreed on one.** Modern paid marketplace courses (Udemy, Skillshare) are widely understood to complete at meaningfully higher rates than free open courses, for the obvious reason that payment filters out casual enrollees — but this session found no rigorously sourced sector-wide figure for that claim, and it should be treated as a plausible inference, not a verified statistic, until checked further.

## The Binding Constraint — Assessment Never Left Multiple Choice

The instrument that would resolve the completion ambiguity — a real measurement of whether a learner can now do the thing the course claims to teach — barely exists anywhere in the category. Assessment is overwhelmingly multiple-choice quizzes or unreviewed projects; a certificate certifies attendance and quiz performance, not demonstrated capability. Learning-record standards like xAPI, built specifically to capture structured evidence of a learner's competence rather than just their clicks, exist as a specification and are, per this vault's own hub note, "barely used outside corporate systems." **The platforms hold what may be the most detailed behavioural record of human learning ever assembled** — every pause, rewind, replay, quiz attempt and abandonment, across millions of learners moving through identical material — and the sector has spent its first decade-plus optimising enrolment and recommendation rather than turning that record into an estimate of what a learner actually knows.

## What Is Being Displaced Right Now, in Real Time

This is not a settled graveyard entry, and it should not be written as one — it is a live, ongoing shift, not a completed death, and the file should say so rather than overclaim. The product this entire category was built to sell — a competent recorded explanation of a concept — has been substantially commoditised by generative tutoring assistants that explain the same concept interactively, on demand, adjusted to the question actually asked. Every major platform in the category has bolted on a generative assistant in response. **What remains scarce, and what none of these assistants provide on their own, is structured practice, real assessment, feedback on submitted work, and a credential an employer actually trusts** — precisely the four things this vault's hub note identifies as the category's least-invested-in capabilities, and precisely the four a generative explainer does not substitute for.

## What's Still Open

- [[problems/online-course-platforms/high-impact|🔴 Enrolment Is the Product and Learning Is Unmeasured]]
- [[problems/online-course-platforms/low-impact-2|🟡 Course Maintenance and Content Decay]]
- [[niches/online-course-platforms/knowledge-state-estimation/profile|Knowledge State Estimation]]
- [[niches/online-course-platforms/learning-measurement/profile|Learning Measurement]]
- [[niches/online-course-platforms/practice-and-feedback/profile|Practice and Feedback]]
- [[niches/online-course-platforms/credential-and-outcome-verification/profile|Credential and Outcome Verification]]

## The Transferable Pattern

> **When a business is paid for a proxy — enrolment, watch time — rather than the outcome it claims to produce, the highest-value product is the instrument that measures the real outcome, not more of the proxy.**

This is the same shape [[history/creator-businesses|Creator Businesses]] and [[history/newsletter-media|Newsletter Media]] both reach independently in this batch, applied to a domain where the proxy failure has a human cost beyond a business's bottom line: a learner who completes a course and still cannot do the job it claimed to prepare them for has lost time they cannot get back, on the strength of a signal — enrolment, rating, a certificate — that was never measuring capability in the first place. An FDE evaluating this category should be honestly sceptical of vendor completion and outcome claims exactly as this file has been, ask what denominator a stated completion rate uses before repeating it, and treat "we can finally tell you whether the learner can do the thing" as the actual product this sector has never shipped.

**Sources:** Wikipedia, *Massive open online course* (pre-MOOC correspondence-course completion rates; Stanford AI course, autumn 2011, ~160,000 enrolled; Thrun/Udacity, Koller-Ng/Coursera, MITx→edX, all 2012; Harvard/MIT 2012 completion figures ~22% average; Stanford-affiliated 5–27% by enrollee type; auditor/completer definitional distinction); this vault's `industries/online-course-platforms.md` and `series/eras/wave-06-cloud-saas.md`.
