# Fix: Nobody Has Shown That the Score Predicts Anything

**Niche:** [[niches/remote-work-infrastructure/workforce-monitoring/profile|Workforce Monitoring]]
**Industry:** [[industries/remote-work-infrastructure|Remote Work Infrastructure]]
**Type:** Fix (Pain Point)
**One-liner:** The productivity score is on every dashboard and no vendor or employer has ever published evidence that it correlates with anything an employer cares about.
**Tags:** #hypothesis-testing #confidence-intervals #evaluation-metrics #descriptive-statistics #causal-inference #compliance #quick-win #worker-facing
**Contested on:** Whether anyone will test the score against an outcome.

## The Problem

Monitoring products compute a productivity score from activity — active time, application categories, keystroke and mouse rates, idle periods. It appears on a dashboard, managers look at it, and in some organisations it informs performance conversations and occasionally employment decisions.

Nobody has established that it means anything. The vendors publish no validation. The employers deploying it run no study. And the score's construction gives ample reason for doubt: it is defeated by a cheap device, it penalises reading and thinking, it varies by role and tooling more than by contribution, and the application categorisation that drives much of it is a vendor's guess about which software is productive.

The test is available. Score against manager assessment, against team delivery, against outcomes the organisation already measures, on the employer's own population. It is a correlation on data they already have.

## Why It's Still Broken

Testing it risks the answer. An employer who establishes that the score predicts nothing has spent money on a tool, has subjected their workforce to it, and has to explain both.

The vendors have a clearer interest still: a validation study is the one piece of evidence that could end the category, and none has reason to produce it.

And the score is used partly for reassurance rather than for information, and a reassurance instrument does not need to be valid to serve its purpose.

## What a Fix Looks Like

Run the correlation. It is an afternoon on data the employer already holds.

Correlate the score against whatever the organisation already measures — manager performance ratings, team delivery metrics, peer assessment, objective output where it exists. Report the coefficient with an interval, by role and function. If the correlation is meaningful, the tool is doing something and the employer knows it; if it is not, they have learned the most important fact about a tool they are using on people.

Check the obvious confounds before concluding anything. Role, tooling, seniority and work type drive activity patterns heavily, and an uncontrolled correlation will be dominated by them.

Look for the score's failure cases specifically. The highest-rated performers with low scores, and the reverse. These will be identifiable individuals and the pattern among them is usually immediately explanatory — the senior person who spends their day in meetings and thinking, the engineer reading code.

Measure what it costs. Attrition, engagement and trust measures before and after deployment, and among monitored versus unmonitored groups where any exist. The evidence that monitoring damages trust and correlates with attrition is better established than the evidence that it helps, and an employer can check it on their own population.

Ask the workers. Whether they alter their behaviour to satisfy the tool, and how. The answers are consistent and unflattering and they are the clearest evidence of what is actually being measured.

And publish the finding internally regardless. If the score works, that is worth knowing; if it does not, continuing to use it after establishing that is a different thing from using it in ignorance.

## Who Feels the Pain

Workers, evaluated on a number nobody has shown means anything, and adjusting their behaviour to satisfy it rather than to do the work. Managers, given a metric with apparent authority and no guidance about its validity. Employers, spending money and trust on an unvalidated instrument. And the platforms, who are the legal employer in jurisdictions where an unjustified monitoring deployment is itself unlawful.

## Impact If Fixed

The score gets tested against an outcome the organisation already measures, which is an afternoon's work and is the single most consequential unknown about a tool applied to an entire workforce. The failure cases become visible and usually explain themselves. And the cost side — attrition and trust — gets measured alongside, which is the comparison the deployment decision should always have been made on.
