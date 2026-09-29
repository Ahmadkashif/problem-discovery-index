# Build: Pull, Do Not Request

**Niche:** Evidence Collection & Request Management
**Industry:** [[industries/soc2-audit-firms|SOC 2 & Attestation Audit Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Retrieve evidence directly from the client's connected systems, and where a request is unavoidable, state exactly which artefact from which system would satisfy it.
**Tags:** #evaluation-metrics #compliance #data-integration #automation #workflow-orchestration #worker-facing #bert
**Contested on:** Whether evidence is pulled from connected systems or requested, chased and received as files.

## The Problem

An engagement sends a hundred and forty evidence requests. Several weeks pass. Items arrive in batches, some correct, some not, some in formats that need reworking. Reminders go out. The compliance manager on the client side spends days assembling files. The associate spends days chasing and organising.

Almost none of this needs to happen. The cloud configuration is queryable. The identity provider's access review records are queryable. The ticketing system's change approvals are queryable. The compliance platform holds most of it already, in structured form, continuously.

Where a request is genuinely necessary — a signed policy, a board minute, a walkthrough with a person — the request itself is usually the problem. It is phrased in the control's language: provide evidence of logical access review for the in-scope systems. The client must decide what that means, which system, which period, and what form of evidence would satisfy it. They produce something. It is rejected. They produce something else.

The specific, answerable version — export the quarterly access review report from this system covering these dates showing reviewer and date — takes the same time to write and eliminates the rejection cycle.

## Why Nobody Has Built This

**Integration work is per-client and looks expensive.** Each client's systems must be connected, which appears costly per engagement until it is built as a reusable library across a client base using the same platforms.

**The request list is the established process.** The audit programme produces requests, the portal tracks them, and the workflow is built around the cycle rather than around eliminating it.

**Clients vary in what is connectable.** Some have everything in a compliance platform and some have nothing, so the capability applies unevenly.

**Direct system access is a different arrangement.** Read access to the client's systems requires security review and contractual basis, which is heavier than receiving files.

**The delay is not costed.** Elapsed time is absorbed by the engagement calendar and the associate's chasing, so its cost does not appear.

**Request phrasing is inherited from the programme.** Standard audit programmes express requests in control language, and rewriting them specifically per client is work nobody has been assigned.

## What to Build

**Connect once, reuse everywhere.** A connector library for the common platforms — compliance platforms, cloud providers, identity providers, ticketing, code hosts — built centrally and used on every engagement.

**Pull everything that can be pulled.** For connected systems, retrieve the evidence rather than requesting it. This removes the majority of the request list and most of the elapsed time.

**Phrase the residual requests specifically.** System, artefact, period, and what it must show. Generated from the control and the client's system inventory rather than from a generic programme.

**State what would satisfy it, with an example.** The accepted artefact from last period, or from a comparable client, shown alongside the request. This eliminates the produce-reject-reproduce cycle that accounts for most of the delay.

**Remember across periods.** Most requests recur. Pre-filling with last period's artefact and asking for confirmation or an update turns a request into a confirmation.

**Send progressively, not in bulk.** Requests released as the engagement progresses rather than as a hundred and forty item list, which is easier for the client to absorb and produces faster responses.

**Route to the right person.** Requests addressed to the system owner rather than to the compliance manager who must forward them, which removes a hop and a delay from every item.

## Target Customer

Audit firm operations, for whom evidence collection determines engagement elapsed time and associate hours, and where the connector library is a durable asset.

Client compliance functions, for whom the evidence request cycle is a recurring imposition on their own time and on their engineering colleagues.

Compliance platform vendors, who hold most of the evidence and could offer an auditor-facing retrieval interface that would make their customers' audits faster.

## Impact If Built

Engagement elapsed time falls substantially, because it is dominated by waiting for evidence rather than by testing it.

Specific, answerable requests with an example of what satisfies them eliminate the rejection cycle, which is the largest source of friction for both the associate and the client.

And a reusable connector library converts a per-engagement cost into a firm-level asset, which is the only durable efficiency advantage available in a market that competes on price.
