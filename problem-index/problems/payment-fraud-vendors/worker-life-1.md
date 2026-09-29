# The Manual Review Analyst at Forty Seconds a Case

**Industry:** [[payment-fraud-vendors|Payment Fraud Vendors]]
**Type:** Worker Life Changing
**One-liner:** Analysts make irreversible decisions about strangers' purchases in under a minute, on exactly the cases the model could not decide, and are graded on a chargeback rate that reflects only half their decisions.
**Tags:** #large-language-models #bert #k-nearest-neighbors #gradient-boosting #graph-neural-networks #evaluation-metrics #worker-facing #automation

## The Problem
Manual review exists where the model is uncertain. By construction these are the hardest cases in the stream, and they are handled at production pace.

The analyst sees an order, a device fingerprint, an email and phone reputation, a shipping and billing address pair, velocity counters and the model's score with some indication of what drove it. They decide approve, decline or contact the customer.

The signals conflict, which is why the case is here. A new customer, an expensive item, express shipping, a billing address that does not match the shipping address — that is a fraud pattern and also a gift.

There is a handle time target. Review is a cost centre and capacity is planned against average handling time, so the analyst has under a minute.

The feedback is halved and lagged. Approvals may generate a chargeback in six weeks, which is a partial grade on part of the work. Declines generate nothing, ever. So an analyst's quality is assessed on their approvals alone, which rewards declining.

And the cases repeat. A fraud ring produces dozens of superficially distinct orders that share a device pattern, an email structure or a shipping address cluster, and they arrive as separate cases to separate analysts at separate moments.

## Why It Matters to the Worker
The decisions are consequential and anonymous. Declining a legitimate customer denies a real person a purchase and frequently ends their relationship with that merchant; the analyst never knows they did it.

The grading is structurally unfair. Being measured on an outcome that exists for only one of two possible decisions produces a documented and predictable drift toward declining, and analysts know the incentive is wrong while having no way to argue against it.

Pace precludes thoroughness. Everyone in the role knows that another two minutes would improve a meaningful share of decisions, and the capacity model does not allow it.

The work is isolating and repetitive. Hundreds of strangers' transactions a day, in silence, with no colleague to consult on a difficult case at the moment it matters.

And the expertise is unrecognised. Good analysts develop genuine pattern recognition — this email structure, this address pattern, this order composition — and it is tacit, uncredited, and lost when they leave.

## What a Solution Looks Like
Case linking before review. Orders sharing a device, an address cluster, an email structure or a payment instrument should be presented as one linked case, not as twelve separate ones. This is the single largest improvement available and it is graph work on data already collected.

Precedent retrieval. The most similar prior cases, what was decided, and what happened afterwards, shown alongside the case. It transfers the tacit expertise to every analyst immediately.

Evidence assembled rather than looked up. Address validation, email and domain age, phone-to-name matching, device history and prior order behaviour, presented as findings rather than as fields to interpret.

Symmetric feedback wherever it can be obtained. Where a randomised approval allowance exists, declined cases produce outcomes and analysts can finally be graded on both directions. Even without it, retry behaviour and subsequent purchases by the same identity elsewhere in the network give partial evidence about declines.

Consistency measurement. Analysts should be able to see where their decisions diverge from colleagues' on near-identical cases, which improves calibration and is currently invisible.

Time allocated by difficulty. A uniform handle time across cases of wildly varying difficulty is the wrong model; routing genuinely hard cases to more time and more experienced analysts is a straightforward operational change.

## Impact If Solved
Manual review holds the hardest decisions in the pipeline, performed fastest, graded on half the outcomes. Case linking, precedent retrieval and symmetric feedback improve the decisions and the job simultaneously, and linking alone typically collapses a substantial fraction of the queue into a handful of real cases.
