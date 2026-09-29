# Supplier Risk & Dependency

**Parent Industry:** [[industries/procurement-spend-platforms|Procurement & Spend Platforms]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in supplier risk is fighting to tell a company which single supplier failure would actually stop its operations — and whoever maps dependency rather than scoring suppliers takes the account.

## Profile
**Market Size:** ~$1.1B US supplier risk monitoring, third-party risk management and resilience software
**Share of Parent Industry:** ~12% of procurement software revenue, grown sharply on concentration and disruption concerns
**Digital Adoption:** Medium — risk subscriptions are widely bought and describe suppliers rather than exposure
**Target Buyer:** Supply chain risk, third-party risk and business continuity leaders
**Automation Potential:** Very High — dependency mapping is a graph problem over data the company already holds

## What Makes This a Distinct Niche
Supplier risk became a board-level concern through a decade of disruption, and the market responded with subscriptions that supply information about suppliers: financial health scores, sanctions screening, cyber ratings, sustainability assessments, adverse media. All of it is about the supplier. None of it answers the question the board is actually asking, which is about the buyer: if this supplier fails, what stops, how quickly, and what would we do. That is a question about dependency — which parts, sites, products and revenue lines rest on which supplier, whether an alternative exists and has been qualified, how much inventory buffers the gap, and whether the tooling can be moved. Every input to it is inside the company: bills of materials, sourcing records, qualification status, inventory positions, revenue attribution. The risk subscriptions cannot answer it because they do not have that data, and the procurement systems that do have it do not ask the question.

## Current Tools & Gaps
Dun & Bradstreet, EcoVadis, Craft, Interos and the third-party risk platforms supply supplier-level monitoring and scoring; business continuity tooling exists separately; some enterprises have built dependency mapping internally at substantial cost. The gaps: dependency is not modelled, so criticality is assessed by spend — which is the wrong proxy, since the supplier of a low-cost single-source component can stop a production line while the largest supplier by spend has three alternatives; sub-tier visibility is asserted by questionnaire rather than derived; qualification status of alternative suppliers is held in quality systems and is not visible in risk assessment, so a theoretical second source that would take six months to qualify is counted as mitigation; and nobody measures time-to-recovery, which is the only output that matters and is the one a board actually asks for.

## Problems
- [[niches/procurement-spend-platforms/supplier-risk-dependency/build|🔨 Build: The Dependency Graph and Time to Recovery]]
- [[niches/procurement-spend-platforms/supplier-risk-dependency/buy|🛒 Buy: Network Resilience Methods From Reliability Engineering]]
- [[niches/procurement-spend-platforms/supplier-risk-dependency/fix|🔧 Fix: Criticality Assessed by Spend]]
