# Business Location Data Licensing

**Parent Industry:** [[industries/directory-and-list-publishers|Directory & List Publishers]]
**Category:** High Market Share
**Contested on:** Every serious competitor in this niche is fighting to be the licensee's reference file for which businesses exist where right now — catching openings, moves and closures first — and whoever scores freshest in the licensee's own ground-truth audit takes the contract.

## Profile
**Market Size:** ~$600M US licensing of compiled business-location (place) data to map, search, navigation, local listing, retail analytics and risk platforms (estimate)
**Share of Parent Industry:** ~8% of the ~$8B US buyer spend on directories, lists and compiled business data, including directory advertising (estimate; see overview)
**Digital Adoption:** High — bulk files and APIs, refreshed monthly or faster
**Target Buyer:** Head of Maps or Places data at a platform; VP of Data Partnerships at a location-analytics firm
**Automation Potential:** High for ingestion and matching; closure and attribute verification still need calls or field signals

## What Makes This a Distinct Niche
Here the compiled file is not sold to a marketer by the thousand but licensed whole to a platform that shows it to millions of people: a map's business pins, a voice assistant's "open now", a navigation app's destination, a retail analytics firm's competitor set. Compilers such as Data Axle, TransUnion's Localeze and Foursquare have long fed these platforms, and the local-listings industry syndicates corrections through them (see [[niches/marketing-agencies-smb/local-listings-reputation-data/profile|🔍 Local Listings & Reputation Data]]). The licensee audits the file against its own ground truth — user reports, field visits, its own crawls — and the contract follows freshness, above all on closures. Since July 2023 the Overture Maps Foundation has published an open places layer (59M+ places at launch, under a permissive licence), so the baseline is now free and the contest is entirely about being fresher and more correct than it.

## Current Tools & Gaps
Multi-source ingestion, entity matching, call verification and web change detection; licensee feedback through correction APIs. Gaps: closures are detected late because a closed business stops generating signals rather than generating a "closed" signal; licensees' user corrections rarely flow back to the compiler in structured form; and attribute freshness (hours, category, phone) is not measured separately from existence.

## Problems
- [[niches/directory-and-list-publishers/business-location-data-licensing/build|🔨 Build: Closure Detection Before the Licensee's Audit]]
- [[niches/directory-and-list-publishers/business-location-data-licensing/buy|🛒 Buy: Open Places Data as the Base Layer]]
- [[niches/directory-and-list-publishers/business-location-data-licensing/fix|🔧 Fix: The Correction Loop That Ends at the Licensee]]
