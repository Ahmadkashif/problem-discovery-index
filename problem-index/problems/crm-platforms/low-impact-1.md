# Lead Routing and Territory Assignment

**Industry:** [[crm-platforms|CRM Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Routing engines are mature and every company still runs a rules tree nobody dares modify, because territory design is compensation politics and the rules encode a truce rather than an optimisation.
**Tags:** #gradient-boosting #logistic-regression #optimization-fundamentals #k-means-clustering #feature-engineering #evaluation-metrics #workflow-orchestration

## The Problem
An inbound lead arrives and must reach a representative. So must every account in a territory plan. The mechanics are well served — assignment rules, round robin, queues, escalation on no-response — and every CRM ships them.

The logic inside is the problem. Routing rules accumulate: by geography, then by company size, then by product interest, then by an exception for a strategic account, then by a carve-out negotiated when someone changed roles. After a few years the tree has hundreds of branches, several contradict each other, and nobody can safely change it because each branch is somebody's compensation.

Territory design has the same shape. Territories are drawn annually, usually by dividing a map or an account list until each representative's quota looks defensible, and the exercise is dominated by fairness arguments rather than by any estimate of where the revenue actually is.

## What Already Exists
Assignment rules and round-robin routing are standard in every platform. Territory management modules exist in Salesforce and its peers. Specialist vendors (LeanData, Chili Piper, Openprise) handle complex routing and matching well. Speed-to-lead tooling is mature. Enrichment supplies the firmographic attributes routing keys off.

## The Customisation Gap
Nobody measures whether the routing is any good. A lead routed to representative A rather than B produces an outcome, and across thousands of leads the difference between assignment policies is measurable — and no company measures it, because the counterfactual is never constructed and the routing is never varied.

Fit prediction is the unexploited half. Which representative converts which kind of lead is estimable from the company's own history — by industry, size, product, seniority of contact — and is a far better routing key than a geography rule inherited from 2019. The honest framing matters here: this is about matching characteristics to outcomes, not ranking people, and the version that ranks people will be rejected by the sales organisation.

Territory design is a genuine optimisation problem — balancing expected opportunity, travel or coverage cost, existing relationships and quota fairness — and it is solved with a spreadsheet and an argument. Opportunity estimation per account from the platform's own conversion history is what the optimisation needs and nobody computes it.

## Impact If Solved
Routing determines who works which opportunity, which is upstream of every revenue outcome, and it is set by accumulated politics. Measuring assignment quality and estimating territory opportunity converts an annual argument into a decision with evidence, using data the platform already holds.
