# Build: Score Reports That Prevent Over-Reading

**Niche:** [[niches/talent-assessment-platforms/score-interpretation/profile|Score Interpretation by Hiring Managers]]
**Industry:** [[industries/talent-assessment-platforms|Talent Assessment Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Report the score with its measurement error, show what it cannot distinguish, and build guardrails that stop the decision the instrument does not support.
**Tags:** #confidence-intervals #bayesian-inference #evaluation-metrics #hypothesis-testing #descriptive-statistics #compliance #worker-facing #workflow-orchestration
**Contested on:** Whether a vendor will present their score in a way that makes its limits obvious.

## The Problem

A score report shows a number, a percentile and a band. Nothing on it indicates how precise the estimate is, and every instrument has a standard error of measurement large enough that adjacent candidates are indistinguishable.

The consequence is a decision the instrument cannot support. A recruiter sorts by score and interviews the top of the list, which is defensible if the differences are real and arbitrary if they are not. A hiring manager rejects a candidate one point below a band boundary. Two candidates three percentile points apart are described as a clear difference.

Every vendor knows the standard error of their instrument. Almost none puts it on the report, because a number with visible uncertainty looks less useful than one without.

## Why Nobody Has Built This

A confident-looking score sells. A report saying "this candidate scores 61st percentile, and we cannot distinguish them from anyone between the 48th and 74th" is a harder product to demo, even though it is what the instrument actually supports.

Buyers also want a number to sort on, and a vendor who provides a less sortable output loses to one who does not. This is a coordination problem: the honest presentation is competitively disadvantaged unless everyone adopts it or a standard requires it.

And the interpretation training that would substitute for better presentation reaches almost nobody — recruiters are busy, turnover is high, and a training module is not how a hiring decision gets made at four in the afternoon.

## What to Build

A report designed around what the score can support.

**Show the interval, prominently.** The score with its standard error of measurement rendered visually, so the range is the primary object rather than the point. Once a recruiter sees two candidates' intervals overlapping almost completely, they stop treating the difference as real.

**Say what it cannot distinguish.** A plain sentence: this instrument cannot reliably distinguish candidates within about fifteen percentile points. That single line prevents most of the over-reading and every vendor can write it from their own technical data.

**Band deliberately and make the boundary soft.** If the instrument supports three bands, report three bands rather than a percentile that invites finer distinctions. And flag candidates near a boundary as such rather than assigning them cleanly to a side.

**Build guardrails into the workflow.** Warn when a list is being sorted by score for a decision the instrument does not support. Warn when the score is being used for a role outside its validated range. Warn when a rejection is being made on a score alone below a defined stakes threshold. These are product decisions and they are where behaviour actually changes.

**Give guidance on combining the score with other evidence.** The common error is treating the assessment and the interview as independent when they measure overlapping things, which double-counts. Structured guidance on weighting — and, better, a structured interview designed to cover what the assessment does not — is the highest-value interpretation support and is almost never provided.

**Report what the score means in outcome terms.** "Candidates in this band have historically been rated above average at this employer at a rate of X" is far more interpretable than a percentile, and it is available once local validation exists — which is the connection between this niche and the validity work.

## Target Customer

Vendors willing to differentiate on honesty, and large employers' assessment functions, who carry the legal exposure when a score is used in a way the instrument does not support. Regulatory pressure is also relevant here: an employer asked to justify a rejection wants a record showing the score was used appropriately.

## Impact If Built

The score gets used for the distinctions it can actually support, which is the difference between a valid instrument and a valid decision. Band boundaries stop being cliffs. And the combination of assessment and interview — where most practical error occurs — gets structured guidance for the first time.
