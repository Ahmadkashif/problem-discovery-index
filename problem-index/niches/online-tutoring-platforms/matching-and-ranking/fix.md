# Fix: The First Match Fails and the Family Leaves

**Niche:** [[niches/online-tutoring-platforms/matching-and-ranking/profile|Matching & Tutor Ranking]]
**Industry:** [[industries/online-tutoring-platforms|Online Tutoring Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A poor first match produces a bad session, the family concludes tutoring does not work, and nobody at the platform notices that the problem was the match.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #workflow-orchestration #hypothesis-testing #quick-win #worker-facing #automation
**Contested on:** Whether a failed first match is treated as a recoverable event or as a lost customer.

## The Problem

A family books a tutor. The session goes poorly — the tutor pitched too high, the student did not engage, the style did not suit. The family does not rebook. The platform records a non-repeating customer and moves on.

What actually happened is a fixable matching failure, and the family has drawn a conclusion much larger than the evidence supports: that tutoring does not help their child. They tell other parents. They do not come back.

This is the largest churn event in the business, and the platform's response to it is nothing. There is no follow-up asking what did not work, no supported rematch, no record of the failure as anything other than an absence of a second booking. The single most informative event the platform generates — a match that did not work, with a reason — is discarded.

## Why It's Still Broken

The metric hides it. Conversion is measured on the first booking, which succeeded. Retention is measured in aggregate, where the failed first matches are indistinguishable from families whose needs were met in one session or whose circumstances changed.

Asking why also feels risky: a follow-up after a poor session invites a complaint, a refund request and a negative review. The safer path is silence, and silence is what happens.

And nobody owns the rematch. Support handles complaints, matching handles search, and a family who quietly does not rebook belongs to neither.

## What a Fix Looks Like

Treat a non-rebooking after a first session as an event, not an absence.

Detect it. A first session with no rebooking within a window is a specific, identifiable state and the platform can flag it the same day. Most platforms do not because nobody asked for the query.

Ask, briefly and well. One message: did that work for your child, and if not, what was off — too advanced, too slow, style, communication, scheduling. Four options and a free text box. Response rates to a short, genuinely-curious question at this moment are better than expected, because the parent has an opinion and nobody has asked for it.

Offer a supported rematch immediately, with the reason carried forward. "You said the pace was too fast — here are three tutors who work well with students who need more time on fundamentals," with the first session free or discounted. The cost of a discounted session is far below the cost of losing the family, and this is the moment where a second attempt is possible.

Record the failure reason as training data. Failed matches with stated reasons are the most informative dataset in the whole matching problem, and they are currently thrown away. Even a few thousand labelled failures materially improves the intake design and the ranker.

Protect the tutor. A poor fit is not a poor tutor, and a mismatch attributed to a tutor's rating punishes them for a matching failure. Fit-related non-rebookings should be identifiable and should not count against a tutor the same way a quality complaint does — which also makes tutors willing to say, honestly, when they are not the right person for a student.

Then close the loop upstream: if a particular intake pattern keeps producing mismatches, the intake questions are wrong, and the failure record says which.

## Who Feels the Pain

Families, who try tutoring once, get a poor fit, and conclude their child cannot be helped. Students, who take the failure personally more often than adults realise. Tutors, who are rated down for a mismatch that the matching produced. And the platform, which loses its most expensive-to-acquire customers at the point where a single message and a discounted session would have kept them.

## Impact If Fixed

The most common churn event becomes recoverable. The platform acquires labelled matching failures, which is the training data the entire matching problem lacks. And a family whose first attempt went wrong gets a second one informed by what went wrong, instead of a conclusion about their child.
