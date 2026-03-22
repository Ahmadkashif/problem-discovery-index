# Spectora Multilingual Report Module

**Niche:** [[niches/home-inspection/non-english-homebuyers/profile|Non-English Homebuyers]]
**Industry:** [[industries/home-inspection|Home Inspection]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Spectora generates polished, interactive inspection reports exclusively in English — adding a one-click translation feature that converts the complete report into the buyer's language using inspection-domain-trained translation would make Spectora the first inspection platform to serve the 22% of homebuyers who speak a non-English language at home.
**Tags:** #seq2seq #data-integration #quick-win #automation #large-language-models

## The Problem
Spectora's interactive web-based reports are the most polished in the industry — buyers can filter by severity, view photos with annotations, and navigate by system category. But the entire interface is English-only: navigation labels, category names, severity indicators, inspector narratives, and summary sections. A Spanish-speaking buyer navigating a Spectora report sees "Major Defect" instead of "Defecto Grave," "Recommend Repair" instead of "Se Recomienda Reparación," and a paragraph of technical English describing the specific issue. The interactive features that make Spectora best-in-class are wasted on a buyer who can't read the interface.

## What Already Exists
Spectora's architecture separates content from presentation — inspection data is structured (categories, items, comments, photos, severity ratings) with a rendering layer that produces the interactive report. This architecture is well-suited for translation: the structured elements (labels, severity ratings, category names) can be translated from a fixed dictionary, while the narrative comments (inspector-written text) require dynamic translation. Spectora already supports template customization, suggesting the infrastructure for language-variant templates exists.

## The Customization Gap
A multilingual module that: (1) translates all static UI elements (navigation, categories, severity labels, section headers) from a curated translation dictionary maintained by Spectora; (2) translates inspector-written narrative comments using a domain-trained translation model with an inspection terminology glossary; (3) generates a dual-language report option where each finding shows both English (for the agent and for legal record) and the target language (for the buyer); (4) translates the summary page and repair recommendation sections with particular care for accuracy, since these drive buyer decisions; and (5) offers the buyer a language selector at the top of the interactive report, allowing them to toggle between English and their preferred language. Initial launch in Spanish (serving 60% of the non-English market), with Mandarin and Korean as phase 2.

## Target Customer
Spectora as a platform seeking competitive differentiation and market expansion. Inspectors in multilingual markets (top 20 US metros) who lose referrals because they can't serve non-English-speaking buyers. Real estate agencies serving immigrant and non-English-speaking communities.

## Impact If Solved
Positions Spectora as the first multilingual inspection platform, capturing market share from competitors in the 20+ metros where non-English buyers represent 25-40% of transactions. Increases per-inspection revenue by $50-100 for the translation feature. Opens referral partnerships with real estate agencies serving non-English-speaking communities. Reduces fair-housing-related concerns about language barriers in the home buying process.
