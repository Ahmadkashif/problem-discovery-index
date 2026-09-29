# Best Practice as Prose Rather Than Checks

**Niche:** [[niches/database-platform-vendors/fleet-corpus-anti-patterns/profile|Fleet Corpus & Anti-Patterns]]
**Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Every vendor publishes a best practice guide, every support team has a knowledge base of recurring problems, and none of it runs against a customer's actual schema.
**Tags:** #bert #k-means-clustering #graph-theory #descriptive-statistics #evaluation-metrics #confidence-intervals #quick-win #automation
**Contested on:** Every serious competitor that gets here is fighting to warn a customer about a failure thousands of other customers have already had — and whoever does that holds a corpus of how databases actually fail that no single organisation can assemble.

## The Problem
The vendor publishes a thorough best practice document. It is accurate, comprehensive and read by almost nobody, and by nobody at all at the moment it would matter. The support knowledge base contains articles on the forty problems customers most commonly have, written by the engineers who have explained each of them hundreds of times. A customer whose schema exhibits three of those forty problems will discover them one at a time over the following two years, each as an incident, and will be sent the corresponding article after each.

## Why It's Still Broken
Best practice guidance is written by documentation and support teams as prose, which is the natural output of those functions, and converting it into executable checks requires engineering effort owned by neither. The checks would need access to the customer's schema, which managed vendors have and self-managed customers must grant. And the guidance is generic by necessity when written, whereas a check can be specific to the customer's actual structure, which is the entire difference between a document and a warning.

## What a Fix Looks Like
Convert the prose into checks that run. Take the support knowledge base and the best practice guide and encode each recurring problem as a check against schema structure, index definitions, query shapes and configuration — which is mechanical work with an immediate return, since the knowledge already exists and only its form is wrong. Run the checks continuously against every customer rather than offering them as a tool to be invoked, since the value is in the warning arriving unprompted. Rank the findings by the vendor's own observed incident rate for each pattern, which is information only the vendor has and which turns a list into a priority. Deliver them where they will be read — in the console, in the review, in the client — rather than in a report. Measure which checks fire and which precede incidents, which validates the catalogue and identifies the prose that was wrong. And feed the support queue back in continuously, since every recurring ticket is a check that does not yet exist and the queue is a standing specification for the next one.

## Who Feels the Pain
Support engineers writing the same article link for the hundredth time; customers discovering documented problems one incident at a time; and vendors whose accumulated knowledge is in a form that cannot act.

## Impact If Fixed
The knowledge exists and only its form prevents it from helping, which makes encoding it mechanical work with a direct return. Ranking by the vendor's observed incident rate is information nobody else has and converts a long check list into a short priority.
