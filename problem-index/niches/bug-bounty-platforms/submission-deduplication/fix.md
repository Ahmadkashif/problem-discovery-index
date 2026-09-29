# Fix: Keyword Search Finds the Duplicates That Rhyme

**Niche:** Submission Deduplication & Filtering
**Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Duplicate detection depends on the second researcher having chosen similar words to the first, which is a coin flip dressed up as a process.
**Tags:** #evaluation-metrics #confidence-intervals #worker-facing #automation #workflow-orchestration
**Contested on:** Whether the mechanical share of triage is removed before a human reads, or absorbed by analysts one submission at a time.

## The Problem

An analyst suspects a submission may be a duplicate. They search prior submissions for a term. The search is lexical, so it returns submissions containing that term and nothing else.

Whether the duplicate is found therefore depends on vocabulary coincidence. Security has many words for the same thing — broken access control, IDOR, horizontal privilege escalation, missing authorisation check, object-level authorisation failure — and researchers choose among them by habit, background and translation. Two accurate descriptions of one finding can share almost no terms.

The consequences run in both directions. Undetected duplicates get triaged, reproduced and sometimes paid twice, which costs the programme money and analyst time. And detected duplicates are found by whichever analyst happened to remember or guess the right term, which means the process is not a process — it is individual recall, unevenly distributed across a team and degrading as the corpus grows.

It also produces the disputes that damage researcher relations most. A researcher told their finding is a duplicate, with no evidence shown, when the detection method is a keyword search of uncertain reliability, is being asked to accept a judgement the platform itself cannot fully justify.

## Why It's Still Broken

**It mostly works, visibly.** Keyword search catches the obvious cases, which are the majority, so the failure is invisible — nobody sees the duplicates that were never found, because they were never found.

**Nobody measures the miss rate.** The rate at which duplicates escape detection is unknown at every platform, because measuring it requires deliberately re-examining sets of submissions for missed pairs. With no number, there is no case for investment.

**Analysts compensate and it looks like the system working.** Experienced analysts develop good search instincts and personal memory of a programme's history, which masks the tooling gap and makes the problem worse when they leave.

**The cost falls on researchers.** An undetected duplicate that gets paid costs the programme. A wrongly-claimed duplicate costs the researcher, and researchers have no way to contest it.

**Search is a feature nobody owns.** It sits between platform engineering and triage operations, works adequately, and never reaches the top of a roadmap.

## What a Fix Looks Like

**Measure the miss rate.** Take a sample of submissions marked unique and re-examine them against the corpus deliberately, with a second analyst and better search. The resulting number is the case for everything else, and no platform has it.

**Search on extracted attributes, not free text.** Even without embeddings, indexing submissions by extracted target, endpoint, parameter and weakness class makes search structural rather than lexical. This is a modest engineering change and it fixes most of the vocabulary problem.

**Normalise the vocabulary.** A synonym map across the common ways the same weakness class is named, applied at index and query time. Unglamorous, cheap, and it would immediately catch a large share of the currently-missed pairs.

**Surface candidates automatically, always.** The analyst should never have to remember to search. Possible duplicates presented alongside every submission, ranked, with the matching evidence visible — which also means the analyst sees candidates they would not have thought to look for.

**Show the researcher the match.** When a duplicate is claimed, show the timestamp and enough redacted detail to verify it. This converts an unverifiable assertion into an evidenced one, and it is the single change that would most reduce duplicate disputes.

**Search across the programme's full history, not the recent queue.** A finding reported two years ago and never fixed is still a duplicate, and search interfaces that default to recent submissions miss exactly those.

## Who Feels the Pain

The researcher told their week produced a duplicate, on the basis of a search whose reliability nobody has measured, with no evidence shown.

The analyst, whose duplicate detection rate depends on personal recall and search instinct, and who has no way to know what they are missing.

The programme, paying twice for findings whose duplication was never detected, and paying for the analyst time spent re-triaging them.

And the platform, whose most common researcher grievance rests on a mechanism that is weaker than either side assumes.

## Impact If Fixed

Measuring the miss rate once would reveal the size of a problem currently assumed to be small because it is invisible.

Vocabulary normalisation and attribute-based indexing are cheap engineering changes that would catch most of the currently-missed pairs without any machine learning at all.

And showing the researcher the matching evidence turns the industry's most common dispute from an assertion into a verifiable claim, at essentially no cost to any honest programme.
