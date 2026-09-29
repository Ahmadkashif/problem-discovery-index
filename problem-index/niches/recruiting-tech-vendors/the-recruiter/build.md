# Build: Hire Outcomes, Delay Attribution and Difficulty-Weighted Load

**Niche:** [[niches/recruiting-tech-vendors/the-recruiter/profile|The Recruiter]]
**Industry:** [[industries/recruiting-tech-vendors|Recruiting Tech Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Show recruiters how their hires turned out, attribute pipeline delay to whoever caused it, and allocate requisitions by difficulty rather than by count.
**Tags:** #survival-analysis #gradient-boosting #confidence-intervals #evaluation-metrics #descriptive-statistics #causal-inference #worker-facing #data-integration
**Contested on:** Whether hire quality can be attributed to a recruiter at all given everything else that determines it.

## The Problem

A recruiter fills a role and never learns anything about it. Whether the hire stayed, performed, was promoted or was let go in four months is in the HR system and is not shown to the person who found them.

So the feedback loop that would make a recruiter better does not exist. A recruiter with ten years of experience has ten years of time-to-fill numbers and no evidence about which of their judgements were good.

Two other measurement failures compound it. Delay caused by a manager taking three weeks to review a shortlist lands in the recruiter's time-to-fill, undifferentiated. And requisitions are allocated by count, so a recruiter carrying five impossible roles and one carrying five easy ones are treated as equally loaded.

## Why Nobody Has Built This

Hire outcome attribution is genuinely contested. Whether a hire succeeded depends on the manager, the team, the onboarding and the role, and attributing it to the recruiter who screened them is unfair in both directions.

That argues for reporting outcomes without ranking on them, which is a distinction the industry has not made — so it reports nothing, and the recruiter learns nothing at all.

Delay attribution is straightforward and is not built because time to fill is a single headline number that leadership likes and nobody has asked to decompose. And requisition difficulty is unmodelled because nobody has framed load allocation as anything other than a count.

## What to Build

Three measurements, each modest and each absent.

**Show hire outcomes to the recruiter.** Tenure, performance ratings, progression and voluntary versus involuntary exit for the people they hired, as a personal view, with peer distributions for context. Presented as learning rather than as a ranking — which is both the fairer framing and the one that gets it built, because the objection to ranking is legitimate and the objection to showing someone their own results is not.

**Decompose time to fill by who held it.** Days waiting on the recruiter, on the hiring manager, on scheduling, on the candidate, on approvals. Every transition is timestamped and the decomposition is a query. This single report changes the conversation about every ageing requisition, because in most cases the largest block is manager review.

**Model requisition difficulty.** From role, level, location, compensation against market, requirement count and restrictiveness, historical fill time for comparable roles, and the size of the qualified pool. A difficulty score allows load to be allocated by weight rather than by count, and allows time to fill to be assessed against an expectation rather than a flat target.

**Warn early on a requisition heading for trouble.** Low application rate, poor pass rate at screen, manager unresponsiveness, offer declines — each predicts a failing requisition weeks before it is obviously failing, and an early conversation about compensation, requirements or process is far more effective than a late one.

**Build the recruiter's own record.** Roles filled by family and level, time to fill against difficulty, offer acceptance, hire tenure and outcomes — owned by the recruiter, portable. This is a profession with high mobility and no professional record.

**Fix the metric set.** Time to fill adjusted for difficulty and attributed by delay-holder, alongside quality of hire and candidate experience. A single unadjusted speed number produces exactly the screening behaviour the industry complains about.

## Target Customer

Recruiting leadership at organisations where recruiter turnover and manager friction are chronic, which is most of them. Also ATS vendors, for whom delay attribution is a query they could ship tomorrow and which would immediately become the most-used report in the product.

## Impact If Built

Recruiters find out how their hires turned out, which is the feedback that turns experience into skill and which the profession currently lacks entirely. Delay lands on whoever caused it, which changes every conversation about an ageing requisition. And load gets allocated by difficulty, which is the difference between a manageable desk and an impossible one.
