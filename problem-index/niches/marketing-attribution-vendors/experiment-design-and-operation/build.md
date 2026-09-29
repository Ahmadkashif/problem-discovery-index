# The Only Method That Does Not Guess, Used Occasionally

**Niche:** [[niches/marketing-attribution-vendors/experiment-design-and-operation/profile|Experiment Design & Operation]]
**Industry:** [[industries/marketing-attribution-vendors|Marketing Attribution Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Randomised experiment is the one method in this category that does not guess at a counterfactual, and it is treated as an occasional supplement because it is expensive to run.
**Tags:** #causal-inference #hypothesis-testing #monte-carlo-methods #confidence-intervals #evaluation-metrics #automation #workflow-orchestration #bayesian-inference
**Contested on:** Every serious competitor in this niche is fighting to make experiments cheap and continuous rather than occasional and expensive — and whoever does that supplies the ground truth the whole category needs and does not have.

## The Problem
Running a proper geographic experiment means selecting matched regions, deciding the split, calculating power, coordinating suppression across platforms, running for enough weeks, and analysing the result — a project taking a measurement scientist several weeks and costing real media suppression. Because it is expensive it happens rarely, which means the category's only source of ground truth is scarce, which means models cannot be validated, which is the original problem. The expense is largely operational rather than fundamental: most of the cost is bespoke design and manual execution, not the suppressed spend.

## Why Nobody Has Built This
Experiments are treated as consulting projects rather than as a product, which keeps the cost structure artisanal — this framing is the binding constraint and it is commercial rather than technical. Vendors selling models have limited interest in making the thing that could contradict them cheap. Execution spans platforms that each work differently. And nobody has built the operational layer because the category's identity is statistical rather than operational.

## What to Build
Industrialise the experiment. Generate the design automatically — region matching, assignment, duration, power — from the business's own data, which is the core and removes most of the cost that keeps experiments rare. Refuse to run underpowered tests, which is the fix note's subject and is the single most valuable constraint the product can impose. Execute across platforms through their interfaces, since manual suppression coordination is error-prone and is where designs are silently broken. Monitor execution during the test, because the most common failure is the suppression not holding and it is currently discovered at analysis. Analyse automatically with a pre-registered method, which removes the flexibility that lets a result be talked into existence. Run continuously as a small always-on allocation rather than as a project, which is the change that converts ground truth from scarce to abundant and makes everything else in this category possible. Sequence tests to answer the most valuable open questions, connecting to the validation work, since a limited experimental budget should target where models are least reliable. Handle small advertisers with designs suited to low power, including accepting that some questions cannot be answered and saying so. Pool designs and learnings across clients, which is the priors work. And report the cost per experiment, because the whole argument is that it can fall by an order of magnitude and nobody currently tracks it.

## Target Customer
Measurement vendors, client measurement teams, and advertisers whose entire measurement stack lacks ground truth because tests are too expensive to run often.

## Impact If Built
Most of an experiment's cost is bespoke design and manual execution rather than suppressed spend, and treating it as a consulting project keeps it that way. Automating design and execution converts the category's only source of ground truth from scarce to continuous.
