# Coverage Policies Are Public and Nobody Has Made Them a Corpus

**Niche:** [[niches/medical-device-mfg/reimbursement-hta-strategy/profile|Reimbursement & Health Technology Assessment Strategy]]
**Industry:** [[industries/medical-device-mfg|Medical Device Manufacturing]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every payer publishes what it covers and why, and reimbursement strategy is built from a consultant reading a few of them.
**Tags:** #text-classification #large-language-models #graph-ml #word-embeddings #evaluation-metrics

## The Problem
A cleared device with no coverage has no market. Getting covered means securing a code, then persuading payers — a national programme and hundreds of commercial plans — to write a policy that pays for it. The evidence required is different from the evidence that cleared the device, and the timeline is longer.

Payers publish their medical policies. Thousands of them, revised continuously, each stating what is covered for whom under what conditions and citing the evidence relied on. Coverage determinations at the national level are published with full rationale. Technology assessment bodies publish their reviews.

That is a complete public record of what evidence has persuaded payers, by technology, by claim, by plan. Reimbursement strategy is nonetheless built from a consultant's reading of a handful of relevant policies and their recollection of prior engagements. Nobody can answer: for technologies like this, what evidence appeared in policies that granted coverage and what appeared in the ones that denied it, and how long did the shift take.

## Why Nobody Has Built This
The work is understood as policy analysis, which is a reading discipline. Consultants read policies because reading policies is what the job has always been, and the corpus was genuinely unmanageable by hand — thousands of documents in inconsistent formats across hundreds of plans, revised on their own schedules.

There is also no single source. Each payer publishes on its own site in its own format, so assembling the corpus is an acquisition problem before it is an analysis problem, and no one client's engagement justifies building it.

And nobody measures. A coverage strategy either works or does not, over years, with many confounders, so the profession has never been able to say which arguments actually move policies.

## What to Build
Assemble the coverage corpus and analyse it.

**Acquire and version payer policies at scale.** Thousands of documents across hundreds of plans, tracked over time so that a policy change is detectable and datable. This is the foundational work and the durable asset.

**Extract policy structure.** Technology, covered indications, exclusions, prior authorization requirements, and — critically — the evidence cited. Policies are formulaic enough to make this tractable.

**Model coverage change.** When a policy moves from non-coverage to coverage, what changed beforehand: a trial publication, a guideline endorsement, a national determination, a competitor's coverage. Sequencing those across many technologies is how you learn what actually causes coverage to move.

**Map the evidence requirement by technology class.** What evidence appears in policies covering comparable technologies is the specification for a client's evidence generation plan, and today it is inferred from a few examples.

**Track policy diffusion.** Coverage spreads between payers in patterns — which plans lead, which follow, how long the lag runs. Knowing that turns a scattergun payer strategy into a sequenced one.

## Target Customer
Practice leader or managing director at a reimbursement and market access consultancy. The commercial argument is that evidence generation is the client's largest cost after development, and a firm that can specify what evidence will actually secure coverage — from the record rather than from experience — is selling a materially better product.

## Impact If Built
Devices that work fail commercially because they never get covered, and clients spend years generating evidence chosen by judgment. Making the coverage corpus queryable specifies the evidence requirement from what has actually persuaded payers, and shortens the most expensive and least guided phase of bringing a device to market.
