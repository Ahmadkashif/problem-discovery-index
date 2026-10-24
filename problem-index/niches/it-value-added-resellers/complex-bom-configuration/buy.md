# Asset Inventory Read Into the Configurator

**Niche:** [[niches/it-value-added-resellers/complex-bom-configuration/profile|Complex BOM Configuration & Site Fit]]
**Industry:** [[industries/it-value-added-resellers|IT Distributors & Value-Added Resellers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Customers' network and asset inventories already list the switches, PDUs and licences a new BOM must fit; nobody reads them into the quote.
**Tags:** #large-language-models #word-embeddings #data-integration #feature-engineering #automation
**Contested on:** Every serious competitor in this niche is fighting to send solution quotes whose bills of materials install as quoted at the customer's site, and whoever ships the lowest share of quoted lines needing a post-order change order or return takes the account.

## The Problem
The customer's existing switches, optics, rack power and licence entitlements decide whether a new configuration fits. The engineer learns them from a site survey, an old project folder or a phone call.

## What Already Exists
Network monitoring and discovery tools, CMDBs (ServiceNow), vendor install-base and support-contract reports, and the reseller's own order history for the account.

## The Customization Gap
The adaptation needs: discovery and install-base data normalised to vendor SKUs and part families; rules that turn site facts into BOM constraints (optic platform coding, PDU connector type, cabinet depth, licence tier prerequisites, support co-term dates); and a check that runs on the configurator export before pricing, written in the vocabulary the engineer uses.

## Target Customer
Resellers with managed or co-managed customers whose inventories they can already see.

## Impact If Solved
Reading the customer's own inventory into each quote removes the site-fact errors that cause an estimated third of solution change orders, without waiting for a model to learn them.
