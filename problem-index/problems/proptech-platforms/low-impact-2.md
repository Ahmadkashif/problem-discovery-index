# Jurisdiction-Specific Screening Compliance

**Industry:** [[proptech-platforms|Proptech Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Tenant screening is an outsourced commodity and the rules governing what a landlord may consider now differ by state, county and city — configured per property by managers who are not lawyers, in software that ships one national default.
**Tags:** #large-language-models #bert #transformers #word-embeddings #change-point-detection #transfer-learning #compliance

## The Problem
Screening a rental applicant means checking credit, income, rental history and, where permitted, criminal history and eviction records. What is permitted has fragmented dramatically. Jurisdictions differ on whether criminal history may be considered at all and for how far back, whether an individualised assessment is required before denial, whether housing vouchers and other non-wage income must be treated as income, what application fees may be charged, whether records of sealed or dismissed matters may be used, and what notice a denied applicant must receive.

These rules change frequently, apply at city level as often as state level, and carry real liability — fair housing enforcement and private litigation both. The property manager configuring screening criteria in the software is a site-level employee with no legal training, choosing from a settings page that ships a national default.

The platform vendors are cautious here for good reason and have largely responded by making the configuration the customer's responsibility, which places the burden on precisely the least equipped party.

## What Already Exists
Consumer reporting agencies and screening vendors integrate with every platform and handle the data retrieval and FCRA mechanics competently. Adverse action notice generation is standard. Some platforms offer state-level rule presets. Legal publishers track fair housing developments. Industry associations issue compliance guidance.

## The Customisation Gap
Presets exist at state level and the rules increasingly live at city and county level, which is where coverage collapses. A national operator running properties in two hundred municipalities cannot configure two hundred rule sets by hand and does not.

Monitoring is the gap that matters most. Ordinances change, and nothing watches for it — the operator discovers a new requirement through a complaint or a trade newsletter. Continuously tracking municipal code changes and ordinance adoptions relevant to tenant screening, extracting the operative rule, and flagging affected properties is a monitoring problem on public documents, and it is the sort of long-tail coverage no vendor has been willing to fund by hiring.

The individualised assessment requirement is a second, more specific gap. Where a jurisdiction requires the landlord to consider the nature and recency of an offence and its relevance to tenancy before denying, the process must be documented per applicant. Most platforms provide no structure for it at all, which means the requirement is either ignored or handled in email.

## Impact If Solved
Screening compliance is a growing liability applied at the property level by staff without the training to carry it, and the failure mode is a fair housing action rather than an inefficiency. Making jurisdiction-correct configuration automatic protects residents from unlawful denials and operators from a category of claim they currently cannot systematically prevent.
