# Personal Data Classification

**Parent Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Category:** Contested Sub-Niche
**Contested on:** Whether a system can determine that data is personal, whose it is, what category it falls into and on what basis it is processed — or whether that remains a lawyer's judgement about meaning.

## Profile

**Market Size:** ~$560M
**Share of Parent Industry:** ~8%
**Digital Adoption:** Low — pattern matching over structured stores
**Target Buyer:** Privacy counsel, privacy engineering, data governance
**Automation Potential:** High for identification, low for basis and purpose

## What Makes This a Distinct Niche

This is the interpretive half of the map. Observation establishes that a column exists and that its contents move to a particular destination. Classification asks what it is: personal data or not, whose, which category, under which lawful basis, for which purpose, subject to what retention.

None of that is settled by measurement. A column of integers may be a customer identifier — personal data by linkage — or a product count. A free-text field may contain anything. A postcode alone is not personal data and a postcode with a birth date frequently is, because identifiability is a property of the combination and of what else the holder can access. And lawful basis and purpose are legal determinations about the organisation's intent, which no scanner can observe at all.

That interpretive character is what separates it from [[niches/privacy-tech-vendors/data-flow-observation/profile|🎯 Data Flow Observation]], which is a systems problem answerable in weeks by instrumentation. Classification is a semantic and legal problem, partially automatable and irreducibly dependent on judgement, and a vendor can ship excellent flow observation while classification remains a wizard over regular expressions — which is approximately where the category is.

## Current Tools & Gaps

Pattern-based scanning for recognisable formats — email addresses, card numbers, national identifiers — across databases, warehouses and file stores. Some machine learning classifiers for less structured content. Classification taxonomies mapped to regulatory categories. Manual tagging in data catalogues. Lawful basis and purpose recorded in the record of processing as free text entered by a privacy manager.

The gaps are where meaning lives. Identifiability by linkage is barely handled, so the identifier columns that make a dataset personal are frequently missed while the obvious email column is found. Unstructured content — documents, logs, free-text fields, message bodies — is where a great deal of personal data actually sits and is covered worst. Special category data requires understanding that a field implies health, belief or sexuality rather than matching a pattern. Whose data it is, which matters enormously for fulfilling requests, is rarely determined. And lawful basis and purpose are typed into a form by one person and attached to systems they have never seen.

## Problems

- [[niches/privacy-tech-vendors/personal-data-classification/build|🔨 Build: Identifiability, Not Pattern Matching]]
- [[niches/privacy-tech-vendors/personal-data-classification/buy|🛒 Buy: Disclosure Control From Statistical Agencies]]
- [[niches/privacy-tech-vendors/personal-data-classification/fix|🔧 Fix: Lawful Basis Is a Dropdown Someone Filled In]]
