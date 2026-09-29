# Build: Capability Search and Coverage Measurement
 
**Niche:** [[niches/recruiting-tech-vendors/sourcing-and-discovery/profile|Sourcing & Candidate Discovery]]
**Industry:** [[industries/recruiting-tech-vendors|Recruiting Tech Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Search on what people have demonstrably done rather than on the words they used, and measure who the search is systematically failing to reach.
**Tags:** #word-embeddings #transformers #large-language-models #evaluation-metrics #confidence-intervals #k-nearest-neighbors #descriptive-statistics #automation
**Contested on:** Whether capability can be inferred from a profile well enough to find people whose vocabulary does not match.

## The Problem

Sourcing search matches vocabulary. A recruiter searches for a title, a set of skills and a company list, and gets people who used those words. Someone with five years of exactly the relevant experience, described in a different vocabulary — a different industry's terminology, an idiosyncratic title, a company nobody has heard of, a career built through routes the search's vocabulary does not cover — is not returned.

This failure is systematic rather than random. It disadvantages people who changed industries, who worked at small or foreign companies, who came through non-standard routes, whose first language is not English, and who are not on the platform being searched at all.

And it is invisible. The recruiter sees the results, not the absences. Response rates are measured on people contacted. No metric anywhere describes who the search did not reach.

## Why Nobody Has Built This

Keyword and boolean search is what recruiters know, what the tooling provides and what the training teaches. It is also fast and deterministic, which recruiters value.

Capability inference was not feasible until recently — reading a profile and determining what someone can actually do, rather than matching strings, is a language task that has only recently become cheap and reliable.

Coverage measurement is harder still, because measuring who you did not find requires a reference population, which is not in the database by definition. Partial approaches exist and nobody has assembled them.

## What to Build

Capability-based retrieval and an honest coverage measure.

**Extract capability, not keywords.** Read each profile and infer what the person has demonstrably done — the problems solved, the systems worked with, the scale operated at, the responsibilities held — as structured attributes independent of the vocabulary used to describe them. Generative extraction handles this well and is the substantive improvement over the current state.

**Search the capability space.** A query expressed as required capabilities rather than as keywords, matched semantically against the extracted attributes. The gain is exactly the population keyword search misses: equivalent experience described differently.

**Explain the match.** Which capability, evidenced by what in the profile. A recruiter presented with an unfamiliar title and no explanation will skip the candidate; one shown the evidence will look.

**Measure coverage against an external reference.** Compare the searched population's composition to labour market data for the role and geography — occupational statistics, licensure registries, professional bodies, published workforce data. Where the database's composition diverges sharply from the labour market's, the search cannot find those people and the recruiter should know.

**Surface the near misses deliberately.** Candidates who match on capability but not on the obvious filters — wrong title, unfamiliar company, adjacent industry, career gap — presented as a separate set rather than mixed in and buried. This is where the value of capability search actually lands.

**Track outreach coverage.** Who has been contacted, how often, by whom across requisitions. The concentration is usually extreme, and knowing it is the first step to broadening.

**Report the funnel from the top.** Population reachable, population searched, population contacted, population responded. Every recruiting funnel starts at applications, which is the second stage of the real one.

## Target Customer

Sourcing platform vendors, for whom capability retrieval is the substantive product improvement available and keyword search is commoditised. Also employers hiring for roles where the obvious pool is exhausted, and diversity-focused talent functions, for whom coverage is the measurement they currently lack entirely.

## Impact If Built

Search finds people whose relevant experience is real and described differently, which is a large population and the one keyword search systematically misses. Coverage becomes measurable against the labour market rather than against the database. And the funnel starts at who could have been reached rather than at who applied.
