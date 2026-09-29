# Lineage: Procurement & Spend Platforms

**Industry:** [[industries/procurement-spend-platforms|Procurement & Spend Platforms]]
**Wave:** [[series/eras/wave-04-client-server-erp|4 — Client–Server & ERP]]
**The tool:** UNSPSC — the United Nations Standard Products and Services Code, an eight-digit Segment/Family/Class/Commodity taxonomy set up in 1998
**Builder:** United Nations Development Programme & Dun & Bradstreet
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

An enterprise could see what it paid each supplier. It could not see what it bought.

Accounts payable records a supplier and an amount. General-ledger codes record which budget paid. Neither records the *thing*. A question like "how much do we spend on safety gloves, across every site?" had no answer, because gloves came from a dozen distributors, each describing them its own way, under a dozen ledger lines.

**Without a shared name for the goods, spend could not be added up. Without an added-up figure, there was nothing to negotiate with.** ERP systems in the 1990s pulled purchasing into one database, and that made the gap plain. The rows were there. The rows could not be grouped.

## What Got Built

A published, hierarchical code list for everything an organisation buys.

UNSPSC uses a two-digit level repeated four times, giving eight digits in all: **Segment → Family → Class → Commodity**, with an optional business-function extension. It was formed by merging two existing lists: the United Nations' own Common Coding System and Dun & Bradstreet's Standard Product and Service Codes (SPSC).

The dates are unusually precise. John S. Svendsen, director of UNDP's Inter-agency Procurement Services Office, signed the founding Memorandum of Understanding on **29 September 1998**. Lawrence M. Barth, a Dun & Bradstreet vice president, signed it on **1 November 1998**. Peter R. Benson oversaw the first version and designed its code-management procedure, adapted from the Delphi forecasting method. The Electronic Commerce Code Management Association (ECCMA) was formed in **1999** to run it. ECCMA did so until March 2003. GS1 US then served as code manager from May 2003 to the end of 2024, when the job went back to UNDP. The August 2023 release held 158,448 items.

## Who Built It, And Why Them

Two parties, each already running a version of the list for its own reasons.

**UNDP's procurement office** bought on behalf of many UN agencies. A shared commodity code was how it could compare and pool what those agencies spent. **Dun & Bradstreet** sold data about companies, keyed on its D-U-N-S number. A product-and-service code attached to each supplier record made that database answer a buyer's question — *who sells this?* — and not only a lender's — *is this firm solvent?* Both motives are inferences from what each organisation did. Neither is a stated reason I could find.

Why a merger and not one list winning: a classification is only worth what its adoption is worth. A UN code would not travel into corporate ERP by itself. A proprietary D&B code would not be trusted by public buyers or rival data vendors. Putting a UN name on a commercial list produced something both could adopt. I could not establish which list supplied most of the first structure, so the key names both parties.

## What It Cost

**The code classifies products, and spend arrives as suppliers.** A commodity code is exact about "nitrile gloves." An invoice line from a broad-line distributor often is not. So in practice companies map *suppliers* to codes by rule, and a distributor that sells gloves, paper and pump parts lands in a single bucket. The vault's high-impact note describes exactly this failure.

The taxonomy is also general by design and changes with each version. Many firms therefore keep their own category tree, with UNSPSC as one crosswalk among several. The shared vocabulary exists, but it is not the one most spend cubes actually use.

## What You Still Touch

Every spend-classification engine is, underneath, a machine for assigning eight digits:

- [[problems/procurement-spend-platforms/high-impact|🔴 Spend Classification and the Supplier Master]] — classify at the line, not the supplier
- [[problems/procurement-spend-platforms/low-impact-1|🟡 Contract Price Compliance at Invoice]] — a negotiated price is only checkable once the item is identified
- [[niches/procurement-spend-platforms/spend-classification-supplier-master/buy|Product Classification and Entity Resolution Off the Shelf]] — UNSPSC and D&B linkage, the two halves of the 1998 bargain, as off-the-shelf inputs

**Sources:** Wikipedia, *UNSPSC* (fetched) for the 29 September and 1 November 1998 MoU signatures by Svendsen and Barth, Benson's role and the Delphi-based procedure, ECCMA 1999–March 2003 (v6.0315), GS1 US from May 2003 to 31 December 2024 and the return to UNDP, the eight-digit Segment/Family/Class/Commodity structure, and the 158,448-item count in v26.0801; search summaries of ECCMA and Peter Benson biography pages (**not read at source**) for ECCMA's April 1999 formation to merge D&B's SPSC with the UN Common Coding System; unspsc.org FAQ returned 403. This vault's procurement problem and niche notes (vault material, not independent corroboration). ⚠️ **Not established:** when D&B first built SPSC, and when the UN Common Coding System began; which of the two contributed most of UNSPSC's first structure; Benson's employer in 1998; any adoption figures for UNSPSC in corporate spend analysis. The D-U-N-S number's origin year was not checked this session and is left out.
