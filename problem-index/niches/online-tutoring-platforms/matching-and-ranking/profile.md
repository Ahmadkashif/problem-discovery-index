# Matching & Tutor Ranking

**Parent Industry:** [[industries/online-tutoring-platforms|Online Tutoring Platforms]]
**Category:** High Market Share
**Contested on:** Whether the tutor a family is shown is the one most likely to help this particular student, or the one most likely to be booked.

## Profile
**Market Size:** ~$1.6B — 20% of US online tutoring
**Share of Parent Industry:** ~20%
**Digital Adoption:** High — ranked search and recommendation, optimised on conversion
**Target Buyer:** Platform marketplace and search engineering
**Automation Potential:** Fully automated; the contest is the objective

## What Makes This a Distinct Niche

A family searching for a tutor sees a ranked list. That ranking determines which tutors earn and which do not, and it is optimised for booking conversion — the only outcome available within the session that produced it.

Matching in tutoring has a property that most marketplace matching does not: the right answer depends on a compatibility between two specific people. A tutor who is excellent with confident students who need stretching may be poor with an anxious student who has decided they are bad at maths. A tutor whose strength is exam technique is the wrong choice for a student with a conceptual gap three years back. The platform has the data to learn these interactions — the same tutors and the same student types recur thousands of times — and ranks on price, subject, rating and availability.

It is distinct from effectiveness measurement because a ranking can improve on interaction fit even with an imperfect quality signal, and because the ranking has its own contested questions about exposure and new-tutor cold start.

## Current Tools & Gaps

Learned ranking over subject, price, rating, rebooking, response time and availability, refined against booking conversion. Some platforms run an intake questionnaire and a rules-based match; a few offer a human matching service at the premium end, which is a tacit admission that the automated version is inadequate.

The gaps are the interaction and the objective. Nobody models tutor-student compatibility as an interaction term, despite it being the thing families are actually trying to find. Nobody optimises against a retention or outcome target rather than the first booking. And new tutors have no path to their first student except price, so the cold start is as unsolved here as in any labour marketplace.

## Problems
- [[niches/online-tutoring-platforms/matching-and-ranking/build|🔨 Build: Compatibility-Aware Matching]]
- [[niches/online-tutoring-platforms/matching-and-ranking/buy|🛒 Buy: Marketplace Ranking Stacks Adapted to a Relationship]]
- [[niches/online-tutoring-platforms/matching-and-ranking/fix|🔧 Fix: The First Match Fails and the Family Leaves]]
