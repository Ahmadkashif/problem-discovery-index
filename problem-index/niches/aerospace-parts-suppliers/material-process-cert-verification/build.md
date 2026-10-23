# Cert Values Checked Against the Spec on Arrival

**Niche:** [[niches/aerospace-parts-suppliers/material-process-cert-verification/profile|Material & Special-Process Certification Verification]]
**Industry:** [[industries/aerospace-parts-suppliers|Aerospace Parts Suppliers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Receiving inspectors glance at a mill cert's heat number and spec callout; nobody checks every reported value against the specification's limits, or notices when a cert looks different from that mill's last fifty.
**Tags:** #large-language-models #transformers #gaussian-mixture-models #k-nearest-neighbors #feature-engineering #evaluation-metrics #compliance #automation
**Contested on:** Every serious competitor in this sub-niche is fighting to check every mill cert and special-process cert against the specification, the purchase order and the approved-processor list before material is cut, and whoever catches a non-conforming or falsified cert earliest in the chain takes the account.

## The Problem
A titanium bar arrives with a mill test report listing chemistry, tensile results, heat treatment condition and the specification (an AMS number, say). Receiving checks the heat number matches the tag and the spec matches the PO. Whether each value sits inside the specification's limits, whether the spec revision is current, and whether the document resembles that mill's genuine certs is rarely checked. The 2024 falsified-titanium case (search summary of AP and FAA statements) showed how far paper can travel before someone notices.

## Why Nobody Has Built This
Specifications are licensed documents (SAE AMS, ASTM, customer specs) that a tool must encode; cert formats vary by mill; and the check that catches forgeries, comparing against a mill's genuine history, needs data across many buyers.

## What to Build
Extraction of every value, heat and spec from mill and processor certs; a rules library of spec limits per revision, maintained under the customer's licences; automatic pass/fail per value; and a format-anomaly score comparing each cert with the same source's past certs (layout, signatories, value distributions). Processor certs are checked against Nadcap status and the customer's approved list at the processing date.

## Target Customer
Quality managers and receiving leads at structures and engine-part suppliers buying titanium, nickel and aluminium through distributors.

## Impact If Built
Catching one non-conforming or falsified lot before it is machined avoids containment and recall work that can run to ~$100,000+ per event (estimate) and protects the supplier's standing with its prime.
