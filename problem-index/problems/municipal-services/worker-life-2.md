# City Clerk FOIA/Records Request Burden

**Industry:** [[municipal-services|Municipal Services]]
**Type:** Worker Life Changing
**One-liner:** City clerks stop spending 10-15 hours per week manually searching, reviewing, and redacting public records — reclaiming time for the legislative support work they were actually hired to do.
**Tags:** #large-language-models #transfer-learning #attention-mechanisms #transformers #word-embeddings #entropy-cross-entropy-kl-divergence #worker-facing #compliance

## The Problem
City clerks in mid-size municipalities handle 20-80 FOIA/public records requests per month, each requiring a multi-step process: interpret the request scope, search across email archives, meeting minutes, contracts, personnel files, police reports, and financial records, identify responsive documents, review each for redaction requirements (SSNs, medical info, law enforcement sensitive, attorney-client privilege, deliberative process), apply redactions, compile the response, and track the statutory deadline (typically 5 business days). A single complex request — "all emails between the city manager and XYZ Development regarding the Main Street project" — can take 8-12 hours to fulfill across fragmented document management systems, email servers, and physical filing cabinets. Clerks do this on top of their primary duties: preparing council agendas, recording minutes, managing elections, and maintaining ordinance codification.

## Why It Matters to the Worker
City clerks are typically one-deep positions — there is one clerk (maybe with one deputy) serving an entire municipality. Missing a FOIA deadline creates legal liability for the city and personal professional risk for the clerk. The work is tedious, high-stakes, and invisible: no one notices when 40 requests are fulfilled on time, but a single missed redaction of a Social Security number becomes a news story. Many clerks report that FOIA work has grown from 10% of their week to 40%+ over the past decade as request volume increases and requestors become more sophisticated. The cognitive load of remembering 50 different redaction rules across different document types while scanning hundreds of pages is genuinely draining.

## What a Solution Looks Like
An LLM-powered records request assistant that takes a FOIA request in natural language, searches across connected document repositories (email, DMS, minutes, contracts), retrieves candidate responsive documents, flags likely redaction targets (PII patterns, privilege markers, exemption categories specific to the state's public records law), and generates a draft response package for the clerk to review and approve. The clerk shifts from doing the search-and-redact work to reviewing and validating it — a 12-hour request becomes a 2-hour review.

## Impact If Solved
Clerks reclaim 8-12 hours per week currently consumed by records requests, FOIA response times drop from an average of 4.2 business days to under 2, redaction error rates decrease (the model does not get fatigued at page 47 of a 200-page document review), and the clerk can return focus to legislative support, election administration, and the civic functions that drew them to the role in the first place.
