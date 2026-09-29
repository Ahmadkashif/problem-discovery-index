# The Tacit Exclusions Every Analyst Knows

**Niche:** [[niches/bi-analytics-platforms/natural-language-query/profile|Natural Language Query]]
**Industry:** [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Every organisation's data has a dozen conventions that are applied to every correct query and written down nowhere — exclude the test accounts, the region field is unreliable before 2023, orders includes cancellations.
**Tags:** #tacit-knowledge-ml #word-embeddings #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #data-integration #quick-win
**Contested on:** Every serious competitor in conversational analytics is fighting to return an answer that is correct against a governed model and to refuse when the model cannot support the question — and whoever refuses well takes the account, because one confidently wrong answer ends the deployment.

## The Problem
A new analyst writes a query that looks right and returns a number that is wrong by four percent, because they did not exclude the internal test accounts that everyone who has been there a year excludes automatically. They find out in review, if they are lucky. This knowledge — perhaps twenty facts per organisation, each of the form "when you query X you must always do Y" — is the difference between a plausible query and a correct one, and it exists in the memory of a few long-tenured analysts, in scattered chat messages, and implicitly in the WHERE clauses of every query they have ever written.

## Why It's Still Broken
Nobody is assigned to write it down and it is invisible to the people who hold it, because it has become automatic — the classic shape of tacit knowledge, and the reason asking analysts to document it produces a short and incomplete list. Data catalogues have a description field for it that is empty or contains the column name restated. And the cost is diffuse: a new analyst's wrong number, an occasional bad decision, a self-service user quietly abandoning an attempt — none of which is attributed to the missing convention.

## What a Fix Looks Like
Recover the conventions from the queries that encode them. Mine the query log for filters and joins that appear with high consistency whenever a given table is used — a WHERE clause present in ninety-four percent of queries against the orders table is a convention, and finding it is a frequency count rather than a modelling exercise. Present the candidates to the analysts for confirmation and explanation, which is a far easier task than asking them to recall the list unprompted and is the step that makes this work. Record the confirmed conventions as first-class model content attached to the table or metric, so they surface in the catalogue, in the query editor, and in whatever grounds the natural language system. Flag queries that violate a convention at the point of writing, which is where the correction is cheap. And review them periodically, since conventions expire — "unreliable before 2023" stops mattering and "exclude the legacy region" becomes wrong when the legacy region is reactivated.

## Who Feels the Pain
New analysts producing confidently wrong numbers in their first months; long-tenured analysts who are consulted constantly because the knowledge is in them; and every self-service or conversational tool that produces plausible SQL missing the one clause that mattered.

## Impact If Fixed
The conventions are recoverable from the query log by frequency analysis, which requires no modelling, and confirming a candidate is far easier than recalling one. The same content improves the catalogue, the onboarding of analysts and the grounding of every natural language feature at once.
