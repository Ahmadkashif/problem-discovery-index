# The Author's Judgment Is the Product and It Is Stored as Prose

**Niche:** [[niches/urgent-care/clinical-reference-decision-support/profile|Clinical Reference & Decision Support Content Publishers]]
**Industry:** [[industries/urgent-care|Urgent Care]]
**Type:** Fix (Pain Point)
**One-liner:** A physician author weighs conflicting trials and a contested guideline and produces a paragraph; the reasoning that produced it is not recorded anywhere.
**Tags:** #tacit-knowledge-ml #large-language-models #evaluation-metrics #compliance #worker-facing

## The Problem
What a clinical reference publisher actually sells is expert judgment: an experienced physician deciding what the evidence supports when the trials disagree, when the guideline is contested, when the population studied is not the population in front of the reader, and when the honest answer is that nobody knows.

That judgment is delivered as prose with citations. The reasoning behind it — which studies were considered and set aside, why one guideline was followed over another, what the author thought about applicability, and what evidence would change the recommendation — is not captured in structured form.

Three consequences follow. Consistency across the corpus is unmeasured: two authors handling comparable evidence in adjacent specialties may grade differently, and nothing surfaces the divergence. Defensibility depends on reconstruction: when a health system or a plaintiff's expert asks why a recommendation reads as it does, someone re-derives it. And succession is a live problem, because the authors carrying decades of clinical and methodological judgment are senior physicians and the pipeline behind them is thin.

It also blocks the automation the category now needs. A model that proposes content revisions requires training examples of the form "this evidence, this decision, this reasoning". The decisions exist in the revision history; the reasoning does not.

## Why It's Still Broken
The output format was fixed by the medium. A reference topic is prose because clinicians read prose, every downstream consumer is satisfied by the paragraph, and nothing in the pipeline creates pressure to record more.

Author time is the scarcest resource in the business. Practising physicians write these topics alongside clinical work, and asking for structured rationale on top of the writing is asking for the thing they have least of.

And there is real caution about recording deliberation in a product with clinical liability exposure. A written record of authors debating whether the evidence supports a recommendation is discoverable. The safe institutional habit has been to publish the conclusion.

## What a Fix Looks Like
**Capture the decision, not an essay.** For each graded recommendation: the key evidence relied on, the evidence considered and set aside with a one-line reason, the applicability caveat, and what would change the grade. Minutes per recommendation, inside the revision workflow that already exists.

**Store the "what would change this" field deliberately.** It is the single most valuable field, because it converts monitoring from a general watch into a specific trigger — the literature can be searched for exactly the evidence the author said would matter.

**Make prior decisions retrievable by evidence pattern.** Authors reason by analogy to how comparable evidence situations were handled elsewhere in the corpus. A retrieval layer over past decisions is immediately useful, which is what determines adoption.

**Measure consistency deliberately.** Route the same evidence package to several authors and compare the grades. It is uncomfortable and it is the only way to know whether the grading scale means the same thing across the corpus — and it produces the calibration set any automated grading would need.

**Feed it upward.** The decision record is the supervision for automated revision proposal, which is the highest-value automation available here and is impossible without labelled examples of how ambiguous evidence gets resolved.

**Settle the discoverability question first.** Decide with counsel what is recorded and in what form. The current default — record only conclusions — also means the publisher cannot demonstrate a rigorous, consistent editorial process, which is its own exposure and is about to matter a great deal more.

## Who Feels the Pain
Senior physician authors, who are the product and cannot scale; junior authors, who learn the house standard by apprenticeship the organisation cannot supply at volume; clinicians, who receive a graded recommendation with no visible basis and cannot distinguish strong synthesis from conservative default; and the publisher, whose deepest asset against fluent generative competition is a body of judgment whose consistency it has never measured.

## Impact If Fixed
The publisher's most valuable and least durable asset — decades of physician judgment about what the evidence supports — becomes an institutional record rather than a set of careers. Consistency becomes measurable, the editorial process becomes demonstrable, and the labelled corpus that any automation of clinical synthesis requires comes into existence as a by-product of work that is happening anyway.
