# Name Matching Adapted to Adversarial Transliteration

**Niche:** [[niches/customs-brokers/sanctions-screening-data-providers/profile|Sanctions & Restricted Party Screening Data]]
**Industry:** [[industries/customs-brokers|Customs Brokers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Fuzzy matching libraries handle typos; here the variation is generated deliberately, across scripts and naming conventions, by parties whose objective is that the match fails.
**Tags:** #contrastive-learning #bert #transformers #word-embeddings #evaluation-metrics #probability-distributions #confidence-intervals #feature-engineering #compliance #automation

## The Problem
Screening quality is decided by name matching, and the failure modes run in both directions with severe consequences. Too loose and every shipment generates alerts that a compliance team must clear, which in practice means a real match is buried in noise. Too tight and a designated party passes under a transliteration variant. The variation is not random noise: the same Arabic, Cyrillic, or Chinese name has many legitimate romanizations, naming conventions differ in how many components exist and which are surnames, corporate suffixes vary by jurisdiction, and adversarial parties select variants specifically because they defeat matching. Thresholds are tuned by hand and the tuning is a compromise nobody can evaluate.

## What Already Exists
Name matching is a well-served problem. Established libraries handle phonetic algorithms and edit distance; commercial matching engines from the screening vendors themselves and from specialist providers offer configurable scoring, cultural name handling, and threshold management. Every screening platform ships with something workable.

## The Customization Gap
Most available approaches score string similarity, sometimes with cultural rules layered on. What is needed is a model of name equivalence learned from confirmed matches across scripts and naming systems, where similarity is defined by whether two strings denote the same person or entity rather than by how they look. That requires labelled equivalence data, which the vendor uniquely possesses in its own research history — every time an analyst confirmed that a variant referred to a designated party, that was a labelled pair, and those are stored as profile aliases rather than as training data. The adaptation is a matching model trained on that history, with per-population calibration, since matching behaviour differs fundamentally between Arabic personal names, Chinese corporate names, and Latin-script entities. Confidence must be calibrated rather than scored, so a compliance team can set a threshold that means something. And adversarial variation deserves explicit treatment: variants designed to evade differ systematically from ordinary transliteration noise, and the vendor's own history contains examples of both.

## Target Customer
Heads of screening technology and research operations at data providers, and the sanctions compliance leaders at brokers and importers who tune alert thresholds by feel and clear the resulting volume by hand.

## Impact If Solved
Attacks both failure modes at once — false positive volume, which is the compliance team's daily burden, and false negatives, which are the enforcement exposure. Calibrated confidence also lets a customer set a defensible threshold and document why, which is exactly what a regulator asks after a miss.
