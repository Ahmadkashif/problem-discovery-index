# Entitlement Truth Across Every Publisher

**Niche:** [[niches/libraries-and-archives/academic-unified-resource-management/profile|Academic Unified Resource Management]]
**Industry:** [[industries/libraries-and-archives|Libraries & Archives]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No system continuously checks that what a library pays for, what its knowledge base says it has and what the publisher actually serves are the same list.
**Tags:** #large-language-models #feature-engineering #evaluation-metrics #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to keep one record of what a university library has paid for, is entitled to and can actually deliver across print and every publisher platform, and whoever keeps entitlements, links and access correct for the most publishers with the least staff effort takes the platform renewal.

## The Problem
Three lists should agree and rarely do: the titles and years the licence and invoice entitle the library to; the titles activated in the knowledge base that drives discovery and link resolution; and the titles the publisher platform actually serves to the library's IP ranges and proxy. Publishers move titles between packages, transfer journals to other publishers, and change platforms. Each drift either blocks a patron from something paid for or quietly shows content the library is not licensed for.

## Why Nobody Has Built This
Each platform vendor owns one of the lists and assumes the others are right. Libraries reconcile by hand when a patron complains, and an electronic resources team of two or three cannot audit thousands of titles a month.

## What to Build
A reconciliation engine that reads licences and invoices (with LLM extraction of title lists and perpetual-access clauses), harvests KBART files and activations from the platform, and probes publisher platforms with sampled access tests from the library's own network. It reports every mismatch by cause — not activated, wrongly activated, platform moved, entitlement expired — with a fix routed to the right system.

## Target Customer
Electronic resources and discovery librarians at research and mid-size universities; consortia offering shared e-resource support.

## Impact If Built
Access failures found before patrons find them, perpetual-access rights actually exercised after cancellations, and an audit trail of what the library paid for versus what it received.
