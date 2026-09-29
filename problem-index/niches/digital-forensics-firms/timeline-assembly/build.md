# Build: Correlation Before Interpretation

**Niche:** Evidence Collection & Timeline Assembly
**Industry:** [[industries/digital-forensics-firms|Digital Forensics Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A correlation layer that resolves clocks, links related activity across sources into single events, and presents the examiner with a candidate sequence to interpret rather than millions of rows to merge.
**Tags:** #graph-theory #graph-neural-networks #change-point-detection #evaluation-metrics #confidence-intervals #k-means-clustering #automation #data-integration
**Contested on:** Whether a defensible sequence of events emerges from tooling, or from one examiner reconciling a dozen formats and three disagreeing clocks by hand.

## The Problem

An examiner has parsed output from fifteen sources covering an eleven-day intrusion. Millions of events. Several million are routine.

Their task is to find the sequence that describes what the attacker did and to establish it well enough to defend. That means correlating across sources — an authentication in the identity provider, a process execution on an endpoint, a network connection in the firewall log and a file write on a server are frequently one action seen four ways — and reconciling clocks that disagree by seconds or hours.

There is no tooling for the correlation. Timeline tools merge sources into one chronological list, which is necessary and is not correlation: the four rows describing one action remain four rows, in a list of millions, and the examiner recognises them as related through knowledge and attention.

So the most experienced person available spends days on mechanical correlation, and the interpretation they are actually there for happens in whatever time remains. The volume also forces filtering by intuition, which is where things get missed — the examiner filters to what looks relevant, and what looks relevant depends on the hypothesis they already have.

## Why Nobody Has Built This

**Every firm has built parsers and stopped.** Parsing is tractable and visible; correlation is harder and less obviously a product, so the tooling investment has gone to breadth of format support.

**Correlation rules are artefact-specific and numerous.** Knowing that this authentication event and this process creation are the same action requires knowing both artefact types in detail. Encoding that across every source pair is substantial knowledge engineering.

**Clock reconciliation is genuinely hard.** Sources disagree by unknown offsets, and establishing the offset requires an anchor event visible in both — which may not exist. Inference is possible and is uncertain, and an incorrect reconciliation produces a wrong sequence.

**Wrong correlation is worse than none.** An automated system that links unrelated events produces a false narrative that an examiner may not catch, and the consequence lands in a report that informs a notification decision.

**Examiners distrust automation on this.** The correlation is where their judgement lives, and tooling that appears to do it for them will be resisted unless it is transparently a suggestion.

**Firms compete on people, not tools.** Internal tooling is built as needed and not productised, so each firm rebuilds the same thing partially.

## What to Build

**Reconcile clocks explicitly and show the confidence.** Establish inter-source offsets from anchor events visible in multiple sources, state the residual uncertainty per source, and propagate it into the timeline so an examiner knows which orderings are certain and which are within the margin. Presenting the uncertainty rather than concealing it is what makes this usable.

**Correlate into candidate events, not conclusions.** Group rows across sources that plausibly describe one action, with the correlation basis shown and an easy way to reject. The examiner is confirming rather than assembling, which is where the time is saved and where their judgement still governs.

**Encode artefact knowledge as a shared reference.** What each artefact type means, what it proves, what it does not, and which other artefacts it co-occurs with. This is the field's tacit knowledge and it would help junior examiners more than anything else in this niche.

**Surface anomalies against the environment's own baseline.** Rather than filtering to what looks relevant, rank by unusualness relative to that organisation's normal activity. This addresses the filtering-by-hypothesis problem directly.

**Record the assembly as a reproducible artefact.** Which events were correlated, on what basis, with what clock assumptions. This makes the timeline reviewable now and defensible in litigation later, where currently it must be reconstructed.

**Keep the examiner in control and make rejection cheap.** Every correlation shown with its reasoning and rejected in one action. A system that hides its reasoning will be distrusted and abandoned, which is what has happened to previous attempts.

**Share the artefact reference openly.** The interpretation knowledge is not where firms compete and would benefit the whole field, including the smaller firms and the in-house teams who have the least of it.

## Target Customer

Forensics firms, sold on examiner capacity — correlation is the largest consumer of scarce expert time and the least dependent on expertise.

In-house incident response teams, who have the same problem with less tooling and fewer experienced examiners.

Forensic tooling vendors, for whom correlation is the obvious next layer above the parsing they have already solved.

## Impact If Built

Examiner attention moves from mechanical correlation to interpretation, which is both a better use of the scarcest resource in the industry and a faster route to the conclusion.

Explicit clock reconciliation with stated uncertainty addresses a known and largely unmanaged source of error in a sequence that litigation may later depend on.

And a reproducible assembly record would make a timeline defensible years later without the examiner reconstructing their reasoning from memory — which is currently how it works.
