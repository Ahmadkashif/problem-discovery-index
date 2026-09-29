# Fix: Punishing the Click Teaches Silence

**Niche:** Simulation Harm & Consent
**Industry:** [[industries/security-awareness-training|Security Awareness Training]]
**Type:** Fix (Pain Point)
**One-liner:** The behaviour the organisation needs is people reporting things that look wrong, and a programme that penalises being deceived teaches them not to draw attention to themselves.
**Tags:** #evaluation-metrics #confidence-intervals #worker-facing #compliance #hypothesis-testing #revenue-impact
**Contested on:** What deliberately deceiving employees costs them, and whether the resistance the programme produces can be obtained without it.

## The Problem

An employee clicks a well-crafted simulated phishing email during a busy afternoon. They are added to a list, assigned remedial training, and in some organisations their manager is notified or their name appears in a departmental report.

The intended lesson is to be more careful. The lesson actually learned is that interacting with something that turns out to be a test has consequences, and that the security function is a party that tests you and reports the result.

That matters because of what the organisation actually needs. Technical controls stop most phishing. The residual risk is handled by a person noticing something wrong and telling somebody. Reporting is the behaviour that helps — it triggers investigation, it protects colleagues who received the same message, and it is the only thing an employee can do that a control cannot.

A programme that penalises the failure mode and does little to reward the helpful behaviour teaches people to minimise their visible interaction with security. An employee who clicks something and is unsure now has a reason to say nothing and hope. An employee who is not sure whether a message is suspicious has a reason not to raise it and risk looking foolish.

The programme's own metric does not capture any of this, because it measures clicks rather than reports.

## Why It's Still Broken

**Clicking is measurable and reporting is not, by default.** The platform records a click automatically. Reporting requires a button, integration and a process, and is frequently not the headline metric.

**Punitive measures feel like accountability.** Naming, assignment and escalation look like a serious programme to leadership, and the case that they are counterproductive is indirect.

**The behavioural effect is not measured.** Nobody tracks whether reporting rates fall after punitive measures are introduced, so the cost is invisible.

**Repeat clickers create pressure for consequences.** A small number of people click repeatedly, and the natural response is escalation — which is also the response that most damages the relationship.

**Security owns the programme and not the workforce relationship.** The function running it is not the function that carries the cost of the trust damage.

**A low click rate is what gets reported.** The metric that goes to leadership rewards the punitive approach, because fear does reduce clicking.

## What a Fix Looks Like

**Make reporting the headline metric.** Report rate, time to first report, and the proportion of a campaign's recipients who reported. These reward the behaviour that helps and are far harder to improve by making tests easier.

**Reward reporting visibly.** Acknowledge it, thank people, and tell them when their report mattered. The single most effective change available and almost nothing costs less.

**Remove the punitive apparatus.** No lists, no manager notification, no disciplinary consequence for clicking a simulation. Assignment of a short, non-humiliating explanation is enough, and everything beyond it buys fear rather than capability.

**Treat repeat clickers as a support problem.** Someone clicking repeatedly needs a conversation about their workflow and their exposure, not escalation. Frequently they are in a role where the pretexts are genuinely plausible.

**Never blame for a well-crafted lure.** The debrief should say plainly that this one was designed to be difficult and that many colleagues also clicked. This is true, it is the honest framing, and it is the opposite of the current default.

**Measure the trust effect.** Reporting rates for real suspicious messages, and survey measures of willingness to approach security. If these fall when punitive measures are introduced, the programme is trading its own objective for a metric.

**Give people a no-consequence route for uncertainty.** An explicit channel for "I might have clicked something, I am not sure" with a stated guarantee of no consequence. The person who clicked a real phishing email and says nothing is the outcome that costs the most, and this is the mechanism that prevents it.

## Who Feels the Pain

The employee, deceived by a professionally designed message during a busy day, then listed, assigned training and sometimes discussed with their manager.

The organisation, whose actual residual defence is people speaking up, and which has taught them not to.

The security function, which needs the workforce's cooperation and has spent it on a metric.

And the person who clicked a real phishing email, is not certain, and decides that saying nothing is safer — which is the failure this whole apparatus exists to prevent.

## Impact If Fixed

Making reporting the headline metric costs a reporting button and a change of dashboard, and it aligns the programme's measurement with the behaviour that actually helps.

Removing the punitive apparatus is free and would remove the mechanism by which the programme undermines its own objective.

And an explicit no-consequence route for uncertainty is the single most valuable channel an organisation can offer, because the employee who is unsure and stays quiet is how a contained incident becomes a serious one.
