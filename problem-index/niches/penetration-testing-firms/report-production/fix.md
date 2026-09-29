# Fix: A Different Template for Every Client

**Niche:** Report Production
**Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The same findings are reassembled into a different document structure for every client, for reasons nobody can articulate and nobody has ever questioned.
**Tags:** #evaluation-metrics #workflow-orchestration #automation #worker-facing #compliance #revenue-impact
**Contested on:** Whether the document is assembled from structured findings captured during the engagement, or retyped into a different client's template every time.

## The Problem

A tester finishes an engagement and opens the client's required report format. It wants the executive summary before the methodology, severity on a five-point scale with different labels from the firm's own, findings grouped by asset rather than by class, a risk matrix in a particular layout, and an appendix structure that differs from the last client's in every detail.

None of these differences carry information. A finding is a finding whether the summary precedes the methodology or follows it. The five-point scale maps onto the firm's four-point scale with a lookup table. Grouping by asset rather than by class is a rendering choice. The client's format exists because someone at that client wrote a template years ago, possibly copied from a firm they used before, and it has never been revisited.

So the tester spends hours reassembling content into a shape that serves nobody, on every engagement, for every client, indefinitely. And the reformatting introduces errors, because moving content between structures by hand is exactly the operation that leaves a severity inconsistent between two places.

Across the industry this is a substantial amount of skilled, expensive time spent converting between arbitrary document shapes.

## Why It's Still Broken

**Templates are contractual and nobody wants the conversation.** Enterprise clients specify format in the statement of work, sometimes for genuine reasons — an internal process consumes it, an auditor expects a shape — and more often because it is what the template says. Challenging it during a bid is not where a firm wants to spend goodwill.

**Nobody has quantified the cost.** Reformatting hours are inside unbilled write-up time, which is itself unmeasured. The cost is invisible, so nobody proposes standardising.

**There is no standard to converge on.** Unlike financial reporting or clinical trials, this profession has no accepted report structure. Several have been proposed; none has become the convention, partly because the accreditation bodies have focused on testing methodology rather than on the deliverable.

**Format is mistaken for differentiation.** Firms invest in their report's look as a mark of quality, which makes convergence feel like commoditisation — though what actually differentiates a report is the findings and the reasoning, not the layout.

**Clients genuinely cannot evaluate the content.** A buyer who cannot judge the technical depth judges the artefact, which rewards presentation and entrenches the custom formats.

## What a Fix Looks Like

**Separate content from presentation, internally first.** Even without any client agreeing to anything, a firm that holds findings as structured data can render any template without reassembling content by hand. This is entirely within the firm's control and removes most of the cost regardless of what clients require.

**Push for a common structured interchange format.** Not a visual standard — a data format for findings that any firm can emit and any client platform can ingest. Clients keep their preferred presentation, rendered from the data. This is the version of standardisation that is achievable, because it asks nobody to give up their template.

**Offer the structured export alongside the document.** A firm that delivers both a PDF in the client's format and machine-readable findings is more useful than one that delivers only the PDF, and it directly helps the receiving engineer. Doing this unilaterally is a differentiator now and would become an expectation quickly.

**Ask clients why, once.** A meaningful share of custom templates exist because nobody has ever asked. A polite question during scoping — what does this format need to support — frequently reveals that the client is happy with the firm's standard structure and adopted theirs from a predecessor.

**Measure the reformatting hours.** Same argument as everywhere in this industry: the cost is real, unmeasured, and would fund the fix several times over if anyone counted it.

**Take it to the accreditation bodies.** A recommended report structure, published by CREST or an equivalent, would give firms something to point at and would let clients adopt a default rather than inventing one. This is the kind of collective-action fix an individual firm cannot achieve.

## Who Feels the Pain

The tester, spending hours on document carpentry at the end of an engagement, in the evenings, during the next one.

The client's security engineer, who receives a bespoke PDF and has to extract findings by hand into their own systems — the custom format serves them no better than a standard one would.

The firm, paying senior rates for format conversion and unable to see the cost in any system it runs.

And the buyer, who is charged for it inside a day rate and receives nothing for the money.

## Impact If Fixed

Separating content from presentation is available to any firm today and removes the majority of the reformatting cost without needing a single client to agree to anything.

A structured interchange format would let the industry standardise the part that matters — the data — while leaving every client their preferred appearance, which is the only version of this that could actually be adopted.

And offering machine-readable findings alongside the document would make a firm's deliverable materially more useful than its competitors', at close to zero cost, which is a rare thing in a market that competes on day rate.
