# Build: The Engagement Instrument

**Niche:** Technical Assessment
**Industry:** [[industries/fractional-cto-services|Fractional CTO Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An assessment instrument that turns a repository clone, an issue export and a delivery log into the picture a fractional CTO currently spends two weeks constructing by hand.
**Tags:** #gradient-boosting #time-series-forecasting #k-means-clustering #graph-neural-networks #evaluation-metrics #confidence-intervals #automation #worker-facing
**Contested on:** Whether the advisor's picture of the system is built from evidence the organisation already produces or from reading and asking.

## The Problem

A fractional CTO walks into an engagement with a fixed and short budget of days and an open-ended question: what is actually wrong here, and what should be done about it. The available method is to clone the repository and read, interview the engineers, sit in on a planning session, and form an opinion. That opinion then informs whether a system is rebuilt, whether a team is restructured, whether a company is acquired.

The method has a specific failure. Reading a codebase reveals its structure but not its dynamics — which parts change constantly and which have been stable for three years, where defects concentrate, which module every feature has to touch. Interviews reveal what people believe about the bottleneck, and people are systematically wrong about bottlenecks in ways that follow predictable patterns: the loudest pain is rarely the largest. Nothing in the method measures the gap between the two.

All of the dynamics are recorded. The repository knows exactly where change concentrates, over what period, by whom, and whether those files also attract the bug-fix commits. The issue tracker knows how long work sits in each state and where it stalls. The CI record knows how often builds break and how long recovery takes. The advisor is forming conclusions about a system whose own history answers most of the questions directly, and is not looking at it because there is no instrument that makes looking cheap.

## Why Nobody Has Built This

The buyer is small and fragmented. Fractional CTOs are largely independent practitioners and boutiques of three to fifteen people, and a tool sold to them competes against a habit that feels free — the practitioner is already billing for the reading time, so the instrument has to justify itself by making the assessment better rather than faster, which is a harder sale and a harder thing to demonstrate.

There is a status dimension the market is coy about. The value proposition of a fractional CTO is judgement, and judgement is sold on the premise that it cannot be systematised. A tool that derives the picture mechanically implies that a large part of the two weeks was mechanical. Practitioners are, reasonably, ambivalent about buying something that makes that argument on their behalf.

Engineering analytics vendors built for the opposite shape. Their products assume a team installing them on their own estate, gaining value as data accumulates over quarters, with metrics chosen to support continuous improvement. An advisory instrument needs a cold start — clone, import, answer in an afternoon — against an estate the buyer has no administrative rights to and will leave in eight weeks. Almost nothing in the analytics stack is designed for a transient outsider.

And the hard part is not computing the metrics. It is interpretation. Change concentration in a file means something different in a mature payments core than in a six-month-old prototype, and an instrument that reports numbers without that framing hands the practitioner more work rather than less.

## What to Build

An instrument that ingests a repository history, an issue tracker export and whatever CI and deployment record exists, and produces the evidence base for a technical assessment within hours of arriving.

The structural layer builds a map of the system from the code and the commit history together: modules, their dependencies, and — crucially — their co-change relationships, because files that always change together are coupled regardless of what the architecture diagram says. Coupling discovered from history is the finding most often absent from the client's own understanding, and it is the finding that decides whether a rebuild is bounded or not.

The concentration layer answers where effort goes. Change frequency weighted by complexity, defect-fix commits localised to files and modules, review burden, and the resulting ranking of which parts of the system consume disproportionate effort relative to their footprint. Mapped, where issue labels permit, onto business capability, so the output is "forty per cent of engineering effort in the last year went into billing and reconciliation" rather than a list of file paths.

The flow layer answers how work moves: state durations in the issue tracker, where items sit longest, batch sizes, how much work is in progress simultaneously per engineer, how often work is abandoned or reopened. The bottleneck the record shows, stated plainly next to what the interviews claimed.

The discrepancy layer is the product's actual argument. It takes the advisor's structured interview notes — what the team says is slow, what they say is fragile, what they say the plan depends on — and places each claim beside the measurement. Agreement is reassurance. Disagreement is where the engagement's value is, and it is exactly what an unaided practitioner is least likely to find, because the interviews are also their source of hypotheses.

Everything is scoped to run without production access, without an agent install, on data exportable in an afternoon by a client who has agreed to an assessment. Read-only, portable, and deletable at engagement end, because the alternative is a security review that outlasts the engagement.

## Target Customer

Independent fractional CTOs and boutique advisory practices of three to twenty people, where the assessment is the core deliverable and the practitioner is personally accountable for it. The private equity technical operating groups are a second and better-funded tier with the same shape of need and a sharper deadline.

The buying trigger is an engagement that went badly — an assessment that missed a coupling problem, a rebuild estimate that was wrong by a factor, a recommendation the client executed and regretted. Practitioners who have had one of those buy instruments; practitioners who have not, do not.

## Impact If Built

The assessment stops being bounded by how much code one person can read in two weeks. Coupling structure, effort concentration and flow bottlenecks arrive on day two rather than day nine, which leaves the days that remain for the part only a person can do: deciding what it means and what to do about it.

The discrepancy output changes the conversation with the client. Arriving at a management meeting with a measured account of where effort actually went, next to the account the team gave, is a different professional act from arriving with an opinion — and it is the thing that makes an uncomfortable recommendation survive contact with the people it implicates.

For the buyer of the engagement, the variance drops. The worst assessments are not the ones with bad judgement; they are the ones where the practitioner never found the thing that mattered because it was in a part of the system they did not read.
