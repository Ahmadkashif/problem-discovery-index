# Hundreds of Settlements, Each a Live Experiment in Reaching People, None of Them Compared

**Niche:** [[niches/personal-injury-law/mass-tort-claims-administration/profile|Mass Tort & Class Action Claims Administration]]
**Industry:** [[industries/personal-injury-law|Personal Injury Law Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Administrators design a notice programme, observe exactly who then filed a claim, and repeat this across hundreds of settlements and millions of class members — the only empirical evidence on whether legal notice works, and it is never looked at twice.
**Tags:** #causal-inference #logistic-regression #hypothesis-testing #confidence-intervals #evaluation-metrics

## The Problem
When a class action or mass tort settles, an administrator runs the machinery: design and execute the notice programme that tells class members the settlement exists, take in claims, review each for eligibility against a court-approved matrix, calculate allocations, detect fraud, and distribute the money. It happens under court supervision, on court deadlines, at scale — hundreds of settlements a year across the industry, some with millions of class members.

Every settlement contains an experiment that nobody treats as one.

Notice is designed in advance by media experts who file affidavits projecting reach: this combination of direct mail, email, digital placement, publication and earned media will reach some estimated percentage of the class. A court relies on that projection to find the notice adequate. Then the claim period runs, and the administrator observes precisely what happened — how many class members filed, when, through which channel, in response to which touch.

The projection and the outcome are never compared. Not within a settlement, and emphatically not across settlements. The affidavit is a filing; the claim rate is an operational statistic in a distribution report. They live in different documents and no one has ever put them side by side across the hundreds of matters an administrator has run.

The same is true of everything else in the process. Claim form design varies enormously — some demand documentation people threw away a decade ago, others accept an attestation — and its effect on who claims is unmeasured. Deficiency notices are sent to claimants with incomplete submissions, and what fraction cure and what fraction give up is unstudied. Allocation matrices are negotiated by counsel and approved by courts with no evidence base on how similar matrices performed before.

The administrator holds all of it. Across hundreds of settlements they know which notice strategies reach a dispersed consumer class, which reach an occupationally exposed population, which reach people who moved twice since the conduct occurred. That knowledge exists as senior people's intuition and nowhere else.

## Why Nobody Has Built This
The invoice is administration, priced by claim volume and process steps. Nothing in the fee structure pays for an analysis of whether the process worked, and the client — class counsel, defence counsel, the court — has not asked for one.

The court order is the more serious constraint and deserves care. Every engagement operates under an order that governs what may be done with class member data, and that order is not permission to build a cross-matter dataset. This is a real limit, and it is worth separating what it forbids from what it does not. Pooling identified claimant records across settlements is out of the question. Measuring, in aggregate, that notice programmes of a certain design produced claim rates in a certain range for classes of a certain type is methodological learning about the administrator's own process, and it is the thing that has not been done.

Nobody is incentivised to find low claim rates either. A low claim rate is awkward for class counsel, whose fee was justified by a settlement's value to the class, and for the defendant, who is content. The administrator's job is to run the process the order specifies, and asking whether the process reached people invites a question about every settlement previously approved.

And the industry has no research tradition. It grew out of legal operations and mailing, and it is staffed for throughput.

## What to Build
**Compare projected reach with realised claiming, across matters.** The most straightforward and most overdue analysis in the field. Notice experts project; administrators observe; the comparison is a table nobody has assembled.

**Model claim rate as a function of what was actually decided.** Class type, how members were identified, notice channels used, claim form length, documentation required, deadline length, reminder cadence. These vary across hundreds of settlements, which is exactly the variation needed to estimate their effects.

**Measure the documentation burden.** Requiring proof of purchase versus accepting attestation is the single largest design lever on who claims, it is argued about in every negotiation on intuition, and its effect is estimable.

**Study the deficiency cycle.** Claimants who submit incomplete claims and are asked to cure are a population with an observable outcome. Cure rates by deficiency type, by notice wording, by claimant channel, tell you where the process is losing legitimate claimants.

**Run genuine experiments where the order permits.** Reminder timing, subject lines, form layout — randomising these within a settlement is low-risk, well within ordinary administration, and would build an evidence base in two years that currently does not exist at all.

**Give courts something to rely on.** A judge assessing whether notice is adequate has affidavits and precedent. Evidence from hundreds of comparable matters about what reach a given design actually achieves would change how these settlements are approved, and would come from the only party positioned to supply it.

## Target Customer
Chief Operating Officer or VP of Claims Administration at a settlement administration firm. The competitive argument is real: administrators are selected by counsel and approved by courts largely on capacity and reputation, and the first one able to say what its notice programmes actually achieve, with evidence, changes the basis of selection.

## Impact If Built
Class actions and mass torts are the mechanism by which large numbers of people are compensated for harm they cannot individually litigate, and whether that mechanism reaches them is decided on projections nobody has ever checked against outcomes.
