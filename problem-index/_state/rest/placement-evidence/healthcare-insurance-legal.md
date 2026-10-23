Method note: roles below were seen as listings in live web-search results on 2026-10-23 (ATS/YC/company URLs where given); I did not open each posting, so "open" means listed today, not re-verified on the page. Aggregator-only or old-dated roles are flagged and not counted toward E.

## physician-practices
scores: E P M F R = 4 4 3 4 3
employers: Commure/Athelas (Senior Forward Deployed Engineer, FDE, https://www.ycombinator.com/companies/athelas/jobs/qo3HoMz-senior-forward-deployed-engineer); Hippocratic AI (Forward Deployment Engineer, FDE, https://jobs.generalcatalyst.com/companies/hippocractic-ai/jobs/82622170-forward-deployment-engineer); Opmed.ai (Forward Deployed Engineer, FDE, https://careers.grovevc.com/companies/opmed-ai-2-a45091ec-b972-4741-9486-9580106baf11/jobs/88892489-forward-deployed-engineer); Asha Health (FDE, AI Agents, India-based, https://jobs.reachcapital.com/companies/asha-health-2/jobs/60861291-forward-deployed-engineer-ai-agents, not counted); Notable (FDE seen via aggregator, careers page, role not confirmed)
pain: Practices must handle payer prior auth with new 72-hour/7-day decision rules and FHIR PA APIs due 2027, and still do much of it by phone/fax (https://www.cms.gov/files/document/fact-sheet-cms-interoperability-and-prior-authorization-final-rule-cms-0057-f.pdf)
mvp: Prior-auth packet assembler that turns a synthetic clinical note plus payer policy text into a PA request and appeal letter, using Synthea synthetic FHIR patients and public payer medical-policy PDFs.
pitch: Practice administrators, COOs of MSOs, Heads of Product/CTO at scribe/RCM startups via MGMA and state medical society member/exhibitor lists, YC company directory, HLTH/HIMSS exhibitor lists.
note: M held at 3 because no public real-note corpus; E only 4 because several roles are health-system or non-US focused.

## skilled-nursing-facilities
scores: E P M F R = 4 4 5 3 4
employers: PointClickCare (Intermediate Software Engineer, https://jobs.lever.co/pointclickcare/92bd0a33-a934-499a-81ec-b38956488cc5; Principal AI Engineer (Autonomous Agent) US, https://jobs.lever.co/pointclickcare/ca6bed88-d453-4661-9308-825c1b7b2fa9); Aline (Agentic AI Engineer, Junior, remote US, https://www.remoterocketship.com/us/company/aline/jobs/agentic-ai-engineer-junior-united-states-remote/, aggregator); SafelyYou (Senior Software Developer, https://jobs.foundationcapital.com/companies/safely-you/jobs/69381427-senior-software-developer-c-n)
pain: Chronic nursing-home staffing shortage plus daily RN/PBJ reporting stays after the federal minimum-staffing rule was repealed, so scheduling and staffing-compliance tooling is still bought (https://www.porh.psu.edu/cms-repeals-minimum-staffing-standards-for-nursing-homes/)
mvp: Staffing-gap and PBJ-anomaly dashboard that ranks facilities by RN-hour shortfalls using CMS Payroll-Based Journal public data and CMS Care Compare provider files.
pitch: Administrators, DONs, VPs Operations of regional chains, plus PointClickCare marketplace partners via AHCA/NCAL and state association member lists, CMS Care Compare facility lists, conference exhibitor lists.
note: PointClickCare roles are on its own Lever board but may be older postings (some 2025); not re-opened.

## diagnostic-imaging-centers
scores: E P M F R = 3 4 4 3 3
employers: HOPPR (Forward Deployed ML Engineer, FDE, https://job-boards.greenhouse.io/hoppr/jobs/4950408008); 5C Network (FDE Provider Solutions Group, Bangalore on-site, https://www.5cnetwork.com/jobs/forward-deployed-engineer-provider-solutions-group, not counted); Rad AI (careers page, role not confirmed)
pain: Radiology carries the heaviest prior-auth burden of any specialty and faces a radiologist workforce shortage (https://radiologybusiness.com/topics/healthcare-management/healthcare-policy/radiologists-physician-cms-prior-authorization)
mvp: Imaging order prior-auth checker that matches an order and indication to appropriateness criteria, using public ACR Appropriateness Criteria and synthetic orders; or a report-QA demo on the open NIH ChestX-ray14 / RSNA datasets.
pitch: Center administrators/owners, practice managers, radiology IT leads via AHRA and SIIM/RSNA exhibitor and speaker lists, state imaging association rosters.
note: Few distinct vendors with confirmed US eng roles, so E=3.

## general-hospitals
scores: E P M F R = 5 5 4 2 4
employers: OpenAI (Forward Deployed Engineer (FDE) Healthcare, SF/NYC/Seattle, FDE, https://openai.com/careers/forward-deployed-engineer-(fde)-healthcare-sf-san-francisco/); Cair Health (Founding Forward Deployed Engineer, FDE, https://www.ycombinator.com/companies/cair-health/jobs/Ye8X3VN-founding-forward-deployed-engineer); Smarter Technologies (Forward Deployed Engineer, Brazil, https://job-boards.greenhouse.io/smartertechnologies/jobs/4654804005); AKASA (FDE, careers page, role not confirmed); Hippocratic AI (FDE, https://jobs.generalcatalyst.com/companies/hippocractic-ai/jobs/82622170-forward-deployment-engineer); Opmed.ai (FDE, https://careers.grovevc.com/companies/opmed-ai-2-a45091ec-b972-4741-9486-9580106baf11/jobs/88892489-forward-deployed-engineer)
pain: Hospitals and payers face the CMS-0057 FHIR prior-authorization API deadline of 2027-01-01 and denials/RCM backlog (https://www.insurancebusinessmag.com/us/news/benefits/health-plans-have-10-weeks-to-meet-the-prior-auth-api-deadline-and-the-burden-hasnt-eased-yet-594390.aspx)
mvp: Denial-prediction and appeal-drafting demo on CMS hospital price-transparency files and Care Compare data plus synthetic remittances (Synthea).
pitch: Founders/heads of engineering at the vendors above (YC directory, HLTH/HIMSS exhibitor lists); hospital RCM directors only via AHA/HFMA member and chapter lists.
note: F=2 because the end buyer is a hospital committee; pitching the hiring vendors instead is faster.

## clinical-laboratories
scores: E P M F R = 3 4 3 3 4
employers: Quest Diagnostics (Sr. LIMS Software Engineer, remote, https://careers.questdiagnostics.com/job/norristown/sr-lims-software-engineer-remote/38852/86588221008); CareDx (Staff Software Engineer, https://job-boards.greenhouse.io/caredxinc/jobs/4139901009); Personalis (Sr. Software Engineer, Clinical Software, https://job-boards.greenhouse.io/personalisinc/jobs/7587255003)
pain: Medicare lab fee cuts of up to 15% a year were only delayed through 2026 and resume in 2027 unless Congress acts, squeezing lab margins (https://ascp.org/news/news-details/2026/02/09/medicare-laboratory-payment-cuts-averted-for-2026)
mvp: Claim-denial and underpayment finder for lab billing using the public CMS Clinical Laboratory Fee Schedule files against synthetic claims; or a LIS result-routing demo on synthetic HL7.
pitch: Lab directors, billing managers, CIOs via the CMS CLIA lab directory, ACLA/ADLM/CLMA member and exhibitor lists.
note: Employers found are labs themselves (not vendors); no lab-software vendor roles confirmed, so E=3. M=3, no public lab-result corpus.

## medical-supply-distributors
scores: E P M F R = 2 4 3 4 4
employers: No medical/DME-specific vendor with an open engineering role found. Adjacent only: Comena (FDE, order-intake automation for industrial distributors, Munich, https://www.ycombinator.com/companies/comena/jobs/y1pnAQ6-forward-deployed-engineer, not counted)
pain: DME suppliers face a 2026 competitive-bidding window, prior-auth exemptions, and documentation audits from January 2027 (https://www.hmenews.com/article/cms-provides-contract-counts-other-details-in-new-updates)
mvp: Referral/order-intake agent that extracts HCPCS items and documentation gaps from synthetic faxed prescriptions and checks them against public CMS DMEPOS LCD/coverage rules.
pitch: Owners, intake/billing managers of regional DME shops via VGM, AAHomecare and state HME association member lists, HME News and Medtrade exhibitor lists.
note: Weak E, strong F and R: fastest pitch route is direct to owner-operators, not vendors.

## assisted-living-communities
scores: E P M F R = 4 3 3 4 4
employers: SafelyYou (Senior Software Developer, https://jobs.foundationcapital.com/companies/safely-you/jobs/69381427-senior-software-developer-c-n); Aline (Agentic AI Engineer, https://www.remoterocketship.com/us/company/aline/jobs/agentic-ai-engineer-junior-united-states-remote/, aggregator); Mon Ami (Sr Data Engineer, https://www.engineeringforchange.org/?p=69836); Sensorum Health (Senior Software Engineer, https://talents.vaia.com/companies/sensorum-health/senior-software-engineer-152338990/); AxisCare (Senior Software Engineer, home care, https://wellfound.com/jobs/4141420-senior-software-engineer)
pain: No dated source found today; staffing turnover and move-in/care-plan paperwork are known pains (~, no URL)
mvp: Resident care-plan and incident-note summarizer on synthetic notes, with facility lists from state assisted-living licensing files.
pitch: Executive directors and operators of small AL chains, vendor founders via ALFA and state association member lists, state licensing registries, LeadingAge exhibitors.
note: P=3 because I found no sourced, budgeted pain; E depends on several adjacent roles (data engineer, home care).

## residential-treatment-centers
scores: E P M F R = 2 4 3 4 4
employers: No open engineering roles found. Vendors exist (ZenCharts, BehaveHealth) but careers pages not checked, role not confirmed.
pain: 42 CFR Part 2 consent/disclosure rules became enforceable 2026-02-16, forcing records and consent workflows to change (https://mondaq.com/unitedstates/healthcare/1739384/are-you-ready-the-42-cfr-part-2-final-rule-compliance-date-is-almost-here)
mvp: Part 2 consent-and-disclosure checker that flags notes/releases needing consent, using synthetic chart notes and the public rule text.
pitch: Clinical directors, admissions directors, owners via NAATP member list, SAMHSA treatment locator, state licensing lists, behavioral-health conference exhibitors.
note: Small facility owners decide fast, but no hiring-vendor evidence found.

## pharmaceutical-manufacturers
scores: E P M F R = 3 4 4 2 3
employers: Seal (Forward Deployed Engineer, FDE, GxP platform, London listing, US customers, https://www.ycombinator.com/companies/seal-2/jobs/FrYzntx-forward-deployed-engineer); Medable (AI Deployment Engineer, clinical not manufacturing, via Insight Global, https://insightglobal.com/jobs/find_a_job/california/palo-alto/ai-deployment-engineer/job-531918/, not counted); Veeva/MasterControl/Tulip (careers pages, roles not confirmed, listings seen were old)
pain: FDA keeps issuing CGMP warning letters citing data integrity and weak quality-unit oversight (https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/warning-letters/huons-co-ltd-724650-06152026)
mvp: Warning-letter observation classifier and CAPA draft generator, trained on the public FDA warning-letter archive and 483 observations.
pitch: Heads of Quality/QA, QMS leads, validation managers via ISPE/PDA exhibitor and speaker lists, FDA drug establishment registry, Seal and similar YC founders.
note: F=2: validated-system pharma buyers are slow; only Seal confirmed, and its role is London.

## education-consulting-and-testing
scores: E P M F R = 2 2 3 4 4
employers: No test-prep or admissions-consulting vendor with an engineering role found. Adjacent only: Cengage (FDE AI/ML, https://edtechjobs.io/jobs/6865313a-09b9-4772-98c9-502b95c38b5f-forward-deployed-engineer-ai-ml-data-science, not counted)
pain: No sourced, budgeted open pain found (~); essay feedback and admissions-counselor capacity are known, small-budget pains
mvp: College-essay feedback assistant using public Common App prompts and synthetic essays.
pitch: Owners of independent test-prep and admissions firms via IECA, NACAC and HECA member directories.
note: Weak E and P; quick sales to owners but little hiring signal.

## health-insurance-carriers
scores: E P M F R = 4 5 4 2 3
employers: Cohere Health (Sr. Forward Deployed Engineer, FDE, https://jobgether.com/offer/6a642dcc1b23f4f87b38475a-sr.-forward-deployed-engineer, aggregator, careers page role not confirmed); CLERA (Forward Deployed Engineer, FDE, via aggregator https://www.wearedevelopers.com/jobs/ext/7134231/forward-deployed-engineer); OpenAI (FDE Healthcare, payers, https://openai.com/careers/forward-deployed-engineer-(fde)-healthcare-nyc-new-york-city/); Hippocratic AI (https://jobs.generalcatalyst.com/companies/hippocractic-ai/jobs/82622170-forward-deployment-engineer)
pain: Payers must have FHIR prior-auth APIs operational by 2027-01-01 (about 10 weeks away) (https://www.insurancebusinessmag.com/us/news/benefits/health-plans-have-10-weeks-to-meet-the-prior-auth-api-deadline-and-the-burden-hasnt-eased-yet-594390.aspx)
mvp: Da Vinci CRD/PAS prior-auth API prototype on the public HL7 Da Vinci reference implementation and Synthea FHIR data.
pitch: Heads of Engineering/Product at payer-tech vendors and health plan IT/interoperability leads via CMS payer lists, AHIP and HIMSS exhibitor lists, YC directory.
note: F=2: payer buyers are slow, so pitch the vendors.

## property-casualty-insurers
scores: E P M F R = 3 4 4 4 4
employers: Strada (Forward Deployed Engineer, FDE, https://jobs.645ventures.com/companies/strada-2/jobs/53973094-forward-deployed-engineer, posted 2025, not re-confirmed); Outmarket.AI (Forward Deployed AI Engineer, https://jobs.signalfire.com/companies/outmarket-ai/jobs/83608710-forward-deployed-ai-engineer, India, older); Insurity (FDE, Noida, https://jobs.jobvite.com/insurity-in/job/ofGZzfwd); ReSource Pro (Senior Forward Deployed AI Engineer, Pittsburgh, https://www.careerbuilder.com/job-details/senior-forward-deployed-ai-engineer-pittsburgh-pa--3762ed26-0257-456a-b8bb-6beba0eae0a3); Harper (underwriter role only, not engineering)
pain: Commercial submission intake backlog: brokers send messy emails/PDFs and underwriters re-key them, a workload carriers are buying AI for (https://www.insurancethoughtleadership.com/ai-machine-learning/making-ai-work-commercial-submission-intake)
mvp: Submission-intake extractor turning sample ACORD 125/140 PDFs and broker emails into structured quote requests, using public ACORD sample forms and synthetic emails.
pitch: Heads of Underwriting Ops, COO/CTO at MGAs via state DOI licensee lists, MGAA and Dearborn Labs/accelerator portfolios, ITC and InsurTech exhibitor lists.
note: E=3 because many roles are dated or India-based; none confirmed this week.

## legal-support-services
scores: E P M F R = 5 4 5 4 4
employers: OpenAI (FDE Legal, NYC/SF, FDE, https://jobs.ashbyhq.com/openai/832094fd-4d89-4fe4-bc18-9ba88d347a18/application); August (Forward Deployed Engineer, FDE, https://jobs.signalfire.com/companies/august-2-dafedc8d-65f7-4c0b-aa26-88566ca82e29/jobs/79550982-forward-deployed-engineer); Norm AI (Forward Deployed Legal Engineer, FDE, NYC, posted 2026-07-28, via search listing, careers page not opened); Everlaw (Senior Software Engineer, AI Platform, via search listing); Phaselab (Founding AI Engineer, https://jointaro.com/jobs/phaselab/founding-ai-engineer-phaselab)
pain: Document review and eDiscovery cost remain heavy, which is why Everlaw, Phaselab and legal-AI vendors are hiring AI engineers (https://jointaro.com/jobs/phaselab/founding-ai-engineer-phaselab); no stronger budget source found (~)
mvp: Privilege/responsiveness review demo on the public Enron email corpus (EDRM) and CourtListener/RECAP filings.
pitch: Founders/CTOs at legal-AI startups, LPO owners, litigation support directors via ILTACON and Legalweek exhibitor lists, ACEDS and state bar/LPO directories, YC directory.
note: Strong across the board; P rests on hiring signal, not a dated budget source.

## answering-services
scores: E P M F R = 5 4 3 5 4
employers: Phonely (Forward Deployed Engineer, FDE, https://www.ycombinator.com/companies/phonely/jobs/sTAy0qR-forward-deployed-engineer); Acrely (Forward Deployed Engineer, FDE, https://www.ycombinator.com/companies/acrely/jobs/3hQTILl-forward-deployed-engineer); Retell AI (Senior Forward Deployed Engineer, FDE, via https://builtin.com/job/senior-forward-deployed-engineer/7698544); PolyAI (Forward Deployed AI Engineer, FDE, NY, https://careers.georgian.io/companies/polyai-2/jobs/54958430-forward-deployed-ai-engineer-must-be-in-ny); Synthflow (Senior Python / Go engineer, via https://www.devjobsscanner.com/company/synthflow-ai/, aggregator)
pain: SMBs and call centers are switching to voice agents to replace human receptionists and overflow, shown by multiple funded FDE-hiring vendors (https://www.workatastartup.com/jobs/85445); no spend figure found (~)
mvp: Voice receptionist for a trade business built on Twilio plus an LLM, demoed on synthetic call scripts (no public call dataset).
pitch: Owners of answering services, founders and heads of deployment at voice-AI vendors via ATSI member list, YC directory, workatastartup.com, Twilio/Vapi community.
note: E and F are very strong; M=3 as demos rely on synthetic calls.
