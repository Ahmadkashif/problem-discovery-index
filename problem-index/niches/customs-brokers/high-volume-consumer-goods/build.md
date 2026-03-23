# Duty Optimization Review Engine

**Niche:** [[niches/customs-brokers/high-volume-consumer-goods/profile|High-Volume Consumer Goods Importers]]
**Industry:** [[industries/customs-brokers|Customs Brokers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool systematically reviews an importer's entry history to identify legal HTS reclassification opportunities, unclaimed trade program benefits, and eligible duty drawback claims — savings that exist in the data but require an expert to find.
**Tags:** #transformers #bert #tacit-knowledge-ml #revenue-impact #compliance

## The Problem
An importer of consumer electronics from China pays $2.3M annually in duties across 500 entries. An experienced customs broker reviewing the entry history might identify: 15 product lines classified under a general HTS heading at 4.4% duty that could be legally classified under a more specific heading at 2.6% (saving $180K); 3 products eligible for Section 301 tariff exclusions that were never claimed (saving $90K); and duty drawback claims on re-exported goods that were never filed (saving $40K). This "duty optimization review" is a high-value advisory service that only senior brokers perform — and only for their largest clients, because the analysis requires deep HTS expertise and 20-40 hours of manual review per client.

## Why Nobody Has Built This
Duty optimization requires tacit classification expertise: knowing that a "portable wireless speaker" classified under 8518.22 (loudspeakers in enclosures) at 4.9% might also qualify under 8527.92 (reception apparatus for radio-telephony) at free duty — if the product includes Bluetooth reception capability. This kind of classification arbitrage knowledge is built through years of experience with CBP rulings and HTS interpretation. Encoding it into a systematic review tool requires capturing the classification expert's reasoning patterns, not just the HTS code lookups.

## What to Build
A duty optimization engine that: (1) ingests an importer's 12-month entry history (HTS codes, duty rates, values, countries of origin); (2) identifies product lines where alternative HTS classifications exist at lower duty rates, supported by CBP CROSS rulings; (3) flags products eligible for trade program benefits (USMCA, GSP, Section 301 exclusions) not currently claimed; (4) calculates duty drawback eligibility for re-exported goods; (5) generates a duty savings report with specific recommendations and estimated annual savings.

## Target Customer
Senior customs brokers and trade compliance directors at brokerages serving importers with $1M+ in annual duty spend. Approximately 500 brokerages handle clients at this scale. Average engagement value: $15-30K per client review (performance fee on identified savings).

## Impact If Built
A systematic duty optimization review typically identifies 5-15% savings on an importer's duty spend. On $2M annual duties, that's $100K-$300K in client savings — generating significant advisory fee revenue for the broker and client loyalty that prevents competitive displacement.
