# Every Dismissal Discarded

**Niche:** [[niches/software-supply-chain-security/dependency-corpus-intelligence/profile|Dependency Corpus Intelligence]]
**Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Type:** Fix (Pain Point)
**One-liner:** A security engineer's determination that a finding does not apply is the most expensive and most informative data the category produces, and it is stored as a suppression flag with a free-text note.
**Tags:** #bert #k-means-clustering #descriptive-statistics #evaluation-metrics #confidence-intervals #compliance #quick-win #automation
**Contested on:** Every serious competitor that gets here is fighting to use a fleet-wide record of dependency graphs, dismissals, fixes and upgrade outcomes — and whoever does that can estimate real exploitability, real upgrade risk and real remediation effort, which are the three questions every finding raises.

## The Problem
An engineer spends forty minutes determining that a vulnerability does not apply, and records it as a dismissal with a note reading not reachable. That note is the output of expert analysis and is stored as an unstructured string attached to one finding in one service in one customer. The same determination is made thousands of times across the industry for the same component, and every instance is a string in a different database. The category's most expensive and most informative signal is produced continuously and discarded.

## Why It's Still Broken
A dismissal is modelled as an action on a finding rather than as an observation about a component, because the tools are built around the finding list. The reasoning is free text because a structured taxonomy was never defined, which makes the determinations unanalysable even within one organisation. The exchange formats that would express them portably exist and are thinly supported. And nobody has framed the dismissal as data, so it is stored as an audit trail.

## What a Fix Looks Like
Capture the determination as structured data. Define a small taxonomy of dismissal reasons — not reachable, not exploitable in this configuration, test-only dependency, mitigated by a control, accepted risk — since the set is small and stable and a structured reason is analysable where a note is not. Require the evidence alongside the reason, which improves the determination's quality and makes it reviewable. Record it against the component and usage pattern rather than the finding instance, which is what makes it reusable and connects to the triage niche's reuse mechanism. Adopt the exchange formats so the determination is portable between tools and organisations. Analyse the dismissal distribution per component, which within one organisation identifies the components generating the most unnecessary work and across the fleet estimates real applicability. Distinguish a determination from a deferral, since accepting a risk and establishing inapplicability are entirely different and are currently both dismissals. And report dismissal rates by assessor and by evidence, since a dismissal with no evidence recorded in ten seconds and one with a reachability analysis are not the same observation and pooling them would corrupt everything built on top.

## Who Feels the Pain
Security engineers whose expert determinations vanish; organisations repeating analysis they have already done; and an industry making the same determination thousands of times about identical public components.

## Impact If Fixed
A structured reason taxonomy costs almost nothing and converts the category's most expensive signal from an audit note into analysable data. Recording against the component rather than the finding is what makes it reusable, and separating determination from deferral is what keeps the resulting estimates honest.
