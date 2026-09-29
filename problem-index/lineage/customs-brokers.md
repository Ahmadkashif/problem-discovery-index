# Lineage: Customs Brokers

**Industry:** [[industries/customs-brokers|Customs Brokers]]
**Wave:** [[series/eras/wave-04-client-server-erp|4 — Client–Server & ERP]]
**The tool:** the Automated Broker Interface (ABI) — the electronic channel through which a licensed broker transmits entry data into Customs' Automated Commercial System
**Builder:** US Customs Service
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

An import entry was a paper packet, and somebody at Customs had to type it.

Commercial invoice, bill of lading, entry form: a broker assembled them, carried or mailed them to the port, and a Customs officer reviewed them and released or held the cargo by hand. Once Customs built a mainframe system of record for entries — the **Automated Commercial System (ACS)**, assembled across the 1980s — the paper did not go away. It simply acquired a second cost: a government clerk re-keying what a broker had already written.

That is the constraint the tool answers. Every entry was being written twice, once by the party who knew the goods and once by the party who owned the computer.

## What Got Built

**ABI is a door into the government's own mainframe, cut for the people who were already filling in the forms.** A broker keys entry data into a terminal or broker software, it transmits to ACS, and a response comes back — release, hold, duty due. Brokers use it, in the government's own words, "to obtain release of cargo, pay duties, update importer data, and carry out many more functions."

The artefact a working broker's software is actually built against is the interface specification — today the **CATAIR** (Customs and Trade Automated Interface Requirements), which fixes record layouts field by field. ABI survived the move from ACS to the **Automated Commercial Environment (ACE)** in 2016: the mainframe behind the door changed, the door did not.

## Who Built It, And Why Them

The US Customs Service, and the reason is ownership of the data rather than any interest in brokers.

Customs held the one thing no broker could build: the system of record that decided release. A private network could make a broker's office faster; only Customs could make the entry itself electronic. And the filers were concentrated. The federal government's 1994 *National Performance Review* recorded that **in 1993, 1,324 brokers and importers provided 93 percent of the data entered into ACS** — a few thousand parties writing nearly every entry in the country. Wire that population and you have wired the whole flow.

The same source gives the before figure: **in 1984, brokers and importers represented 8 percent of all Customs data entries.** ABI's start is widely dated to that same year. Whether 1984 is the launch or merely the first year counted, the curve is the story: in under a decade the trade went from keying almost none of Customs' data to keying almost all of it.

## What It Cost

**The government outsourced its data entry to the people it regulates, and the liability followed the keystrokes.**

Before ABI, a Customs clerk's typing error was Customs' problem. After it, the data arrived already typed, under the broker's filer code. The **Customs Modernization Act of 1993** then wrote the consequence into law as "reasonable care" and "informed compliance" — the filer is responsible for what the filer transmits. `history/customs-brokers.md` traces the Section 592 penalties that sit behind that duty.

The second cost is dependence. A broker's software can only ever be as capable as the government channel it feeds. When a Partner Government Agency's data set was not yet built into ACE, no vendor could file it electronically, however good its own code. The door sets the vendor's roadmap.

## What You Still Touch

Every ACE entry a broker files today still goes through ABI, record by record against a government-published layout. What the door never carried is the judgement. ABI transmits an HTS code; it has never helped choose one. It confirms an entry arrived; it does not warn that a field is missing until CBP says so.

- [[problems/customs-brokers/high-impact|🔴 HTS Classification Prediction from Product Descriptions]] — the decision ABI was never built to make
- [[problems/customs-brokers/worker-life-1|🟢 Entry Summary Completion Checklist and Missing Data Detection]] — the check a broker must now run before the door, because the door only answers after
- [[problems/customs-brokers/low-impact-1|🟡 Commercial Invoice Data Extraction for Entry Preparation]] — the re-keying ABI moved from Customs' desk to the broker's
- [[niches/customs-brokers/entry-filing-ace-automation/profile|Entry Filing & ACE Automation]]
- [[niches/customs-brokers/hts-classification-workflow/profile|HTS Classification Workflow]]

**Sources:** The White House, National Performance Review, *Reengineering Through Information Technology* (May 1994, clintonwhitehouse6.archives.gov) — the 1984 8% and 1993 93% / 1,324 filer figures, and the description of broker functions in ACS; help.cbp.gov Article 1844 and eCFR 19 CFR Part 143 Subpart A (ABI as a voluntary program for brokers, importers and service centres); cbp.gov, *ACE ABI CATAIR*; GAO reports IMTEC-87-10 and IMTEC-89-4BR (titles only — ACS existed and was under GAO review by 1987; contents not read); DHL, DocShipper and IT Law Wiki glossary pages (the "implemented in 1984" claim). This vault's `history/customs-brokers.md` (Mod Act, ACE cutover, PGA dependence), cited as vault material, not independent corroboration. ⚠️ **Not established:** ABI's launch year against a primary Customs Service or Federal Register record — the 1984 date comes only from secondary glossaries, and the 1994 NPR document gives a 1984 participation figure without saying ABI began that year. **Not established:** who inside the Customs Service designed ABI, or ACS's go-live date; no individual is named above for that reason. CATAIR's first publication date was not searched.
