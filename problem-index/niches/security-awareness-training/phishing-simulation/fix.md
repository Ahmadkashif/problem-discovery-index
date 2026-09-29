# Fix: The Click Rate Fell and Nobody Knows Why

**Niche:** Phishing Simulation
**Industry:** [[industries/security-awareness-training|Security Awareness Training]]
**Type:** Fix (Pain Point)
**One-liner:** The number improved, the programme is declared effective, and the improvement is equally consistent with the tests having got easier.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #descriptive-statistics #compliance #revenue-impact
**Contested on:** Whether the simulation is a measuring instrument or a number the vendor and customer jointly produce.

## The Problem

The annual review shows the click rate down from twenty-eight per cent to five. The programme is working.

Several things would produce that chart and only one of them is learning. The campaigns may have drifted toward more recognisable templates, because the ones that caused complaints were retired. The sender infrastructure may be whitelisted, so simulated messages arrive with different characteristics from real ones. Employees may have learned to recognise the simulation platform's landing pages, its link format, or the fact that simulations arrive on Tuesdays. The population may have shifted. Or difficulty may simply have been reduced without anyone deciding to.

Nobody is fabricating anything. Campaign design decisions accumulate, each reasonable, and the aggregate effect on difficulty is never tracked because difficulty is not a measured quantity.

So the chart that justifies the programme is uninterpretable, and the organisation's belief that its workforce has become resistant to phishing rests on an improvement in a test it controls.

## Why It's Still Broken

**Difficulty is not measured, so drift is invisible.** Without a difficulty parameter there is no way to notice that the average difficulty of campaigns has fallen.

**Every party benefits from the improving number.** The vendor renews, the programme owner reports success, and leadership has evidence of a control working.

**Harder campaigns generate complaints.** Each complaint pushes design toward safer templates, which is a reasonable response and produces exactly the difficulty drift nobody tracks.

**Recognition is a form of learning that does not transfer.** Employees learning to spot the simulation platform will show improving numbers and no improvement in resistance to a real attack.

**Benchmarks make it look normal.** Published industry click rates show similar trends everywhere, which reads as validation rather than as evidence that everyone's tests drift the same way.

**Nobody anchors to the real threat.** The organisation's gateway records the phishing it actually receives, and the simulation programme has never been compared against it.

## What a Fix Looks Like

**Track campaign difficulty explicitly, however crudely.** Even a structured rubric — sender plausibility, pretext specificity, visual fidelity, urgency, personalisation — applied consistently, would reveal drift. This costs a form and is the minimum viable fix.

**Hold a fixed anchor set.** A small set of templates of known composition, run periodically and unchanged, whose click rate over time is a drift-free measure. This is a standard equating device in testing and costs almost nothing.

**Compare simulation to real received phishing.** Sample what the gateway caught, characterise its sophistication, and check whether campaigns resemble it. A programme testing against easier material than the organisation actually receives should know that.

**Watch for platform recognition.** Vary sender infrastructure, landing page design, timing and link patterns. An improving click rate accompanied by falling report rates for real phishing is a recognition signal rather than a learning one.

**Report the reporting rate alongside the click rate.** Reporting is a positive behaviour, is harder to produce by making tests easier, and is the response that actually helps.

**Ask whether the trend holds under a harder campaign.** A programme confident in its results can test the claim directly, once a year, with a campaign at genuinely realistic difficulty — and should expect the number to jump.

**Separate operational reporting from the assurance claim.** Click rate is useful for running the programme. Presenting it upward as evidence of workforce resistance is the claim that needs the calibration.

## Who Feels the Pain

The organisation, which believes its workforce is resistant to phishing on the basis of a trend in a test it controls.

The security leader, presenting a number to a board as evidence of a control's effectiveness with no way to know if it means anything.

The awareness manager, who frequently suspects the drift and has no measurement to demonstrate it or to argue against making campaigns easier.

And the insurer or auditor treating a low click rate as evidence of a functioning control, which is a claim nobody has substantiated.

## Impact If Fixed

A fixed anchor set run periodically costs almost nothing and would immediately separate real improvement from difficulty drift — it is the cheapest measurement fix available in this category.

Comparing campaign difficulty against the organisation's actually-received phishing would tell a programme whether it is testing against the real threat or against a template library.

And reporting the reporting rate alongside the click rate shifts attention to the behaviour that actually helps, which is both a better metric and considerably harder to improve by accident.
