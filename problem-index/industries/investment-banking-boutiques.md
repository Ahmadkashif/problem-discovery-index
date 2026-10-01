# Investment Banking Boutiques

## Profile
**Category:** Capital Markets & Investment Research
**Market Size:** ~$12B a year in global M&A advisory fees earned by independent advisers (Dealogic reported ~$6B for the first half of 2026), plus mid-market sell-side, capital-raising, restructuring and opinion fees at the regional and middle-market banks — a combined fee pool in the order of ~$20–25B, as an estimate
**Tech Maturity:** Medium at the data layer, low at the workflow layer — every firm licenses Capital IQ, FactSet or PitchBook and runs its processes through Datasite or Intralinks, and almost every deliverable is still assembled by hand in Excel and PowerPoint by analysts working through the night.
**Workforce:** Analysts and associates (the production layer), vice presidents and directors running processes, sector-coverage managing directors originating mandates, restructuring and valuation specialists, fairness-opinion committees, research and knowledge-management staff, and offshore support teams producing comps and profiles

## Key Pain Themes
A boutique sells judgment and pays for it in analyst hours. Every pitch is a book of forty to eighty pages — situation overview, trading comps, precedent transactions, a valuation football field, a buyer universe, credentials — built on spec for a mandate the firm may not win, and the same comps are re-spread and the same pages re-formatted for the next pitch a week later. Once a mandate is won the work shifts to the process: a teaser and a CIM, a buyer list of fifty to three hundred names, NDAs, a data room, hundreds of diligence questions, first-round indications, management meetings, final bids. The process is the product the client pays for, and every one of those steps generates a record of which buyers engaged, how deeply, and what they eventually offered.

That record is the industry's most valuable asset and is kept in a buyer tracker spreadsheet that dies with the deal. The managing director who knows that a particular sponsor "always takes the meeting and never bids", or that a strategic acquirer's corporate development team goes quiet before its board says no, carries that knowledge personally and takes it with them when they move firms. Meanwhile restructuring practices race court and maturity calendars, fairness-opinion committees work under the shadow of Delaware litigation, and the analyst class absorbs it all as hours.

## Current Tech Landscape
Market data comes from S&P Capital IQ, FactSet, PitchBook, LSEG and Bloomberg; deal intelligence from Mergermarket and PitchBook; restructuring intelligence from Octus, Debtwire and 9fin. Relationship and pipeline tracking runs in DealCloud (Intapp) or Salesforce, data rooms in Datasite, Intralinks, Ansarada or Firmex, and pitch production in PowerPoint with Macabacus, UpSlide or FactSet's Office plug-ins. A new layer of generative research tools — Rogo, Hebbia, AlphaSense — is being trialled for document search and first drafts. The gap is the same everywhere: the tools hold the inputs and the deliverables, and none of them holds the process outcomes, so nothing the firm learns on one mandate is available, in usable form, on the next.

## Problems
- [[problems/investment-banking-boutiques/high-impact|🔴 High Impact: The Buyer List Built From Memory]]
- [[problems/investment-banking-boutiques/low-impact-1|🟡 Low Impact: Comps and Precedents for Companies Nobody Covers]]
- [[problems/investment-banking-boutiques/low-impact-2|🟡 Low Impact: The Diligence Q&A Log]]
- [[problems/investment-banking-boutiques/worker-life-1|🟢 Worker Life: The Analyst Building Pitches That Will Not Win]]
- [[problems/investment-banking-boutiques/worker-life-2|🟢 Worker Life: The Associate Ticking and Tying at Midnight]]
- [[problems/investment-banking-boutiques/ml-opportunity|🧠 ML Opportunities]]
- [[problems/investment-banking-boutiques/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
A boutique running forty sell-side processes a year contacts several thousand buyers, and for every one of them records — somewhere — whether they signed the NDA, opened the data room, submitted an indication, attended the management meeting and bid in the final round, and at what price. Over a decade that is a labelled dataset of buyer behaviour that no data vendor can reconstruct, because it consists of private conduct in private processes. It is the single thing a boutique owns that a competitor structurally cannot buy, and it is stored in per-deal Excel files that nobody reopens. The honest constraint is that much of the surrounding material — the client's financials, the CIM, the data room contents — belongs to the client and is bound by NDAs; the buyer-behaviour record is the bank's own work product and is the part worth building on. Research workflow automation in this industry is therefore less about writing the CIM faster and more about turning the firm's process history into institutional memory.
