# Activity Monitoring That Measures Motion

**Industry:** [[remote-work-infrastructure|Remote Work Infrastructure]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Keystroke counts, periodic screenshots and idle detection measure whether someone is moving, which is not the same as whether they are working, and the deployment has grown faster than the evidence for it.
**Tags:** #gradient-boosting #time-series-forecasting #confidence-intervals #hypothesis-testing #causal-inference #evaluation-metrics #compliance #worker-facing

## The Problem
Workforce monitoring grew substantially with remote work. Products capture keystroke and mouse activity, take periodic screenshots, log application and website usage, detect idle time, and produce productivity scores from these signals. They are widely deployed, particularly over contractors and offshore teams where the trust deficit is largest.

What they measure is motion. A developer thinking about a problem registers as idle; a person reading documentation registers as low activity; a meeting away from the keyboard registers as absence. The signals are weakest exactly for the work that involves thinking, and strongest for work that involves typing, which inverts the value ordering.

The behavioural response is well documented and predictable: mouse jigglers, activity padding, and the ordinary human response to being measured on a proxy, which is to optimise the proxy. Monitoring therefore produces both a distorted measurement and a distorted working pattern.

The evidence base is thin in one direction and better in the other. Demonstrations that monitoring improves output are scarce and contested; associations between surveillance intensity, reduced trust, stress and turnover are better established in the organisational research literature. Legal constraints vary considerably — several jurisdictions require notice, consent or works council agreement, and some restrict screenshot capture outright.

## What Already Exists
Hubstaff, Time Doctor, ActivTrak, Teramind, Insightful and others provide activity monitoring with varying intensity. Time tracking with proof-of-work screenshots is standard on several freelance platforms. Endpoint management tools have overlapping capability. Some vendors have deliberately moved toward output-oriented reporting and away from keystroke-level capture. Privacy regulation in several jurisdictions constrains what may be collected and requires disclosure.

## The Customisation Gap
Output measurement is the alternative and is domain-specific, which is why generic monitoring persists. For software work, delivery flow metrics; for support, resolution and repeat contact; for sales, pipeline progression; for creative work, delivery against agreed scope. Each requires integration with the systems where the work actually lands, and each is a far better signal than keystroke counts — which is precisely why building it is harder and why the generic proxy wins.

The evaluation that is not done is whether monitoring works. An organisation deploying it could compare outcomes across teams with and without it, and the fact that this is essentially never run — despite being straightforward — suggests the deployment is driven by trust deficit rather than by evidence.

Proportionality should be designed rather than defaulted. Collecting the minimum signal necessary for the stated purpose, with retention limits, aggregate rather than individual reporting where possible, and worker visibility of their own data, is both better practice and closer to what several jurisdictions require.

And the trust-deficit root cause deserves naming. Monitoring is usually deployed because a manager cannot see what a distributed team is doing, and the durable fix is work visibility through the systems where work happens rather than surveillance of the person doing it.

## Impact If Solved
Monitoring is deployed widely on an evidence base that does not support it, measures a proxy that inverts the value of thinking work, and is associated with the trust and attrition damage that remote arrangements can least afford. Output-based measurement through the systems where work lands is the substantive alternative, actually evaluating whether monitoring improves anything is a straightforward study nobody runs, and proportionate collection with worker visibility is both better practice and increasingly a legal requirement.
