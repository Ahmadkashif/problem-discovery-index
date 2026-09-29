# Support Engineer Repeat-Ticket Treadmill

**Industry:** [[healthcare-practice-software|Healthcare Practice Software]]
**Type:** Worker Life Changing
**One-liner:** Support engineers stop answering the same rejection code for the four-hundredth time and start working the genuinely novel failures that currently sit in the queue behind it.
**Tags:** #bert #large-language-models #word-embeddings #k-means-clustering #transfer-learning #evaluation-metrics #automation #worker-facing

## The Problem
Support at a practice management vendor handles a queue dominated by repetition. A payer rejection code the practice has never seen. A template that stopped populating a field. An interface to a lab or an imaging centre that failed overnight. An eligibility check returning nothing. A statement batch that did not go out. Individually each is a real problem for that practice. Collectively, the same forty issues account for most of the volume, and a support engineer works through them in a rotation that does not change.

The engineer usually knows the answer within seconds of reading the ticket. Most of the handling time is not diagnosis, it is the ritual around it — locating the practice's configuration, reproducing the state, writing an explanation in terms a practice manager will follow, and documenting the resolution in a form the next engineer will not read.

## Why It Matters to the Worker
Support engineers in this category are quietly among the most knowledgeable people at the vendor. They know how the product behaves in the field, which configurations break, which payers misbehave, and which release introduced which regression. That knowledge is the product's real documentation and it accumulates in individuals.

The role gives them no way to use it. They are measured on tickets closed and time to first response, both of which punish the engineer who stops to fix the underlying cause. The pattern they can see — that this rejection has spiked across sixty practices in one state since Tuesday — has no route to anyone who could act on it, so they answer it sixty times. People leave the role for that reason specifically, and their field knowledge leaves with them.

## What a Solution Looks Like
Automatic clustering of incoming tickets so that a spike is visible as a spike. Sixty practices reporting the same rejection in one state is a payer change, not sixty tickets, and it should reach the rules team as a single signal within hours.

Draft resolutions retrieved from the corpus of prior tickets, with the practice's own configuration already pulled in, so the engineer edits and sends rather than assembles. Routing that puts a genuinely novel ticket in front of a senior engineer rather than letting it queue behind the routine. And a route by which an engineer's observation about a recurring defect is recorded as evidence with a count attached, rather than as an opinion in a Slack channel.

## Impact If Solved
Support is the vendor's highest-fidelity view of how its software actually behaves across thousands of live practices, and it is organised to discard that view one closed ticket at a time. Restructuring it around repetition converts the queue from a cost centre into the product's early warning system, and makes the job survivable for the people who understand the product best.
