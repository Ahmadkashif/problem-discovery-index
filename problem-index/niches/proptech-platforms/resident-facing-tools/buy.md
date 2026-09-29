# Support Deflection Tooling Pointed at the Resident's Questions

**Niche:** [[niches/proptech-platforms/resident-facing-tools/profile|Resident-Facing Tools]]
**Industry:** [[industries/proptech-platforms|Proptech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Customer support automation is a mature commodity that every consumer business uses to answer account questions instantly, and rental housing answers them with a voicemail box at a leasing office.
**Tags:** #large-language-models #bert #transformers #evaluation-metrics #confidence-intervals #workflow-orchestration #automation #worker-facing
**Contested on:** Every serious competitor building resident-facing software is fighting to let a renter answer a question about their own tenancy — what they owe, what was fixed, what their lease says, where their deposit is — without calling the office, and whoever makes the record genuinely legible to the resident takes the resident-experience market.

## The Problem
A resident's question — why is my balance what it is, when is my lease up, is my work order scheduled — is an account question of exactly the kind that banks, telecoms and utilities answer instantly in an app. In rental housing it is answered by a site manager during office hours, if they pick up. The resident calls twice, leaves a message, and the site manager returns it between two showings. Both parties lose time on an exchange that required no judgement at all.

## What Already Exists
Retrieval-based question answering over a customer's own account data is standard practice, with mature tooling and well-understood patterns for grounding answers in records rather than generating them. Multilingual support is commodity. Messaging channels — SMS, WhatsApp, in-app — are cheap. Escalation to a human with full context is a solved workflow. Nothing here requires development beyond integration.

## The Customization Gap
The adaptation is to a domain where a wrong answer has legal weight. It requires: (1) strict grounding in the resident's own record with citation, so an answer about a charge points at the ledger entry and the lease clause rather than paraphrasing; (2) a firm boundary between answering and advising — the system can say what the lease provides and must not characterise what the resident is legally entitled to, because that is a line an operator's counsel will care about and residents deserve not to be misled about; (3) genuine multilingual coverage in the property's resident languages, since the population least able to reach a leasing office by telephone is the one most affected; (4) escalation that carries the full context to a human, so a resident who does need a person does not start over; and (5) logging every question and answer, which produces the first dataset anyone has on what residents actually need to know — currently invisible because it all happens by telephone.

## Target Customer
Property operators whose site staff are consumed by status and balance calls, and platform vendors competing on resident experience.

## Impact If Solved
Instant answers to account questions is the single largest available reduction in site staff interruption, and it is achieved with off-the-shelf components against data the operator already holds. The question log is a valuable secondary output: it shows, for the first time, which parts of the tenancy are systematically unclear to residents, which is usually a fixable communication problem rather than a support one.
