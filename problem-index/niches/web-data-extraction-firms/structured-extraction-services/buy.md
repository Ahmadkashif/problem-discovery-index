# Information Extraction and Wrapper Induction

**Niche:** [[niches/web-data-extraction-firms/structured-extraction-services/profile|Structured Extraction Services]]
**Industry:** [[industries/web-data-extraction-firms|Web Data Extraction Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Wrapper induction and information extraction produced decades of methods for learning how to read a site's pages from examples, and model-based extraction reinvented the problem without reading any of it.
**Tags:** #transfer-learning #large-language-models #evaluation-metrics #graph-theory #cross-validation #hypothesis-testing #confidence-intervals #automation
**Contested on:** Every serious competitor in this sub-niche is fighting to return the right fields from a page nobody wrote a parser for, at a cost per page that beats the customer doing it themselves — and whoever does that takes the account, because the alternative is now genuinely available to the buyer.

## The Problem
Learning to extract structured records from a site's pages given a handful of labelled examples is wrapper induction, an extensively studied problem with methods for learning extraction rules, detecting when a wrapper has broken, and repairing it automatically. Information extraction more broadly has mature evaluation methodology and a large literature on structure-aware extraction. The current wave of model-based extraction largely started from scratch, and inherited neither the techniques nor the evaluation discipline.

## What Already Exists
Wrapper induction methods learning extraction rules from labelled examples; wrapper verification and automatic repair techniques; structure-aware extraction exploiting repeated page templates; information extraction evaluation methodology with per-field precision and recall; and template detection for identifying repeated regions across pages.

## The Customization Gap
The adaptation is to combine learned templates with a model that can read anything. It requires: (1) a hybrid where a learned template handles the common case cheaply and the model handles novelty and verification, since running a model on every page ignores that most pages are structurally identical to the last thousand — this hybrid is the central cost and accuracy adaptation; (2) wrapper verification techniques applied to model extraction, because the literature's methods for detecting a broken wrapper transfer directly to detecting silent breakage and are not being used; (3) automatic wrapper repair seeded by model output, which is a natural pairing and makes repair nearly free; (4) per-field evaluation discipline from information extraction, since the field measures precision and recall per field and the commercial practice quotes a single accuracy; and (5) template detection across customers extracting from the same sites, which is where the accumulated asset comes from and which the academic work did not need to consider.

## Target Customer
Extraction firms, data teams building their own, and the information extraction research community whose methods pair naturally with model-based approaches.

## Impact If Solved
Decades of wrapper induction and verification exists and the current wave started from scratch. A template-plus-model hybrid is the central adaptation for both cost and accuracy, and the literature's wrapper verification techniques transfer directly to detecting silent breakage.
