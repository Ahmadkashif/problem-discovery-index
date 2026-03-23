# Intelligent Condition-to-Document Matching Engine

**Niche:** [[niches/mortgage-brokers/condition-clearing-automation/profile|Condition Clearing & File Processing]]
**Industry:** [[industries/mortgage-brokers|Mortgage Brokers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool reads an underwriting condition in natural language, identifies which document satisfies it, checks if that document already exists in the loan file, verifies it meets the condition's requirements, and auto-clears or flags discrepancies.
**Tags:** #bert #text-classification #nlp #ocr #automation #workflow-orchestration #ai-agent

## The Problem
After AUS approval, an underwriter issues 15-40 conditions per loan — each a free-text instruction like "Provide evidence of 2 months reserves in liquid assets" or "Letter of explanation for the $3,200 deposit on page 4 of the March bank statement." The processor reads each condition, interprets what's needed, searches the loan file for matching documents, reviews whether the document satisfies the condition's specific requirements (correct date range, correct amounts, correct account), and either clears the condition or requests additional documentation from the borrower. This interpret-match-verify loop repeats 15-40 times per loan and consumes 2-4 hours of processor time per file.

## Why Nobody Has Built This
Conditions are written in inconsistent natural language — the same requirement phrased ten different ways by ten different underwriters. Matching conditions to documents requires understanding both the semantic meaning of the condition and the content of the document (a pay stub is not just any pay stub — it must show YTD earnings and fall within the date range specified). The verification step requires reading and reasoning about document content, not just classifying document type. This is a multi-step NLP + document understanding problem that only recently became tractable with LLM and multimodal model capabilities.

## What to Build
An engine that ingests the condition list (parsed from the LOS or from an underwriting decision email), classifies each condition by type and requirement, searches the loan file for matching documents, uses OCR + document understanding to verify the document meets the condition's specific parameters (dates, amounts, names), and auto-clears conditions where the match is high-confidence. For unmatched or partially matched conditions, it generates a specific document request to the borrower with exactly what's needed and why.

## Target Customer
Mid-size brokerages (10-30 loan officers) with dedicated processing teams of 3-8 processors, each handling 15-25 files per month. These operations spend $150K-400K annually on processor labor, with 40-60% of that labor going to condition clearing.

## Impact If Built
Automates 40-60% of condition clearing — the conditions that are straightforward document matches (pay stubs, bank statements, tax returns with specific date ranges). Reduces per-file processing time by 1-2 hours, enabling each processor to handle 25-35% more volume. At an average processor salary of $50K-65K, a 10-processor shop saves $200K-300K annually or absorbs proportionally more volume without hiring.
