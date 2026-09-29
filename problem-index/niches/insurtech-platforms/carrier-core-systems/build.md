# The Submission-to-Loss Chain as a Queryable Asset

**Niche:** [[niches/insurtech-platforms/carrier-core-systems/profile|Carrier Core Systems]]
**Industry:** [[industries/insurtech-platforms|Insurtech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A carrier's core system holds every submission, decline, quote, bind and subsequent loss, which is the empirical basis for every question underwriting leadership guesses at, and the system was designed to administer policies rather than to be asked anything.
**Tags:** #data-integration #survival-analysis #gradient-boosting #confidence-intervals #evaluation-metrics #causal-inference #descriptive-statistics #revenue-impact
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
An underwriting leader asks what the carrier's hit ratio is by class and by broker, whether accounts quoted above a certain rate change bind at all, and whether the business written in a particular segment two years ago has developed worse than expected. Each answer requires a data request, a quarter of work, and a set of caveats about what the extract does and does not include. The chain those questions run along — submission, decline reason, quote, bind, premium, loss — is complete inside the carrier's own systems, distributed across policy, billing, claims and whatever the submission platform holds, joined by nothing.

## Why Nobody Has Built This
Core systems are transaction processors and their data models are optimised for administering a policy lifecycle rather than for analysis, which is a legitimate design choice that has never been complemented. Carriers have responded by building data warehouses as separate multi-year programmes with their own consultants, which produce something and rarely produce the chain, because the chain crosses the submission boundary into systems the warehouse programme did not scope. And the vendors' incentives point toward configuration and implementation services rather than toward making their customers' data answerable.

## What to Build
An analytical layer over the lifecycle, delivered as part of the core system rather than as a separate programme. Every submission carries an identity that persists through decline, quote, endorsement, renewal and claim, so the chain is joinable by construction rather than by reconstruction. Standard questions are answered out of the box: hit ratio by any dimension, rate change against retention, quoted-and-lost analysis, loss development by underwriting cohort and by appetite decision. Underwriting cohort tracking is the most valuable piece and the least available — knowing how the business written under a particular appetite or pricing decision has actually developed is the feedback loop that underwriting judgement is supposed to run on and currently does not. The analytical layer is also what makes every model elsewhere in this industry trainable, which is why it belongs in the core rather than beside it.

## Target Customer
Carriers of all sizes, the core system vendors who could differentiate on answerability rather than on configurability, and the MGAs operating on carrier paper who face the same problem with less data engineering capacity.

## Impact If Built
Underwriting leadership currently makes appetite, pricing and distribution decisions from quarterly reports built by hand, and the underlying record would support continuous measurement. Cohort-level loss development against the decisions that produced the business is the feedback loop the discipline is founded on and that most carriers cannot actually run.
