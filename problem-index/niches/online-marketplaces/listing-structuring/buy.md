# Attribute Extraction and Taxonomy Management

**Niche:** [[niches/online-marketplaces/listing-structuring/profile|Listing Structuring]]
**Industry:** [[industries/online-marketplaces|Online Marketplaces]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Product information management and attribute extraction are mature disciplines in retail, and marketplaces ask amateur sellers to do the work by hand.
**Tags:** #large-language-models #word-embeddings #cnns #evaluation-metrics #automation #graph-theory #transfer-learning #data-integration
**Contested on:** Every serious competitor in this niche is fighting to turn an amateur's photograph and paragraph into the structured attributes everything downstream depends on — and whoever does that takes the account, because search, pricing, matching and recommendation all rest on structure the seller never provided.

## The Problem
Retail solved product information: a managed taxonomy with defined attributes per category, extraction from supplier feeds and descriptions, governance over the values, and enrichment services that fill the gaps. The discipline exists with products, practitioners and standards. Marketplaces have the same need with a harder input — amateur text and photographs instead of supplier feeds — and mostly handle it with a form.

## What Already Exists
Product information management platforms with taxonomy and attribute governance; attribute extraction from unstructured product text; image-based attribute recognition in retail; taxonomy mapping and reconciliation tooling; data quality rules for attribute values; and enrichment services filling gaps from reference data.

## The Customization Gap
The adaptation is to an input written by the seller rather than by a manufacturer. It requires: (1) extraction robust to amateur language, where a retail extractor expects specification-style text and a marketplace gets conversation — which is exactly what language models handle and what the previous generation of extractors could not; (2) images as a primary source rather than as a supplement, since for used and handmade goods the photograph carries what no feed would have; (3) a taxonomy derived from how buyers search rather than designed by category managers, which the fix note develops and which is the difference between a tree that works and one that does not; (4) confidence and provenance per attribute, since an extracted value and a seller-asserted one carry different weight and downstream systems should know which they have; and (5) continuous re-extraction as models improve, because the back catalogue was extracted with whatever was available at the time and is worth revisiting.

## Target Customer
Marketplace catalogue and search teams, product information vendors for whom marketplaces are an adjacent market, and the sellers relieved of a form.

## Impact If Solved
Retail solved this for supplier feeds and marketplaces have a harder input and a form. Language models handle amateur prose in a way the previous extractor generation could not, and images are the primary source for exactly the goods marketplaces specialise in.
