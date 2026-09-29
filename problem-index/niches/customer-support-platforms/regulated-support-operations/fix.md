# Quality Assurance by Sample When Every Conversation Is Available

**Niche:** [[niches/customer-support-platforms/regulated-support-operations/profile|Regulated Support Operations]]
**Industry:** [[industries/customer-support-platforms|Customer Support Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Support quality assurance reviews a few conversations per agent per month against a scorecard, produces a number that cannot distinguish an agent from noise, and leaves the overwhelming majority of conversations unexamined.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #bert #compliance #worker-facing #quick-win
**Contested on:** Every serious competitor in regulated support is fighting to let an organisation answer with verified accuracy in a domain where being wrong is a compliance event — and whoever makes an automated answer defensible takes the account.

## The Problem
A quality assurance team reviews four conversations per agent per month against a twenty-point scorecard. Four conversations out of several hundred is a sample so small that the resulting score is dominated by which conversations happened to be selected, yet it is used in performance reviews, in coaching and occasionally in pay. Meanwhile the compliance purpose — establishing that disclosures were given and boundaries respected across the whole population — is entirely unserved by a sample of that size, and the conversations most likely to contain a problem are no more likely to be selected than any other.

## Why It's Still Broken
Sampling was the only option when review required a human listening to a recording, and the cadence was set by reviewer capacity. It has persisted through the arrival of transcription and automated analysis because the scorecard, the process and the reviewer team are institutionally established. And the statistical inadequacy is rarely confronted: a manager presented with an agent's quality score of 87% does not usually ask what the confidence interval is on four observations, and the answer would make the number unusable.

## What a Fix Looks Like
Review everything for the things that can be checked automatically, and target human review where it adds judgement. Disclosure delivery, required process steps, prohibited statements, complaint indicators and boundary adherence are checkable across every conversation, which converts the compliance purpose from a sample to full coverage. Human review is then reserved for the dimensions that require judgement — empathy, appropriateness, handling of a difficult situation — and is targeted at conversations flagged as unusual or risky rather than selected at random, which makes each review worth more. Report agent-level scores with their uncertainty, and stop reporting them at all where the sample cannot support a conclusion, which is most of the time — this is the honest correction and it protects agents from being evaluated on noise. And use the full-coverage results at the population level, where they are statistically meaningful, to identify process and content problems rather than individual ones, since a disclosure omitted by forty agents is a script problem and not forty performance problems.

## Who Feels the Pain
Agents evaluated on a sample too small to mean anything; compliance functions asserting oversight from a fraction of a percent of conversations; and customers in the conversations nobody reviewed.

## Impact If Fixed
Automated full-coverage checking of the objective requirements is now inexpensive and transforms the compliance assurance from a sample to a census. Reporting agent scores with their uncertainty — and withholding them when the sample is inadequate — is the fairness correction, and the population-level view reliably shows that most apparent individual failures are process failures.
