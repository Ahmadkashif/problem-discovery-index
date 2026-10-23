# One Package From Drawing, PO and Certificates

**Niche:** [[niches/aerospace-parts-suppliers/first-article-inspection/profile|First Article Inspection & AS9102 Packages]]
**Industry:** [[industries/aerospace-parts-suppliers|Aerospace Parts Suppliers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The three AS9102 forms draw on three separate piles (the drawing, the purchase order and the certificates), and no tool assembles them into one checked package.
**Tags:** #object-detection #large-language-models #transformers #evaluation-metrics #compliance #automation #quick-win
**Contested on:** *Not terminal as stated.* The honest partial sentence is: every serious competitor in this niche is fighting to get an AS9102 package accepted by the customer's quality representative the first time. Two contests sit inside it, with different inputs, vendors and winners: extracting every requirement from the drawing or model onto Form 3, and proving every material and special process on Form 2 with genuine, conforming certificates from approved sources. Decomposed into contested sub-niches below.

## The Problem
A quality engineer builds Form 1 from the PO and the drawing title block, Form 2 from a folder of mill certs and processor certs, and Form 3 from the drawing and the CMM report. The forms are checked against each other only by the engineer's attention, and the customer rejects packages for mismatches between them: a drawing revision on Form 1 that differs from the PO, or a special process on the drawing with no cert on Form 2.

## Why Nobody Has Built This
FAI vendors grew from ballooning and measurement; certificate handling sits in receiving inspection or the ERP; and PO clause review is a contracts task. Each lives with a different person.

## What to Build
An assembler that reads the PO (part, revision, clauses), the drawing or model (requirements and processes called out), and the certificates (materials, heat lots, processors, specs). It drafts all three forms, cross-checks revision, material, process and processor approval across them, and lists exactly what is missing before the inspector starts measuring. The sub-niches hold the two hard extraction problems; this build is the package and the cross-checks.

## Target Customer
Quality managers at AS9100 suppliers producing ~10–40 full or delta FAIs a month.

## Impact If Built
Catching cross-form mismatches before submission could lift first-time acceptance from roughly four in five to above 95% (estimate), releasing invoices that rejected packages hold for days or weeks.
