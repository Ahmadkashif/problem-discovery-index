# Fix: They Reported It and Heard Nothing

**Niche:** Employee Report Triage
**Industry:** [[industries/security-awareness-training|Security Awareness Training]]
**Type:** Fix (Pain Point)
**One-liner:** The programme asks people to report suspicious messages, they do, and the silence that follows teaches them not to bother.
**Tags:** #evaluation-metrics #confidence-intervals #worker-facing #workflow-orchestration #automation #descriptive-statistics
**Contested on:** Whether the reporting stream the programme creates is handled as a detection source or dumped on a security team that never asked for it.

## The Problem

An employee receives a message that looks wrong. They hesitate, decide to do the right thing, and report it.

Nothing happens. No acknowledgement, or an automated receipt with no content. No indication of whether it was a real threat. No thanks. The message disappears into a queue and the person never hears anything again.

They report the next one too. And the one after. Then they stop, because reporting costs them a minute and returns nothing, and because after several reports with no response the reasonable conclusion is that nobody is reading them.

This is the programme's central behavioural objective being extinguished by its own operations. Every awareness campaign asks people to report. The response to a report determines whether they keep doing it. And the response is frequently silence, because the queue is handled by a team measured on detection and response rather than on the reporter's experience.

The cost is larger than it appears. The reports that matter most are the novel campaigns that got past automated defences, which is exactly the category employee reporting is best at catching — and the people who would catch them have stopped looking.

## Why It's Still Broken

**Acknowledgement is nobody's objective.** Operations is measured on alerts handled, not on reporters retained.

**The volume makes individual response seem impractical.** Hundreds of reports a week, so responding to each feels impossible — though most of the responses are templated and automatic.

**The awareness function does not own the response.** They asked people to report; somebody else receives the reports.

**Telling people the outcome feels like disclosure.** Confirming that a report was a real threat can seem like sharing security information, which is over-cautious for a message the person already received.

**Nobody measures reporting attrition.** Whether individual reporting rates decline after unacknowledged reports is not tracked, so the extinction is invisible.

**The report button feels like it completes the loop.** Having a button creates the impression that reporting is handled, which reduces attention to what happens afterwards.

## What a Fix Looks Like

**Acknowledge every report within seconds.** Automatic, immediate, with a genuine message rather than a receipt. This is the single most important thing in this niche and it is a templated email.

**Close the loop on the outcome.** Tell the reporter what it turned out to be — a real phishing attempt, a legitimate message, the organisation's own simulation. Templated, automatic for the mechanical categories, and it is what makes the next report happen.

**Tell them when it mattered.** Where a report led to a block, a takedown or protection of colleagues, say so. This is the strongest possible reinforcement and costs a sentence.

**Handle simulation reports positively and instantly.** Someone reporting the organisation's own campaign did exactly what was asked, and should receive immediate confirmation of that rather than silence.

**Track individual reporting rates over time.** Whether people who report stop reporting is directly measurable and would reveal the extinction currently happening invisibly.

**Never make reporting feel risky.** Someone reporting a message they already clicked should be thanked, not investigated. The person who clicked and reports is the best outcome available and the current experience frequently discourages it.

**Give the awareness function visibility of the queue.** They created the behaviour and have no view of what happens to it, which means they cannot advocate for the response their programme depends on.

## Who Feels the Pain

The employee, who did the right thing repeatedly, heard nothing, and reasonably concluded it was pointless.

The security team, receiving fewer reports over time from a workforce that has learned reporting is a void, and losing a detection source they never valued.

The awareness manager, whose programme's central behavioural objective is undermined by an operational queue they do not control.

And the organisation, whose best defence against the phishing that gets past its filters is people who have stopped looking.

## Impact If Fixed

Immediate automated acknowledgement is a templated email and is the difference between a reporting behaviour that persists and one that decays.

Telling people the outcome, especially when it mattered, is the strongest reinforcement available and costs a sentence per report.

And tracking individual reporting rates over time would reveal an extinction that is currently happening in every organisation running one of these programmes and that nobody has ever measured.
