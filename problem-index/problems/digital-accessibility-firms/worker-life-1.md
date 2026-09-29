# The Auditor Doing the Manual Pass

**Industry:** [[digital-accessibility-firms|Digital Accessibility Firms]]
**Type:** Worker Life Changing
**One-liner:** An expert works through a site keyboard-only, then with a screen reader, then again with a second screen reader, documenting each failure against a criterion, for weeks.
**Tags:** #transformers #large-language-models #cnns #gradient-boosting #evaluation-metrics #worker-facing #automation #tacit-knowledge-ml

## The Problem
The manual audit is the substance of an accessibility engagement. An auditor works through the defined scope with the keyboard alone, checking focus order, visible focus, traps and reachability; then with a screen reader, checking announcements, labels, landmarks, live regions and dynamic content; then frequently with a second screen reader and browser combination, because behaviour differs between them in ways that matter; then with magnification and often with voice control.

Each finding is recorded with its location, the criterion it fails, a description of what happens, a screenshot or recording, and a remediation recommendation. On a large site this runs for weeks and the documentation is a substantial share of it — writing the same description of the same pattern, in the same words, for the twentieth instance.

The multi-technology matrix multiplies everything. The same flow tested across three screen reader and browser pairings produces three sets of observations that mostly agree and sometimes diverge, and the divergences are where the useful findings are.

And the auditors are scarce. Genuine expertise here takes years to develop, the certification pipeline is small, and the same people are the only ones who can do the work that automation cannot.

## Why It Matters to the Worker
The expertise is in judgement — knowing which pattern will actually confuse a screen reader user, recognising an ARIA misuse that technically validates, understanding how a particular assistive technology behaves in an edge case — and it competes for time with documentation and repetition.

The repetition is heavy. The same component appears on hundreds of pages and the auditor documents it repeatedly because the report is organised by page. Practitioners describe the writing as the bulk of the work and the least valuable part of it.

Scarcity makes it worse. Because there are few qualified people, they are fully booked, and the parts of the job that would develop the field — training others, contributing to standards, researching new patterns — never happen. The pipeline stays small because the people who could widen it have no capacity.

## What a Solution Looks Like
Remove the repetition through component recognition. Identifying that a finding concerns a recurring component and documenting it once with its instances enumerated is an enormous reduction in writing and produces a better report — because a fix applied to a component resolves every instance.

Generate the documentation from the observation. An auditor should record what happened in whatever form is fastest — a short note, a recording — and the structured finding with its criterion mapping, description and remediation guidance should be drafted from it for review. The criterion mapping in particular is mechanical for experienced auditors and consumes real time.

Automate the traversal groundwork. Programmatic keyboard traversal, focus order extraction, accessibility tree capture and screen reader output capture across technology pairings can be run before the auditor starts, so the expert arrives at a prepared comparison rather than performing the mechanical passes themselves. The divergences between technology pairings — where the interesting findings are — can be surfaced directly.

Preserve the pattern knowledge. Experienced auditors carry a library of known patterns and their consequences that exists nowhere outside their heads, and capturing it as the corpus behind the drafting tooling is how the field scales beyond the number of people currently qualified.

## Impact If Solved
Auditor scarcity is the binding constraint on this entire industry, and a large share of a scarce expert's time goes to documentation and repetition. Component-level grouping, drafted findings and automated traversal groundwork return that time to judgement — which both increases how much can be audited and gives the field's most experienced people the capacity to train the people who are not yet in it.
