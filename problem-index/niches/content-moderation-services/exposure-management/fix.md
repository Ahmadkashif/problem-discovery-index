# Fix: The Liability Sits Downstream of the Controls

**Niche:** Reviewer Exposure Management
**Industry:** [[industries/content-moderation-services|Content Moderation Services]]
**Type:** Fix (Pain Point)
**One-liner:** The party that can reduce the exposure is not the party that pays when it causes harm, and the contract between them has never priced the difference.
**Tags:** #evaluation-metrics #compliance #worker-facing #data-integration #confidence-intervals #revenue-impact
**Contested on:** Whether the amount and intensity of distressing material a reviewer is exposed to is a managed quantity or an incidental by-product of a queue someone else composed.

## The Problem

A platform decides what its classifiers resolve automatically and what goes to a person. It designs the review interface, sets the default fidelity, decides whether a reviewer sees the flagged segment or the whole file, and composes the queue. Every one of those decisions determines how much distressing material a human being will see.

A vendor employs that human being, carries the employment relationship, and faces the claim when harm occurs. It has no input into any of the decisions above, frequently cannot see the classifier confidence on the item it is being handed, and in many arrangements cannot modify the review interface at all because the interface belongs to the client.

So the controls are on one side of a contract and the liability is on the other, and the contract itself is silent — it specifies volume, turnaround, accuracy and price. It does not specify queue composition, severity mix, presentation defaults or exposure caps, because those have never been contractual objects. The result is a system where the party who could most cheaply reduce the harm has no financial reason to, and the party with every reason to has no ability.

This is not a story about bad actors. Both parties are behaving rationally inside an agreement that never contemplated the hazard as something to allocate.

## Why It's Still Broken

**The contract is a volume contract.** It was written for a business-process-outsourcing relationship measured in decisions per hour, and the hazard was not a recognised object when the template was established. Nobody has had a reason to reopen the template, because reopening it means pricing something neither side wants to price.

**Pricing the harm is unattractive to both sides.** A platform that agrees to exposure terms has conceded a duty toward workers it does not employ, which is precisely the position its structure was designed to avoid. A vendor that demands them raises its cost in a market where it wins on price. Mutual silence is the stable equilibrium.

**The vendor's bargaining position is weak.** These contracts are large, concentrated among a few clients, and the vendor is replaceable. Raising labour-condition terms in a renegotiation risks the account, and it is the account that employs everyone.

**Visibility is contractually withheld.** A vendor often cannot see classifier confidence, cannot see what was auto-resolved, and cannot measure what fraction of what it reviews needed human eyes at all. Without that, it cannot even quantify the problem to argue about it.

**Harm is slow and attribution is contested.** Psychological injury emerges over months or years, often after the reviewer has left. Both the causal link and the apportionment between the exposure and everything else in a life are genuinely arguable, which makes the liability real enough to fear and vague enough to defer.

**Everyone is waiting for the regulator.** The most likely forcing function is statutory or judicial, and both sides know it, so the rational move for each is to change nothing until they must.

## What a Fix Looks Like

**Make exposure a contractual object.** Severity mix, presentation defaults, segment isolation, classifier confidence visibility and cumulative exposure caps written into the statement of work as specified terms with prices attached, the way turnaround and accuracy already are. Once exposure has a line in the contract it has an owner, and the negotiation can be about level rather than about whether it exists.

**Give the vendor the classifier output.** The single highest-value change, and close to free for the platform. A vendor that can see confidence scores on incoming items can decide what genuinely needs a person, route by severity, and measure what fraction of its queue was avoidable. Withholding it serves no purpose beyond keeping the vendor unable to make the argument.

**Let the vendor control presentation.** Reduced fidelity, greyscale, audio suppression and segment isolation applied by default, under the vendor's control, with the reviewer able to escalate to full fidelity when the decision requires it. This requires the client to accept that quality auditing will grade decisions made at reduced fidelity, which is the real obstacle and is entirely solvable by auditing the same way.

**Price the avoided review.** A contract that pays per decision rewards volume. One that shares the saving when the vendor demonstrably reduces unnecessary human review aligns both parties toward the same outcome, and turns exposure reduction from a cost the vendor absorbs into a benefit both sides collect.

**Standards rather than bilateral negotiation.** No single vendor can move alone in a price-competitive market. An industry exposure standard — developed with occupational health clinicians, published, and adopted as a floor across the specialist tier — changes the terms for everyone at once and removes the first-mover penalty. This is the move that has worked in every other industry with a recognised occupational hazard.

**Clients should ask for it before they are made to.** Platforms under public and regulatory scrutiny over supply-chain labour conditions have a direct interest in being able to describe what they require of their vendors. Specifying exposure terms is cheaper than the alternative and is currently available to any platform that wants it.

## Who Feels the Pain

The reviewer, entirely. The whole cost of the misalignment lands on the person at the end of the queue, who has no party to the contract at all.

The vendor, which carries a liability it cannot manage and cannot price, and whose insurance position in this line of business is deteriorating for exactly that reason.

The platform, later and indirectly, through litigation that increasingly names it, and through a regulatory direction that is unmistakable.

And the industry, which cannot compete on working conditions because working conditions are unmeasured, so the only available competition is price — which makes conditions worse.

## Impact If Fixed

Naming exposure in the contract is the whole unlock. Once it is specified it can be measured, priced, audited and improved, and every technical intervention in this niche becomes deployable. While it is unnamed, none of them are.

Classifier visibility alone would let vendors demonstrate how much human review is unnecessary, which is the argument that makes the commercial case for everything else.

And the first-mover problem dissolves under a shared standard, which is why the standard is the intervention that matters most and the one no individual vendor can produce alone.
