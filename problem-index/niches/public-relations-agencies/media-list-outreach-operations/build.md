# Beat and Move Detection From Bylines

**Niche:** [[niches/public-relations-agencies/media-list-outreach-operations/profile|Media List Building & Outreach Operations]]
**Industry:** [[industries/public-relations-agencies|Public Relations Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A reporter's published work shows a change of beat or outlet weeks before any database record changes, and nobody reads it that way.
**Tags:** #word-embeddings #k-means-clustering #logistic-regression #evaluation-metrics #automation #data-integration
**Contested on:** Every serious competitor in this niche is fighting to keep every pitch list current to the week as reporters change beats, outlets and status, and whoever holds the freshest verified map of who covers what wins the database renewal.

## The Problem
A retail reporter starts writing about logistics and labour; a business reporter's byline disappears from one outlet and appears on a newsletter platform; a technology writer goes freelance and starts filing for three outlets. Database records change when a researcher next verifies the contact, which can be months later. Pitches in between go to the wrong desk.

## Why Nobody Has Built This
Database vendors verify by calling and emailing, a labour model built before cheap text embeddings. Their research teams are measured on records verified, not on time-to-detect a change.

## What to Build
A detection layer over every byline the monitoring feed already ingests: resolve reporter identities across outlets and newsletters, cluster each reporter's recent articles to track beat drift, flag disappearance and reappearance of bylines, combine with bounce and auto-reply signals from outreach, and push ranked "probably changed" alerts into the research team's verification queue.

## Target Customer
Data and research leads at media database vendors; large agencies maintaining their own verified lists.

## Impact If Built
Changes caught in days rather than months, with research effort spent on the records most likely to be wrong.
