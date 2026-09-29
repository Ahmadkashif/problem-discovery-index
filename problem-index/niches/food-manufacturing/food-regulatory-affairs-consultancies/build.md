# Enforcement History as a Predictive Review Layer

**Niche:** [[niches/food-manufacturing/food-regulatory-affairs-consultancies/profile|Food Regulatory Affairs & Label Compliance]]
**Industry:** [[industries/food-manufacturing|Food Manufacturing]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The published rules say what a label must contain; the firm's own correspondence and refusal history says what regulators actually act on, and only the first is used to review a label.
**Tags:** #gradient-boosting #bert #transformers #large-language-models #evaluation-metrics #feature-engineering #cross-validation #confidence-intervals #compliance #data-integration

## The Problem
A label review is a judgment about risk, not a checklist. Some requirements are enforced strictly and some are technically binding and rarely acted on; some claim wordings draw warning letters and near-identical ones do not; some import entries are refused for reasons that appear nowhere in the published guidance. The firm accumulates exactly this knowledge — agency correspondence, warning letters received by clients, import refusal notices, and the outcomes of positions it advised — and it lives in matter files and in senior specialists' memory. So reviews are performed against the rules while the differentiating knowledge, which is what the client is actually buying, is applied inconsistently depending on who does the work.

## Why Nobody Has Built This
Reviews are delivered as opinions per client under deadline, and the outcome — whether a label ever drew an issue — arrives months or years later attached to a different matter or not at all. Correspondence and refusal notices come in inconsistent forms across agencies and ports. And there is a familiar defensive reflex: a structured record of which requirements the firm advised were low-risk, alongside cases where that proved wrong, is uncomfortable to hold even though it is the only route to being systematically right.

## What to Build
An enforcement record joining review positions to outcomes. Every review records the specific requirements evaluated, the positions taken, and the risk assessment; agency correspondence, warning letters, and refusal notices are structured against the same requirement taxonomy, including public enforcement data covering the whole industry rather than only the firm's clients. That produces the layer no competitor has: empirical enforcement likelihood per requirement, by product category, claim type, and port or district, which turns a rules-based review into a risk-based one. Reviewers see, at the point of judgment, how often this position has drawn an issue and where. And the same record answers the question clients ask most and firms currently answer by anecdote — what will actually happen if we do this.

## Target Customer
VPs of regulatory services and practice leaders at food regulatory firms running 100-500 specialists, and the regulatory affairs leaders at manufacturers who receive risk opinions with no basis they can inspect.

## Impact If Built
Converts senior specialists' accumulated enforcement intuition into an institutional asset, which is both a quality gain and the answer to a capacity ceiling set by how many experienced reviewers exist. Public enforcement data makes the corpus buildable beyond the firm's own client base, which is unusual — most of the outcome records this sweep identifies are locked inside client relationships.
