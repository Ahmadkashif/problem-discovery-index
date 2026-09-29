# The Mechanism: What the Mozer Team Actually Built

**Origin:** [[origins/telecom-carriers/profile|Telecom Carriers]]
**Tags:** #logistic-regression #decision-trees #gradient-boosting #perceptron-and-mlps #evaluation-metrics #data-integration #workflow-orchestration #revenue-impact

> This is the file an FDE should read twice. It is a worked example of turning "customers are leaving" into a modelling problem with a dollar figure attached to every decision.

## The Question, Stated Properly

A wireless carrier has roughly 47,000 subscribers on file. Some fraction will cancel service next month. **Which ones, and is it worth spending money to stop them?**

Note what this is not. It is not "how many subscribers will we lose" — that is a forecasting question a finance team can already answer from the aggregate churn rate. It is **which named subscriber, this month, is worth an intervention** — and that is a per-customer prediction problem the billing system had never been asked before.

## The Decomposition

**1. Assemble one subscriber, from several systems.** Usage, billing, credit and complaints lived in separate operational systems, built for separate purposes — rating a call, processing a payment, screening an applicant, logging a ticket. None of them was built to answer "will this person leave." Joining them into one row per subscriber was the first piece of real engineering, and it is the same join this vault calls **the missing join** everywhere else it appears — except here it was actually made.

**2. Label the outcome.** A subscriber either churned in a defined future window (the Mozer study used January–February 1999) or did not. This turns a vague worry into a supervised binary classification problem.

**3. Compare models honestly.** The study did not pick one algorithm and declare victory. It ran **logistic regression, decision trees, neural networks, and boosting** against the same data and compared them on how well each identified subscribers who actually churned — not on which was newest or most fashionable.

**4. Turn a score into a decision.** A predicted probability of churn is not yet an action. The paper's load-bearing contribution asks a second question on top of the first: *given* a subscriber is likely to leave, what incentive is worth offering, and does the expected value of retaining them exceed the cost of the offer? A subscriber who is both likely to churn *and* cheap to retain is worth targeting; one who would only stay for a discount larger than their remaining value is not.

**5. Price it in the business's own terms.** The paper's headline number is not a precision or recall score — it is that reducing monthly churn from 2% to 1% on a base of 1.5 million subscribers is worth on the order of **$54M a year**, roughly **$150M in shareholder value** at a plausible multiple. That framing, model performance translated through to a board-level number, is why this is remembered as a production case rather than an academic exercise.

## Why This Was Hard in 1999

The join itself was the real engineering: usage, billing, credit and complaints were four systems built at different times for different purposes, and nobody before this had a reason to reconcile them at the individual-subscriber level. Getting a clean, honest label was its own problem — "churned" sounds simple until you decide whether a subscriber who downgraded, went dormant, or was involuntarily disconnected for non-payment counts the same as one who walked to a competitor. And the comparison across logit, trees, neural nets and boosting reflects a field genuinely unsure in 1999 which technique would win on this kind of data — notable in retrospect, when tabular business problems are now assumed to default to gradient boosting.

## What It Gave Up — the trade-offs

The model treats retention as a spend, not a relationship repair: a discount offered to a subscriber flagged as likely to churn addresses the symptom the model can see — a probability — not necessarily the underlying grievance. It is only as good as the join, since every field it depends on has to exist, be current, and be attached to the right subscriber, or it degrades silently. And it assumes the past predicts the future — a model trained on 1998 behaviour assumes 1999 subscribers leave for the same reasons, which a new competitor's launch or a price war can break exactly when the model is needed most.

## The Transferable Pattern

> **The record of what a customer already did, sitting in systems nobody built for this purpose, usually contains the answer to what they will do next — if someone joins it and asks.**

An FDE meeting a gym's member roster, a SaaS product's usage logs, or a subscription box's shipping and support history is meeting this exact problem, one join and one label away from the same $54M-shaped answer.

**Sources:** Mozer, Wolniewicz, Grimes, Johnson & Kaushansky, *Predicting Subscriber Dissatisfaction and Improving Retention in the Wireless Telecommunications Industry*, IEEE Trans. Neural Networks 11(3), 2000; NeurIPS 1999 precursor, *Churn Reduction in the Wireless Industry* (mlanthology.org).
