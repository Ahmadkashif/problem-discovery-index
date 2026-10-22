# Sender Resolution Across Agents and Scripts

**Niche:** [[niches/money-service-businesses/msb-transaction-monitoring/profile|MSB Transaction Monitoring & SAR Operations]]
**Industry:** [[industries/money-service-businesses|Money Service Businesses]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Structuring detection is only as good as knowing that five spellings at four stores are one person, and MSBs do that linking by hand.
**Tags:** #k-nearest-neighbors #word-embeddings #graph-neural-networks #dbscan #evaluation-metrics #compliance #data-integration
**Contested on:** Every serious competitor in this niche is fighting to resolve each sender across agents, brands and name spellings into one person before a structuring alert is worked, and whoever resolves senders most accurately takes the account.

## The Problem
Monitoring rules aggregate by exact name and ID, so a sender who varies a spelling or an ID digit splits into several people and stays under thresholds, while an extended family sharing an address merges into one suspicious "sender". Analysts repair this case by case.

## Why Nobody Has Built This
Monitoring vendors built on bank data, where the account number resolves identity. Multilingual transliteration matching (Urdu, Arabic, Amharic, Bengali to Latin script) is a specialised problem, and the large transmitters that solved parts of it keep the work in-house.

## What to Build
A probabilistic identity graph over every transfer's sender and receiver fields — transliteration-aware name embeddings, ID and phone fuzzy matching, address normalisation, device links in app channels — clustered into persons with the evidence for each link shown, trained on analysts' historical merges and splits, and feeding the monitoring rules and the case timeline.

## Target Customer
BSA officers and monitoring leads at mid-sized and large transmitters.

## Impact If Built
Fewer false alerts on families, fewer missed structuring rings, and analyst time moved from linking records to deciding cases.
