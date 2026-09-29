# Build: Multi-Party Disclosure That Scales

**Niche:** Disclosure Coordination
**Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Coordination infrastructure for a finding that affects many parties — notification, embargo tracking, dependency propagation and downstream fix verification — instead of one person managing it by email.
**Tags:** #graph-theory #graph-neural-networks #evaluation-metrics #change-point-detection #compliance #data-integration #workflow-orchestration
**Contested on:** Whether disclosure runs on an agreed process with defined timelines and legal protection, or on the goodwill of whoever answers the email.

## The Problem

A researcher finds a vulnerability in a widely used library. It affects the maintainer, every package depending on it, every distribution shipping it, every product embedding it, and every organisation running any of those. The number of parties who need to know, in a defined order, under an embargo, before a coordinated publication date, can run into the hundreds.

This is coordinated by a person with a spreadsheet and an email client.

The failures are predictable. Parties are missed, usually the smaller downstream ones furthest from the maintainer. Embargo dates slip because one vendor needs longer and there is no mechanism to renegotiate with everyone. Details leak, sometimes from a fix commit that lands publicly before the embargo ends. Downstream projects that forked the code years ago are never notified at all. And nobody tracks whether the fix actually propagated — the maintainer patches, the advisory publishes, and the vulnerable version continues shipping in derivatives for years.

The dependency data that would make most of this mechanical exists in public package registries and software bills of materials. Nobody has connected it to disclosure.

## Why Nobody Has Built This

**Nobody owns multi-party coordination.** National coordination bodies handle a small number of high-profile cases with limited capacity. Platforms coordinate within their own programmes. Maintainers are volunteers. There is no party whose job this is at scale and no revenue model obviously attached to it.

**Trust is the binding constraint, not technology.** Embargo participation requires every party to trust the coordinator and each other. Building that trust is institutional work over years, which is why the existing coordination bodies matter and why a commercial entrant would struggle to replace them.

**A registry of who to notify is itself sensitive.** A complete list of parties affected by an undisclosed vulnerability is a target. Any system holding embargo membership and vulnerability detail is an extremely attractive one, which raises the security bar enormously.

**Downstream propagation is genuinely hard.** Dependency graphs are incomplete, forks are invisible to package registries, vendored copies do not appear as dependencies, and embedded firmware is opaque. The data is good enough to help and not good enough to be complete, and partial coverage has to be communicated honestly.

**Incentives diverge sharply.** Researchers want timely publication, vendors want time, downstream users want notice, and coordinators want order. A tool cannot resolve a genuine conflict of interest and can only make the state visible.

## What to Build

**Derive the notification set from dependency data.** Package registries, software bills of materials and vulnerability databases, resolved into the set of affected downstream parties with their maintainer contacts. Partial by construction, and far better than a person recalling who to email. Coverage stated explicitly, because a list presented as complete when it is not is worse than one honestly labelled.

**Track the embargo as shared state.** Who has been notified, who has acknowledged, who has a fix ready, who has asked for extension, what the current coordinated date is. Every participant sees the same state, which is the single largest improvement over email — most embargo failures are coordination failures rather than bad faith.

**Handle extension negotiation explicitly.** When one party needs longer, the request and its effect on everyone else is visible, and the decision is recorded. Today this happens in side conversations and other participants discover the slip late.

**Detect leaks automatically.** Monitor public repositories for commits that reveal the vulnerability before the embargo ends — a fix landing publicly is the most common leak and is detectable. Alerting the coordinator early lets the timeline be compressed deliberately rather than overtaken.

**Verify downstream propagation after publication.** Which affected packages have released a fixed version, which have not, which distributions have picked it up, which forks remain on the vulnerable code. This is the part nobody does and it is where the long tail of exploitation lives.

**Support the researcher's position.** A recorded timeline of when the report was made, what was promised, and what happened, so a researcher considering publication after a stalled process has an evidenced account rather than an assertion.

**Build it as public infrastructure.** This should sit with the existing coordination bodies, an open-source foundation or a consortium rather than a commercial platform, because participation depends on trust that a vendor-owned system will struggle to earn.

## Target Customer

National and sector coordination bodies, who do this work today with inadequate tooling and whose capacity is the binding constraint on how many multi-party cases get handled properly.

Open-source foundations and large maintainer organisations, who face this repeatedly and coordinate by hand.

The platforms as participants and funders rather than owners, since their programmes generate findings that require coordination and they benefit from the infrastructure existing without needing to own it.

## Impact If Built

The long tail of downstream parties stops being missed. The organisations that never hear about a vulnerability in a component they depend on are consistently the smaller ones, and they are the ones with the least capacity to find out any other way.

Shared embargo state would remove most coordination failure, which is the dominant cause of disclosure processes going wrong — far more common than anyone acting in bad faith.

And propagation verification would address the years-long tail in which a fixed vulnerability continues shipping in forks and derivatives, which is where a large share of real-world exploitation of known flaws actually comes from.
