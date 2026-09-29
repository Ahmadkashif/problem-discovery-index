# Document Extraction Adapted to the Project Manual

**Niche:** [[niches/construction-tech-platforms/submittal-rfi-routing/profile|Submittal & RFI Routing Content]]
**Industry:** [[industries/construction-tech-platforms|Construction Tech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Layout-aware document extraction is a commodity capability sold into every document-heavy industry, and construction specifications — which follow a published numbering standard across most of the market — are processed by people.
**Tags:** #large-language-models #transformers #bert #word-embeddings #evaluation-metrics #confidence-intervals #automation #data-integration
**Contested on:** Every serious competitor in document workflow is fighting to read the specification and decide who a submittal or RFI should go to, in what sequence, and by when — and whoever routes most accurately against the spec takes the account.

## The Problem
A project manual is a structured document pretending to be an unstructured one. It follows MasterFormat numbering, divides into divisions and sections, and within each section follows a conventional three-part structure with submittal requirements in a predictable place. It is also a PDF assembled from multiple authors, with inconsistent formatting, scanned inserts, addenda that modify sections after the fact, and cross-references that change meaning. Generic extraction handles the structure and fails on the exceptions, and the exceptions are where the consequential requirements hide.

## What Already Exists
Layout-aware parsing, table extraction, long-context language models and structured output generation are all commodity, available from multiple providers and as open implementations. Document AI products handle scanned and mixed-quality PDFs competently. MasterFormat and the CSI three-part section format are published, stable and near-universal in US commercial construction, which gives the extraction a strong prior that most industries do not have.

## The Customization Gap
The adaptation is in exploiting the standard and handling what breaks it. It requires: (1) using MasterFormat structure as a parsing prior rather than treating the document as free text, which resolves most of the segmentation problem before any model runs; (2) addenda and revision handling as a first-class concern — a specification is amended repeatedly before and after award, and an extraction that reads the original and ignores addendum three is confidently wrong in exactly the way that causes a missed requirement; (3) cross-reference resolution, since sections routinely defer to the general conditions or to another section and the operative requirement is elsewhere; (4) master-text recognition, because most sections derive from a small number of widely used master specifications and recognising a familiar section makes extraction both cheaper and more reliable; and (5) evaluation against project engineer-built registers as ground truth, which every general contractor has thousands of and none has ever used as a dataset.

## Target Customer
Construction platform vendors, large general contractors with in-house preconstruction teams, and the specification writing side — architects and specifiers — who would benefit from seeing what their own documents actually require.

## Impact If Solved
Extraction accuracy is measurable against registers that already exist, which means this can be validated before it is trusted — the rare case where the ground truth is abundant and free. Exploiting the MasterFormat prior makes the adaptation far cheaper than general document extraction, and addenda handling is the specific capability that separates a usable product from a demo.
