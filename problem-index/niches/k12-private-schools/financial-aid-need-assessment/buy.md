# Document Verification in a Six-Week Season

**Niche:** [[niches/k12-private-schools/financial-aid-need-assessment/profile|Financial Aid Need Assessment Services]]
**Industry:** [[industries/k12-private-schools|K-12 Private Schools]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Hundreds of thousands of families upload tax returns and pay stubs into a six-week window, and every figure has to be read and reconciled.
**Tags:** #ocr #large-language-models #anomaly-detection #data-integration #workflow-orchestration

## The Problem
A need assessment rests on documents: federal returns with their schedules, W-2s, pay stubs, business returns, and increasingly whatever a self-employed parent can produce. Families upload photographs of paper, partial PDFs, and returns for the wrong year.

The staff has to read every relevant line, reconcile it against what the family reported on the application, and resolve the discrepancies — in the compressed season Pass 1 describes, where schools need awards out before their contract deadlines.

The volume is seasonal to an extreme degree, which means staffing is either idle for eight months or overwhelmed for two, and quality is worst exactly when the stakes are highest.

## What Already Exists
Tax document extraction is a mature commercial capability — the lending and tax preparation industries have driven it hard, and W-2 and 1040 extraction works well. Document processing platforms handle classification, extraction, and human review routing at scale.

## The Customization Gap
Lending-oriented extraction stops well short of what a need methodology consumes.

**The schedules are the answer.** For a wage earner, the top-line figures suffice. For the families where need assessment is hardest — self-employed, business owners, rental property, partnership interests — the methodology reaches into Schedule C, E, and K-1 detail, adds back depreciation and specific deductions, and treats business assets under its own rules. Generic extraction returns the summary and stops.

**Reconciliation against the application is the work.** The valuable output is not the extracted figure but the discrepancy: the family reported an income that does not match the return, or omitted an asset the return implies. That is a cross-document consistency problem no extraction product frames.

**Seasonality demands elastic confidence routing.** With volume concentrated into weeks, the system must auto-accept aggressively where confidence is high and route only genuine exceptions — and it must be calibrated, because a wrong figure changes a family's award.

**Missing and non-standard documents are normal.** Families without conventional documentation are disproportionately the ones needing the most aid. The workflow has to reason about what can be concluded from an incomplete set, and ask the one question that resolves it rather than sending a generic request.

**Every figure must trace to its source.** Awards are appealed. The system must show which document, which line, which year produced each input, years later.

## Target Customer
VP of Operations or Chief Product Officer at a need assessment provider, where seasonal document processing is the operational constraint and the quality risk simultaneously.

## Impact If Solved
Turnaround in the award season directly determines whether schools can make offers on time, and accuracy determines whether the award is right. Automating the reconciliation rather than just the extraction lets a stable team absorb the seasonal peak and concentrates human judgment on the complex families where the methodology is weakest.
