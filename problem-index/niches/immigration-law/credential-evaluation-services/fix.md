# Country Expertise Sits in Analysts and Retires With Them

**Niche:** [[niches/immigration-law/credential-evaluation-services/profile|Foreign Credential Evaluation Services]]
**Industry:** [[industries/immigration-law|Immigration Law Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The person who understands how one country's education system actually works is one person, and the organization has no copy.
**Tags:** #tacit-knowledge-ml #large-language-models #graph-ml #worker-facing #data-integration

## The Problem
Evaluating credentials from a country well means understanding its education system historically: what the degree structures were before a reform and after, which accrediting authority governed which period, which institutions changed names or merged, how the grading scale actually maps in practice rather than on paper, which institutions have recognition that is nominal rather than real.

That understanding is held by country specialists — often one person per region, sometimes one person for several. They acquired it over years, partly from reference works and partly from thousands of documents and dozens of unusual cases they had to resolve.

Almost none of it is written down in a form the organization can use. There are reference books and there is a body of prior reports, and between them sits the specialist's actual working knowledge, which is what makes a hard case resolvable. When they retire, the organization's ability to evaluate that region degrades immediately and takes years to rebuild.

## Why It's Still Broken
The output format has no room for it. An evaluation report states a determination and its basis; it does not carry the analyst's understanding of why that country's 2011 reform makes a pre-2013 degree different from a post-2013 one. The reasoning is applied and discarded, report after report.

The reference material is external and static. Published comparative education resources exist, they are useful, and they lag reality and never cover the specific institution-level facts that decide cases. The specialist's knowledge is precisely the delta between the published reference and the real world, and nothing captures a delta.

And the work is relentless. Cap season and steady volume mean specialists are always behind, and documentation is the thing that yields. The organization also, quietly, benefits from specialists being irreplaceable, so nothing pushes against it.

## What a Fix Looks Like
Build the country knowledge base as a living structure the specialists maintain as part of doing the work.

**Country education systems as structured records.** Degree structures by period, governing authorities and their eras, grading scales with practical mapping notes, and the reforms that separate one period from another. Versioned by date, because the whole point is that a 2009 degree and a 2019 degree from the same country are different objects.

**Institutions as entities with history.** Recognition status over time, name changes and mergers, the programmes offered, and the organization's own determinations about them with dates and reasoning.

**Precedent cases attached to countries and institutions.** When a specialist resolves an unusual case, the resolution and its reasoning should attach to the country and institution so the next analyst finds it. This is the highest-value capture and it costs a few minutes at the end of a case the analyst has already worked out.

**Prompted capture rather than a documentation project.** A specialist deviating from the recorded determination is exactly the moment to ask why, in a structured field, in seconds. Asking someone to write down what they know about a country is a project that never happens; asking them to explain one deviation is a habit.

**Currency signals.** Determinations resting on a recognition status or a degree structure that may have changed should surface for review on a schedule. Today an outdated understanding persists until someone notices.

## Who Feels the Pain
Country specialists, who are single points of failure and cannot take leave without the queue for their region stalling. New analysts, who take years to become independent on a region. Leadership, holding a capability that depends on individual tenures. And applicants, whose evaluation quality depends on whether the right specialist was available.

## Impact If Fixed
Country expertise is the organization's product and its succession risk, and it currently has no copy. A structured, maintained knowledge base compresses the years it takes to develop a new specialist, makes determinations consistent across analysts and over time, and — with recognition and structure changes surfaced on a schedule — keeps the reference current in a domain where education systems reform continuously and the reference books do not keep up.
