# Fix: Nobody Knows When the Rule Was Last Checked

**Niche:** [[niches/remote-work-infrastructure/classification-and-determination/profile|Classification & Compliance Determination]]
**Industry:** [[industries/remote-work-infrastructure|Remote Work Infrastructure]]
**Type:** Fix (Pain Point)
**One-liner:** The internal note the determination rests on has no date, no author and no source, and the specialist reading it cannot tell whether it is current.
**Tags:** #compliance #descriptive-statistics #workflow-orchestration #evaluation-metrics #confidence-intervals #data-integration #quick-win #worker-facing
**Contested on:** Whether the guidance a determination rests on will carry a date and a source.

## The Problem

A compliance specialist determines whether an engagement in a particular country is acceptable. They consult the internal knowledge base. They find a page about that country's classification test.

The page has no last-verified date. It does not say which statute, case or guidance it derives from. It does not say who wrote it or when, or whether anyone has checked it since. It might have been written by someone who left two years ago, from advice received from local counsel four years ago, under a test that has since changed.

The specialist applies it, the determination is made, the green tick appears. Nobody in the chain — specialist, product, client — knows how old the underlying rule is.

## Why It's Still Broken

Knowledge bases accrete. Pages get written when a question arises, edited when something is noticed, and never systematically reviewed, because review is unfunded work against dozens of jurisdictions.

Dating the pages also makes the staleness visible, which produces an immediate backlog: forty countries whose guidance has not been verified in two years is a problem the moment you can see it, and not seeing it is cheaper this quarter.

And the guidance is not treated as a versioned artefact. It is a wiki, and wikis do not carry provenance unless someone decides they must.

## What a Fix Looks Like

Date every rule, cite its source, and show the staleness.

Add three fields to every guidance page: last verified on, verified by, and the primary source it derives from. Populating them retrospectively where possible and marking the rest as unverified is a week of work and it immediately produces the map of where the risk is.

Set a review cadence by volume and volatility. High-volume jurisdictions and those with active legislative change get reviewed quarterly; stable low-volume ones annually. Reviewing everything at the same frequency is what makes review unaffordable.

Show the staleness in the product. A determination relying on guidance verified eighteen months ago should say so, internally at minimum. A specialist who can see the vintage of what they are reading makes a different judgement about how much to rely on it.

Link to the primary source. A determination citing a statute or a piece of guidance is checkable; one citing an internal page is not. Adding the citation is the single highest-value field.

Route change alerts to the affected pages. A monitoring service alert about a country's contractor test should attach to that country's guidance and mark it for review, rather than arriving in someone's inbox.

And track the backlog as a metric. Jurisdictions unverified beyond their cadence, trending. It is the compliance function's true risk position and it is currently nobody's number.

## Who Feels the Pain

Compliance specialists, making consequential determinations from guidance whose age they cannot establish, and carrying the professional weight of it. Clients, who receive a green tick whose basis may be four years old. Workers, whose employment terms depend on it. And the platform, whose central product claim rests on a wiki.

## Impact If Fixed

Every determination's underlying rule acquires a date, an author and a source, which takes a week and makes the staleness visible for the first time. Review effort goes where volume and volatility are rather than uniformly. And the specialist making the judgement can see how much to trust what they are reading.
