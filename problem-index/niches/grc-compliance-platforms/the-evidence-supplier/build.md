# Build: Requests in the Engineer's Language

**Niche:** The Engineer Supplying Evidence
**Industry:** [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Evidence requests that name the specific system, state exactly what artefact would satisfy them, arrive in the engineer's own tooling, and remember what was supplied last cycle.
**Tags:** #large-language-models #bert #word-embeddings #evaluation-metrics #workflow-orchestration #automation #worker-facing #data-integration
**Contested on:** Whether the residual evidence work reaches engineers as a specific, contextualised, one-off task or as recurring interruption.

## The Problem

An engineer receives a ticket: provide evidence of logical access review for the data platform, due Friday.

They do not know what a logical access review is in this context. They do not know whether the quarterly permissions check they already run satisfies it, or whether it needs a documented approval, or in what form. They do not know whether a screenshot is acceptable or whether an export is required. They do not know who to ask, because the requester is a compliance manager who phrased the request in the framework's language because that is the language the platform gave them.

So the engineer guesses, produces something, and it is returned as insufficient. They produce something else. Two rounds later the right artefact exists, having cost far more of everyone's time than the underlying task warranted.

Then next year the same request arrives, phrased the same way, and the fact that this exact question was answered twelve months ago by this exact person with this exact artefact is recorded nowhere either of them can see.

The framework's language is the problem's source. It specifies intent deliberately, so that it applies across organisations. Translating that intent into a specific request about a specific system is work, and it is currently pushed onto the least-equipped party.

## Why Nobody Has Built This

**Translation requires system knowledge the compliance function lacks.** Turning a control requirement into a specific request about the payments service needs someone who understands both, and organisations rarely have that person.

**Evidence sufficiency is not specified anywhere.** Frameworks do not say what artefact satisfies a requirement — auditors decide. So even a well-intentioned requester cannot state what would be enough, because they do not know until it is submitted.

**Platforms optimise for the compliance buyer.** The product is bought by compliance and designed for their workflow. The engineer is a downstream recipient whose experience nobody is measured on.

**Ownership mapping is genuinely hard.** Knowing which team owns which system requires a service catalogue that is current, which many organisations lack.

**There is no memory across cycles.** Evidence is collected per audit period and archived. The knowledge of what satisfied a request last time exists in the archive and not in the request.

**Nobody counts the cost.** Engineering time spent on compliance evidence is not tracked anywhere, so the burden is invisible in every system and competes for attention against problems with numbers.

## What to Build

**Translate the requirement into the specific system's terms.** The request should name the service, the environment and the exact artefact — an export of the permissions review for this repository, covering this period, showing the reviewer and the date. Generating that from the control requirement plus the service catalogue is tractable and is the core of the product.

**State what would satisfy it, precisely.** A worked example of an acceptable artefact, drawn from what was accepted last cycle or from comparable organisations. This eliminates the produce-reject-reproduce loop that accounts for most of the wasted effort.

**Remember across cycles.** What was supplied last period, by whom, and whether it was accepted. Most requests recur, and most could be pre-filled with last year's artefact updated, which turns a twenty-minute task into a two-minute confirmation.

**Arrive in the engineer's own tools.** As a pull request, an issue in their tracker, or a chat prompt — not an email from a compliance platform they have no account for. Context switching is a large share of the cost.

**Route by actual ownership.** From the service catalogue and code ownership files, so the request reaches the person who can act rather than a team lead who forwards it.

**Explain why, briefly.** One line on what this control is for and what it protects against. The resentment this work generates comes largely from its apparent arbitrariness, and a sentence of purpose changes the experience substantially at no cost.

**Spread requests across the year.** Continuous collection rather than a pre-audit surge, which is a scheduling change that the platform is well placed to enforce and currently does not.

**Offer to eliminate the request.** Where an engineer supplies the same artefact manually every cycle, that is a case for an integration or a script. The platform should surface these as automation candidates rather than asking again indefinitely.

## Target Customer

Engineering leadership, who bear the cost and currently have no say in the tooling — the argument is engineering hours recovered and a measurable reduction in interruption.

Compliance leadership, for whom better-specified requests mean faster collection and less chasing, which is their own largest pain.

The platforms, for whom engineer experience is an unclaimed differentiator in a category competing mainly on integration counts.

## Impact If Built

The produce-reject-reproduce loop disappears when the request states what would satisfy it, which is the largest single waste in this workflow.

Cycle memory turns most recurring requests into confirmations, and the great majority of evidence requests recur.

And explaining why, in one line, addresses the attitude problem that makes every part of a compliance programme harder — engineers who understand the purpose of a control behave differently toward it than engineers who experience it as arbitrary.
