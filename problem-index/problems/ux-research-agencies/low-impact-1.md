# Participant Recruitment and Screening Fraud

**Industry:** [[ux-research-agencies|UX Research Agencies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Screening is done by self-report against people whose income depends on passing screeners, and a study's entire validity rests on whether the eight people in it were who they said they were.
**Tags:** #gradient-boosting #dbscan #graph-neural-networks #bert #k-means-clustering #evaluation-metrics #feature-engineering #compliance

## The Problem
Every study begins with recruitment: define the participant criteria, write a screener, field it to a panel, and select from those who qualify. The criteria are often demanding — a specific job role, a particular tool in use, a recent purchase — and the incentive is meaningful, frequently a hundred dollars or more for an hour.

That combination has produced a professional participant population. People who take research studies as an income stream learn what screeners are looking for, maintain multiple accounts, and answer to qualify rather than to describe themselves. Researchers report sessions where a participant claiming to be a hospital procurement director clearly is not, discovered five minutes in, with the session wasted and the slot unrecoverable.

Outright fraud sits alongside it: duplicate accounts, coordinated groups, and increasingly assisted responses in unmoderated studies where a text answer can be generated rather than written. Unmoderated testing is the most exposed, because nobody is watching.

The cost is not only wasted sessions. A study that includes two misrepresented participants out of eight has a substantially corrupted finding, and nobody knows which studies those are.

## What Already Exists
User Interviews, Respondent, Prolific and Userlytics all run identity and quality controls, and Prolific in particular has invested seriously in participant quality for academic use. Panel providers maintain their own verification. Attention checks and trap questions are standard screener practice. Some platforms verify employment through professional network linkage. Payment and identity verification vendors are used at the account level.

## The Customisation Gap
Screening tests what someone says; validity depends on what is true, and the signals that distinguish them are behavioural and relational rather than declarative. Response timing, answer patterns across a participant's history, the consistency of claimed attributes across studies, device and network characteristics, and the relationship structure between accounts all carry information that a screener does not — and the platform holds all of it while the agency holds none.

The second gap is that fraud detection here needs to protect participants as much as it filters them. Wrongly excluding a legitimate participant removes a real income source from someone, often someone who needs it, on the basis of an algorithm they cannot see. A system that flags for review rather than silently excluding, and that offers a route to contest, is the version that is defensible — and the current practice at most panels is a quiet quality score nobody is told about.

The third is per-study customisation. What constitutes a suspicious pattern depends on the population: a screener for enterprise software buyers has a tiny qualifying population and a high incentive, which produces very different fraud economics from a consumer study. Thresholds set globally will over-filter the hard-to-recruit populations that matter most.

And unmoderated studies need response-level validity signals — assisted or generated text, contradictory answers, implausible timing — which is a different problem from account-level screening and is currently almost unaddressed.

## Impact If Solved
Participant validity is the foundation everything in this discipline rests on, and it is currently established by asking. Behavioural and relational verification at the panel level, with review rather than silent exclusion and thresholds fitted per population, protects both the study and the participants — and response-level validity checking addresses the fastest-growing gap, which is unmoderated research where nobody is watching.
