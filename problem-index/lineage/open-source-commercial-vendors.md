# Lineage: Open Source Commercial Vendors

**Industry:** [[industries/open-source-commercial-vendors|Open Source Commercial Vendors]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** the Server Side Public License (SSPL) v1 — the AGPL v3 with its section 13 rewritten so that anyone offering the software as a public service must release the source of the whole service stack; effective for MongoDB releases from 16 October 2018
**Builder:** MongoDB
**Builder in vault:** [[industries/open-source-commercial-vendors|Open Source Commercial Vendors]]
**Verification:** verified — see Sources

## The Problem That Came First

An open-source database company gave the product away and sold everything around it: support, enterprise features, and eventually the product run for you as a service.

The last of those was the one that paid. MongoDB launched its own database-as-a-service, **Atlas, in 2016**, and by 2024 Atlas was roughly 70 percent of company revenue. But a hosted service is exactly the business a cloud provider is better placed to run. It already owns the machines, the billing relationship and the console the customer logs into every day. Nothing in a permissive licence stopped it offering the same database as a managed service, and nothing required it to pay the vendor who wrote it.

MongoDB was already on the **AGPL v3**, the strongest copyleft in common use, whose section 13 obliges anyone who modifies the software and lets users interact with it over a network to offer them the modified source. A provider running unmodified code behind its own control plane owed nothing.

## What Got Built

A licence clause.

The SSPL keeps the AGPL's text and rewrites section 13. Anyone who makes the program's functionality available to third parties as a service must release, under the SSPL, **"the entirety of the service's source code, including all software, APIs, and other software that would be required for a user to run an instance of the service themselves"** — which MongoDB's FAQ spells out as management software, user interfaces, APIs, automation, monitoring, backup, storage and hosting software.

It was not written to be obeyed. It was written so that obedience would be unthinkable for a cloud provider, whose control plane is its moat. The practical effect is: run it yourself freely, or buy it from us, or negotiate a commercial licence.

## Who Built It, And Why Them

MongoDB, because it had the most to lose to a hosted copy and was already one licence-step away.

10gen began writing MongoDB in **2007** as a component of a planned platform-as-a-service, so the company had been a would-be hosting business from the start. It went public on NASDAQ on **20 October 2017**. Its FAQ gives the reason for the change directly: "once an open source project becomes interesting, it is too easy for large cloud vendors to capture all the value but contribute nothing back", having watched "international cloud vendors begin to test the boundaries of the AGPL".

A foundation could not have written this licence; foundations exist to be neutral between vendors, including hyperscalers. Only the controlling rights-holder of a single-vendor project could relicense the next release unilaterally — and MongoDB did.

## What It Cost

**It cost the words "open source".** MongoDB submitted the SSPL to the Open Source Initiative in 2018 and **withdrew it in March 2019**; Bruce Perens argued it discriminated against use as a service and encumbered separate programs. MongoDB's own FAQ now states that SSPL software "is not considered open source by the OSI".

It cost distribution: **Debian, Red Hat Enterprise Linux and Fedora dropped MongoDB.** And it did not stop the competitor it aimed at — Amazon released **DocumentDB**, a proprietary MongoDB-compatible service, rather than comply. When Elastic moved to SSPL-or-proprietary on **14 January 2021**, AWS and partners forked the code as OpenSearch.

The licence protected the next release, not the market.

## What You Still Touch

Every "source-available" licence change announcement, every enterprise procurement questionnaire asking whether a dependency is OSI-approved, and every community fork named after a relicensing descends from a clause written to make one kind of customer impossible.

- [[problems/open-source-commercial-vendors/low-impact-2|🟡 Drawing the Open-Core Boundary]] — the boundary redrawn by licence instead of by feature
- [[problems/open-source-commercial-vendors/high-impact|🔴 Adoption That Cannot Be Seen]] — a vendor that knew its users would not need to fence them
- [[niches/open-source-commercial-vendors/hosted-service-vs-hyperscalers/profile|Hosted Service Against Hyperscalers]]
- [[niches/open-source-commercial-vendors/open-core-and-licensing/profile|Open Core & Licensing]]
- [[niches/open-source-commercial-vendors/enterprise-procurement-compliance/profile|Enterprise Procurement & Compliance]]

**Sources:** Wikipedia, *Server Side Public License* (16 October 2018 introduction; section 13 quotation; OSI submission 2018 and withdrawal March 2019; Perens on OSD sections 6 and 9; Debian, RHEL and Fedora dropping MongoDB; DocumentDB; Elastic's 14 January 2021 announcement and OpenSearch); MongoDB, "Server Side Public License FAQ" (stated rationale quotations; list of service software covered; 16 October 2018 cut-off; not OSI-approved); Wikipedia, *MongoDB* (10gen, 2007, PaaS component; licence change shipped with 4.0.4 on 8 November 2018; Atlas 2016; IPO 20 October 2017; Atlas ~70% of revenue in 2024). ⚠️ **WebSearch was unavailable this session (session cap reached)**; research was by direct fetch only. ⚠️ **Not established:** the individual drafters of the SSPL inside MongoDB, and MongoDB's contributor-agreement terms — the relicensing argument rests on the fact that it did relicense, not on a text I read.
