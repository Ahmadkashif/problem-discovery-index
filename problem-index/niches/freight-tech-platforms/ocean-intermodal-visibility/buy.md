# Entity Resolution and Event Reconciliation Off the Shelf

**Niche:** [[niches/freight-tech-platforms/ocean-intermodal-visibility/profile|Ocean & Intermodal — Milestone Reconciliation]]
**Industry:** [[industries/freight-tech-platforms|Freight Tech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Reconciling the same event reported by multiple systems with different identifiers and vocabularies is a thoroughly solved problem in data engineering, and container tracking does it with hand-maintained mapping tables.
**Tags:** #bert #word-embeddings #graph-theory #k-nearest-neighbors #evaluation-metrics #confidence-intervals #data-integration #automation
**Contested on:** Every serious competitor in ocean and intermodal visibility is fighting to reconcile milestones reported by carriers, terminals, customs brokers and drayage providers into one true container timeline — and whoever produces the earliest correct availability and pickup signal takes the account.

## The Problem
The same physical container appears as a container number in one feed, a bill of lading number in another, a booking reference in a third and a house bill in a fourth, with the relationships between those identifiers held in the forwarder's system and nowhere else. The same physical event is called "discharged" by one carrier, "unloaded" by another and reported as a status code by a terminal. Mapping all of this is done by integration engineers maintaining tables, and every new carrier or terminal is a fresh project.

## What Already Exists
Entity resolution across identifier systems and schema mapping across event vocabularies are mature data engineering disciplines with substantial tooling, both open source and commercial. Standards exist in shipping — the Digital Container Shipping Association has published event and data standards intended for exactly this — and adoption is partial. Text and code mapping using embedding similarity is commodity. Everything required is available and most of the mapping work being done by hand could be done by a model with human review.

## The Customization Gap
The adaptation is to shipping's identifier structure and its partial standards. It requires: (1) an identifier graph linking container, booking, bill of lading, house bill, purchase order and equipment interchange references, built from the feeds themselves rather than maintained manually, since the relationships are visible in overlapping reports; (2) event vocabulary mapping to a canonical model — preferably the published industry standard — learned from observed sequences rather than hand-coded, with human confirmation; (3) per-source lag and reliability measured automatically per port and per event type, which is the input the reconciliation model needs and which nobody currently records; (4) terminal website scraping treated as a maintained data acquisition function with change detection, because terminals are a primary source, they change their pages, and a silent scrape failure looks exactly like a container that has not moved; and (5) graceful degradation, since coverage will always be partial and a product that implies completeness is worse than one that states what it does not know.

## Target Customer
Visibility platforms, freight forwarders maintaining their own integrations, and the larger importers who have built internal container tracking and are maintaining mapping tables by hand.

## Impact If Solved
Automated identifier and vocabulary reconciliation removes the integration engineering that currently gates coverage expansion, which is what allows a platform to add carriers and terminals at a pace the market needs. The per-source reliability measurement is the input the reconciliation model depends on and is produced for free once the mapping is systematic.
