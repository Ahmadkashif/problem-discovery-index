# A Rule Tree Nobody Can Evaluate

**Niche:** [[niches/email-sms-marketing-platforms/journey-design-and-attribution/profile|Journey Design & Attribution]]
**Industry:** [[industries/email-sms-marketing-platforms|Email & SMS Marketing Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every brand builds the same dozen automated journeys as hand-drawn rule trees, and then nobody can say which branches earn anything.
**Tags:** #causal-inference #hypothesis-testing #confidence-intervals #evaluation-metrics #markov-decision-processes #revenue-impact #gradient-boosting #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to tell a brand which branches of its automated journeys earn anything — and whoever does that turns a hand-drawn rule tree into something that can be improved.

## The Problem
The abandoned cart flow has nine branches, added over four years by five different people, each responding to a specific idea at the time. It reports revenue in aggregate and the aggregate is good. Whether the third reminder earns anything, whether the discount branch cannibalises the full-price one, whether the delay before the second message is right, whether two of the branches ever fire at all — none of this is known, because the reporting attributes revenue to the flow and the flow is a single object. The brand keeps adding branches, because adding is the only available action and the aggregate keeps looking fine.

## Why Nobody Has Built This
Journey builders were designed to configure sending rather than to be evaluated as policies — the object model has a branch and no notion of the branch's counterfactual, which is the structural gap. Branch-level attribution requires a control group at each branch, which nobody constructs. Aggregate flow revenue is a large flattering number nobody wants to decompose. And the accumulation of branches is invisible until someone tries to understand the diagram.

## What to Build
Evaluate the journey as a policy. Attribute outcomes to the path taken rather than to the flow, which is the foundation and is a computation over data the platform already holds. Build in holdouts at branch level, so each branch has a comparison population and its contribution is measured rather than assumed — this is what makes improvement possible and it must be part of the builder rather than a separate exercise. Estimate marginal contribution, since the question about a third reminder is whether it adds anything beyond the first two and the aggregate cannot answer it. Detect cannibalisation between branches and between flows, because a discount branch that captures purchases the full-price branch would have made is a loss recorded as a gain. Test structural changes rather than only message content, which is where the significant gains are and which no current tooling supports. Flag dead and unreachable branches, which is the fix note's subject. Model the journey as a sequential decision problem where the question is what to send next given everything known, which is the eventual form and is a substantially better framing than a static tree. Simplify aggressively, since these structures accumulate and a simpler journey that performs the same is more valuable than a complex one. Report branch-level contribution as standard, because what is measured gets pruned. And measure against a much simpler baseline flow, since a nine-branch journey that does not beat a two-message one is common and nobody has checked.

## Target Customer
Lifecycle and CRM teams, messaging platforms whose journey builders produce unevaluable structures, and the agencies building flows for clients.

## Impact If Built
The builder configures sending and has no notion of a branch's counterfactual, so the tree accumulates and the aggregate keeps looking fine. Branch-level holdouts built into the builder turn an unevaluable diagram into something that can be pruned and improved.
