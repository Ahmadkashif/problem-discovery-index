# History: BI & Analytics Platforms

**Industry:** [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
**Primary Wave:** [[series/eras/wave-07-big-data|7 — Big Data]]
**Secondary Wave:** [[series/eras/wave-03-pc-spreadsheet|3 — The PC & the Spreadsheet]]
**Origin Parent:** none — see "The Missing Origin," below
**Episode Tier:** 1
**Transferable Pattern:** A category that competes with a free, already-installed, zero-training-cost incumbent has not won until its own users stop exporting the answer back into that incumbent.

> **Template note.** This industry has no single origin institution and no origin event in the SABRE or ERMA sense. What it has instead is a three-decade succession of vendors solving the same problem — getting a business question answered without waiting for the data-processing department — against a competitor that never left the building. That succession, not a founding moment, is this file's spine.

## Before the Semantic Layer Had a Name

By the late 1980s the constraint [[series/eras/wave-03-pc-spreadsheet|Wave 3]] describes — a business question had to be turned into a program by someone who wrote programs — had a partial answer inside IT: a **query and reporting layer** sitting on top of the corporate database, so a report could be generated without a new COBOL job for every request. **Business Objects, founded in 1990 by Bernard Liautaud and Denis Payre**, built its whole product around a specific idea it called the "universe" — a semantic layer translating database tables into business terms, "stored centrally and made selectively available to communities of users." **Cognos**, founded in 1969 as Quasar Systems and renamed in 1982, and **MicroStrategy**, founded in 1989, ran variations on the same idea: IT builds and governs the model, business users query within it.

This was real progress and it was also gate-kept. A universe or a Cognos model was built by IT, changed slowly, and reflected IT's priorities. Meanwhile, on every desk in the same building, [[series/eras/wave-03-pc-spreadsheet|the spreadsheet]] answered the questions the governed reporting layer was too slow to reach — ungoverned, instant, and, per that wave's own file, wrong in some cell of roughly 94% of audited real-world models. **Both things were true of the same organisation at once: a slow, correct, centrally governed number, and a fast, ungoverned, frequently wrong one** — and employees overwhelmingly chose fast.

## The Origin Event — a Succession, Not a Moment

There is no single trigger here, and naming one would misstate the category. Instead there is a sequence, each entrant winning by being closer to where the data or the user already was:

| Year | What arrived |
|---|---|
| **1993** | **QlikTech founded in Lund, Sweden**, by Björn Berg and Staffan Gestrelius; QlikView ships 1994. Its associative, in-memory engine let a user click any value and see every related value re-filter live, without pre-aggregating a cube — a genuinely different architecture from the query-against-a-warehouse model. |
| **2003** | **Tableau founded** in Mountain View by Christian Chabot, Pat Hanrahan, Chris Stolte and Andrew Beers, commercialising Polaris, a Stanford visualisation research project. Its VizQL engine turned drag-and-drop shelf placement directly into a database query, making a business analyst — not a report author — the one driving. |
| **Jan 2008** | **SAP completes its $6.8B acquisition of Business Objects**; **IBM completes its $4.9B acquisition of Cognos** — nine days apart. The first wave of BI vendors, one after another, gets absorbed into infrastructure giants rather than continuing as an independent category. |
| **2009–2011** | Microsoft's SQL Server Reporting Services team, under the codename **"Project Crescent,"** ships an Excel-native visualisation add-in in July 2011 — the direct ancestor of Power BI, itself built on the earlier PowerPivot/Power Query Excel add-ins. |
| **2012** | **Looker founded** by Lloyd Tabb and Ben Porterfield, reintroducing Business Objects' governed-semantic-layer idea for the warehouse era under the name **LookML** — a modelling language a data team writes once so a business user can explore without knowing SQL. |
| **2013 → 2015** | Microsoft rebrands Crescent as **Power BI for Office 365** (Sept 2013), then ships it as a free-standing **general-availability product on 24 July 2015** — bundled into the Office estate Microsoft already owned. |
| **2013** | **Tableau IPOs on the NYSE (ticker DATA), 17 May 2013**, raising over $250M. |

**The pattern across every row is the same one Wave 3 already names**: whichever tool sat closest to where the user or the data already lived — the spreadsheet interface, the warehouse, the Office 365 licence a company had already paid for — took share from whichever tool asked the user to go somewhere new.

## The Contest

The contest that matters most for this file is not the founding sequence above; it is what happened to the founders in **2019**, and it settles the question of who won.

**On 10 June 2019, Salesforce announced its acquisition of Tableau for $15.7 billion in an all-stock deal** — its largest acquisition to date — closing that August. **On 6 June 2019, four days earlier, Google announced its acquisition of Looker for $2.6 billion**, closing in February 2020 once regulatory review cleared. Two of the category's most technically distinct products — Tableau's visual-query engine, Looker's warehouse-native semantic layer — were absorbed within days of each other into two of the largest platform companies on earth, each looking for a data-and-analytics anchor inside its own cloud or CRM estate. **Qlik**, the earliest of the three, had already left public markets in **August 2016** when Thoma Bravo completed an approximately $3B all-cash take-private acquisition.

By the time the dust settled, none of the three defining self-service BI vendors of the 2000s and 2010s remained an independent public company. **The category's own winners did not survive as a category — they survived as acquisitions inside larger platforms**, echoing SAP–Business Objects and IBM–Cognos a decade earlier almost exactly. Two consolidation waves, roughly a decade apart, absorbing two successive generations of the same idea. Microsoft, notably, never needed to acquire its way in: **Power BI won distribution simply by already being inside Office 365**, which every one of these companies' prospective customers had already bought.

## The Trade-Off

Every vendor in this file's table rebuilt some version of Business Objects' 1990 universe — Looker's LookML is the clearest instance, an openly stated re-solving of the same problem three decades later — and every rebuild made the identical trade explicit without ever fully resolving it: **speed of self-service versus a single governed definition of a metric.**

A governed semantic layer, correctly maintained, guarantees that "active users" means the same thing in every dashboard built against it. Maintaining it is slow, requires a data team's continuous attention, and is exactly the friction self-service tooling exists to remove. Remove the friction and a business user can define their own calculated field in an afternoon — which is precisely how an organisation ends up, as this vault's own hub note for the industry puts it, with "three dashboards report active users and give three numbers, each defensible, each computed slightly differently." **Nobody in this history solved this trade. Each generation rediscovered it, gave it a new product name, and shipped a partial fix that the next generation's self-service layer eroded again.**

## What Became Cheap

**Asking an ad hoc question of a large dataset without waiting for someone in IT to write the query.** That is the entire arc from Business Objects' universes through Qlik's associative engine, Tableau's drag-and-drop VizQL, and Power BI's bundled Excel-native interface — each one further lowering the skill and time cost of getting from "I wonder whether" to a chart. It is the same cost Wave 3's spreadsheet made cheap first, applied to warehouse-scale data the spreadsheet's row limits and single-machine memory could not hold — which is exactly why this file's primary wave is 7, not 3, even though its opponent has never changed.

## The Missing Origin

No `origins/` file in this vault claims this industry as a child, and none should be invented here. Retail banking, hospital systems, exchanges — the vault's eighteen origins — all involve an institution computing something about its own operations under competitive or statutory pressure. BI and analytics platforms are not that: they are tooling built to answer questions *about* other industries' data, sold horizontally across all of them, with no single institutional parent whose founding pressure explains the category. **If this file has an origin at all, it is Wave 3 itself** — the spreadsheet's demonstration, in 1979, that a non-programmer could ask a computer a business question directly — and Wave 3's own file is explicit that it "created no industry of its own," only an incumbent every later category has had to answer to. This file treats that incumbent as this industry's true origin pressure, and the absence of an institutional parent as a finding, not a gap to paper over.

## What's Still Open

The vault's own hub note for this industry states the diagnosis directly: these platforms hold "the complete record of how an organisation asks questions about itself" and "render[s] charts and never analyses the asking" — the one dataset the category uniquely holds and has never turned on itself.

- [[problems/bi-analytics-platforms/high-impact|🔴 Metric Definition Drift]] — Business Objects' 1990 problem, unsolved through four subsequent product generations
- [[problems/bi-analytics-platforms/low-impact-1|🟡 Dashboard Sprawl and Certification]]
- [[problems/bi-analytics-platforms/low-impact-2|🟡 Data Quality Alerting]]
- [[problems/bi-analytics-platforms/worker-life-1|🟢 Analyst Ad Hoc Request Queue]]
- [[niches/bi-analytics-platforms/spreadsheet-last-mile/profile|Spreadsheet Last Mile]] — the export-to-Excel button every platform still ships, because every platform still loses there
- [[niches/bi-analytics-platforms/metric-definition-drift/profile|Metric Definition Drift]]
- [[niches/bi-analytics-platforms/question-log-intelligence/profile|Question Log Intelligence]] — the unbuilt idea this file's diagnosis points straight at
- [[niches/bi-analytics-platforms/natural-language-query/profile|Natural Language Query]] — the newest attempt at the same 1990 problem
- [[niches/bi-analytics-platforms/dashboard-estate-lifecycle/profile|Dashboard Estate Lifecycle]]

## The Transferable Pattern

> **When a product category's real competitor is not the other vendors in its Gartner quadrant but a free, universally known, already-installed tool, look for the feature every vendor ships to lose gracefully to it — the export button, the "download as CSV," the API built expressly to hand data back to the incumbent. That feature is an admission, and it tells you exactly where the product has not yet won the argument it thinks it is having.**

Every vendor in this file's table ships an export-to-Excel button, without exception, across four decades and three changes of underlying architecture. That is not a minor interoperability courtesy. It is the industry's own quiet confession that the spreadsheet remains the last mile of every workflow it sells against — the place a number goes to be trusted, reshaped, or checked by a human who does not trust the dashboard it came from. An FDE evaluating this category, or any category shadowed by a general-purpose incumbent, should treat that escape hatch's usage rate as a truer adoption metric than any dashboard-view count the vendor will show you.

**Sources:** Wikipedia, *Tableau Software* (2003 founding, Stanford/Polaris origin, 17 May 2013 IPO, 10 June 2019 Salesforce acquisition, $15.7B, closed 1 Aug 2019); Wikipedia, *Looker (company)* (Jan 2012 founding, LookML, 6 June 2019 Google acquisition, $2.6B, closed Feb 2020); Wikipedia, *Qlik* (1993 founding in Lund, Sweden; QlikView 1994; 2010 IPO; Aug 2016 Thoma Bravo take-private, ~$3B); Wikipedia, *Power BI* (Project Crescent, July 2011; Power BI for Office 365, Sept 2013; general availability, 24 July 2015); Wikipedia, *BusinessObjects* (1990 founding; "universes" semantic layer; SAP acquisition announced 7 Oct 2007, completed 22 Jan 2008, $6.8B); Wikipedia, *Cognos* (1969 as Quasar Systems, renamed 1982; IBM acquisition announced Nov 2007, completed 31 Jan 2008, $4.9B); `series/eras/wave-03-pc-spreadsheet.md` and `series/eras/wave-07-big-data.md`; this vault's `industries/bi-analytics-platforms.md`.
