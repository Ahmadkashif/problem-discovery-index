# Win Rate Nobody Reports by Reason Code

**Niche:** [[niches/retail-pos-platforms/chargeback-dispute-operations/profile|Chargeback & Dispute Operations]]
**Industry:** [[industries/retail-pos-platforms|Retail POS Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Merchants and platforms know their overall chargeback win rate and cannot decompose it by reason code, evidence type or merchant category — so nobody knows which disputes are worth fighting and effort is spread uniformly across winnable and hopeless cases.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #logistic-regression #revenue-impact #quick-win #automation
**Contested on:** Every serious competitor in dispute operations is fighting to win a representment against the card network's own evidence rules before the deadline — and whoever holds win rate highest per dollar of effort takes the merchant.

## The Problem
A merchant fights every dispute with the same template and wins some. They do not know that disputes under one reason code are won three-quarters of the time with the right delivery evidence and disputes under another are essentially never won regardless of what is submitted. So they spend the same effort on both, get discouraged by the losses, and eventually stop fighting any of them — including the ones they would have won. The platform has thousands of merchants' dispute outcomes and reports a rate.

## Why It's Still Broken
Outcomes come back from the network in a form that is recorded as a financial result rather than as a labelled case, and joining an outcome to the evidence that was submitted requires the representment itself to be structured — which it is not, because it is a document. Nobody has asked for the decomposition, because merchants do not know it is possible and platforms have treated disputes as a cost of doing business. And the specialist vendors who do measure this treat it as proprietary, which is defensible and leaves the general market uninformed.

## What a Fix Looks Like
Structure the representment and record the outcome against it. Every dispute carries its reason code, the evidence elements submitted, the merchant category, the transaction characteristics and the result. Within a quarter the platform can report win rate by reason code and by evidence combination — which is the analysis that tells a merchant where to spend effort and tells the platform which evidence elements actually move outcomes. Publish it to merchants, because the merchant's decision about whether to fight is the one being informed. Estimate win probability per dispute from that history and show it at the moment the merchant decides, with the expected value of fighting stated. And surface the evidence gaps: if delivery confirmation is the element that wins a reason code and the merchant does not capture it, that is a change to make in fulfilment rather than in disputes.

## Who Feels the Pain
Merchants fighting hopeless disputes and conceding winnable ones; dispute operations staff working a queue with no prioritisation; and small merchants who gave up entirely and now absorb every chargeback.

## Impact If Fixed
Decomposed win rate turns dispute handling from a uniform effort into a prioritised one, and it typically shows that a minority of reason codes account for most of the winnable value. The evidence-gap finding is the more durable output, because it changes what the merchant captures at the point of sale and fulfilment, which raises the win rate on every future dispute.
