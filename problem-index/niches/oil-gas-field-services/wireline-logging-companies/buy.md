# Basin-Specific Log Interpretation Templates

**Niche:** [[niches/oil-gas-field-services/wireline-logging-companies/profile|Wireline Logging Companies]]
**Industry:** [[industries/oil-gas-field-services|Oil & Gas Field Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Petrophysical interpretation software provides generic calculation modules, but each basin requires specific parameter sets (Archie's exponents, shale volume models, porosity-permeability transforms) that petrophysicists currently configure from scratch.
**Tags:** #gradient-boosting #regression #tabular-ml #tacit-knowledge-ml #quick-win

## The Problem
When a petrophysicist begins interpreting a well in the Delaware Basin Wolfcamp formation, they need basin-specific parameters: Archie cementation exponent (m=1.8-2.2 for this rock type), saturation exponent (n=1.7-2.0), shale volume model (Larionov non-linear for young rocks), porosity-permeability transform (which empirical correlation works for Wolfcamp? Core data from offset wells suggests log(k) = 15*PHI - 0.5), and pay cutoffs (PHI>6%, Sw<55% for this formation). These parameters are not default values in any interpretation software — they are basin-specific, formation-specific knowledge that senior petrophysicists carry in their heads or in personal spreadsheets. Junior petrophysicists use generic defaults that produce inaccurate results.

## What Already Exists
Techlog and Interactive Petrophysics allow users to create interpretation templates, but these are individual user files shared informally (email, USB drives). Some wireline companies maintain internal "best practices" documents with recommended parameters by basin. Academic publications and SPE papers provide formation-specific parameter studies. No centralized, curated library of basin-specific interpretation parameters exists as a product.

## The Customization Gap
The industry needs a curated, version-controlled library of interpretation templates organized by basin and formation, containing: validated parameter sets (Archie exponents, shale volume model, porosity-permeability transforms), recommended curve processing workflows (environmental corrections, depth matching), pay zone cutoffs calibrated to basin-specific production data, and reference offset well interpretations for pattern comparison. Templates should be importable into major interpretation platforms (Techlog, IP) and should include provenance information (what core data or production data validates these parameters).

## Target Customer
Junior petrophysicists and independent logging companies that lack basin-specific institutional knowledge built up over decades of operations in a particular geological setting.

## Impact If Solved
Reduces parameter selection time from 2-4 hours to 15 minutes per well, improves interpretation accuracy for junior petrophysicists by 20-30% by providing validated basin-specific starting points, and creates institutional memory that persists independent of personnel turnover.
