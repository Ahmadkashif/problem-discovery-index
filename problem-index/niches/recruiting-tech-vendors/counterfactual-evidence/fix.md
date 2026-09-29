# Fix: The Natural Experiments Already Happened and Nobody Analysed Them

**Niche:** [[niches/recruiting-tech-vendors/counterfactual-evidence/profile|Counterfactual Evidence]]
**Industry:** [[industries/recruiting-tech-vendors|Recruiting Tech Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Requirements were relaxed during a hiring surge, thresholds were dropped to fill a role, exceptions were made — and the outcomes of those hires were never compared to anything.
**Tags:** #causal-inference #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #survival-analysis #quick-win #data-integration
**Contested on:** Whether the employer will analyse the exceptions it has already made.

## The Problem

Every large employer has already run the experiment, repeatedly, without recording it as one.

A hiring surge forced requirements to be relaxed for a quarter. A role that would not fill had its degree requirement dropped. A hiring manager insisted on a candidate the screen rejected. A referral bypassed the filter. A location expansion brought in a cohort screened against different criteria. An acquisition brought in people nobody screened at all.

Each of these produced hires who would not have passed the standard screen, working alongside those who did, with performance and tenure outcomes for both sitting in the HR system. That is quasi-experimental evidence about screening validity, generated repeatedly at every employer, and analysed by none.

## Why It's Still Broken

The exceptions were not recorded as exceptions. A hire who bypassed the screen looks identical in the HRIS to one who passed it, because the reason was a conversation rather than a field.

Nobody has framed these events as evidence. They are remembered as operational compromises — the quarter when we had to lower the bar — and the memory carries an assumption about how those hires turned out that has never been checked.

And the analysis requires linking hiring-route data to performance, which is the same join that nobody makes for any other purpose here.

## What a Fix Looks Like

Find the exceptions, label them retrospectively, and compare.

Identify the natural experiments from the records. Periods when a requirement was relaxed, requisitions where a threshold was lowered, hires flagged as manager overrides, referral hires who bypassed screening, cohorts from an acquisition or a location expansion. Most are reconstructable from requisition history, offer records and hiring notes.

Label them going forward with a field. Screening route — standard, exception, override, referral bypass, relaxed requirement — recorded at hire, which makes every future analysis a query rather than an archaeology project.

Compare the outcomes. Performance, tenure, progression and termination for exception hires against standard hires, controlling for role and cohort. The comparison is confounded — exceptions were made for reasons — and it is far more informative than the assumption currently standing in for it.

Look hardest at the relaxed-requirement periods, which are the cleanest quasi-experiment available. A quarter when the degree requirement was dropped produces a cohort selected on everything except that requirement, and comparing them to adjacent cohorts is the closest thing to evidence most employers can obtain without any new intervention.

Run the discontinuity analysis on the threshold. Candidates just above and just below a numeric screening cut are similar in everything except the cut, and comparing the outcomes of the just-above group across periods when the cut moved is a real design available on historical data.

And report the results internally regardless of what they say, which is the part that determines whether the exercise is worth running.

## Who Feels the Pain

Candidates screened out by requirements the employer has already, repeatedly, waived without consequence — and has never noticed. Recruiting leaders defending requirements they have no evidence for against hiring managers who want them relaxed. And the organisation, which has run the experiment several times and filed the results as anecdotes.

## Impact If Fixed

The evidence that already exists gets analysed, at the cost of a retrospective labelling exercise and a query. Relaxed-requirement periods become the quasi-experiments they were. And the requirements that have been waived repeatedly without consequence get identified as the ones to drop permanently.
