# FAI Software Taught Each Prime's Rules

**Niche:** [[niches/aerospace-parts-suppliers/first-article-inspection/profile|First Article Inspection & AS9102 Packages]]
**Industry:** [[industries/aerospace-parts-suppliers|Aerospace Parts Suppliers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** FAI software produces a correct AS9102 report; each prime then wants its own additions, formats and portal uploads.
**Tags:** #large-language-models #transformers #compliance #automation #workflow-orchestration #data-integration
**Contested on:** *Not terminal as stated.* The honest partial sentence is: every serious competitor in this niche is fighting to get an AS9102 package accepted by the customer's quality representative the first time. Two contests sit inside it, with different inputs, vendors and winners: extracting every requirement from the drawing or model onto Form 3, and proving every material and special process on Form 2 with genuine, conforming certificates from approved sources. Decomposed into contested sub-niches below.

## The Problem
Suppliers to several primes find that a compliant AS9102 report is necessary but not sufficient. Each customer's supplier quality requirements add rules on key characteristics, extra forms or fields, digital-product-definition handling, and how and where the FAIR is submitted. Quality engineers keep a crib sheet per customer and rebuild reports to match.

## What Already Exists
Net-Inspect (which some primes use as their supplier FAI portal), DISCUS, High QA, InspectionXpert and GroundControl generate AS9102 reports and export PDF and Excel.

## The Customization Gap
A rules layer per customer, built from Boeing's D6-82479, GE Aerospace's S-1000, Pratt & Whitney's ASQR-01, Rolls-Royce's SABRe and others (recalled), that knows which characteristics need key-characteristic treatment, which extra fields apply, when a partial is allowed, and which portal and format receive the report. The rules need version control, because customers revise these documents, and an LLM-assisted way to update them when a new revision arrives.

## Target Customer
Quality engineers at suppliers serving three or more primes on an existing FAI tool.

## Impact If Solved
Removing per-customer rework saves ~1–2 hours per FAI (estimate) and prevents rejections for format rather than substance.
