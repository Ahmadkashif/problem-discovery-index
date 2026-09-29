# Support Deflection for an Internal Product

**Niche:** [[niches/internal-developer-platforms/platform-engineer-support/profile|The Platform Engineer]]
**Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Customer support solved question deflection, knowledge reuse and queue measurement a decade ago, and internal platform teams run their support in a chat channel with no instrumentation at all.
**Tags:** #bert #word-embeddings #large-language-models #k-nearest-neighbors #evaluation-metrics #confidence-intervals #worker-facing #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to stop a platform team being the help desk for its own abstractions — and whoever does that takes the platform function, because that support load is what prevents the platform improving.

## The Problem
An inbound stream of repetitive questions, a knowledge base that could answer many of them, and a skilled team whose time is the constraint — this is the customer support problem, and the product category that solves it is mature. Internal platform teams, facing an identical problem at a smaller scale with a captive audience, have a chat channel and a wiki.

## What Already Exists
Support platforms with deflection and suggested answers; retrieval over a knowledge base; question similarity and intent classification; article generation from resolved conversations; and chat-integrated support bots. All mature and mostly already licensed by the same company for its external support.

## The Customization Gap
The adaptation is to an internal audience with a technical, context-heavy question set. It requires: (1) answering from the platform's live state rather than only from documentation, since many questions are about this service's specific configuration and a generic answer is useless — which means the answering layer needs read access to the catalogue, the configuration and the deployment record; (2) chat-native operation, because the queue lives there and a portal will not be adopted by colleagues who are blocked; (3) a high bar for answering, since a wrong answer to a colleague who then acts on it is worse than no answer and the relationship is ongoing rather than transactional — silence with a routing to a human is the correct low-confidence behaviour; (4) capture of human answers as the corpus, since the platform's documentation is incomplete by definition and the real answers are in the channel history; and (5) honest deflection measurement, avoiding the failure this vault documents elsewhere where somebody giving up counts as a success.

## Target Customer
Platform engineering teams, internal developer platform vendors, and the support platform vendors for whom internal technical teams are an unserved segment.

## Impact If Solved
A mature product category addresses this exact problem at larger scale, and the internal version has none of it. Answering from live platform state is the adaptation that makes the answers useful, and capturing human answers is what builds a corpus the documentation never will.
