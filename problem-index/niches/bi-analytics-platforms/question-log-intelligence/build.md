# The Record of What the Business Asks Itself

**Niche:** [[niches/bi-analytics-platforms/question-log-intelligence/profile|Question Log Intelligence]]
**Industry:** [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every analytics platform holds a complete record of how its customer's organisation questions itself, and every one of them uses it for billing.
**Tags:** #word-embeddings #bert #k-means-clustering #change-point-detection #graph-theory #evaluation-metrics #confidence-intervals #automation
**Contested on:** Every serious competitor that gets here is fighting to turn the record of how an organisation questions itself into a product — and whoever does that takes a position no competitor can copy, because the query log is the one asset each platform holds exclusively.

## The Problem
A data team plans its quarter from a backlog of requests, which is a record of who asked loudest rather than of what the organisation needs. Meanwhile the platform holds four million query events from the last year: what was looked at, by whom, how often, which filters, which drill-downs, which explorations were abandoned after three steps. That log would answer what the organisation actually cares about, which questions it keeps asking that nothing answers well, and what changed in June when a whole department started slicing by a dimension they had never used. Nobody has looked, at any organisation, on any platform.

## Why Nobody Has Built This
Logs are retained for audit and consumption billing, and the teams who own them are platform engineers rather than analysts, so the log has never been anybody's dataset. The analysis also requires mapping queries to business questions, which is a semantic step nobody has framed. There is a mild organisational discomfort as well, since analysing what people look at is adjacent to surveillance and the careful answer — aggregate and question-level rather than person-level — has not been articulated by anyone, so the topic gets avoided rather than designed. And vendors have not built it because it does not demo like a chart.

## What to Build
The question log as a product. Map queries and dashboard interactions to business questions using the assets' semantics, the filters applied and the language in titles and descriptions, which turns a stream of SQL into a stream of concerns. Cluster the concerns, and report what the organisation asks about most, which is rarely what its dashboards emphasise. Detect coverage gaps from the behavioural signature of not finding an answer — repeated reformulation, abandoned drill-downs, an export followed by an analyst request — which identifies what the estate cannot answer without anybody filing a ticket. Detect shifts over time with change-point methods, because a department that starts slicing by a new dimension is telling the data team something weeks before it becomes a request. Feed all of it into the roadmap, so the data team builds against measured demand rather than against the backlog of the loudest. And design it aggregate-first and question-first from the start, with individual-level analysis available to the individual and not to management, which is the same posture this vault takes to people analytics and to invisible contribution work, and for the same reasons.

## Target Customer
Data leadership planning against demand rather than requests, and the BI vendors, for whom this is the only genuinely uncopyable asset they hold.

## Impact If Built
The dataset is complete, exclusive and untouched, which is a rare combination. Coverage-gap detection from abandonment behaviour is the most immediately useful output, since it names what the estate cannot answer without anyone having to complain.
