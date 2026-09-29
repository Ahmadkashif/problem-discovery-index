# Business Data Is Sequences and Generation Produces Rows

**Niche:** [[niches/synthetic-data-providers/relational-and-constraint-preservation/profile|Relational & Constraint Preservation]]
**Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Enterprise data is mostly event sequences attached to entities, and generators sample rows independently, which destroys the ordering and the lifecycle that every downstream use depends on.
**Tags:** #hidden-markov-models #markov-chains #seq2seq #lstms-and-grus #time-series-forecasting #survival-analysis #evaluation-metrics #probability-distributions
**Contested on:** Every serious competitor in this niche is fighting to make a generated database behave like the real one under the customer's own queries and joins — and whoever does that takes the account, because a dataset that falls apart on a join is worth nothing however well it scored on distributions.

## The Problem
A synthetic customer in the generated database has a subscription that was cancelled before it started, three consecutive upgrade events with no downgrade between them, a support ticket closed before it opened, and a payment applied to an invoice issued the following month. Each row is individually plausible and the marginal distributions of every column match the source. The sequence is nonsense. The application under test throws on the state transition, the analytics query that measures time-to-first-value returns negative numbers, and the team concludes that synthetic data does not work for them.

## Why Nobody Has Built This
Sequence modelling for heterogeneous business events is harder than modelling a table: variable-length histories, irregular timing, event types with their own attribute schemas, and state machines that are implicit in application code rather than declared anywhere. The evaluation literature is row-oriented, so sequence violations do not appear in any published score and therefore do not appear in any vendor's incentives. And the lifecycle rules that are being violated live in the application, which the generator has never seen.

## What to Build
Generate the entity's history rather than its rows. Model each entity as a sequence of typed events with timing, so the generated history is produced as a trajectory and the ordering is a property of the model rather than an accident — which is the structural change and everything else follows from it. Mine the implicit state machine from the source data: which event types follow which, which transitions never occur, which are terminal, and the holding-time distribution in each state. All of it is recoverable from the event log and none of it is documented, which makes discovery a deliverable. Preserve inter-event timing distributions, since the interval between signup and first purchase is frequently the measured quantity and row-wise generation replaces it with noise. Model entity lifetime explicitly, because the population mixes entities at every stage of their life and sampling without that structure produces a cohort that never existed. Report sequence-level validity as a headline: illegal transitions per thousand entities, ordering violations, lifecycle impossibilities — all mechanically computable and never reported. And validate by replaying the customer's application against the synthetic database, which surfaces exactly the violations that matter because it is the thing that will run against it.

## Target Customer
Enterprise data platform and QA teams building non-production environments, application teams needing realistic test data, and the test data management vendors whose subsetting approach cannot produce new volume.

## Impact If Built
Row-wise generation destroys the sequence structure that most business data consists of, and no published metric penalises it. Mining the implicit state machine from the event log is both the modelling input and a standing deliverable in its own right.
