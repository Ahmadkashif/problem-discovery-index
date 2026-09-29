# Build: Composition Management and Honest Deflection Measurement

**Niche:** [[niches/digital-bpo-operations/deflection-and-work-composition/profile|Contact Deflection & Work Composition]]
**Industry:** [[industries/digital-bpo-operations|Digital BPO Operations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Measure whether deflected contacts were actually resolved, and manage the composition of what is left as a first-class operational variable.
**Tags:** #survival-analysis #gradient-boosting #change-point-detection #confidence-intervals #evaluation-metrics #descriptive-statistics #automation #revenue-impact
**Contested on:** Whether a deflected contact that produced no human interaction actually resolved the customer's problem.

## The Problem

Deflection is measured by absence. A customer entered self-service and did not reach an agent, so the contact was deflected and the saving is booked.

That measure cannot distinguish three very different outcomes: the issue was resolved, the customer gave up, or the customer will call tomorrow about the same thing. The second and third are not savings — the second is a customer experience failure that shows up in churn, and the third is the same contact arriving later with more frustration attached.

The second problem is compositional. What remains after deflection is a selected population — the hard, the ambiguous, the upset — and it keeps changing as deflection improves. Every downstream parameter depends on that composition and none is managed against it.

## Why Nobody Has Built This

Deflection programmes are usually the client's, reported against a cost-saving target, and the incentive is to count deflections generously. A measure that reclassified a third of them as abandonment would reduce the reported benefit of a programme that is already funded and celebrated.

Following a deflected customer requires linking their self-service session to any subsequent contact on any channel, which spans systems and frequently spans the client's and the vendor's boundaries — an integration nobody owned because nobody was asking the question.

And the compositional effect falls on the operation rather than on the deflection programme, so the party creating it does not experience it.

## What to Build

An honest deflection measure and a composition management capability.

**Classify the deflection outcome.** For each self-service session that did not escalate: was there evidence of resolution — a completed transaction, a confirmed answer, a satisfaction signal — or did the session end mid-flow? Then check for a subsequent contact on any channel about a related issue within a window. Resolved, abandoned and delayed become three separate numbers instead of one.

**Report net deflection.** Sessions that did not reach an agent, minus those that produced a later contact, minus those that abandoned. This is the honest figure and it will be materially lower than the reported one, which is the point.

**Track composition continuously.** The mix of contact types reaching agents, their handle time distribution, their difficulty and emotional intensity scores, week over week, with change-point detection so a deflection release is visible as the intervention it is.

**Propagate the composition change automatically.** When the mix shifts, handle time targets, staffing models, skill requirements and agent load expectations should all update. Today each is adjusted manually, late, after somebody complains. Wiring composition to these parameters is what turns a chronic problem into a managed one.

**Identify what should be deflected next by net value.** The best deflection candidates are high-volume, low-complexity, reliably resolvable types. The worst are those where deflection produces abandonment or a delayed harder contact. Ranking candidates by net rather than gross deflection changes what gets built, and requires the honest measure to exist first.

**Give the deflection programme the downstream cost.** The client's deflection business case should carry the compositional effect — higher cost per contact, higher agent load, skill mix shift. This is an accounting change and it is what makes deflection decisions honest.

## Target Customer

Client operations leadership owning the deflection programme, who have a reported saving and no measure of its quality. Also BPO account leadership, for whom the compositional effect is currently an unfunded cost and an unwinnable argument without these numbers.

## Impact If Built

Deflection gets measured by whether the customer's problem went away rather than by whether they reached an agent. The composition of the remaining work becomes a managed variable that propagates into targets and staffing automatically. And the next tranche of deflection gets chosen on net value rather than on volume.
