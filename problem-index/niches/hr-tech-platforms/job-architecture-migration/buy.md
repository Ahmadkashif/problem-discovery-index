# Title Normalisation and Classification Reference Data

**Niche:** [[niches/hr-tech-platforms/job-architecture-migration/profile|Job Architecture & Migration]]
**Industry:** [[industries/hr-tech-platforms|HR Tech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Job title normalisation against standard occupational taxonomies is a solved problem with public reference data and commercial products, and HCM implementations map titles by hand in a spreadsheet.
**Tags:** #bert #word-embeddings #k-nearest-neighbors #contrastive-learning #evaluation-metrics #confidence-intervals #data-integration #transfer-learning
**Contested on:** Every serious competitor in HCM implementation is fighting to infer an employer's job architecture and employment history from the data rather than rebuilding it from spreadsheets — and whoever shortens time-to-configured most takes the implementation.

## The Problem
Eleven hundred titles include "Senior Software Engineer II", "Sr. SWE II", "Software Engineer, Senior (II)" and "Engineer III — Software", which are the same job recorded four ways by four systems and four hiring managers. Separating that noise from the genuine distinctions — where "Senior" means something different in two functions, or where a title was inflated at hire — is the substance of the mapping work, and it is done by a consultant reading a list.

## What Already Exists
Standard occupational taxonomies — O*NET and the SOC system in the United States, ESCO internationally — are public, detailed and maintained. Commercial job taxonomy and skills libraries are available from several providers with mappings to compensation survey data. Job title normalisation is offered as a service by market data vendors. Text embedding models handle title similarity trivially. Skills extraction from job descriptions is a developed capability. The reference data and the matching technology are both entirely available.

## The Customization Gap
The adaptation is to an employer's internal architecture rather than to an external taxonomy. It requires: (1) two-stage mapping — noise reduction within the employer's own titles first, then mapping the resulting distinct jobs to an external taxonomy — since collapsing straight to a standard taxonomy loses the internal distinctions the architecture needs; (2) pay distribution as a disambiguator, because two titles that look identical and pay differently are different jobs and two that look different and pay identically usually are not, which is the most useful signal available and is absent from any text-based normalisation; (3) function-specific level semantics, since a "Director" in sales and in engineering are frequently not the same level and a global mapping will flatten them wrongly; (4) historical titles included, because the employment history being converted contains titles that no longer exist and mapping them is required for tenure, promotion and mobility analysis to work at all; and (5) confidence-gated review, so the consultant reviews the ambiguous minority rather than the full list, which is the difference between weeks and days.

## Target Customer
Implementation partners, HCM vendors, compensation and market data providers, and employers undertaking architecture rationalisation.

## Impact If Solved
Title normalisation is the largest single manual task in an HCM implementation and the reference data to automate it is public. Using pay distribution as a disambiguator is the specific adaptation that makes the result correct rather than merely tidy, and including historical titles is what makes the converted employment history analysable rather than merely present.
