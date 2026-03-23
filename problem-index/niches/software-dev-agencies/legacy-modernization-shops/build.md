# Legacy Business Rule Extraction Engine

**Niche:** [[niches/software-dev-agencies/legacy-modernization-shops/profile|Legacy System Modernization Shops]]
**Industry:** [[industries/software-dev-agencies|Software Dev Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product extracts human-readable business rules from COBOL/mainframe code — the single most expensive and error-prone step in every legacy modernization project.
**Tags:** #llm #text-classification #nlp #tacit-knowledge-ml #revenue-impact

## The Problem
A typical mainframe modernization project begins with a code assessment phase where senior COBOL developers read through thousands of programs to understand what business logic they implement. A single COBOL program might contain a rate calculation buried inside 3,000 lines of file I/O, error handling, and formatting logic. The developer must mentally separate the business rule ("if customer tenure > 5 years AND payment history = 'A', apply 2.5% discount") from the implementation plumbing. This extraction is done manually, documented in Word documents, and verified through interviews with business users who may not understand the code. For a 5,000-program modernization, the assessment phase alone takes 6-12 months and costs $1-3M.

## Why Nobody Has Built This
COBOL business rule extraction requires understanding both COBOL semantics (PERFORM VARYING, copybook structures, implicit decimal handling, REDEFINES) and the business domain (what constitutes a "business rule" vs. "implementation detail"). LLMs can parse COBOL syntax but struggle to distinguish business logic from infrastructure code without domain context. The training data is limited — COBOL codebases are proprietary and not available in public repositories. Earlier attempts (IBM Rational Asset Analyzer) produced call graphs and data flow diagrams but not business-level rule descriptions.

## What to Build
An analysis engine that ingests COBOL source code (programs, copybooks, JCL), identifies business rule segments using code structure patterns (EVALUATE/WHEN blocks, nested IF conditions, COMPUTE statements with domain-specific variables), extracts them as human-readable rule statements, and organizes them by business domain (pricing, eligibility, calculation, validation). The engine should flag ambiguous rules for human review and cross-reference rules across programs to identify duplicates and conflicts. Output is a structured business rules catalog that serves as the specification for the modern replacement.

## Target Customer
Legacy modernization agencies tackling mainframe-to-cloud migrations with 1,000+ COBOL programs, particularly in financial services, insurance, and government.

## Impact If Built
Reduces assessment phase duration from 6-12 months to 2-3 months, saving $500K-$2M per project. Catches 30-40% more business rules than manual review, reducing post-migration defects by a comparable amount.
