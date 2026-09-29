# Fix: The Referee Is Also the Payer

**Niche:** Severity & Scope Adjudication
**Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The party deciding whether a finding is in scope and what severity it carries is the party whose budget pays for the answer.
**Tags:** #evaluation-metrics #confidence-intervals #compliance #worker-facing #hypothesis-testing #revenue-impact
**Contested on:** Whether the rules a researcher works under are knowable before the work, or decided afterwards by the party who pays.

## The Problem

A researcher submits a finding. The programme decides whether it is in scope, whether it is a duplicate, what severity it carries, and therefore what it pays. Every one of those decisions moves money from the programme's budget to the researcher, and the programme makes all of them.

This is not an allegation of bad faith, and most programmes are run by people trying to be fair. It is a structural observation: a decision-maker with a budget, facing a judgement call, under no obligation to explain and with no external reference, will over time drift toward the cheaper reading. The drift is invisible from inside, because each individual decision is defensible.

The researcher has almost no recourse. They can ask for reconsideration, from the same party. They can escalate to the platform, whose customer is the programme. They can post publicly, which risks their standing and violates most programme terms. Or they can accept it, which is what almost everyone does.

The cost is not primarily the individual unfair decision. It is that the best researchers — the ones with options, whose time is genuinely valuable — respond to an unpredictable payoff by working elsewhere. A marketplace that treats its supply side as having no alternatives gradually finds that the ones with alternatives have used them.

## Why It's Still Broken

**The paying side is the platform's customer.** Programmes pay the fees. Researchers generate the supply and pay nothing. Every product decision that trades programme discretion for researcher fairness is a cost to the revenue side, which is the fundamental reason this persists.

**Each decision is individually defensible.** Severity genuinely is a judgement. Scope genuinely is ambiguous. No individual decision looks wrong, and the pattern is only visible in aggregate — which nobody computes.

**Researchers do not organise.** Independent participants across many jurisdictions with no collective structure have little bargaining power, and the ones with the most leverage are the least likely to spend it on a dispute.

**Public complaint is punished.** Programme terms typically restrict disclosure, and a researcher with a reputation for disputes finds private programme invitations drying up. The enforcement is informal and effective.

**Nobody publishes the aggregates.** Acceptance rates, severity distributions, downgrade frequency and payment timeliness by programme all exist in the platform's database and are not surfaced, so the pattern that would make the problem visible stays invisible.

**Duplicates are unfalsifiable.** A researcher told their finding duplicates an earlier private submission cannot verify the claim. Almost all programmes are honest about this and the researcher has no way to know that, which corrodes trust regardless of the truth.

## What a Fix Looks Like

**Publish programme behaviour statistics.** Acceptance rate, severity distribution relative to the platform-wide reference for comparable classes, downgrade frequency, mean time to triage and to payment, dispute rate and outcome. Per programme, visible before a researcher commits time. This is the intervention — it changes behaviour through comparison rather than through rules, uses data the platform already holds, and requires nobody to adjudicate anything.

**Show the duplicate.** When a submission is closed as a duplicate, show the researcher enough of the original — timestamp, finding class, redacted detail — to verify the claim. Honest programmes lose nothing and gain trust; the unfalsifiable claim disappears.

**Separate adjudication from the platform's commercial relationship.** An ombuds function or an external panel for contested cases, with published outcome statistics. Even a modest degree of independence changes the incentive structure, and full independence is not required for that.

**Publish anonymised precedent.** Resolved disputes, with the reasoning. Both sides can then predict outcomes, and the same argument stops being relitigated monthly.

**Let researchers rate programmes.** Every mature labour marketplace has two-sided reputation. Bounty platforms have one, pointed at the side with less power, which is a conspicuous asymmetry.

**Commit severity before the detail.** For common finding classes, programmes state their payout band in advance rather than assessing after submission. This removes the discretion for the bulk of findings and leaves judgement for the genuinely novel ones, where it belongs.

## Who Feels the Pain

The researcher, who invests unpaid effort against rules decided afterwards by the counterparty, and whose only recourse is to ask them again.

The strong researchers most of all, because they have alternatives and use them — which means the cost lands as a slow quality decline nobody attributes to this.

Programmes run fairly, which are indistinguishable from programmes that are not, and therefore get no benefit from their own good behaviour.

And the platform, whose marketplace depends entirely on supply it treats as inexhaustible.

## Impact If Fixed

Publishing programme statistics is the whole fix in one move. It requires no new adjudication mechanism, no rule change and no negotiation — only surfacing data the platform already has, and letting researchers allocate their effort accordingly.

Showing the duplicate removes the single most corrosive unfalsifiable claim in the relationship, at no cost to any honest programme.

And two-sided reputation would bring this marketplace to the standard every comparable one reached years ago, which matters because researcher supply is the product and it is currently the only part of the market with no protection at all.
