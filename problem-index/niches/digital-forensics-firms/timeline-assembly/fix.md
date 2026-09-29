# Fix: Three Clocks That Disagree

**Niche:** Evidence Collection & Timeline Assembly
**Industry:** [[industries/digital-forensics-firms|Digital Forensics Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The sequence a notification decision rests on is assembled from sources whose clocks differ by unknown amounts, and the reconciliation is done by inference and not recorded.
**Tags:** #evaluation-metrics #confidence-intervals #change-point-detection #compliance #worker-facing #hypothesis-testing
**Contested on:** Whether a defensible sequence of events emerges from tooling, or from one examiner reconciling a dozen formats and three disagreeing clocks by hand.

## The Problem

Evidence sources do not agree about time. A server's clock drifted. An appliance logs in local time with no offset recorded. A cloud service logs in UTC with millisecond precision while an application logs to the second. A workstation's clock was wrong by four minutes for six months. And some artefacts carry no reliable timestamp at all.

The examiner reconciles these by inference. They find an event visible in two sources and use it as an anchor to establish the offset. Where no anchor exists, they estimate. Where precision differs, they accept the coarser. The reconciliation is performed in their head and in the construction of the timeline, and it is not written down.

The consequences are real. Order of events can determine conclusions — whether the attacker accessed a system before or after a particular control was applied, whether an exfiltration preceded a containment action, whether two activities were the same session. A four-minute offset can invert an ordering that matters.

And because the reconciliation is not recorded, nobody can review it, and if the timeline is challenged in litigation two years later the examiner must reconstruct from memory why they believed these clocks related this way.

## Why It's Still Broken

**It is treated as craft.** Clock reconciliation is regarded as something a competent examiner does, not as a step requiring documentation.

**No convention exists for recording it.** There is nowhere in a standard timeline artefact to state the assumed offset per source and its basis.

**Anchors are not always available.** Where no event appears in two sources, the offset is genuinely uncertain, and the honest response — stating the uncertainty — makes the timeline look weaker.

**Tools smooth it away.** Timeline tools merge into a single chronological list, which implies a precision the underlying data does not have and conceals the reconciliation entirely.

**Precision differences are collapsed silently.** A source logging to the second and one logging to the millisecond are merged, and the resulting ordering within a second is arbitrary and looks authoritative.

**Nobody has been caught by it publicly.** The failure mode is quiet — a wrong ordering leading to a wrong inference — and would rarely be identified as the cause.

## What a Fix Looks Like

**Record the assumed offset and its basis per source.** A table in every timeline artefact: this source, this offset, established from this anchor event, with this residual uncertainty. Ten minutes of work and it makes the reconciliation reviewable and defensible.

**Propagate uncertainty into the timeline.** Where two events are within the combined uncertainty of their sources, their ordering is not established. Showing that visually — as an unordered group rather than a sequence — prevents an inference the data does not support.

**Flag sources with no anchor.** Where an offset could not be established, say so. An unanchored source is a known weakness and is currently invisible in the finished artefact.

**Collect clock configuration during evidence acquisition.** Time source, configured timezone, drift history where available. Gathered at collection, it removes most of the later inference and costs a field in the collection procedure.

**Never merge precisions silently.** Present a source's native precision, so a second-resolution event is not displayed as though it were ordered within a millisecond-resolution sequence.

**Review the reconciliation as part of peer review.** It is a step with a defensible basis or it is not, and reviewing the conclusion without reviewing the clock assumptions skips the assumption the conclusion rests on.

**Advise clients on time synchronisation in readiness work.** Consistent, logged, synchronised time across the estate is cheap, is a recognised hygiene item, and directly determines whether a future investigation can establish an ordering.

## Who Feels the Pain

The examiner, carrying clock assumptions in their head across a weeks-long investigation and unable to hand them over or defend them later without reconstruction.

The client, whose notification decision may rest on an ordering established through an undocumented inference.

The expert witness, asked in cross-examination how they know these two events occurred in this order, with no record of the reconciliation.

And the next examiner on the same engagement, who inherits a timeline and no statement of what it assumed.

## Impact If Fixed

A per-source offset table is ten minutes of work and converts an invisible assumption into a documented, reviewable, defensible one.

Propagating uncertainty so that events within the margin are shown as unordered prevents a class of inference the evidence does not support — which is exactly the kind of overstatement that damages expert credibility.

And collecting clock configuration at acquisition removes most of the later guesswork at the cost of one field in a collection procedure.
