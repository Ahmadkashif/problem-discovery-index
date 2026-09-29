# Lineage: B2B Commerce Platforms

**Industry:** [[industries/b2b-commerce-platforms|B2B Commerce Platforms]]
**Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**The tool:** cXML 1.0 and its PunchOut transaction — PunchOutSetupRequest, the supplier-hosted browsing session, and PunchOutOrderMessage returning the cart to the buyer's procurement system
**Builder:** Ariba
**Builder in vault:** [[industries/procurement-spend-platforms|Procurement & Spend Platforms]]
**Verification:** partial — see Sources

## The Problem That Came First

A large company's purchasing system needed to know the price before anyone clicked "buy", and the supplier was the only party who knew it.

Industrial and office supply prices are contract prices: this customer, this part, this quantity, this date. Late-1990s procurement software handled it by loading supplier catalogues into the buyer's own system as static files. That worked for a stationery list. It failed for configurable products, for catalogues of hundreds of thousands of parts, and for prices that changed faster than the files could be reloaded — and every stale catalogue produced an invoice that did not match the purchase order.

EDI existed for the order itself, but EDI moved documents between back offices. It had no way to let an employee at the buyer shop inside the supplier's live catalogue and bring the result home as an approvable requisition.

## What Got Built

A round trip through the supplier's website that starts and ends in the buyer's system.

The cXML 1.0 specification, dated **16 August 1999** and copyrighted by Ariba, Inc., defines it. The buyer's procurement application sends a **PunchOutSetupRequest** over HTTP, carrying credentials, an opaque **BuyerCookie** so the buyer can match the session back to the requisition, and a **BrowserFormPost** URL saying where to return. The supplier answers with a URL; the employee's browser opens a session on the supplier's own storefront, logged in as that customer, seeing that customer's prices. When they finish, the supplier sends a **PunchOutOrderMessage** — the cart — URL-encoded and posted back through the browser to the buyer's system, where it becomes a requisition subject to the buyer's approval rules. The formal purchase order follows as a separate cXML OrderRequest.

The spec's own example return URL is `ariba.cisco.com`; its introduction says most feedback came from actual implementations.

## Who Built It, And Why Them

**Ariba**, founded in Palo Alto in **1996** by a team including Keith Krach, Bobby Lent, Boris Putanec and Paul Touw, around using the internet to run corporate procurement. It went public in 1999, the same year it published cXML.

Why them is that Ariba sold to the buyer and needed thousands of suppliers it did not control to connect cheaply. Its product was worthless to a customer whose suppliers could not be reached, and EDI onboarding was slow and expensive for a small distributor. A lightweight XML protocol over plain HTTP, with a username-and-password credential instead of a public-key infrastructure — the spec says so explicitly — lowered the supplier's cost of saying yes. PunchOut specifically let Ariba avoid owning the hardest data in the transaction: rather than host every supplier's contract prices, it sent the buyer to the supplier and took back only the result.

SAP's rival Open Catalog Interface did the same job for SAP buyers from around the same period. Ariba was acquired by SAP in 2012 and cXML is still controlled by it.

## What It Cost

**The protocol standardised the envelope and left the connection bespoke.**

PunchOut defines how a cart travels, not what a customer's identity, account hierarchy, ship-to codes, unit-of-measure or approval fields must look like. Those travel as optional "Extrinsic" elements and credentials each buyer configures its own way. So every large customer's procurement system is a separate integration with its own test cycle, and a supplier maintains two protocols — cXML and OCI — in parallel. The hard part the protocol deliberately stepped around, resolving a customer's price in real time, landed on the supplier's storefront, where it still sits.

## What You Still Touch

An engineer at a manufacturer clicks "shop Grainger" inside their company's procurement system, lands on a storefront showing their company's negotiated prices, and clicks "return cart". That is the 1999 round trip, nearly unchanged.

- [[problems/b2b-commerce-platforms/low-impact-1|🟡 Procurement System Integration]] — a standard everyone supports and every customer still configures
- [[problems/b2b-commerce-platforms/high-impact|🔴 Customer-Specific Pricing and Entitlements at Scale]] — the price resolution PunchOut pushed onto the supplier
- [[niches/b2b-commerce-platforms/procurement-integration/profile|Procurement Integration]]
- [[niches/b2b-commerce-platforms/entitlement-and-price-resolution/profile|Entitlement & Price Resolution]]

The classification side of the same buyer system is traced in [[lineage/procurement-spend-platforms|Lineage: Procurement & Spend Platforms]].

**Sources:** Ariba, Inc., *cXML/1.0* specification, 16 August 1999 (xml.cxml.org/schemas/cXML/1.0.001/cXML.pdf — read directly: introduction on implementation-driven feedback, PunchOutSetupRequest with BuyerCookie and BrowserFormPost, PunchOutOrderMessage via URL-form-encoding, shared-secret credential "without requiring a public-key end-to-end digital certificate infrastructure", `ariba.cisco.com` example); Wikipedia, *cXML* (created by Ariba 1999, controlled by Ariba, owned by SAP since 2012) and *SAP Ariba* (founded 1996 Palo Alto, founders, 1999 IPO, SAP acquisition announced 22 May 2012, completed 1 October 2012). ⚠️ **Not established:** the year SAP introduced OCI — secondary vendor pages give "around 1999" and "around 2000" inconsistently; stated here only as "around the same period". The Grainger example illustrates current practice; I did not confirm Grainger's PunchOut date. I found no source naming the individual Ariba engineers who authored cXML, and none is asserted. The claim that static catalogue loading failed for large or fast-changing catalogues is inferred from the protocol's design, not from a dated Ariba statement of motive.
