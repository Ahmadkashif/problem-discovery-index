# Mass Filing Platform for DACA/TPS Renewals

**Niche:** [[niches/immigration-law/daca-tps-humanitarian/profile|DACA/TPS & Humanitarian Relief]]
**Industry:** [[industries/immigration-law|Immigration Law]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** When a DACA renewal window or TPS re-registration period opens, legal aid organizations must file hundreds of near-identical applications within weeks using workflows designed for one case at a time — a batch processing platform would turn a crisis response into a routine operation.
**Tags:** #workflow-orchestration #automation #data-integration #large-language-models #quick-win #worker-facing #compliance

## The Problem
DACA renewals and TPS re-registrations are mass filing events. When USCIS opens a DACA renewal period or extends TPS for a country, every beneficiary must file within a specific window — often 60-150 days. A legal aid organization serving 200 DACA recipients must contact each client, verify current address and employment, identify what has changed since the last filing, update the I-821D/I-765/I-765WS forms with new information, collect fees or fee waiver requests, assemble supporting documents (updated employment letters, address verification), and file all 200 applications before the deadline. Using current tools, this is done one case at a time: open client file, review last filing, call client, update information, populate forms, print, review, mail. Each renewal takes 1-2 hours. Processing 200 renewals requires 200-400 hours of staff time compressed into a few weeks — overwhelming organizations that normally handle 10-15 cases per week. Staff work overtime, cut corners on review, and inevitably miss some clients who couldn't be reached in time.

## Why Nobody Has Built This
The market is nonprofits and legal aid organizations with minimal budgets — they cannot pay enterprise software prices. The user base is small (perhaps 500-1,000 organizations nationally that handle DACA/TPS at scale). Policy volatility creates platform risk — if DACA is terminated (as multiple administrations have attempted), the product loses its core use case overnight. The batch workflow requires integration with USCIS filing (either printing and mailing or e-filing through the USCIS online system, which has limited API access). Additionally, the platform must handle the "diff" between the client's current information and their last filing — a deceptively complex data problem when prior filings are stored as PDFs in shared drives rather than structured data.

## What to Build
A batch renewal platform with five components: (1) client database with structured records from prior filings — every field from the last I-821D/I-765 stored in structured format, not as a PDF, (2) renewal preparation workflow — for each client, auto-generate a "what changed?" questionnaire covering only the fields that could have changed (address, employer, criminal history, travel), delivered via text/WhatsApp in the client's language, (3) batch form population — once client updates are received, auto-populate all required forms for each client with updated data, flagging any inconsistencies or missing information, (4) quality control dashboard — show staff which renewals are ready to file, which need client follow-up, which have issues, with aggregate statistics ("178/200 renewals ready, 15 pending client response, 7 have issues"), (5) filing tracking — once filed, track receipt notices and approval for all cases in a single view. An LLM layer handles freeform client responses ("I moved to 123 Oak St in March") and maps them to structured form fields.

## Target Customer
Legal aid organizations and community immigration programs serving 50+ DACA recipients or TPS beneficiaries, currently processing renewals one at a time during compressed filing windows.

## Impact If Built
Reduces per-renewal processing time from 1-2 hours to 15-20 minutes (data update and review only), enabling a 5-person organization to process 200 renewals in 2 weeks instead of 8 weeks. Eliminates missed renewals due to capacity constraints — each missed DACA renewal means a person loses work authorization and risks deportation. For organizations serving 200+ DACA recipients, this is the difference between maintaining service capacity and triaging which clients get helped.
