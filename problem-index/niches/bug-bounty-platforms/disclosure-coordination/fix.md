# Fix: Safe Harbour That Does Not Bind Anyone

**Niche:** Disclosure Coordination
**Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Programme terms promise not to pursue legal action, which is a promise from one company that binds no prosecutor, no third party and nobody outside the programme.
**Tags:** #compliance #evaluation-metrics #worker-facing #confidence-intervals #workflow-orchestration
**Contested on:** Whether disclosure runs on an agreed process with defined timelines and legal protection, or on the goodwill of whoever answers the email.

## The Problem

Bounty programmes include safe harbour language: work within scope and in good faith and we will not pursue legal action against you. Most organisations mean it.

The protection is narrower than researchers generally understand. It binds the organisation that wrote it and nobody else. It does not bind a prosecutor, who in several jurisdictions can act on computer misuse legislation regardless of the affected party's wishes. It does not bind a third party whose infrastructure was incidentally touched — a cloud provider, a CDN, a payment processor. It does not extend past the scope boundary, which is the boundary researchers most often cross by accident because scope is prose. And it does not exist at all for research outside any programme, which is where a great many important findings originate.

The consequences are asymmetric and real. Researchers who find something serious outside a programme face a genuine choice between reporting it — with unclear legal exposure and no guaranteed response — and doing nothing. Some choose nothing. Some choose to sell it somewhere the buyer does not want it fixed. Both outcomes are worse for everyone than a report, and the legal ambiguity is what produces them.

## Why It's Still Broken

**The protection organisations can offer is genuinely limited.** No company can bind a prosecutor. Safe harbour language is not misleading so much as it is the most any single organisation can actually give, and the limit is in the law rather than in the drafting.

**Legislation has moved slowly and unevenly.** Several jurisdictions have narrowed the risk through prosecutorial guidance or statutory amendment, and coverage is patchy and varies enormously. A researcher operating internationally faces a patchwork with no clear map.

**Organisations without programmes have no incentive.** The organisations most likely to react badly to an unsolicited report are exactly the ones least likely to have published a disclosure policy, and there is no pressure on them to.

**Scope boundaries are crossed accidentally.** Because scope is prose, a researcher can exceed it without realising, and safe harbour typically applies only within scope — so the protection lapses precisely where the researcher most needs it.

**Third-party infrastructure is unavoidable.** Testing a modern application touches a CDN, an identity provider and several APIs owned by other companies who never agreed to anything.

**Nobody publishes the outcomes.** How often researchers actually face legal threats, and in what circumstances, is anecdotal. Without data the risk is impossible to calibrate and is probably both over- and under-estimated by different people.

## What a Fix Looks Like

**Adopt a standard safe harbour text with a clear scope-overrun clause.** A widely used standard form — the existing open efforts are a good base — including explicit protection for good-faith activity that inadvertently exceeds scope. That single clause addresses the most common real exposure and costs the organisation nothing, since a good-faith overrun was never something they intended to pursue.

**State the third-party position.** Programmes should say plainly which third-party infrastructure is implicated and whether they have secured any assurance for researchers touching it. Most have not, and saying so lets a researcher make an informed decision.

**Publish a disclosure policy even without a programme.** An organisation with no budget for bounties can still publish a contact, a commitment to acknowledge, and safe harbour terms. This is close to free and is the single highest-value thing most organisations could do, because it converts an ambiguous unsolicited report into an invited one.

**Track and publish incidents.** A record of legal threats against researchers, by jurisdiction and circumstance, maintained by a body with standing. Researchers could then calibrate real risk, and the record would create reputational cost for organisations that behave badly.

**Provide a legal backstop.** Access to counsel for researchers facing threats after good-faith disclosure, funded collectively by platforms and programmes. Rare enough to be affordable and transformative for the person it happens to, and its existence changes the calculation for everyone deciding whether to report.

**Support the legislative direction.** The durable fix is statutory, and the industry's bodies are the natural advocates for prosecutorial guidance and statutory protection for good-faith research. Several jurisdictions have moved and the pattern is available to follow.

## Who Feels the Pain

The researcher, carrying a personal legal risk that no contractual language fully removes, for work that benefits the organisation they are reporting to.

Researchers outside programmes most of all, who have no protection and no assurance of a response, and who are frequently the people who find the most consequential things.

The organisations that never hear about their vulnerabilities, because the finder judged the risk of reporting too high — the most expensive outcome of this and the one nobody counts.

And the ecosystem, which loses findings to markets where the buyer does not want the flaw fixed.

## Impact If Fixed

A standard safe harbour with scope-overrun protection is free, addresses the most common real exposure, and could be adopted by every programme this quarter.

Publishing a disclosure policy without running a programme is the highest-leverage action available to the large majority of organisations, and it costs a page.

And a legal backstop would change the reporting calculation for every researcher facing a finding outside a programme, which is where the industry currently loses the reports it can least afford to lose.
