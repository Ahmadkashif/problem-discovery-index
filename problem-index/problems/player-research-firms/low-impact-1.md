# Recruiting Participants Who Represent the Players

**Industry:** [[player-research-firms|Player Research Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Findings are generalised from whoever answered the screener and turned up, and the people who do that are systematically not the people the game is for.
**Tags:** #gradient-boosting #logistic-regression #bayesian-inference #confidence-intervals #k-means-clustering #hypothesis-testing #evaluation-metrics #feature-engineering

## The Problem
Every study generalises from its participants, and participant selection in games research is weaker than the methodological care applied elsewhere in the process. Recruitment runs through panels, screeners and incentives, and the population that reaches a session is filtered several times: people who joined a research panel, who saw the invitation, who passed the screener, who were available, and who showed up.

Screener misreporting is a known and unmeasured problem. Participants who want the incentive answer the qualifying questions in the way that qualifies them, which means a study of experienced strategy players contains people who have played one, and researchers frequently identify this during the session rather than before it.

The representativeness question is harder than a demographic quota. What matters for most research questions is prior experience with the genre, with the specific control conventions, with the platform, and the player's motivations — and those are poorly captured by the demographic screening most recruitment is built around.

Professional participants are the accumulating version of the problem. Panel members who take many studies become unrepresentative through practice at being researched: they know what a think-aloud is, they anticipate what the moderator wants, and they perform.

## What Already Exists
Playtesting platforms maintain large recruited panels with screening and scheduling, and have made remote unmoderated testing far cheaper than lab work. General research panels supply participants for surveys and sessions. Studios recruit from their own player base for some studies, which solves representativeness for existing players and not for prospective ones. Screening instruments are standard practice. Some platforms track participation frequency and cap it.

## The Customisation Gap
The screening question is a classification problem nobody treats as one. Whether a participant actually has the claimed experience is checkable — from behaviour in a short pre-task, from response patterns in the screener itself, from their history on the panel — and treating screener honesty as something to model rather than to trust would remove a known source of contamination cheaply.

The representativeness measurement is the second gap. A study should be able to state how its participants compare to the target population on the dimensions that matter for its question — genre experience, platform familiarity, motivation profile — and weight or caveat accordingly. Currently that comparison is rarely made because the target population's distribution on those dimensions is not known either, though telemetry from the live game contains it.

Matching to the research question is the third. A study about first-time comprehension needs genuine newcomers, a study about late-game progression needs experienced players, and a general panel serves both badly. Constructing the panel for the question rather than drawing from a general pool is what would most improve the quality of findings.

And practice effects need tracking. Participation history is recorded by platforms and rarely used to exclude or adjust for over-researched participants.

## Impact If Solved
Every finding in this field rests on a participant sample whose relationship to the real player population is asserted rather than measured. Modelling screener honesty, measuring representativeness on dimensions that matter for the question, and constructing panels per question rather than drawing from a pool would raise the validity of findings across the discipline — and would let a firm state, for the first time, how far a result should be expected to generalise.
