# Off-Limits and Conflict Clearance Across a Global Client Book

**Industry:** [[executive-search-firms|Executive Search Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every name on every longlist has to be cleared against every client's off-limits terms, corporate family and time window before anyone calls, and search firms do it with CRM flags, spreadsheets and an email to the partner who owns the client.
**Tags:** #k-nearest-neighbors #graph-theory #word-embeddings #evaluation-metrics #compliance #data-integration #automation

## The Problem
A retained search firm promises its clients that it will not recruit their people. Heidrick & Struggles' 10-K describes refraining from recruiting a client's employees "typically not more than one year from the commencement of a search", often limited by geography or business unit, and Korn Ferry's lists off-limits agreements as a reason it loses search opportunities to competitors. In practice the terms vary by client: some cover the whole group for longer than a year, some only the division served, some only executives above a level; private-equity sponsors may extend them to the portfolio. A firm with thousands of active and recent clients carries thousands of overlapping restrictions with different start and end dates.

Every candidate on a longlist must be checked against all of them. The candidate's employer has to be resolved to its ultimate parent, its sponsor and its joint ventures; the employer's name in the CRM rarely matches the client record; and the restriction may have lapsed last month or started yesterday when a colleague in another office signed a new mandate. A miss means approaching a client's executive, which is the fastest way to lose the client. An over-cautious check strikes candidates who were in fact available, which weakens the slate.

## What Already Exists
Search CRMs (Thrive TRM, Clockwork, Invenias, Ezekia, Cluen Encore) let firms flag client companies and warn when a candidate's current employer is flagged. Law firms solve a structurally similar problem with conflict-checking and relationship-intelligence platforms such as Intapp, which resolve parties to corporate families and route conflicts for clearance; BoardEx data already feeds Intapp through a partnership. Corporate hierarchy data is sold by commercial data vendors.

## The Customisation Gap
The legal conflict model checks parties to a matter; search needs a check on people, against the employer they work for today and the terms each client negotiated. That requires: off-limits terms stored as structured rules (scope by group, division, geography and level; start and end dates; whether the restriction covers sourcing as well as recruiting); entity resolution from the free-text employer on a candidate record to the client's corporate family, including PE portfolio companies and recent acquisitions; time-aware checks that re-run when a mandate is signed or a restriction lapses; a "source but don't approach" category for information calls; and an audit trail showing the client the check was done. None of the search CRMs model terms at that resolution, and legal conflict tools do not model candidates.

## Impact If Solved
The researcher building a ~150-name longlist clears it in minutes rather than a day of cross-checking, the firm stops losing clients to accidental approaches, and partners stop striking available candidates out of caution — which, for a firm whose off-limits list grows with every win, is the difference between growth widening and narrowing the talent pool it can search.
