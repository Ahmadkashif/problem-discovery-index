# Period-Aware Shot Search Trained on Past Licences

**Niche:** [[niches/film-distributors/stock-and-archival-footage-licensing/profile|Stock & Archival Footage Licensing]]
**Industry:** [[industries/film-distributors|Film Distributors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Generic visual search finds "a car factory"; an archive's client needs a 1964 Detroit assembly line in colour, and only the researcher's eye currently tells the decades apart.
**Tags:** #tacit-knowledge-ml #contrastive-learning #transformers #cnns #transfer-learning #evaluation-metrics #automation
**Contested on:** Every serious competitor in this niche is fighting to put a clearable clip of exactly the shot a producer asked for in front of them within hours, and whoever answers the research request first with footage that clears takes the licence.

## The Problem
Experienced archive researchers date footage by film stock, car models, clothes, signage and camera style, and know which reels hold which events. Requests specify period and place precisely, and a wrong-decade clip loses the licence. Off-the-shelf models recognise objects but not decades.

## Why Nobody Has Built This
Archives are small businesses with no ML staff. Their training signal (which clips were licensed against which requests) sits in invoices and email, and legacy footage degrades generic models.

## What to Build
Shot-level indexing of the collection with vision-language embeddings. The models are fine-tuned on the archive's own history of requests and licensed clips, with auxiliary period and location classifiers trained from catalogue dates. Researchers query in plain language or by example, and each kept or rejected candidate becomes a training label.

## Target Customer
Archive directors and heads of licensing at historical footage libraries, news archives and film libraries with digitised collections.

## Impact If Built
Requests answered in minutes rather than hours, more licences won against slower archives, and the researcher's period knowledge captured in the index rather than lost at retirement.
