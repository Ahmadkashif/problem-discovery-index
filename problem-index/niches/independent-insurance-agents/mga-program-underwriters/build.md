# The Declined Submissions Are the Most Informative Data and Are Discarded

**Niche:** [[niches/independent-insurance-agents/mga-program-underwriters/profile|MGAs & Program Underwriters]]
**Industry:** [[industries/independent-insurance-agents|Independent Insurance Agents]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The MGA sees every risk it turned down and keeps records only on the ones it wrote.
**Tags:** #logistic-regression #gradient-boosting #binary-classification #evaluation-metrics #revenue-impact

## The Problem
An MGA with delegated authority receives far more submissions than it binds. A specialized programme might quote a third of what comes in and bind a fraction of that. The rest — declined, not quoted, quoted and lost — passes through and leaves almost no trace beyond a status field.

Those submissions are the most informative data in the business. They describe the risks the market is producing, what competitors are willing to write and at what price, where the MGA's appetite is costing it good business, and which classes are deteriorating before the loss experience shows it.

Instead the analytics run on the bound book: loss ratio by class, by state, by producer. That answers how the written business performed and says nothing about the far larger population it was selected from. An MGA whose loss ratio improves may be underwriting better or may simply be receiving worse submissions and declining more — and the bound book cannot distinguish those, which is the single most consequential question its carrier partner will ask.

## Why Nobody Has Built This
Systems follow money. Policy administration was built to issue, bind, and bill, and a submission that does not bind never becomes a policy record. Declination reasons are captured as a code if at all, and the submission documents are archived rather than structured.

Capacity is the other reason. Underwriters are measured on premium written and on loss ratio, and time spent recording why a risk was declined is time not spent quoting the next one. The information is worth more than the minute it costs and nobody has ever made that argument with a number.

And the missing counterfactual is invisible. Nobody complains about the business you never wrote.

## What to Build
Treat the submission — not the policy — as the unit of analysis.

**Structure every submission at intake**, bound or not: class, exposure characteristics, prior loss experience, producer, source, requested effective date, and the outcome with a coded reason. Most of this arrives in the submission already; it is simply not retained when the answer is no.

**Model quote and bind probability.** With submissions and outcomes, the MGA can predict which incoming risks will bind and at what price — which is capacity allocation, since underwriter hours are the constraint and are currently spent in arrival order.

**Estimate the loss experience of what was declined.** Where declined risks were bound elsewhere and later surface — in industry data, in renewals coming back, in producer feedback — the MGA can begin to test whether its declinations were right. Even partial visibility is more than zero, which is what it has now.

**Measure competitive position from lost quotes.** A quote lost on price says what the market charged; a pattern of losses in one class says the appetite is mispriced relative to competitors. This is the cheapest market intelligence available and it is thrown away daily.

**Watch submission mix as an early warning.** A shift in the risks arriving — worse loss histories, a change in producer mix, more of a class that is hardening elsewhere — precedes deterioration in the bound book by a full policy cycle.

## Target Customer
Chief Underwriting Officer or head of analytics at an MGA or programme platform. The argument lands with the carrier partner too: a delegated underwriter that can demonstrate its selection is improving, rather than that its submission flow changed, is in a much stronger position at treaty renewal.

## Impact If Built
Delegated authority is granted on the basis that the MGA underwrites better than the carrier would, and almost none of them can evidence it, because the evidence lives in the submissions they discard. Retaining and modelling the full funnel turns selection quality from an assertion into a measurement — and directs underwriter capacity, the actual scarce resource, at the risks most likely to bind.
