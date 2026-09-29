# Lineage: Oil & Gas Field Services

**Industry:** [[industries/oil-gas-field-services|Oil & Gas Field Services]]
**Wave:** [[series/eras/wave-04-client-server-erp|4 — Client–Server & ERP]]
**The tool:** the PIDX Field Ticket and Invoice transaction standards — the petroleum industry's electronic-commerce formats, EDI first, then XML schemas (v1.0 dated February 2002)
**Builder:** American Petroleum Institute
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

The work happens at a wellsite. The money is decided in an office hundreds of miles away.

A service crew spends a day on a well — pumping, logging, working over a rod string. Before it leaves, what it did goes onto a **field ticket**: hours, equipment, consumables, signed on site by the operator's representative. Weeks later that ticket becomes an invoice. The invoice is checked against the ticket, the ticket against the contract, and each against the operator's cost codes for that well.

Every step was paper, and every mismatch was a dispute. The operator paid nothing until the dispute was settled. The service company carried the cost of the job for as long as that took. **Hundreds of suppliers each billed a given operator in their own format.** And an operator's accounts-payable clerk rekeyed each one.

## What Got Built

A shared set of document formats.

The American Petroleum Institute ran a standards committee called the Petroleum Industry Data Exchange — PIDX — from **1987**. By its own account the committee "initially developed Electronic Data Interchange (EDI)" standards, a library of X12 and file-transfer formats, "and moved in the 1990′s to XML standards." The earliest dated XML artefacts I found are a data dictionary dated **30 November 2001** and **PIDX XML Schemas v1.0, dated 14 February 2002**, which include Invoice and Field Ticket templates. Implementation guidelines for the field ticket are also listed as 2001.

The field ticket is PIDX's distinctive document. It records the work seen in the field, for the operator to approve *before* the invoice goes out. Once approved, the ticket and the invoice are chained. A standards summary calls this the sector's version of procurement's three-way match.

The first live transactions are dated. On **12 December 2002**, Digital Oilfield brokered what it called the first PIDX XML invoice, through its OpenInvoice tool, between Anadarko Canada and Lonkar Services. On **8 May 2003**, Unocal, Schlumberger and Digital Oilfield announced the "first industry standard e-Invoice transaction."

## Who Built It, And Why Them

The American Petroleum Institute — as the host, not the author, of a committee of its members.

**Why them:** an invoice standard only works if both sides of the invoice accept it. The API was the one room where operators, who buy services, and the large service companies, who sell them, already sat together. PIDX's own membership today is described as "operators (oil companies), suppliers (service companies), technology providers." No single operator could impose a format on hundreds of vendors without the others building rival ones. No single service company could impose one on its customers. The operators wanted rekeying and disputes gone. The suppliers wanted to be paid sooner. The trade association was the neutral party where both could agree.

The Unocal manager's statement at the 2003 launch spells out the bargain: it "reduces transaction costs on both sides."

API did not keep it. In **2010** it stopped hosting the committee, and members formed PIDX, Inc. to carry the standards on. I could not find the names of the people who drafted the first field-ticket schema.

## What It Cost

**The standard digitised the ticket only after someone had written it.** PIDX defines what a field ticket looks like once it is data. It says nothing about how a crew at a remote wellsite, often without signal, turns a day's work into that data. The dispute over *what was done* moved upstream to capture, where it is still handwriting and memory.

Adoption was also left to intermediaries. The early transactions ran through a third-party network, and the large service companies formed their own e-commerce body, OFS Portal, in 2000. The format was shared; the plumbing was not.

## What You Still Touch

Every e-invoice between a service company and an operator carries this document chain:

- [[problems/oil-gas-field-services/low-impact-1|🟡 Field Ticket and Service Report Documentation]] — 45–90 minutes a day turning notes into tickets, the capture PIDX never covered
- [[niches/oil-gas-field-services/field-ticket-digitization/fix|Field Ticket to Invoice Reconciliation Pipeline]] — the ticket-to-invoice chain, still breaking
- [[niches/oil-gas-field-services/field-ticket-digitization/buy|Digital Field Ticketing for Disconnected Wellsites]] — capture where there is no signal

**Sources:** pidx.org "About Us" (fetched) for API's committee from 1987, the "initially developed EDI … moved in the 1990′s to XML" quotation, the 2010 transfer to PIDX, Inc., and the membership quotation; Robin Cover, *Cover Pages*, "Petroleum Industry Data Exchange (PIDX) XML Transaction Standards" (fetched) for the 2001-11-30 dictionary, the 2002-02-14 v1.0 schemas, the December 12 2002 Anadarko Canada–Lonkar transaction, the May 8 2003 Unocal–Schlumberger–Digital Oilfield transaction, RNIF transport, the Unocal quotation, and a reference to API Recommended Practice 3901 whose scope I did not confirm; ediverse.io PIDX summary (search summary, **not read at source**) for the field-ticket-before-invoice description and the X12 library; OFS Portal pages (search summary) for its founding in 2000 and its current members. This vault's field-ticket niche and problem notes (vault material). ⚠️ **Not established:** the date of the first PIDX X12 transaction; how "moved in the 1990s to XML" squares with a v1.0 schema dated 2002; OFS Portal's founding members; any figure for paper field-ticket dispute rates before PIDX. The PPDM-hosted 2013 PIDX overview failed on a certificate error.
