# Build: A Decision Framework, Not a Narrative

**Niche:** The Client During the Incident
**Industry:** [[industries/digital-forensics-firms|Digital Forensics Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Decision support for the notification call — bounded scope, mapped obligations across jurisdictions, costed options and the consequences of each, updated as the picture changes.
**Tags:** #evaluation-metrics #confidence-intervals #bayesian-inference #graph-theory #compliance #workflow-orchestration #revenue-impact #automation
**Contested on:** Whether the person making the notification decision receives what they need to make it, or a technical narrative they must interpret.

## The Problem

A general counsel is on day four of their first serious breach. They must decide whether to notify, which requires knowing what was accessed, which the forensic team can only bound.

What they have is the bridge call. Technical findings, evolving, delivered by people describing what they have established and what they have not, in terms that require interpretation. Somewhere in it is the information they need, mixed with a great deal they do not.

What they need is different in kind. The scope as a range — this many records at minimum, this many at maximum, on this basis. The obligations that attach at each point in the range, across every jurisdiction where affected individuals sit, with their deadlines. The options: notify now at the upper bound, wait for a narrower scope and risk the deadline, or notify in stages. The cost of each. And what would change if the investigation establishes something new.

None of that is assembled anywhere. The counsel builds it themselves, from a technical narrative, under a clock, frequently for the first time in their career — and the quality of the decision depends heavily on whether they have a breach coach who has done it before.

## Why Nobody Has Built This

**It sits between disciplines.** The forensic firm delivers technical findings. Counsel provides legal advice. The decision framework spans both and is owned by neither.

**Multi-jurisdiction obligations are genuinely complex.** Notification thresholds, deadlines and content requirements vary by jurisdiction and sector, and they change. Maintaining that as a usable model is real ongoing work.

**Legal advice is the established product.** Breach coaches provide this service as judgement, and a tool that structures it looks like a competitor to the people who currently hold the relationship.

**Scope arrives as narrative because that is how it is produced.** Without the bounded scope output from [[niches/digital-forensics-firms/scope-determination/profile|🔵 Scope Determination]], a decision framework has nothing quantitative to work with.

**The stakes discourage tooling.** A framework that contributed to a wrong notification decision is a liability nobody wants, which pushes everything back toward advice from a named person.

**The buyer only exists during the crisis.** Nobody procures decision support for a breach they are not having, which is the same preparation problem that runs through this industry.

## What to Build

**Take bounded scope as the input.** Minimum established, maximum defensible, with the basis. The framework's whole value depends on scope arriving as a range rather than as a story.

**Map obligations across jurisdictions, maintained.** For a given affected population, which notification obligations attach, with thresholds, deadlines and content requirements. This is a maintained regulatory model, it is the hardest part to keep current, and it is what counsel currently assembles by hand at three in the morning.

**Model the options and their consequences.** Notify at the upper bound now; wait and risk the deadline; notify in stages as scope narrows. Each with its cost, its regulatory risk and its reputational profile. This is the decision and it is currently held in a counsel's head.

**Update as the picture changes.** Scope narrows or widens during an investigation, and the implications should recompute rather than requiring the counsel to redo the analysis each time.

**Track the clocks.** Multiple jurisdictions, multiple deadlines, several running from different trigger events. A missed deadline because nobody was tracking one of six clocks is an avoidable and recurring failure.

**Prepare the artefacts in advance.** Notification letters, regulator submissions, customer communications and holding statements as templates prepared calmly rather than drafted in a crisis.

**Give the board what it needs.** A standing briefing format — what is established, what is bounded, what decisions are pending and by when — so the board conversation is structured rather than a re-explanation of the technical picture every time.

## Target Customer

Breach coach law firms, for whom this is leverage rather than competition: it lets them serve more clients better and removes the assembly work from a scarce and expensive person.

Cyber insurers, who fund both the response and the notification cost and have a direct interest in the decision being made well — and who could offer the capability across a panel.

General counsel with retainers in place, who would recognise immediately that they are currently prepared for the technical response and not for the decisions they will personally have to make.

## Impact If Built

The person making the most consequential decision in a breach receives a decision framework rather than a technical narrative they must interpret while a clock runs.

Maintained multi-jurisdiction obligation mapping removes the work counsel currently does under the worst possible conditions, and it is exactly the kind of thing that should be prepared once and used many times.

And tracking the clocks prevents a specific, avoidable, recurring failure — a missed deadline in one of several jurisdictions because everyone was focused on the main one.
