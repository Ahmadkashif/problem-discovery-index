# COBOL Business Logic Extraction

**Niche:** [[niches/cloud-infrastructure-consultants/legacy-mainframe-migrators/profile|Legacy Mainframe Migrators]]
**Industry:** [[industries/cloud-infrastructure-consultants|Cloud Infrastructure Consultants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool can read a 500,000-line COBOL codebase and produce a human-readable business rules catalog that a modern developer can use to rewrite the system.
**Tags:** #llm #text-classification #nlp #tacit-knowledge-ml #automation

## The Problem
Legacy mainframes contain business logic accumulated over decades — pricing rules, regulatory calculations, exception handling — buried in COBOL paragraphs, copybooks, and JCL procedures. When consultants attempt migration, they must reverse-engineer this logic line by line, often without documentation or access to the original developers. A typical mainframe has 1-5 million lines of COBOL, and extracting all business rules takes 12-24 months of analyst time at $200-$400/hour.

## Why Nobody Has Built This
COBOL's structure (PERFORM, GO TO, paragraph-based flow control) makes static analysis harder than for modern languages. Business rules are interleaved with data manipulation, I/O operations, and error handling — separating "what the business wants" from "how the computer does it" requires semantic understanding, not just syntax parsing. Previous attempts at automated COBOL analysis produced call graphs and data flow diagrams, but not business-readable rule descriptions.

## What to Build
An LLM-powered COBOL analysis platform that ingests entire codebases (COBOL, JCL, copybooks, CICS maps), identifies business rule boundaries using code structure and naming patterns, and generates plain-English descriptions of each rule with its inputs, outputs, conditions, and edge cases. The system produces a searchable business rules catalog linked back to source code, enabling modern developers to reimplement rules without reading COBOL.

## Target Customer
Mainframe modernization practice leads at consulting firms managing $5M-$50M migration engagements where 40%+ of project cost is business logic analysis.

## Impact If Built
Reduces business logic extraction from 18 months to 4 months per engagement, saving $1M-$5M in analyst labor and accelerating mainframe retirement timelines by 12+ months.
