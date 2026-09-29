# The Era Spine — Twelve Waves of Business Computing

Canonical reference for Phase 3. Every `history/<slug>.md` file names a wave from this list, and every wave expands into `series/eras/<wave>.md`.

**Spec and cursor:** `series/_plan.md` · **Build log:** `series/_bookmark.md`

---

## The argument

Scoped from **when computers arrived**. Pre-computer origins appear only as "what was true the day before."

> **Each wave drove the cost of exactly one thing to near zero, and an industry crystallised around the newly cheap thing.**

Coordination → items → modelling → integration → distribution → compute → memory → location → attention → audience → presence → inference.

All dates are research-verified as of 2026-09-18 and sourced in the individual wave files. Corrections and killed myths live in `series/_plan.md` §5 — **read that before writing any episode.**

## The twelve

| # | Wave | Span | What went to ~zero | Primary | Secondary |
|---|---|---|---|---|---|
| 1 | [[series/eras/wave-01-mainframe-batch\|Mainframe & batch]] | 1955–75 | arithmetic over a whole customer file | 10 | 2 |
| 2 | [[series/eras/wave-02-departmental-item-level\|Departmental & item-level]] | 1964–80 | tracking physical things one at a time | 16 | 8 |
| 3 | [[series/eras/wave-03-pc-spreadsheet\|PC & the spreadsheet]] | 1979–92 | **building a model** | 16 | 16 |
| 4 | [[series/eras/wave-04-client-server-erp\|Client–server & ERP]] | 1992–2000 | one version of a company's own numbers | 18 | 21 |
| 5 | [[series/eras/wave-05-commercial-web\|The commercial web]] | 1993–2004 | distribution and discovery | 45 | 31 |
| 6 | [[series/eras/wave-06-cloud-saas\|Cloud & SaaS]] | 1999–2015 | the **fixed** cost of compute | **83** | 55 |
| 7 | [[series/eras/wave-07-big-data\|Big data]] | 2006–15 | keeping everything | 14 | 34 |
| 8 | [[series/eras/wave-08-mobile-gps\|Mobile & GPS]] | 2007–16 | knowing where the workforce is | 16 | 36 |
| 9 | [[series/eras/wave-09-programmatic\|Programmatic]] | 2005–**21** | pricing attention per impression | 6 | 13 |
| 10 | [[series/eras/wave-10-creator-platform\|The creator platform]] | 2012–20 | reaching an audience | 14 | 11 |
| 11 | [[series/eras/wave-11-covid-dislocation\|The COVID dislocation]] | 2020 | the requirement of physical co-presence | 4 | 13 |
| 12 | [[series/eras/wave-12-transformers\|Transformers]] | 2017– | inference over unstructured text | 8 | 10 |

## Three things this distribution shows

**Wave 6 owns a third of the vault (83 of 250).** Cloud did not make software better; it made a *pricing* change that turned small businesses into addressable customers for the first time. Almost everything the vault calls Vertical SaaS exists because of one shift from capex to opex.

**Wave 3 created nothing and is everywhere.** The spreadsheet wave has 16 industries whose core working artefact is still a spreadsheet model — and the word appears in **1,405 files** across the vault. It is the incumbent an FDE actually competes with.

**Wave 9 is the only wave with a death date.** Programmatic was ended, as a model, by a company that did not ask: Apple's ATT on April 26 2021. That gives it the cleanest three-act shape of anything here.

## The chronology of failure

The vault's Phase 2 sweep found three recurring failure classes. They are not a taxonomy — **they are a chronology.**

| Class | Waves | What happens |
|---|---|---|
| **The missing join** | 1–5 | Two systems never spoke. Nobody's fault, and Wave 12 is now making it cheap to fix. |
| **The declined join** | 6–9 | One party owns both sides and *chooses* not to measure, because the honest number is smaller. |
| **The asymmetric hold** | 8, 10–11 | The platform measures the worker exhaustively and itself not at all. |

The failure mode did not change because engineers got worse. It changed because **as technology consolidated, the party able to measure became the party who benefited from not measuring.**

Note what Wave 12 does and does not touch. It makes the missing join cheap to close. It does nothing at all to the other two, because those were never capability problems.

## Assignment — all 250 industries

**Primary** = the wave that created or decisively reshaped the industry as it exists today. **Secondary** = the next most formative. Regulatory triggers are assigned to the wave matching the *date*; the industry's own file says the trigger was statutory.

### Wave 1 — Mainframe & Batch (1955–1975)  ·  10 industries

| Industry | Secondary |
|---|---|
| [[industries/collections-agencies\|Collections Agencies]] | W7 |
| [[industries/credit-unions\|Credit Unions]] | W6 |
| [[industries/hotels-boutique\|Boutique Hotels]] | W5 |
| [[industries/independent-insurance-agents\|Independent Insurance Agents]] | W4 |
| [[industries/insurance-tpa\|Insurance Third-Party Administrators (TPAs)]] | W4 |
| [[industries/medical-billing\|Medical Billing]] | W7 |
| [[industries/municipal-services\|Municipal Services]] | W6 |
| [[industries/payment-processors\|Payment Processors]] | W6 |
| [[industries/payroll-platforms\|Payroll Platforms]] | W6 |
| [[industries/wealth-management-rias\|Wealth Management RIAs]] | W6 |

### Wave 2 — Departmental & Item-Level (1964–1980)  ·  16 industries

| Industry | Secondary |
|---|---|
| [[industries/auto-dealers-independent\|Independent Auto Dealers]] | W5 |
| [[industries/coffee-shops-independent\|Independent Coffee Shops]] | W6 |
| [[industries/contract-manufacturing\|Contract Manufacturing]] | W4 |
| [[industries/dental-practices\|Dental Practices]] | W7 |
| [[industries/electronics-contract-mfg\|Electronics Contract Manufacturing]] | W4 |
| [[industries/food-manufacturing\|Food Manufacturing]] | W4 |
| [[industries/greenhouse-horticulture\|Greenhouse Horticulture]] | W8 |
| [[industries/independent-restaurants\|Independent Restaurants]] | W8 |
| [[industries/independent-retailers\|Independent Retailers]] | W5 |
| [[industries/livestock-operations\|Livestock Operations]] | W8 |
| [[industries/medical-device-mfg\|Medical Device Manufacturing]] | W4 |
| [[industries/metal-fabrication\|Metal Fabrication]] | W3 |
| [[industries/pharmacy-independents\|Independent Pharmacies]] | W7 |
| [[industries/retail-pos-platforms\|Retail POS Platforms]] | W6 |
| [[industries/rv-dealerships\|RV Dealerships]] | W5 |
| [[industries/specialty-food-retail\|Specialty Food Retail]] | W6 |

### Wave 3 — The PC & the Spreadsheet (1979–1992)  ·  16 industries

| Industry | Secondary |
|---|---|
| [[industries/accounting-firms-smb\|SMB Accounting Firms]] | W6 |
| [[industries/commercial-real-estate\|Commercial Real Estate]] | W7 |
| [[industries/energy-auditors\|Energy Auditors]] | W8 |
| [[industries/engineering-consultants\|Engineering Consultants]] | W6 |
| [[industries/environmental-consultants\|Environmental Consultants]] | W7 |
| [[industries/estate-planning\|Estate Planning Law Firms]] | W6 |
| [[industries/event-planning\|Event Planning]] | W6 |
| [[industries/general-contractors\|General Contractors]] | W6 |
| [[industries/grant-writers\|Grant Writers]] | W6 |
| [[industries/independent-publishers\|Independent Publishers]] | W5 |
| [[industries/printing-shops\|Printing Shops]] | W2 |
| [[industries/public-adjusters\|Public Adjusters]] | W7 |
| [[industries/real-estate-appraisers\|Real Estate Appraisers]] | W7 |
| [[industries/small-law-firms\|Small Law Firms (Solo and 2-10 Attorney Practices)]] | W5 |
| [[industries/tax-prep-firms\|Tax Prep Firms]] | W5 |
| [[industries/video-production-smb\|SMB Video Production]] | W10 |

### Wave 4 — Client–Server & ERP (1992–2000)  ·  18 industries

| Industry | Secondary |
|---|---|
| [[industries/ap-automation-vendors\|AP Automation Vendors]] | W6 |
| [[industries/auto-body-shops\|Auto Body Shops]] | W2 |
| [[industries/auto-repair-shops\|Auto Repair Shops]] | W2 |
| [[industries/charter-bus-operators\|Charter Bus Operators]] | W8 |
| [[industries/compliance-consulting\|Compliance Consulting Firms]] | W6 |
| [[industries/customs-brokers\|Customs Brokers]] | W5 |
| [[industries/database-platform-vendors\|Database Platform Vendors]] | W6 |
| [[industries/digital-forensics-firms\|Digital Forensics Firms]] | W7 |
| [[industries/food-distributors\|Food Distributors]] | W2 |
| [[industries/freight-brokerage\|Freight Brokerage]] | W5 |
| [[industries/insurance-restoration\|Insurance Restoration]] | W3 |
| [[industries/medical-supply-retail\|Medical Supply Retail]] | W5 |
| [[industries/mortgage-brokers\|Mortgage Brokers]] | W5 |
| [[industries/oil-gas-field-services\|Oil & Gas Field Services]] | W7 |
| [[industries/procurement-spend-platforms\|Procurement & Spend Platforms]] | W6 |
| [[industries/restaurant-suppliers\|Restaurant Suppliers]] | W2 |
| [[industries/utility-contractors\|Utility Contractors]] | W8 |
| [[industries/warehouse-3pl\|Warehouse & 3PL]] | W2 |

### Wave 5 — The Commercial Web (1993–2004)  ·  45 industries

| Industry | Secondary |
|---|---|
| [[industries/affiliate-networks\|Affiliate Networks]] | W9 |
| [[industries/b2b-commerce-platforms\|B2B Commerce Platforms]] | W4 |
| [[industries/brand-protection-firms\|Brand Protection Firms]] | W12 |
| [[industries/bug-bounty-platforms\|Bug Bounty Platforms]] | W6 |
| [[industries/content-moderation-services\|Content Moderation Services]] | W12 |
| [[industries/conversion-optimization-firms\|Conversion Optimization Firms]] | W9 |
| [[industries/crowdsourcing-platforms\|Crowdsourcing Platforms]] | W12 |
| [[industries/digital-accessibility-firms\|Digital Accessibility Firms]] | W6 |
| [[industries/digital-audio-platforms\|Digital Audio Platforms]] | W10 |
| [[industries/digital-bpo-operations\|Digital BPO Operations]] | W11 |
| [[industries/digital-goods-marketplaces\|Digital Goods Marketplaces]] | W10 |
| [[industries/digital-native-publishers\|Digital Native Publishers]] | W9 |
| [[industries/dropshipping-suppliers\|Dropshipping Suppliers]] | W9 |
| [[industries/ecommerce-sellers\|E-Commerce Sellers]] | W9 |
| [[industries/edge-cdn-providers\|Edge & CDN Providers]] | W6 |
| [[industries/email-sms-marketing-platforms\|Email & SMS Marketing Platforms]] | W6 |
| [[industries/esignature-document-workflow\|E-Signature & Document Workflow]] | W6 |
| [[industries/freelance-marketplaces\|Freelance Marketplaces]] | W6 |
| [[industries/game-asset-marketplaces\|Game Asset Marketplaces]] | W10 |
| [[industries/identity-verification-vendors\|Identity Verification Vendors]] | W7 |
| [[industries/indie-game-studios\|Indie Game Studios]] | W6 |
| [[industries/it-staffing-firms\|IT Staffing Firms]] | W6 |
| [[industries/language-schools\|Language Schools]] | W11 |
| [[industries/lending-marketplaces\|Lending Marketplaces]] | W7 |
| [[industries/localization-services\|Localization Services]] | W12 |
| [[industries/marketing-agencies-smb\|SMB Marketing Agencies]] | W9 |
| [[industries/moving-companies\|Moving Companies]] | W8 |
| [[industries/music-distribution-platforms\|Music Distribution Platforms]] | W10 |
| [[industries/news-media-local\|Local News Media]] | W9 |
| [[industries/online-marketplaces\|Online Marketplaces]] | W6 |
| [[industries/penetration-testing-firms\|Penetration Testing Firms]] | W6 |
| [[industries/performance-marketing-agencies\|Performance Marketing Agencies]] | W9 |
| [[industries/personal-injury-law\|Personal Injury Law Firms]] | W6 |
| [[industries/print-on-demand-platforms\|Print on Demand Platforms]] | W10 |
| [[industries/recommerce-platforms\|Recommerce Platforms]] | W8 |
| [[industries/recruiting-tech-vendors\|Recruiting Tech Vendors]] | W12 |
| [[industries/seo-tooling-vendors\|SEO Tooling Vendors]] | W6 |
| [[industries/short-term-rentals\|Short-Term Rentals]] | W8 |
| [[industries/software-dev-agencies\|Software Development Agencies]] | W6 |
| [[industries/staffing-agencies\|Staffing Agencies]] | W6 |
| [[industries/stock-media-marketplaces\|Stock Media Marketplaces]] | W10 |
| [[industries/trade-associations\|Trade Associations]] | W6 |
| [[industries/ux-research-agencies\|UX Research Agencies]] | W8 |
| [[industries/vocational-schools\|Vocational Schools]] | W6 |
| [[industries/web-data-extraction-firms\|Web Data Extraction Firms]] | W12 |

### Wave 6 — Cloud & SaaS (1999–2015)  ·  83 industries

| Industry | Secondary |
|---|---|
| [[industries/acupuncture-practices\|Acupuncture Practices]] | W11 |
| [[industries/agtech-platforms\|Agtech Platforms]] | W8 |
| [[industries/alterations-tailoring\|Alterations & Tailoring]] | W8 |
| [[industries/api-infrastructure-providers\|API Infrastructure Providers]] | W5 |
| [[industries/bnpl-providers\|BNPL Providers]] | W8 |
| [[industries/catering-companies\|Catering Companies]] | W3 |
| [[industries/childcare-centers\|Childcare Centers]] | W8 |
| [[industries/chiropractic-practices\|Chiropractic Practices]] | W11 |
| [[industries/ci-cd-platforms\|CI/CD Platforms]] | W7 |
| [[industries/cleaning-companies\|Cleaning Companies]] | W8 |
| [[industries/cloud-cost-management\|Cloud Cost Management]] | W7 |
| [[industries/cloud-infrastructure-consultants\|Cloud Infrastructure Consultants]] | W7 |
| [[industries/construction-tech-platforms\|Construction Tech Platforms]] | W8 |
| [[industries/contract-lifecycle-platforms\|Contract Lifecycle Platforms]] | W4 |
| [[industries/corporate-training\|Corporate Training]] | W11 |
| [[industries/crm-platforms\|CRM Platforms]] | W4 |
| [[industries/crypto-exchanges\|Crypto Exchanges]] | W1 |
| [[industries/customer-support-platforms\|Customer Support Platforms]] | W5 |
| [[industries/cybersecurity-mssp\|Cybersecurity MSSPs]] | W7 |
| [[industries/developer-relations-agencies\|Developer Relations Agencies]] | W5 |
| [[industries/developer-tools-vendors\|Developer Tools Vendors]] | W3 |
| [[industries/ecommerce-aggregators\|Ecommerce Aggregators]] | W5 |
| [[industries/electrical-contractors\|Electrical Contractors]] | W3 |
| [[industries/embedded-finance-platforms\|Embedded Finance Platforms]] | W5 |
| [[industries/faith-organizations\|Faith Organizations]] | W11 |
| [[industries/fitness-wellness-software\|Fitness & Wellness Software]] | W8 |
| [[industries/fractional-cto-services\|Fractional CTO Services]] | W11 |
| [[industries/freight-tech-platforms\|Freight Tech Platforms]] | W4 |
| [[industries/funeral-homes\|Funeral Homes]] | W5 |
| [[industries/game-hosting-providers\|Game Hosting Providers]] | W5 |
| [[industries/game-liveops-services\|Game LiveOps Services]] | W7 |
| [[industries/game-porting-studios\|Game Porting Studios]] | W8 |
| [[industries/grc-compliance-platforms\|GRC & Compliance Platforms]] | W4 |
| [[industries/gyms-independent\|Independent Gyms]] | W8 |
| [[industries/hair-salons-independent\|Hair Salons (Independent)]] | W8 |
| [[industries/headless-commerce-vendors\|Headless Commerce Vendors]] | W5 |
| [[industries/hoa-management\|HOA Management]] | W3 |
| [[industries/home-inspection\|Home Inspection]] | W8 |
| [[industries/hr-consultants\|HR Consultants]] | W3 |
| [[industries/hr-tech-platforms\|HR Tech Platforms]] | W4 |
| [[industries/hvac-contractors\|HVAC Contractors]] | W3 |
| [[industries/immigration-law\|Immigration Law Firms]] | W5 |
| [[industries/insurtech-platforms\|Insurtech Platforms]] | W7 |
| [[industries/internal-developer-platforms\|Internal Developer Platforms]] | W7 |
| [[industries/it-managed-services\|IT Managed Services]] | W4 |
| [[industries/k12-private-schools\|K-12 Private Schools]] | W11 |
| [[industries/landscaping\|Landscaping]] | W8 |
| [[industries/legal-practice-software\|Legal Practice Software]] | W3 |
| [[industries/med-spas\|Med Spas]] | W10 |
| [[industries/neobanks\|Neobanks]] | W8 |
| [[industries/no-code-app-builders\|No-Code App Builders]] | W3 |
| [[industries/nonprofits-social-services\|Social Services Nonprofits]] | W4 |
| [[industries/observability-vendors\|Observability Vendors]] | W7 |
| [[industries/open-source-commercial-vendors\|Open Source Commercial Vendors]] | W5 |
| [[industries/painting-contractors\|Painting Contractors]] | W3 |
| [[industries/pest-control\|Pest Control]] | W8 |
| [[industries/pet-services\|Pet Services]] | W8 |
| [[industries/physical-therapy\|Physical Therapy]] | W7 |
| [[industries/plumbing-contractors\|Plumbing Contractors]] | W3 |
| [[industries/property-management\|Property Management]] | W3 |
| [[industries/proptech-platforms\|Proptech Platforms]] | W5 |
| [[industries/public-defenders\|Public Defenders]] | W7 |
| [[industries/qa-test-automation-vendors\|QA & Test Automation Vendors]] | W7 |
| [[industries/restaurant-tech-platforms\|Restaurant Tech Platforms]] | W8 |
| [[industries/revops-consultancies\|RevOps Consultancies]] | W4 |
| [[industries/robo-advisors\|Robo-Advisors]] | W7 |
| [[industries/roofing-contractors\|Roofing Contractors]] | W8 |
| [[industries/saas-implementation-partners\|SaaS Implementation Partners]] | W4 |
| [[industries/scheduling-booking-platforms\|Scheduling & Booking Platforms]] | W8 |
| [[industries/security-awareness-training\|Security Awareness Training]] | W5 |
| [[industries/security-guard-firms\|Security Guard Firms]] | W8 |
| [[industries/soc2-audit-firms\|SOC 2 & Attestation Audit Firms]] | W4 |
| [[industries/software-supply-chain-security\|Software Supply Chain Security]] | W12 |
| [[industries/solar-installers\|Solar Installers]] | W8 |
| [[industries/spend-management-platforms\|Spend Management Platforms]] | W4 |
| [[industries/streaming-video-platforms\|Streaming Video Platforms]] | W10 |
| [[industries/subscription-commerce\|Subscription Commerce]] | W5 |
| [[industries/talent-assessment-platforms\|Talent Assessment Platforms]] | W7 |
| [[industries/technical-content-agencies\|Technical Content Agencies]] | W5 |
| [[industries/tutoring-centers\|Tutoring Centers]] | W11 |
| [[industries/veterinary-practices\|Veterinary Practices]] | W2 |
| [[industries/work-collaboration-tools\|Work Collaboration Tools]] | W11 |
| [[industries/youth-sports-orgs\|Youth Sports Organizations]] | W8 |

### Wave 7 — Big Data (2006–2015)  ·  14 industries

| Industry | Secondary |
|---|---|
| [[industries/behavioral-health-clinics\|Behavioral Health Clinics]] | W11 |
| [[industries/bi-analytics-platforms\|BI & Analytics Platforms]] | W3 |
| [[industries/customer-data-platforms\|Customer Data Platforms]] | W9 |
| [[industries/data-analytics-consultants\|Data Analytics Consultants]] | W3 |
| [[industries/data-marketplace-brokers\|Data Marketplace Brokers]] | W12 |
| [[industries/data-platform-integrators\|Data Platform Integrators]] | W6 |
| [[industries/game-analytics-vendors\|Game Analytics Vendors]] | W6 |
| [[industries/healthcare-practice-software\|Healthcare Practice Software]] | W6 |
| [[industries/home-health-agencies\|Home Health Agencies]] | W11 |
| [[industries/mlops-platforms\|MLOps Platforms]] | W12 |
| [[industries/payment-fraud-vendors\|Payment Fraud Vendors]] | W1 |
| [[industries/player-research-firms\|Player Research Firms]] | W10 |
| [[industries/threat-intelligence-vendors\|Threat Intelligence Vendors]] | W6 |
| [[industries/urgent-care\|Urgent Care Centers]] | W11 |

### Wave 8 — Mobile & GPS (2007–2016)  ·  16 industries

| Industry | Secondary |
|---|---|
| [[industries/app-marketing-firms\|App Marketing Firms]] | W9 |
| [[industries/cold-chain-logistics\|Cold Chain Logistics]] | W4 |
| [[industries/crop-farming\|Crop Farming]] | W7 |
| [[industries/d2c-brand-operators\|D2C Brand Operators]] | W9 |
| [[industries/field-service-software\|Field Service Software]] | W6 |
| [[industries/fleet-managers\|Fleet Managers]] | W4 |
| [[industries/food-trucks\|Food Trucks]] | W6 |
| [[industries/gig-delivery-platforms\|Gig Delivery Platforms]] | W6 |
| [[industries/land-surveyors\|Land Surveyors]] | W3 |
| [[industries/last-mile-delivery\|Last-Mile Delivery]] | W5 |
| [[industries/mobile-game-publishers\|Mobile Game Publishers]] | W9 |
| [[industries/non-emergency-medical-transport\|Non-Emergency Medical Transport]] | W7 |
| [[industries/owner-operator-trucking\|Owner-Operator Trucking]] | W4 |
| [[industries/product-design-studios\|Product Design Studios]] | W6 |
| [[industries/rideshare-fleet-operators\|Rideshare Fleet Operators]] | W6 |
| [[industries/towing-companies\|Towing Companies]] | W6 |

### Wave 9 — Programmatic (2005–2021)  ·  6 industries

| Industry | Secondary |
|---|---|
| [[industries/audio-adtech-networks\|Audio Adtech Networks]] | W10 |
| [[industries/game-user-acquisition-firms\|Game User Acquisition Firms]] | W8 |
| [[industries/marketing-attribution-vendors\|Marketing Attribution Vendors]] | W5 |
| [[industries/privacy-tech-vendors\|Privacy Tech Vendors]] | W7 |
| [[industries/programmatic-ad-platforms\|Programmatic Ad Platforms]] | W7 |
| [[industries/retail-media-networks\|Retail Media Networks]] | W2 |

### Wave 10 — The Creator Platform (2012–2020)  ·  14 industries

| Industry | Secondary |
|---|---|
| [[industries/creator-businesses\|Creator Businesses]] | W8 |
| [[industries/creator-talent-agencies\|Creator Talent Agencies]] | W9 |
| [[industries/esports-organizations\|Esports Organizations]] | W6 |
| [[industries/influencer-marketing-platforms\|Influencer Marketing Platforms]] | W8 |
| [[industries/live-commerce-platforms\|Live Commerce Platforms]] | W8 |
| [[industries/membership-community-platforms\|Membership & Community Platforms]] | W6 |
| [[industries/newsletter-media\|Newsletter Media]] | W5 |
| [[industries/online-course-platforms\|Online Course Platforms]] | W6 |
| [[industries/personal-trainers\|Personal Trainers]] | W8 |
| [[industries/podcasting-networks\|Podcasting Networks]] | W5 |
| [[industries/tattoo-studios\|Tattoo Studios]] | W6 |
| [[industries/trust-safety-tooling-vendors\|Trust & Safety Tooling Vendors]] | W12 |
| [[industries/ugc-video-platforms\|UGC Video Platforms]] | W6 |
| [[industries/virtual-economy-operators\|Virtual Economy Operators]] | W5 |

### Wave 11 — The COVID Dislocation (2020)  ·  4 industries

| Industry | Secondary |
|---|---|
| [[industries/online-tutoring-platforms\|Online Tutoring Platforms]] | W6 |
| [[industries/remote-work-infrastructure\|Remote Work Infrastructure]] | W6 |
| [[industries/telehealth-platforms\|Telehealth Platforms]] | W6 |
| [[industries/virtual-assistant-services\|Virtual Assistant Services]] | W5 |

### Wave 12 — Transformers (2017– )  ·  8 industries

| Industry | Secondary |
|---|---|
| [[industries/ai-agent-platforms\|AI Agent Platforms]] | W6 |
| [[industries/ai-inference-providers\|AI Inference Providers]] | W6 |
| [[industries/ai-model-evaluation-firms\|AI Model Evaluation Firms]] | W7 |
| [[industries/ai-red-teaming-firms\|AI Red Teaming Firms]] | W7 |
| [[industries/data-labeling-services\|Data Labeling Services]] | W7 |
| [[industries/llm-application-tooling\|LLM Application Tooling]] | W6 |
| [[industries/synthetic-data-providers\|Synthetic Data Providers]] | W7 |
| [[industries/vector-search-vendors\|Vector Search Vendors]] | W7 |

---

**Verification:** every industry appears exactly once as a primary. Checked against `ls industries/` — 250 assigned, zero strays, zero unassigned.

**Created:** 2026-09-18 (Phase 3 · H1)
