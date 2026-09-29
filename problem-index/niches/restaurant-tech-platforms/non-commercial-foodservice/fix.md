# The Allergen Managed by a Warning

**Niche:** [[niches/restaurant-tech-platforms/non-commercial-foodservice/profile|Non-Commercial Foodservice]]
**Industry:** [[industries/restaurant-tech-platforms|Restaurant Tech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A student or patient with a documented food allergy is protected by a flag that appears on a screen at the point of service, which is the last possible moment and the wrong place, because the decision that matters was made when the tray was assembled.
**Tags:** #evaluation-metrics #descriptive-statistics #hypothesis-testing #compliance #workflow-orchestration #automation #worker-facing #quick-win
**Contested on:** Every serious competitor in institutional foodservice software is fighting to produce a cycle menu that satisfies the nutrition regulation, the allergen safety requirement and the per-meal budget simultaneously — and whoever generates a compliant menu people will actually eat takes the account.

## The Problem
A district has a documented peanut allergy on file for a student. The system flags the account at the register. By the time the flag appears, the student is holding a tray they assembled from a line, and the cashier's job is to notice a warning and intervene in front of a queue. In a hospital, a therapeutic diet order arrives and the tray line assembles from a ticket, with the check being that the ticket was read correctly. In both cases the control is a human noticing something at the last step, and the earlier steps — what was offered, what the student could reach, what was on the line — were designed without reference to the restriction at all.

## Why It's Still Broken
Allergen data lives in a student or patient record and the menu lives in a foodservice system, and the two are joined at the point of sale because that is where both happen to be present. Moving the control upstream means the menu planning and production systems have to know about individual restrictions, which crosses a data boundary that is partly a privacy question and partly just an integration nobody built. There is also a liability posture that favours warnings: a flag at the register is a documented control, and documented controls are what an incident review looks for, even when an upstream design change would prevent more incidents than a warning catches.

## What a Fix Looks Like
Move the control upstream and measure how often the downstream one fires. Menu planning should know the aggregate restriction profile of the population it serves, so that every service period offers a safe, appealing option for each significant restriction by design rather than by substitution request — which is both safer and far better for the child, who otherwise eats something visibly different. Production and tray assembly should carry the restriction as a constraint on what is assembled, not as a warning to be read. Keep the point-of-service check as the last line of defence and instrument it: how often does the flag fire, how often does an intervention actually occur, how often is a restricted item already on the tray. That last number is the measurement of how well the upstream design is working and no institution currently has it.

## Who Feels the Pain
Cashiers asked to be the safety control in front of a queue; parents trusting a system whose protection is a screen prompt; and students who eat a substitute in front of their classmates because the menu was not designed for them.

## Impact If Fixed
Designing the offer around the population's restrictions prevents the incident rather than catching it, and it removes the daily social cost borne by the children the system is protecting. Instrumenting how often the last-line check actually fires is free and is the evidence that determines whether the upstream work is needed — which every institution should want and none currently collects.
