# Lineage: SaaS Implementation Partners

**Industry:** [[industries/saas-implementation-partners|SaaS Implementation Partners]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** the Salesforce Sandbox — a separate copy of a customer's production Salesforce org, sold as an add-on subscription, in which customisations are built and tested before being deployed to the live system
**Builder:** salesforce.com
**Builder in vault:** [[industries/crm-platforms|CRM Platforms]]
**Verification:** partial — see Sources

## The Problem That Came First

Software as a service removed the customer's test server.

With installed enterprise software, the customer owned the hardware, so an integrator could stand up a development copy, build there, test there and promote to production on a date both sides chose. Multi-tenant SaaS took that away. Every customer ran on the vendor's servers, on one version, upgraded by the vendor. That was the selling point. salesforce.com's 10-K for the fiscal year ended January 2006 says customers avoid "large and risky upfront investments in software, hardware, implementation services and additional IT staff", and that new features "automatically become part of our service on the release date".

It also meant that anyone configuring the system did it on the live system. A new workflow rule, an integration test, a data load that went wrong — each happened where the sales team was working.

## What Got Built

A second org.

The same 10-K lists **Salesforce Sandbox** among the optional add-on subscriptions and describes it in full: it "enables customers to test new customizations or features before deploying them"; customers can use it "to install, modify, and test applications downloaded from the AppExchange or to create a development environment for building and testing integrations and internally built applications"; and it can serve as "an exact replica of their production salesforce system for employee training purposes."

That is the environment model implementation work still runs on: build in a copy, move the changes, hope the copy matched.

## Who Built It, And Why Them

salesforce.com, founded in March 1999 by Marc Benioff with Parker Harris, Dave Moellenhoff and Frank Dominguez. The engineers who built Sandbox are not named in any source I reached.

**Why the vendor and nobody else.** In a multi-tenant service only the operator can copy a tenant. No integrator, however large, could provision a second instance of a customer's org; the data, metadata and servers were salesforce.com's. And the company had a direct commercial reason to do it in 2005–06. It had just opened itself to third parties — the AppExchange directory in September 2005, the AppExchange API (formerly sforce) and AppExchange Builder for point-and-click customisation. Once customers were installing other people's applications and building their own, they needed somewhere to try them that was not production. Sandbox was priced as an add-on, so the safe environment became a line item.

The same filing lists Accenture, BearingPoint and IBM as competitors to salesforce.com's own professional services — and as firms it "frequently" works with. The partner channel and the vendor's sandbox grew up together.

## What It Cost

**A copy drifts from the original the moment it is made.** Every sandbox is a snapshot; production keeps changing and the vendor keeps releasing. Changes built in the copy have to be carried back across by a separate mechanism, and whatever the copy did not reproduce — data volumes, integrations, users' actual behaviour — shows up only after go-live.

And the environment belongs to the vendor. The partner can rent more copies, but cannot keep one: when the engagement ends, the evidence of what was built, and whether it worked, stays in orgs the partner no longer has access to.

## What You Still Touch

Every Salesforce project still runs through sandboxes, and a market — Gearset, Copado, Flosum, the vendor's own DevOps Center — exists to move changes between them and detect the drift. A consultant leaving a project leaves behind an org nobody else can see into.

- [[problems/saas-implementation-partners/low-impact-1|🟡 Integration and Environment Management]] — the sandbox's direct descendant
- [[problems/saas-implementation-partners/low-impact-2|🟡 Regression Testing Against the Release Treadmill]] — the vendor's upgrade, meeting the partner's copy
- [[niches/saas-implementation-partners/environment-management/profile|Environment & Sandbox Management]]
- [[niches/saas-implementation-partners/release-regression/profile|Release Regression Management]]

**Sources:** salesforce.com, Inc., Form 10-K for fiscal year ended 31 January 2006, filed with the SEC 15 March 2006 (EDGAR accession 0001193125-06-055150) — Sandbox description and add-on status, AppExchange directory introduced September 2005, AppExchange API "previously called sforce", AppExchange Builder "previously called Customforce", the no-upfront-investment and automatic-upgrade language, and the Accenture/BearingPoint/IBM passage; EDGAR full-text search of salesforce.com filings 2004–2008 for "sandbox" returns this filing as the earliest hit, so the product was on sale by early 2006. Wikipedia, *Salesforce* (founding 8 March 1999 and co-founders). Salesforce Ben, "The History of Salesforce DevOps" (Salesforce DX 2017, DevOps Center 2022, change sets). ⚠️ **Not established:** Sandbox's exact launch date and release name, and who inside salesforce.com designed it — the EDGAR result is a lower bound, not a launch date; WebSearch was unavailable this session (session cap reached), and Salesforce's archived press releases could not be located through the Internet Archive.
