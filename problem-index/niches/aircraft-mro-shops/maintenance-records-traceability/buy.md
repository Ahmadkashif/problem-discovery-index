# Records Scanning That Checks Instead of Stores

**Niche:** [[niches/aircraft-mro-shops/maintenance-records-traceability/profile|Aircraft Maintenance Records & Logbook Audits]]
**Industry:** [[industries/aircraft-mro-shops|Aircraft MRO & FBO Shops]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Aircraft records platforms digitise logbooks into searchable PDFs; the owner still pays someone to read them every time a question comes up.
**Tags:** #transformers #large-language-models #feature-engineering #compliance #data-integration
**Contested on:** Every serious competitor in this niche is fighting to prove an aircraft's history complete (every AD, inspection, major repair and alteration traced through its logbooks) before a buyer's or lessor's records auditor finds the gap, and whoever finds the gap first takes the account.

## The Problem
Owners and operators scan their records to protect against loss and to share them for sales and shop visits. The digital copy is an image with OCR text at best, indexed by book and date range. Answering "when was this AD last complied with, and how?" still means paging through.

## What Already Exists
Bluetail (back-to-birth records management with crowdsourced on-site scanning), flydocs (Lufthansa Technik) for airline and lessor records, and generic document management and OCR.

## The Customization Gap
The adaptation needs: (1) handwriting-tolerant extraction of logbook entries into typed events (inspection, AD compliance, repair, alteration, component change); (2) mapping of free-text AD references to the FAA's AD numbers and revisions, including old-format numbers; (3) linkage of 337s and STCs to the entries that installed them; (4) continuous checks against new ADs as they are issued; and (5) an aircraft "records health" view showing open questions before anyone needs the records.

## Target Customer
Records departments at MROs and FBO shops that manage records for customer aircraft; flight departments and management companies.

## Impact If Solved
Turning records lookups from ~30–60 minutes of paging into a query with a cited answer (estimate) saves a records clerk several hours a day. Gaps found before a sale or shop visit avoid the days of delay a late discovery causes.
