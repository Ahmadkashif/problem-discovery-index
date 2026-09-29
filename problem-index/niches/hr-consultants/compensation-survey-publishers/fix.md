# The Job Architecture Is Maintained by the People Least Able to Question It

**Niche:** [[niches/hr-consultants/compensation-survey-publishers/profile|Compensation Survey Publishers]]
**Industry:** [[industries/hr-consultants|HR Consultants]]
**Type:** Fix (Pain Point)
**One-liner:** The taxonomy that defines every job in the economy is edited by the handful of people who have known it longest, using reasoning none of them writes down.
**Tags:** #tacit-knowledge-ml #graph-ml #large-language-models #worker-facing #data-integration

## The Problem
The benchmark architecture — job families, levels, definitions, and the rules for placing a job in one rather than another — is the firm's foundational asset. Everything the company sells is a cut of it.

It is maintained by a small group of very senior compensation methodologists. They know why the level distinction between two roles is drawn where it is, which definitions are historically load-bearing because major clients built their internal structures on them, which family was split in 2016 and what the market change was that forced it, and which benchmarks are quietly obsolete but retained because someone still buys them.

Almost none of this is documented. The architecture exists as definitions; the reasoning behind the definitions exists as institutional memory in perhaps five people. When one retires, the next person inherits a taxonomy full of decisions that look arbitrary and are not.

## Why It's Still Broken
The architecture changes slowly and deliberately, which makes documentation feel less urgent than it is. Consistency across years is a product feature — customers track their position over time and a reclassification breaks their history — so the culture is conservative, and conservative maintenance produces few artefacts.

The governance process compounds it. Changes are debated in committee, agreed, and implemented as edits to definitions. The debate is where the reasoning lives and the minutes record the decision. Two years later the definition is on file and the argument is gone.

And the incentive runs against writing it down. Being the person who knows why the architecture is shaped this way is a source of standing. Nobody is deliberately hoarding, but nothing pulls the knowledge out either.

## What a Fix Looks Like
Give the architecture a memory that outlives its maintainers.

**Every element carries its rationale.** Each benchmark, level boundary, and family split records why it exists, what alternatives were considered, which client structures depend on it, and when it was last revisited. This is a documentation discipline attached to the governance process that already exists, not a new process.

**Decisions as versioned records with evidence.** When a family splits, the record should hold the market change that prompted it, the matching data that supported it, and the customers affected. That turns a taxonomy edit into a reviewable artefact.

**Surface the evidence for review.** Benchmarks with declining incumbent counts, families with persistent matching ambiguity, level boundaries where matched jobs cluster oddly — these are all computable from the firm's own matching data and would tell the methodologists where the architecture is failing. They currently rely on noticing.

**Model the dependency graph.** Which customers, which published cuts, and which historical series depend on a given element. Today the impact of a proposed change is assessed by asking the person who remembers, which is exactly the dependency being described.

**Capture the debate, not just the outcome.** The committee discussion is the reasoning. Recording it against the element it concerns costs almost nothing and is the difference between a taxonomy and a set of arbitrary strings.

## Who Feels the Pain
The senior methodologists, who are the architecture's memory and cannot delegate. Newer analysts, who inherit rules that appear arbitrary and either follow them blindly or break something. Leadership, holding a foundational asset whose maintenance depends on a handful of tenures. And customers, whose internal job structures are built on definitions that could shift for reasons nobody can explain.

## Impact If Fixed
This is the asset the entire business rests on, and its maintenance is a succession risk with no mitigation. Making the reasoning explicit lets the architecture be maintained by more people, evolved on evidence rather than recollection, and changed with a real understanding of what breaks — which matters most precisely when pay transparency is forcing the taxonomy to grow faster than it ever has.
