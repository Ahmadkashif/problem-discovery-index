# NLP-Driven Ticket Classifier with Automated Resolution Orchestration

**Niche:** [[niches/it-managed-services/l1-ticket-automation/profile|L1 Ticket Triage and Automated Resolution]]
**Industry:** [[industries/it-managed-services|IT Managed Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product takes a free-text ticket description, classifies it with sufficient accuracy to trigger automated remediation scripts on the affected device via RMM, and handles the full lifecycle from classification through execution through verification and closure.
**Tags:** #bert #transformer #text-classification #nlp #tacit-knowledge-ml #automation #revenue-impact

## The Problem
An end user submits a ticket: "my outlook keeps freezing and then I can't get to any websites." An experienced L2 technician reads this and immediately suspects a DNS resolution issue (not Outlook-specific, not browser-specific — the common thread is network connectivity), checks DNS settings, flushes the cache, and the issue resolves in 5 minutes. A keyword-based auto-router sees "outlook" and "websites" as two separate issues and creates two tickets, both misrouted. This is the tacit knowledge problem: experienced technicians read between the lines of end-user descriptions to identify root causes that the user cannot articulate. Building an automated classifier that matches this diagnostic inference is the prerequisite for safe automated resolution.

## Why Nobody Has Built This
The classification-to-resolution pipeline requires three components that have not been integrated: (1) an NLP classifier that maps unstructured ticket text to a resolution category (not just an issue type) with high confidence, (2) a resolution orchestration layer that maps each category to a specific remediation script and the affected device, and (3) a safety layer that prevents automated execution when confidence is below threshold or when the resolution could cause harm (rebooting a production server, resetting credentials for the wrong user). Building this end-to-end requires ML expertise, deep PSA/RMM integration, and a robust safety framework — a combination that neither PSA vendors nor AI startups have fully delivered.

## What to Build
An intelligent ticket resolution pipeline: tickets arrive via email, portal, or phone (transcribed). An NLP model classifies the ticket into a resolution category with a confidence score. For high-confidence L1 categories (>95%), the system identifies the affected device from the ticket context and RMM data, executes the appropriate remediation script via the RMM agent, verifies the resolution (checks that the service is running, the connectivity is restored, the password is reset), and closes the ticket with a resolution summary. For medium-confidence tickets (80-95%), the system pre-populates a diagnosis and recommended resolution for technician review. For low-confidence or complex tickets, standard routing applies.

## Target Customer
Service delivery managers at MSPs with 300+ endpoints and 500+ monthly tickets, where L1 resolution consumes 2-3 FTEs of technician capacity.

## Impact If Built
Automates 30-40% of total ticket volume (the high-confidence L1 subset), saving 1-2 FTEs of technician labor annually ($60K-$120K). Reduces average first-response time for automated tickets from 30 minutes to under 2 minutes. Enables the MSP to grow endpoint count by 30-50% without hiring.
