# Rural Plumber Field Reference and Job Documentation App

**Niche:** [[niches/plumbing-contractors/small-rural-plumbers/profile|Small & Rural Plumbers]]
**Industry:** [[industries/plumbing-contractors|Plumbing Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A mobile-first reference app that gives a rural plumber instant access to well pump sizing charts, septic system design tables, agricultural plumbing standards, and IPC/UPC code lookups — all available offline — plus simple job documentation and invoicing that works without cell service.
**Tags:** #large-language-models #decision-trees #feature-engineering #worker-facing #quick-win #automation

## The Problem
A rural plumber arrives at a farmhouse to troubleshoot a well pump that isn't maintaining pressure. They need to know: the well depth and static water level (from the well driller's report, if the homeowner still has it), the pump capacity required for the household's demand, the correct pressure tank sizing, the wire gauge needed for the pump motor at the well depth, and whether the pressure switch is failing or the pump itself is worn. This information lives in manufacturer spec sheets (Franklin Electric, Grundfos), state well construction standards, and the plumber's own experience. On the same day, they'll inspect a septic system for a real estate transaction — needing county health department forms that vary by jurisdiction — and then run a gas line to a shop heater, requiring NFPA 54/IFC code reference for sizing and clearances. Each task requires different reference materials that are currently scattered across truck-cab manuals, bookmarked websites (inaccessible without cell service), and the plumber's memory.

## Why Nobody Has Built This
The rural plumber market is large by establishment count (estimated 80,000-100,000 solo and two-person shops in the US) but each business spends very little on software — typically under $100/month total. Building a comprehensive field reference covering well pumps, septic systems, agricultural plumbing, gas piping, and general plumbing code requires consolidating information from dozens of sources across multiple code bodies (IPC, UPC, NFPA 54, state health departments, equipment manufacturers). The content must be accurate enough that a plumber stakes their license on it but simple enough to use on a phone screen in a crawl space. Offline functionality is mandatory — many rural job sites have no cell coverage. The low per-customer revenue makes traditional SaaS unit economics challenging, but the establishment count supports a high-volume, low-price model.

## What to Build
A mobile app (iOS/Android) with two modules: (1) a field reference library containing well pump sizing calculators (input: well depth, static water level, household demand → output: pump model recommendations, wire sizing, pressure tank sizing), septic system design tables (input: bedroom count, soil percolation rate, jurisdiction → output: tank size, drain field sizing, required setbacks), gas pipe sizing calculator (input: BTU load, pipe run distance, inlet pressure → output: pipe diameter per NFPA 54), and searchable IPC/UPC code sections for common residential scenarios, all cached locally for offline use; (2) a simple job documentation module where the plumber photographs the job, voice-dictates notes (transcribed by LLM), and generates a professional invoice — all syncing when connectivity returns. Priced at $19-39/month to fit the solo plumber's budget. Revenue supplemented by equipment manufacturer partnerships (pump sizing recommendations link to distributor ordering).

## Target Customer
Solo and two-person plumbing shops in rural areas who currently carry paper reference manuals in the truck, write invoices by hand, and lose 30-60 minutes per day looking up specifications they can't remember or can't access without cell service.

## Impact If Built
Saves 30-60 minutes per day in reference lookups and documentation, translating to one additional job per week for a plumber billing $100-150/hour. Reduces specification errors (wrong pump size, undersized gas line) that cause callbacks and code violations. Professional invoicing and job photos improve customer perception and reduce payment disputes. At $29/month targeting 80,000+ establishments, the product addresses a $28M+ annual revenue opportunity.
