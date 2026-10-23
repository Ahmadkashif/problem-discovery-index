# Receiving Inspection Software Taught Aerospace Specs

**Niche:** [[niches/aerospace-parts-suppliers/material-process-cert-verification/profile|Material & Special-Process Certification Verification]]
**Industry:** [[industries/aerospace-parts-suppliers|Aerospace Parts Suppliers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** QMS and ERP receiving modules store certificates and record a pass; they don't know what AMS 4911 or a heat-treat spec requires.
**Tags:** #large-language-models #transformers #feature-engineering #compliance #automation #data-integration
**Contested on:** Every serious competitor in this sub-niche is fighting to check every mill cert and special-process cert against the specification, the purchase order and the approved-processor list before material is cut, and whoever catches a non-conforming or falsified cert earliest in the chain takes the account.

## The Problem
Suppliers already run receiving inspection in their QMS or ERP: a lot arrives, a cert is attached, an inspector signs. The software has a field for "cert reviewed" and nothing behind it.

## What Already Exists
QMS suites (ETQ, MasterControl, Uniphi, Qualio) and ERPs (Epicor Kinetic, Plex, ProShop, JobBOSS²) handle receiving workflows, document attachment and nonconformance (recalled).

## The Customization Gap
The aerospace layer reads the cert, maps each value to the specification and revision called out on the PO, and checks limits, condition, test methods and required statements (melt source, country of melt for specialty metals, recalled). It verifies processor certs against Nadcap and customer approval at the processing date and carries the result straight to AS9102 Form 2. Specification content must be licensed per customer and versioned.

## Target Customer
Suppliers already on a QMS or ERP that want certificate checking without a new system.

## Impact If Solved
Turning "cert reviewed" into a checked record cuts receiving review from ~10–20 minutes a lot to ~2 (estimate) and makes Form 2 a by-product.
