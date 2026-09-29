# Millions of Trajectories Used to Debug Incidents

**Niche:** [[niches/ai-agent-platforms/trajectory-corpus-intelligence/profile|Trajectory Corpus Intelligence]]
**Industry:** [[industries/ai-agent-platforms|AI Agent Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The platforms hold millions of complete task trajectories with tools called, state at each step and outcomes attached, and use them to debug individual incidents.
**Tags:** #gradient-boosting #hidden-markov-models #evaluation-metrics #confidence-intervals #causal-inference #hypothesis-testing #transfer-learning #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to turn millions of complete task trajectories into empirical answers about where approval belongs, which failures are recoverable and what predicts a task going wrong — and whoever does that sets the standard the category is judged by.

## The Problem
Every hard question in this industry — where to put the approval gate, which failures matter, what makes an agent reliable on a task type, whether a prompt change helped — is answered by intuition, and every one is empirically answerable from data the platforms already hold. Millions of trajectories exist with the full step sequence, the tool calls, the state, the outcome and frequently a satisfaction signal. They are queried when something goes wrong with one of them. The category is making design decisions by feel while sitting on the largest record of agent behaviour that exists.

## Why Nobody Has Built This
Traces were built for debugging, so they are shaped for a human reading one rather than for analysis across millions. Cross-customer analysis is contractually awkward and nobody has asked the narrow version. The engineering organisations are building features in a fast-growing market. And the findings would establish reliability numbers the category currently prefers to leave as demos, which is an uncomfortable thing to publish first and a decisive advantage for whoever does.

## What to Build
Turn the corpus into the category's evidence base. Build a failure prediction model from the corpus, which is a well-posed supervised problem with abundant labels and feeds the per-task confidence the whole industry needs — this is the highest-value application and it is available today. Derive approval gate placement empirically, from per-action error rates and outcomes, which replaces the nervous guess with a recommendation grounded in what actually happened. Characterise which failures were recoverable and how, since that distinction determines how much autonomy is safe and is currently asserted rather than measured. Mine successful trajectory patterns by task shape, so agent design converges on what works rather than on what the framework's example did. Quantify the value of design changes — a tool added, a step reordered, a prompt restructured — across deployments, which turns prompt engineering from folklore into something with effect sizes. Publish aggregate reliability by task type, which the field has no source for and which the first credible publisher will define. Establish a narrow, inspectable aggregation basis with customers, since the contractual objection is to open-ended use. Offer per-customer analysis unconditionally, which needs no permission and demonstrates the value. And feed the findings back into product defaults, so every new deployment starts from what the corpus knows.

## Target Customer
The platforms themselves, their customers, the buyers with no reference for what agent reliability looks like, and the research community with no empirical account of agents in production.

## Impact If Built
The category designs by intuition while holding the largest record of agent behaviour in existence. Failure prediction from the corpus is available today and feeds the per-task confidence every other problem here depends on.
