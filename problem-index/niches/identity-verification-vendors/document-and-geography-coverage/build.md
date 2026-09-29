# Reading a Document Never Seen Before

**Niche:** [[niches/identity-verification-vendors/document-and-geography-coverage/profile|Document & Geography Coverage]]
**Industry:** [[industries/identity-verification-vendors|Identity Verification Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A document type not in the template library is rejected, and the library is written by hand one document at a time.
**Tags:** #cnns #object-detection #transfer-learning #semantic-segmentation #evaluation-metrics #confidence-intervals #automation #contrastive-learning
**Contested on:** Every serious competitor in this niche is fighting to support thousands of document types across hundreds of jurisdictions, each with its own layout, security features and revision history — and whoever stops maintaining that library by hand supports the documents everyone else declines.

## The Problem
Coverage is produced by people. Someone obtains a specimen, documents the layout, identifies the security features, encodes the validation rules, and adds it to the library. Multiply by thousands of document types and hundreds of jurisdictions, each revising every few years while older versions stay valid for a decade. The result is a library that lags reality, is strongest where the commercial volume is, and rejects the documents of people from places the vendor has not prioritised.

## Why Nobody Has Built This
Template authoring was the original approach and it worked at small scale, so the architecture assumed it — a system built around explicit templates cannot generalise by design. Specimens for many documents are hard to obtain. Coverage expansion is prioritised by market size, which systematically deprioritises the same populations everywhere. And nobody reports coverage in a way that would expose the gap.

## What to Build
Generalise rather than enumerate. Build models that read and validate documents structurally rather than by template lookup, which is the core and is what removes the per-document production cost. Learn from the library that exists, since thousands of documented types are training data for generalising to the ones that are not. Detect and read unfamiliar documents with an expressed confidence, so an unknown document routes to review rather than to rejection. Identify a new revision automatically from field drift and failure clustering, because revisions currently announce themselves as a spike in failures weeks later. Prioritise coverage by applicant impact rather than by market size, as the current ordering entrenches exclusion. Use the machine-readable and chip-based elements where present, since a standards-based read is far more reliable than a visual one and is underused. Report coverage honestly by jurisdiction and revision, which nobody publishes and which customers serving international populations need. Handle older revisions deliberately, because they remain valid and belong to people less likely to have a new one. Crowd-source specimen collection from production where lawful and consented, as the documents are arriving anyway. And measure rejections attributable to coverage rather than to the applicant, which separates a product gap from a risk decision.

## Target Customer
Coverage and product leadership, customers serving international and immigrant populations, applicants holding documents nobody supports, and document authentication vendors.

## Impact If Built
A system built around explicit templates cannot generalise by design, so coverage is a manual production line. Structural reading learned from the existing library removes the per-document cost and reaches the documents commercial prioritisation never would.
