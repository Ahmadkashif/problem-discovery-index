# Build: One View and an Escalation Case

**Niche:** The Compliance Manager
**Industry:** [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A cross-framework operating view that shows everything outstanding, prioritises it against the audit calendar, and assembles the evidence for the escalation conversation automatically.
**Tags:** #evaluation-metrics #confidence-intervals #time-series-forecasting #gradient-boosting #workflow-orchestration #worker-facing #compliance #automation
**Contested on:** Whether one person running several certification programmes has any leverage over the organisation whose cooperation the whole thing depends on.

## The Problem

A compliance manager's real job is not any framework. It is running a portfolio: four certification programmes with overlapping requirements, competing audit dates, a shared pool of engineering goodwill, and a single person's capacity.

Their tooling does not model that job at all. Each platform shows one framework's readiness. The overlaps between frameworks are in a spreadsheet. The outstanding evidence items are in each platform's own list. The audit calendar is in a calendar. Engineering capacity is unknown. So the manager maintains the actual operating picture in their head and in a spreadsheet, and rebuilds it every Monday.

The harder gap is influence. Their only real lever is escalation — going to a leader and saying this needs to move or the audit will fail. Making that case requires assembling what is outstanding, who owns it, how long it has been open, what the consequence is and what has already been tried. It takes hours to construct, it is done from scratch each time, and it has to be done at exactly the moment the manager is most stretched.

Everything needed for that case is already in the systems. It is simply not assembled.

## Why Nobody Has Built This

**The buyer is not the user.** Platforms are bought on framework coverage and integration count by a security leader or a CFO. The compliance manager's operating experience is not evaluated in the purchase.

**The market looks small.** A function of one, at companies that are not large, buying nothing directly. Venture-scale software is not built for them, even though there are a great many of them.

**Cross-framework views require the mapping to exist.** A unified outstanding-work view depends on knowing which requirements overlap, which is the unsolved mapping problem covered in [[niches/grc-compliance-platforms/framework-mapping/profile|🟠 Framework Mapping & Crosswalks]].

**Platforms compete on their own framework coverage.** A vendor has little incentive to build a view that spans their platform and a competitor's, which is what a multi-framework organisation often has.

**Escalation support looks political rather than technical.** A feature that helps one internal function apply pressure to another is an uncomfortable thing to put in a product roadmap, even though it is the manager's central difficulty.

**Nobody measures the programme's cost.** Without knowing what compliance consumes in engineering hours, there is no basis for the resourcing argument the manager most needs to make.

## What to Build

**A single portfolio view across frameworks.** Everything outstanding, deduplicated across frameworks using the mapping, with owner, age, blocking status and which audits it affects. This is the operating picture the manager currently maintains by hand and it is assembled from data the platforms already hold.

**Prioritise against the calendar and the overlap.** An item blocking three frameworks with the nearest audit in six weeks should be at the top. Ranking outstanding work by audit impact and cross-framework leverage is straightforward and would direct the manager's limited chasing capacity far better than a list per platform.

**Assemble the escalation case automatically.** For any blocked item or team: what is outstanding, how long, who owns it, what has been tried, what the consequence is and what the deadline implies. One click, one page, ready to send. This turns the manager's main lever from a half-day of preparation into a routine action.

**Forecast whether the audit will be ready.** Given current outstanding work, historical completion rates per team and the remaining time, is this programme on track. Managers currently answer this by feel and are asked it constantly.

**Measure what the programme costs.** Engineering hours consumed, by team and by framework, from ticket and evidence data. This is the number that supports every resourcing conversation the manager needs to have and none of them currently have it.

**Capture institutional memory.** Why this exception exists, what the auditor accepted last year, which team needs how much notice, what the subsidiary's situation is. The manager holds all of it and none is written down, which is why their departure is a crisis.

**Support the handover explicitly.** A structured programme state that a successor can read, because turnover in this role is high and the current state of the art is a conversation and a shared drive.

## Target Customer

Compliance leadership at companies with several frameworks and a small compliance function, which is most of the addressable market for the automated-certification tier.

Security and finance leadership as the sponsors, where the argument is programme continuity and predictability rather than the manager's comfort — including the specific risk that the whole programme currently depends on one person's memory.

The platforms, for whom cross-framework portfolio management is a genuine differentiator and an argument for consolidating a customer's frameworks onto one vendor.

## Impact If Built

The manager stops rebuilding the operating picture weekly and starts working from one, which is several hours a week returned to the person with the least of it.

Automated escalation cases turn their main source of leverage from an expensive, occasional act into something they can use routinely and proportionately.

And capturing institutional memory addresses the largest single risk in most compliance programmes, which is that everything depends on one person who has no peer, no documentation and a high probability of leaving within two years.
