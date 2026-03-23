# SMS-First HR Platform for Non-Desk Workers

**Niche:** [[niches/hr-consultants/hr-skilled-trades/profile|HR for Skilled Trades & Field Workforces]]
**Industry:** [[industries/hr-consultants|HR Consultants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An HR interaction layer where every employee touchpoint — document signing, benefits enrollment, PTO requests, policy acknowledgments, safety certifications — happens via text message rather than email or web portal, because trade workers don't have company email and rarely log into software.
**Tags:** #automation #nlp #worker-facing #ai-agent #workflow-orchestration

## The Problem
A plumbing company with 80 field workers needs to distribute a new handbook, collect signed acknowledgments, enroll workers in benefits, and verify safety certifications — all for workers who: don't have company email addresses, don't own computers, may not have smartphones (basic phone with SMS only), work at different job sites daily, and may speak primarily Spanish. The HR consultant sends an email with a DocuSign link, and 60% of workers never see it. The consultant prints paper copies and sends them to job sites, and half come back unsigned. Benefits enrollment requires workers to access a web portal during a 30-day window, and 30% miss the window because they never logged in. Every HR process designed for office workers breaks for field workforces.

## Why Nobody Has Built This
HR technology is built by people who work at desks with email and web browsers. The assumption that every employee has company email and can log into a portal is baked into every HRIS, benefits platform, and compliance tool. Building an SMS-first HR platform requires: text message-based document delivery and e-signature (compliant with ESIGN Act), SMS-based interactive workflows for benefits enrollment and PTO requests, multilingual support (Spanish at minimum, with expansion to Portuguese, Vietnamese, and other trade workforce languages), and integration with the employer's HRIS/payroll system to sync employee data. The SMS infrastructure is straightforward; the compliance layer (ensuring text-based signatures and enrollments are legally valid) is the hard part.

## What to Build
An SMS-based HR interaction platform that handles: (1) document distribution and acknowledgment ("Reply 1 to confirm you received the updated safety policy"), (2) benefits enrollment ("You have 3 plan options: A-Family $150/paycheck, B-Individual $75/paycheck, C-Decline. Reply A, B, or C"), (3) PTO requests ("Reply your requested dates: MM/DD-MM/DD"), (4) certifications and training tracking ("Your OSHA 10 expires in 30 days — reply 1 to schedule renewal"), and (5) two-way HR Q&A ("Text HR to ask a question — responses within 4 hours"). All interactions available in English and Spanish. Data syncs to the employer's HRIS. The HR consultant manages the platform across all their trade company clients.

## Target Customer
HR consultants serving construction, HVAC, plumbing, landscaping, and manufacturing companies with 20-200 field workers who cannot be reached through email-based HR tools.

## Impact If Built
Increases HR communication reach from 40-60% (email/portal-based) to 90%+ (SMS-based) for field workforces. Reduces benefits enrollment failures from 20-30% to under 5%. Enables the HR consultant to serve trade company clients without the manual paper-based workaround that currently doubles the time required.
