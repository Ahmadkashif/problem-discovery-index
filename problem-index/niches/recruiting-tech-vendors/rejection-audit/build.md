# Build: Blind Re-Review of Rejected Applications

**Niche:** [[niches/recruiting-tech-vendors/rejection-audit/profile|Rejection Audit]]
**Industry:** [[industries/recruiting-tech-vendors|Recruiting Tech Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Sample rejected applications, re-review them blind against the stated requirements, and report how often the process disagrees with itself.
**Tags:** #hypothesis-testing #confidence-intervals #evaluation-metrics #descriptive-statistics #cross-validation #large-language-models #compliance #bayesian-inference
**Contested on:** Whether an employer will measure how often its own screening is wrong.

## The Problem

Screening rejects the large majority of applicants and nobody checks any of them. There is no sampling, no re-review, no reliability statistic — the least examined high-volume decision process in any large organisation.

Where anyone has looked, the inconsistency is substantial. The same application reviewed twice produces different outcomes at a rate that would be considered a crisis in any other quality-controlled process, because screening is fast, subjective, done under volume pressure against requirements that are frequently vague.

The measurement is available. Rejected applications are retained. Reviewers exist. The requirements are written down. The only missing thing is the decision to look.

## Why Nobody Has Built This

The finding is uncomfortable and creates an obligation. An employer who learns that a fifth of their rejections are overturned on re-review knows they are discarding candidates they wanted, and knows it in writing — which is discoverable and which raises the question of what happens to the people already rejected.

There is no requirement to do it, no vendor ships it, and no metric in any recruiting function points at it. Time to fill, cost per hire, offer acceptance and source effectiveness are the standard measures and none is a quality measure of the screen.

And the reviewers' time is a real cost in a function that is chronically under-resourced.

## What to Build

An audit capability that runs continuously at low cost.

**Sample stratified, not randomly.** Rejections near a threshold, rejections by automated screen, rejections by particular reviewers, rejections in roles with poor fill rates. Random sampling wastes effort on the obvious cases; stratified sampling concentrates on where errors are likely.

**Blind the re-review properly.** Strip name, contact details, institution names, dates that reveal age, and anything identifying the original reviewer or outcome. The re-reviewer sees the application and the stated requirements and nothing else. Blinding is what makes the result mean something and it is straightforward redaction.

**Use multiple reviewers per sampled application.** Two or three independent verdicts gives an agreement statistic as well as a comparison to the original, which separates "the original reviewer was wrong" from "this application is genuinely ambiguous" — and the second finding points at the requirements rather than the reviewer.

**Report the reversal rate with intervals**, by role family, by reviewer, by automated versus human screen, by stage. The headline number is the share of rejections overturned; the breakdowns are what get acted on.

**Use a model as a third reviewer, carefully.** A generative re-review against the stated requirements, with reasoning, is cheap enough to run on every rejection rather than a sample. Validated against the human re-reviews, it becomes a continuous monitor rather than a periodic audit — and its disagreements are the sampling frame for the human audit.

**Trace the reversals to their cause.** Requirements too vague, reviewer inconsistency, a keyword filter discarding equivalent experience, a knockout question catching legitimate candidates. Each is a different fix and the distribution tells the employer which one they have.

**Act on the ones you find.** A candidate whose rejection was overturned in an audit, for a role still open, should be reconsidered. Doing this is what makes the audit a process rather than a study, and it is a straightforward workflow.

## Target Customer

Employers with high application volume and roles they struggle to fill — where the hypothesis that good candidates are being discarded is already suspected. Also ATS vendors, for whom a rejection audit module is a genuine quality product in a category with none, and compliance functions facing a regulatory direction that asks how decisions were made.

## Impact If Built

The false rejection rate — the most basic quality measure of screening and currently unknown everywhere — becomes a number. Its causes get separated into vague requirements, inconsistent reviewers and bad filters, which are three different fixes. And the candidates found in the audit get reconsidered rather than filed.
