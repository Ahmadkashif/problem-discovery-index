# Business Verification and Web Evidence Off the Shelf

**Niche:** [[niches/retail-pos-platforms/merchant-underwriting-risk/profile|Merchant Underwriting & Risk]]
**Industry:** [[industries/retail-pos-platforms|Retail POS Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Business registry verification, beneficial ownership data, sanctions screening and website content analysis are all commodity services, and merchant category misrepresentation is still caught by an analyst opening a browser tab.
**Tags:** #bert #large-language-models #cnns #evaluation-metrics #confidence-intervals #compliance #data-integration #automation
**Contested on:** Every serious competitor in merchant onboarding is fighting to approve a merchant in minutes at the same loss rate a week of manual review would produce — and whoever holds that trade-off best takes the volume.

## The Problem
A merchant applies as a general retailer. Their website sells products in a prohibited category, or is a template with no products at all, or is a clone of another merchant's site down to the photographs. An analyst who opens the site sees this immediately. At instant-onboarding volumes, an analyst does not open most sites, so the check that would catch the most common form of misrepresentation happens on a sample.

## What Already Exists
Business registry and beneficial ownership data is available through multiple commercial providers. Sanctions, politically exposed person and adverse media screening are commodity. Device and identity intelligence services are mature. Website content classification, template and clone detection, and image similarity are all ordinary capabilities. Consortium negative databases for payments exist. Every individual check is purchasable and most platforms already buy several of them.

## The Customization Gap
The adaptation is to evaluate the merchant's presented business rather than the applicant's identity. It requires: (1) website and social presence analysis as a first-class automated check — what is actually being sold, whether the site is functional, whether it is a template or a clone, whether the stated category matches the goods; (2) consistency checking across the evidence, since the strongest signal is usually a contradiction between the application, the registry record, the website and the bank account rather than anything in one of them; (3) tuning for the prohibited and high-risk categories that specific platform cares about, which differ by acquirer and by card network agreement and are not a generic list; (4) resolving the merchant against prior applications and terminated merchants, which is a graph problem of exactly the shape that appears in freight carrier vetting and is solved the same way; and (5) an explicit confidence output feeding a tiered decision — instant approve, approve with constrained exposure, or human review — rather than a binary, since the value is in shrinking the manual queue to the genuinely ambiguous.

## Target Customer
POS platforms, acquirers, ISOs and payment facilitators onboarding merchants at volume.

## Impact If Solved
Automated presence and consistency checking catches the most common misrepresentation at the speed instant onboarding requires, which is the specific trade-off this sub-niche is contested on. The entity resolution against prior terminated merchants is the highest-value single check and the one least commonly implemented.
