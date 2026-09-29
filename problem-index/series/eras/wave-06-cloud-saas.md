# Wave 6 — Cloud & SaaS (1999–2015)

**Trigger:** Salesforce founded March 8 1999; **AWS S3 launched March 14 2006, EC2 Aug 25 2006**
**What went to ~zero:** the **fixed** cost of compute — capital expenditure became operating expenditure
**Failure class produced:** the declined join matures — one party now owns both sides of the measurement

> **83 of the vault's 250 industries have this as their primary wave.** It is by far the largest cohort, and the reason is a pricing change, not a technical one.

## What Was True The Day Before

Selling software to a small business was structurally impossible, and the reason was arithmetic. Software required a server, the server required capital, and the capital had to be committed before the first customer. That fixed cost had to be amortised across the customer base, which meant the customer base had to be large or the contracts had to be enormous. Enterprise software was sold to enterprises because **nobody else could carry the fixed cost.**

A twelve-person dental practice was not a difficult customer. It was an unreachable one.

## The Trigger

S3 and EC2 turned the server from a purchase into a meter. The fixed cost of serving the first customer collapsed toward the marginal cost of serving the next one, and the amortisation problem disappeared.

Salesforce had proved the commercial model seven years earlier — multi-tenant, subscription, no install — but it ran its own infrastructure. AWS made that model available to a team of three.

*(Myth: Salesforce did not coin "SaaS." The term is in print by Feb 2001 in an SIIA whitepaper and was popularised as an acronym around 2005 — after Salesforce's 1999 founding. Salesforce is the poster child, not the coiner.)*

## What Became Possible

**Vertical SaaS.** The entire category exists because of this wave, and it is the single clearest illustration in the series of a *pricing* change creating industries. Once serving a 12-person practice cost a few dollars a month, it became rational to build software that understood dentistry specifically — its scheduling, its insurance claims, its recall cycles — rather than selling a generic tool and asking the dentist to configure it.

Every one of this vault's 11 Vertical SaaS industries, and most of the 11 Horizontal SaaS ones, is downstream of that single economic fact.

## The Competitive Fight

The fight moved from **owning the system of record** (Wave 4) to **owning the workflow**. With switching costs lower — no server to write off, no implementation to repeat — vendors could no longer rely on exit cost. They competed instead on being where the work actually happened every day, then expanded outward from that beachhead.

This is also when software pricing decoupled from software cost. Seats, usage tiers and platform fees are all attempts to price *value captured* rather than *resource consumed*, because resource consumed had become nearly nothing.

## What It Broke

**The vendor now sees everything and reports selectively.** A multi-tenant platform observes every customer's outcomes, which makes it the only party able to say whether the product works. It is also the party with the least incentive to publish that. The vault's "declined join" class lives here: the data is present, complete and in one place, and the honest measurement is simply not made.

**Configuration replaced engineering.** Serving many tenants from one codebase means differences become settings. Decisions that deserve a model get a dropdown — which is precisely the observation `industries/payment-processors.md` makes about authorisation rates, and it generalises across the whole cohort.

**The integration tax survived the architecture change.** Wave 4's perimeter of connections did not go away; it became APIs, and there are now more of them.

## Children in This Vault

**Primary (83):**
- [[industries/hair-salons-independent|Hair Salons (Independent)]]
- [[industries/electrical-contractors|Electrical Contractors]]
- [[industries/plumbing-contractors|Plumbing Contractors]]
- [[industries/api-infrastructure-providers|API Infrastructure Providers]]
- [[industries/ci-cd-platforms|CI/CD Platforms]]
- [[industries/cloud-cost-management|Cloud Cost Management]]
- [[industries/developer-tools-vendors|Developer Tools Vendors]]
- [[industries/internal-developer-platforms|Internal Developer Platforms]]
- [[industries/observability-vendors|Observability Vendors]]
- [[industries/open-source-commercial-vendors|Open Source Commercial Vendors]]
- [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
- [[industries/software-supply-chain-security|Software Supply Chain Security]]
- [[industries/ecommerce-aggregators|Ecommerce Aggregators]]
- [[industries/headless-commerce-vendors|Headless Commerce Vendors]]
- [[industries/subscription-commerce|Subscription Commerce]]
- [[industries/streaming-video-platforms|Streaming Video Platforms]]
- [[industries/developer-relations-agencies|Developer Relations Agencies]]
- [[industries/fractional-cto-services|Fractional CTO Services]]
- [[industries/revops-consultancies|RevOps Consultancies]]
- [[industries/saas-implementation-partners|SaaS Implementation Partners]]
- [[industries/technical-content-agencies|Technical Content Agencies]]
- [[industries/childcare-centers|Childcare Centers]]
- [[industries/corporate-training|Corporate Training]]
- [[industries/k12-private-schools|K-12 Private Schools]]
- [[industries/tutoring-centers|Tutoring Centers]]
- [[industries/bnpl-providers|BNPL Providers]]
- [[industries/crypto-exchanges|Crypto Exchanges]]
- [[industries/embedded-finance-platforms|Embedded Finance Platforms]]
- [[industries/neobanks|Neobanks]]
- [[industries/robo-advisors|Robo-Advisors]]
- [[industries/spend-management-platforms|Spend Management Platforms]]
- [[industries/game-hosting-providers|Game Hosting Providers]]
- [[industries/game-liveops-services|Game LiveOps Services]]
- [[industries/game-porting-studios|Game Porting Studios]]
- [[industries/chiropractic-practices|Chiropractic Practices]]
- [[industries/med-spas|Med Spas]]
- [[industries/acupuncture-practices|Acupuncture Practices]]
- [[industries/physical-therapy|Physical Therapy]]
- [[industries/veterinary-practices|Veterinary Practices]]
- [[industries/contract-lifecycle-platforms|Contract Lifecycle Platforms]]
- [[industries/crm-platforms|CRM Platforms]]
- [[industries/customer-support-platforms|Customer Support Platforms]]
- [[industries/hr-tech-platforms|HR Tech Platforms]]
- [[industries/no-code-app-builders|No-Code App Builders]]
- [[industries/scheduling-booking-platforms|Scheduling & Booking Platforms]]
- [[industries/work-collaboration-tools|Work Collaboration Tools]]
- [[industries/catering-companies|Catering Companies]]
- [[industries/immigration-law|Immigration Law Firms]]
- [[industries/public-defenders|Public Defenders]]
- [[industries/faith-organizations|Faith Organizations]]
- [[industries/nonprofits-social-services|Social Services Nonprofits]]
- [[industries/talent-assessment-platforms|Talent Assessment Platforms]]
- [[industries/hr-consultants|HR Consultants]]
- [[industries/it-managed-services|IT Managed Services]]
- [[industries/hoa-management|HOA Management]]
- [[industries/property-management|Property Management]]
- [[industries/alterations-tailoring|Alterations & Tailoring]]
- [[industries/cleaning-companies|Cleaning Companies]]
- [[industries/funeral-homes|Funeral Homes]]
- [[industries/pest-control|Pest Control]]
- [[industries/pet-services|Pet Services]]
- [[industries/security-guard-firms|Security Guard Firms]]
- [[industries/gyms-independent|Independent Gyms]]
- [[industries/youth-sports-orgs|Youth Sports Organizations]]
- [[industries/cloud-infrastructure-consultants|Cloud Infrastructure Consultants]]
- [[industries/cybersecurity-mssp|Cybersecurity MSSPs]]
- [[industries/home-inspection|Home Inspection]]
- [[industries/hvac-contractors|HVAC Contractors]]
- [[industries/landscaping|Landscaping]]
- [[industries/painting-contractors|Painting Contractors]]
- [[industries/roofing-contractors|Roofing Contractors]]
- [[industries/solar-installers|Solar Installers]]
- [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
- [[industries/security-awareness-training|Security Awareness Training]]
- [[industries/soc2-audit-firms|SOC 2 & Attestation Audit Firms]]
- [[industries/agtech-platforms|Agtech Platforms]]
- [[industries/construction-tech-platforms|Construction Tech Platforms]]
- [[industries/fitness-wellness-software|Fitness & Wellness Software]]
- [[industries/freight-tech-platforms|Freight Tech Platforms]]
- [[industries/insurtech-platforms|Insurtech Platforms]]
- [[industries/legal-practice-software|Legal Practice Software]]
- [[industries/proptech-platforms|Proptech Platforms]]
- [[industries/restaurant-tech-platforms|Restaurant Tech Platforms]]

**Secondary (55):**
- [[industries/email-sms-marketing-platforms|Email & SMS Marketing Platforms]]
- [[industries/seo-tooling-vendors|SEO Tooling Vendors]]
- [[industries/general-contractors|General Contractors]]
- [[industries/ai-agent-platforms|AI Agent Platforms]]
- [[industries/ai-inference-providers|AI Inference Providers]]
- [[industries/llm-application-tooling|LLM Application Tooling]]
- [[industries/database-platform-vendors|Database Platform Vendors]]
- [[industries/edge-cdn-providers|Edge & CDN Providers]]
- [[industries/online-marketplaces|Online Marketplaces]]
- [[industries/membership-community-platforms|Membership & Community Platforms]]
- [[industries/online-course-platforms|Online Course Platforms]]
- [[industries/ugc-video-platforms|UGC Video Platforms]]
- [[industries/data-platform-integrators|Data Platform Integrators]]
- [[industries/digital-accessibility-firms|Digital Accessibility Firms]]
- [[industries/product-design-studios|Product Design Studios]]
- [[industries/vocational-schools|Vocational Schools]]
- [[industries/credit-unions|Credit Unions]]
- [[industries/wealth-management-rias|Wealth Management RIAs]]
- [[industries/ap-automation-vendors|AP Automation Vendors]]
- [[industries/payment-processors|Payment Processors]]
- [[industries/esports-organizations|Esports Organizations]]
- [[industries/game-analytics-vendors|Game Analytics Vendors]]
- [[industries/indie-game-studios|Indie Game Studios]]
- [[industries/esignature-document-workflow|E-Signature & Document Workflow]]
- [[industries/payroll-platforms|Payroll Platforms]]
- [[industries/procurement-spend-platforms|Procurement & Spend Platforms]]
- [[industries/coffee-shops-independent|Independent Coffee Shops]]
- [[industries/food-trucks|Food Trucks]]
- [[industries/compliance-consulting|Compliance Consulting Firms]]
- [[industries/estate-planning|Estate Planning Law Firms]]
- [[industries/personal-injury-law|Personal Injury Law Firms]]
- [[industries/municipal-services|Municipal Services]]
- [[industries/trade-associations|Trade Associations]]
- [[industries/freelance-marketplaces|Freelance Marketplaces]]
- [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
- [[industries/online-tutoring-platforms|Online Tutoring Platforms]]
- [[industries/remote-work-infrastructure|Remote Work Infrastructure]]
- [[industries/rideshare-fleet-operators|Rideshare Fleet Operators]]
- [[industries/telehealth-platforms|Telehealth Platforms]]
- [[industries/accounting-firms-smb|SMB Accounting Firms]]
- [[industries/engineering-consultants|Engineering Consultants]]
- [[industries/grant-writers|Grant Writers]]
- [[industries/staffing-agencies|Staffing Agencies]]
- [[industries/specialty-food-retail|Specialty Food Retail]]
- [[industries/event-planning|Event Planning]]
- [[industries/tattoo-studios|Tattoo Studios]]
- [[industries/it-staffing-firms|IT Staffing Firms]]
- [[industries/software-dev-agencies|Software Development Agencies]]
- [[industries/towing-companies|Towing Companies]]
- [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
- [[industries/penetration-testing-firms|Penetration Testing Firms]]
- [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
- [[industries/field-service-software|Field Service Software]]
- [[industries/healthcare-practice-software|Healthcare Practice Software]]
- [[industries/retail-pos-platforms|Retail POS Platforms]]

**Sources:** AWS, *Twenty years of Amazon S3*; Wikipedia, *Timeline of Amazon Web Services*, *Salesforce*; SIIA, *Strategic Backgrounder: Software as a Service* (Feb 2001); SDForum "Software as a Service" conference, March 2005 (John Koenig).
