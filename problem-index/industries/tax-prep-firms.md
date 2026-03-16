# Tax Prep Firms

## Profile
**Category:** Financial Services
**Market Size:** ~$14B US tax preparation services; ~100,000 independent tax prep firms/practices beyond H&R Block and Jackson Hewitt
**Tech Maturity:** Medium — Drake Software, Lacerte (Intuit), UltraTax CS (Thomson Reuters), and ProConnect dominate professional prep; e-filing is universal but AI adoption is minimal outside of Intuit's consumer products
**Workforce:** Enrolled Agents (EAs), CPAs moonlighting or full-time, non-credentialed preparers (AFSP holders), seasonal staff hired January through April, reviewers/signers, and admin/intake coordinators who manage the client document funnel

## Key Pain Themes
The defining constraint is extreme seasonality: 60-70% of annual revenue compresses into a 14-week window (late January to mid-April), creating brutal peak-season workflows where a single preparer may handle 15-25 returns per day. Document intake is the bottleneck — clients arrive with shoeboxes of W-2s, 1099s, K-1s, and receipts in varying formats (paper, photos, PDFs, portal uploads), and preparers spend 30-40% of their time just gathering, chasing, and keying data before any tax logic begins. Multi-state complexity is rising as remote work creates nexus questions that small firms lack tooling to handle efficiently. Off-season revenue generation through tax planning advisory is aspirational for most firms but requires scenario modeling capabilities their software does not provide.

## Current Tech Landscape
Professional tax software (Drake, Lacerte, UltraTax CS, ProSeries) handles calculation and e-filing reliably but offers minimal automation for intake, document processing, or client communication. Client portals (SafeSend, Canopy, TaxDome) have improved document collection but still require manual sorting and data extraction. Practice management tools exist but are fragmented — most firms cobble together a tax engine, a portal, a CRM, and a phone system with no integration layer. OCR exists in some tools but accuracy on handwritten or photographed documents remains poor, and no mainstream product offers intelligent document routing or automated data population from source documents into tax forms.

## Problems
- [[problems/tax-prep-firms/high-impact|🔴 High Impact: Client Document Intake and Data Extraction]]
- [[problems/tax-prep-firms/low-impact-1|🟡 Low Impact: Multi-State Filing Complexity]]
- [[problems/tax-prep-firms/low-impact-2|🟡 Low Impact: Tax Planning Scenario Modeling]]
- [[problems/tax-prep-firms/worker-life-1|🟢 Worker Life: Review Queue Overload During Peak Season]]
- [[problems/tax-prep-firms/worker-life-2|🟢 Worker Life: Repetitive Client Status Inquiries]]

## Analysis
- [[problems/tax-prep-firms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/tax-prep-firms/ai-agents-platforms|🤖 AI Agents & Platforms]]
