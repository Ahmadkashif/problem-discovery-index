# Change Order Documentation Automation from Field Observations

**Industry:** [[general-contractors|General Contractors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic voice-to-text and note-taking tools can transcribe field observations, but they can't structure them into formal change order requests with scope description, cost impact, schedule impact, and the owner/architect notification language that protects the GC's claim rights under the contract.
**Tags:** #llm #text-generation #nlp #automation #compliance

## The Problem
Change orders are how GCs get paid for work beyond the original contract scope — and they are a major source of disputes when not documented properly. When a superintendent discovers that the soil conditions require additional excavation depth (a differing site condition), or when the architect's clarification drawing adds work that wasn't in the original scope, the GC has contractual rights to additional compensation — but only if the change is documented, submitted, and approved according to the contract's notice requirements. Most contracts require change order notice within 7-14 days of discovering the changed condition. Superintendents, who are managing 15 concurrent activities on a busy job site, often document changes informally (voice memo, text message, rough note) and rely on project managers to formalize them later. The "later" step gets delayed, deadlines are missed, and valid claims are lost.

## What Already Exists
Procore has change order management workflow tools that handle the formal approval process once a change order is initiated. DocuSign and contract management tools handle the signature workflow. Voice-to-text apps (Otter.ai, Google Recorder) transcribe field dictation. None of these turn an informal field observation ("the foundation wall is 2 feet higher than spec'd, probably adds 3 days") into a properly formatted change order request that includes the contractual basis for the claim, a cost summary, a schedule impact statement, and the required notice language for the specific contract type (AIA, ConsensusDocs, or owner proprietary).

## The Customisation Gap
A change order documentation tool for GCs needs to: accept field observations in natural language (voice or text); classify the type of change (differing site condition, owner-directed change, architect clarification, unforeseen condition); extract the key facts (what changed, what work is affected, what the cost and schedule impact is); and draft a formal change order request in the format required by the contract type, including the proper notice language that protects the GC's claim rights. The construction contract law knowledge (what constitutes proper notice? what is the standard of documentation for a differing site condition claim?) is the customization that no generic text tool can provide.

## Impact If Solved
Reduces change order claim losses — legitimate change work that GCs perform but fail to recover because of documentation failures. Industry estimates suggest 5-15% of annual project revenue is in change work that either isn't submitted or is submitted too late to be recoverable. A $10M annual revenue GC that improves change order recovery by even 3% captures $300K in previously lost revenue.
