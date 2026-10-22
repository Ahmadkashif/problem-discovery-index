# As-Built Reconciliation From Field Photos and OTDR Traces

**Niche:** [[niches/wired-broadband-providers/fiber-network-records/profile|Fibre Network Records & As-Built Inventory]]
**Industry:** [[industries/wired-broadband-providers|Wired Broadband Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The network record drifts from reality with every repair and install, and the evidence that would correct it — OTDR traces, splice photos, port activations — is already being created and thrown away.
**Tags:** #object-detection #cnns #large-language-models #graph-theory #data-integration #feature-engineering
**Contested on:** Every serious competitor in this niche (fibre records and GIS vendors, records-conversion services and operators' own records teams) is fighting to keep a strand-, splice- and port-level record that matches what is actually in the ground and on the poles after every repair and install, and whoever keeps that record truest takes the account.

## The Problem
A splicer repairs a cut, re-splices two buffer tubes differently from the drawing to save time, photographs the tray and shoots an OTDR trace. The photo stays on his phone, the trace on the test set, and the record still shows the old splice. The next technician trusts the record.

## Why Nobody Has Built This
Records vendors assume a records clerk will key changes; small operators don't have one. Reading splice-tray photos and matching OTDR events to the record needed computer vision and trace analysis that weren't packaged for this.

## What to Build
A field capture flow that ingests splice-tray photos, closure labels and OTDR traces at every job; vision models read tray layouts and fibre colours; trace analysis matches event distances to closures and splices in the record; and a reconciliation engine proposes record changes for a records lead to approve. Contractor as-built redlines go through the same engine at turn-up.

## Target Customer
Small and mid-sized fibre operators and co-ops whose records live in a mapping tool with no records staff behind it.

## Impact If Built
Records that stay true with no extra keying, faster restoration of cuts, and installs that can be provisioned remotely because the port record can be trusted.
