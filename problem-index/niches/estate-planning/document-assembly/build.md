# AI-Assisted Full-Plan Assembly Engine

**Niche:** [[niches/estate-planning/document-assembly/profile|Document Assembly & Plan Packaging]]
**Industry:** [[industries/estate-planning|Estate Planning]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Attorneys input client data once, and the system generates a complete, internally consistent estate plan package — 6-8 documents with cross-references, alternative provisions selected by client circumstances, and a funding checklist — ready for attorney review.
**Tags:** #large-language-models #transformers #bert #decision-trees #feature-engineering #automation #workflow-orchestration

## The Problem
Assembling a complete estate plan package requires the paralegal to: enter client data into the document assembly tool, generate each document individually, ensure cross-document consistency (same fiduciaries, same asset references, same contingent provisions across all documents), select appropriate alternative provisions based on client circumstances (married vs. single, minor children vs. adult children, business owner vs. employee, multi-state assets vs. single state), generate a funding checklist tailored to the client's asset types, and compile the package for attorney review. This process takes 3-6 hours per plan for an experienced paralegal and 6-10 hours for a newer one. Errors in cross-document consistency are caught (if at all) during attorney review, requiring rework.

## Why Nobody Has Built This
Current document assembly tools (WealthDocx, HotDocs) are template engines — they fill in blanks in individual document templates. Building a full-plan assembly engine requires a different architecture: a data model that represents the estate plan as a unified structure (with fiduciaries, beneficiaries, assets, and provisions as entities that span multiple documents), a decision engine that selects appropriate provisions based on client circumstances (if the client has minor children, include guardianship provisions in the will and minor's trust provisions in the trust), and a consistency enforcement layer that ensures changes to one entity propagate across all documents. This is architecturally different from template-filling and requires rethinking the document assembly approach from the ground up. WealthDocx's business model depends on selling individual document templates, creating a disincentive to build package-level assembly.

## What to Build
A plan assembly platform where the attorney or paralegal enters client data once into a structured intake form: family structure, fiduciary appointments (trustee, successor trustee, executor, guardian, healthcare agent, financial agent), asset inventory, specific bequests, and planning preferences. The system applies a decision engine to select appropriate document types and provisions (e.g., if client has minor children, include testamentary guardianship; if client owns a business, include business succession provisions; if client has property in multiple states, flag ancillary probate considerations). It generates all documents as a unified package with cross-references resolved, produces a customized funding checklist based on the client's actual asset types, and presents the package to the attorney in a review interface that highlights the key decision points and provisions that require human judgment. An LLM layer assists with: drafting custom provisions for unusual situations, explaining provision implications in plain language for client communication, and flagging provisions that may conflict with state law in the client's jurisdiction.

## Target Customer
Estate planning law firms (1-10 attorneys) where paralegals spend 3-6 hours per plan on document assembly and attorneys spend 1-2 hours reviewing for consistency errors that should have been prevented at assembly.

## Impact If Built
Reduces per-plan assembly time from 3-6 hours to 30-60 minutes. Eliminates cross-document consistency errors (currently found in 10-15% of plans during attorney review). Enables firms to handle 2-3x their current plan volume at the same staffing level. Reduces attorney review time by surfacing only the provisions requiring human judgment rather than requiring full-document review.
