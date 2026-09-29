# The Same Question, Asked Eleven Ways

**Niche:** [[niches/bi-analytics-platforms/analyst-as-release-valve/profile|The Analyst as Release Valve]]
**Industry:** [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A large share of the questions analysts answer have been answered before, or are answerable from an asset that already exists, and nothing connects the incoming question to either.
**Tags:** #word-embeddings #bert #large-language-models #k-means-clustering #evaluation-metrics #confidence-intervals #worker-facing #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to make the estate answer the question so the analyst does not have to — and whoever measurably shrinks the ad hoc queue takes the analytics account, because that queue is the visible cost of everything the platform failed to deliver.

## The Problem
An analyst is asked how many enterprise accounts renewed last quarter. They know there is a dashboard, they know it needs one filter changed, and it takes four minutes to answer including the context switch. The same question, phrased differently, was answered in the same channel in March, in June and in August, by three different analysts, each of whom did not know about the others. Across a year this pattern is a meaningful fraction of the team's capacity, and it is invisible because each instance is four minutes.

## Why Nobody Has Built This
The queue lives in chat, which is not instrumented as a work system, so there is no dataset unless somebody constructs one. Matching a colloquially phrased question to a dashboard requires semantic matching over assets described by their titles, which nobody has attempted because the asset metadata is poor — titles like "Sales Dashboard v3 (new)" do not describe what question they answer. Analysts also under-report the load, partly because helping is part of the culture and partly because the individual instances feel trivial. And the tooling would have to live in the chat tool rather than in the BI platform, which is the wrong side of a product boundary for every vendor.

## What to Build
A layer between the question and the analyst. Capture questions where they are actually asked, in the chat channel, rather than requiring a form nobody will use. Match each incoming question against three things: previously answered questions with their answers, existing assets that cover it, and the semantic model's coverage — returning the best match with a confidence and, importantly, staying silent when it has nothing good, since a wrong deflection is worse than none and will end the tool's credibility in a week. Retain every answer an analyst gives as a reusable artefact, with the question, the answer and the query if there was one, which builds the corpus automatically from work that is happening anyway and is the mechanism that makes this improve. Cluster the queue to surface what the organisation repeatedly needs and does not have, which converts the queue from an interruption stream into a prioritised backlog for the data team. And describe assets by the questions they answer rather than by their titles, generated from their content and their query, which fixes the discoverability problem that causes most of the queue in the first place.

## Target Customer
Analytics leadership at organisations with a standing request queue, the BI vendors whose self-service gap this queue measures, and the data catalogue vendors for whom question-based description is a natural extension.

## Impact If Built
The repeat rate in these queues is high and entirely unexploited, and the corpus builds itself from work the team is already doing. Clustering the queue is the second output and converts the most-complained-about part of an analyst's job into the data team's roadmap.
