# Process Discovery From the Platform's Own Corpus

**Niche:** [[niches/work-collaboration-tools/template-and-process-content/profile|Template & Process Content]]
**Industry:** [[industries/work-collaboration-tools|Work Collaboration Tools]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Clustering structured objects by shape and discovering process variants from event data are mature techniques, and template libraries are built by writing down what somebody thinks a process looks like.
**Tags:** #k-means-clustering #graph-theory #dimensionality-reduction #bert #evaluation-metrics #confidence-intervals #hypothesis-testing #descriptive-statistics
**Contested on:** Every serious competitor in onboarding content is fighting to give a team a starting structure that matches how that team actually works — and whoever produces a template teams keep past the first month takes the adoption problem.

## The Problem
A content team writing a template for a hiring process interviews a few customers, reads some material, and produces a structure. The platform contains tens of thousands of hiring workflows in active use, with their stages, their field sets, their durations and their outcomes. Discovering the variants in that corpus and characterising which ones work is a clustering exercise of entirely ordinary difficulty, and the template is written from three interviews.

## What Already Exists
Structural clustering, graph similarity, dimensionality reduction over categorical and structural features, and process variant discovery are all mature with free implementations. Process mining's variant analysis addresses exactly the question of how many genuinely different ways a process is executed. Embedding-based similarity over text handles the naming variation. Everything required is standard and the corpus is unusually clean.

## The Customization Gap
The adaptation is to workspace structures rather than to event logs. It requires: (1) a structural representation that captures what matters — stage sequence, field semantics, relationship shape, automation patterns — while being robust to naming, since two teams calling the same stage different things is the normal case and a naive comparison will treat them as different processes; (2) process category classification first, since clustering across all workspaces produces nothing and the meaningful clusters exist within a process type; (3) outcome definition, which is the hard part — a structure that is still in use after six months and whose items complete rather than accumulating is a reasonable proxy and should be stated as a proxy rather than as success; (4) privacy by construction, using structure and metadata only and never content, which makes the analysis disclosive of nothing and is a position the vendor should be able to state plainly; and (5) sufficient cohort sizes before publishing a pattern, since a structure observed in four teams is an anecdote and the whole point is to replace anecdote with observation.

## Target Customer
Work management platform vendors with large installed bases, and the process mining and analytics vendors for whom this corpus is an unexploited adjacent domain.

## Impact If Solved
The corpus is the platform's unique asset and the templates are its least evidence-based product, which is an unusual combination. Structure-only analysis is both sufficient and non-disclosive, which removes the main obstacle to using cross-customer data here and makes this one of the safer corpus-based capabilities in this vault.
