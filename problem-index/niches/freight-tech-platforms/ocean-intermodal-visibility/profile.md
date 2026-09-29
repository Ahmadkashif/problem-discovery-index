# Ocean & Intermodal — Milestone Reconciliation

**Parent Industry:** [[industries/freight-tech-platforms|Freight Tech Platforms]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in ocean and intermodal visibility is fighting to reconcile milestones reported by carriers, terminals, customs brokers and drayage providers into one true container timeline — and whoever produces the earliest correct availability and pickup signal takes the account.

## Profile
**Market Size:** ~$800M US ocean and intermodal visibility and container management
**Share of Parent Industry:** ~10% of freight technology revenue
**Digital Adoption:** Medium — data exists and arrives late, inconsistently and from uncooperative parties
**Target Buyer:** International supply chain leaders at importers; operations directors at freight forwarders and drayage providers
**Automation Potential:** High — this is entity resolution and event reconciliation across many sources, which is a well-understood class of problem

## What Makes This a Distinct Niche
An international container's journey is a sequence of reported events rather than a continuous position: booked, gated in at origin, loaded, sailed, transhipped, arrived, discharged, customs held or released, available for pickup, gated out, delivered, empty returned. Each event is reported by a different party — ocean carrier, origin and destination terminals, customs authorities, drayage providers — on its own schedule, in its own format, with its own definition. The same event has different names and different timestamps depending on who reported it, several parties report nothing at all until asked, and the most operationally important events are the ones with the least reliable reporting. An importer's actual question is narrow and specific: when can I pick this container up, and will demurrage start before I can. Answering it requires reconciling contradictory milestone reports into one timeline, which is the whole discipline of this sub-niche and has nothing in common with predicting a truck's arrival.

## Current Tools & Gaps
project44, FourKites and a set of ocean-focused specialists ingest carrier and terminal data with varying coverage. Terminal websites remain a primary source and are scraped. Customs status is available through brokers and government systems with lags. The gaps: milestone definitions are not standardised across carriers, so reconciliation is largely hand-maintained mapping; terminal appointment availability — which is what actually determines whether a container can be collected — is frequently in a separate system nobody integrates; demurrage and detention free-time clocks are calculated by importers in spreadsheets against terms that differ by carrier and terminal; and nothing predicts availability, so drayage is scheduled reactively after a container is already accruing charges.

## Problems
- [[niches/freight-tech-platforms/ocean-intermodal-visibility/build|🔨 Build: One Reconciled Container Timeline From Contradictory Sources]]
- [[niches/freight-tech-platforms/ocean-intermodal-visibility/buy|🛒 Buy: Entity Resolution and Event Reconciliation Off the Shelf]]
- [[niches/freight-tech-platforms/ocean-intermodal-visibility/fix|🔧 Fix: The Demurrage Clock Nobody Is Watching]]
