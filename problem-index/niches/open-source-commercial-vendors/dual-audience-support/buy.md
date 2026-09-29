# Knowledge Management Across Two Corpora

**Niche:** [[niches/open-source-commercial-vendors/dual-audience-support/profile|Dual-Audience Support]]
**Industry:** [[industries/open-source-commercial-vendors|Open Source Commercial Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Knowledge base generation from resolved tickets, semantic search and answer suggestion are standard support tooling, and open-source companies run two disconnected knowledge bases by hand.
**Tags:** #bert #word-embeddings #large-language-models #k-means-clustering #evaluation-metrics #confidence-intervals #cross-validation #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to let one answer serve both a paying customer and a public community without the support engineer holding the boundary personally — and whoever does that takes the support organisation, because that boundary is the job's defining discomfort.

## The Problem
Generating knowledge articles from resolved tickets, matching a new question to prior resolutions, and suggesting answers are all standard capabilities in the support tooling market. Open-source companies have two corpora — the contracted ticket history and the public issue and discussion archive — that contain overlapping answers to the same questions, and neither product searches the other.

## What Already Exists
Support knowledge management platforms with article generation from tickets; semantic search and question matching; answer suggestion; deduplication and clustering; and public issue tracker APIs. All mature and mostly already in use on one side of the boundary.

## The Customization Gap
The adaptation is to two corpora with different visibility rules. It requires: (1) a classification of what may cross, distinguishing generic technical content from customer-specific context, which is the safety property the whole thing depends on and is a text classification problem with an asymmetric cost — wrongly publishing a customer's configuration is a serious incident; (2) matching across corpora with different conventions, since a support ticket and a public issue are written very differently for the same underlying question and lexical matching will fail; (3) attribution and licensing of public content, since community contributions have authors and reusing them commercially without acknowledgement is a relationship problem; (4) a redaction step that is demonstrable rather than assumed, because the support organisation must be able to show what was checked before anything is published; and (5) bidirectional flow, since the public corpus is usually larger and contains resolutions the support team has never seen, which makes the community-to-support direction as valuable as the reverse and is the one nobody considers.

## Target Customer
Support platform vendors, open-source companies, and the community platform providers hosting the public corpus.

## Impact If Solved
The capabilities exist on one side of a boundary and the corpora on both sides contain the same answers. The may-it-cross classification is the safety property and the community-to-support direction is the underappreciated half.
