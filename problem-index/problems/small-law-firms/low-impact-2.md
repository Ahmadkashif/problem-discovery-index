# Client Communication Drafting and Matter Status Updates

**Industry:** [[small-law-firms|Small Law Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** General LLM tools can draft professional emails, but client communications from a law firm need to be drafted in the attorney's specific voice, reflect the matter's current posture and pending actions, and comply with professional responsibility rules about what can and cannot be communicated to a client.
**Tags:** #llm #text-generation #nlp #automation #worker-facing

## The Problem
Small firm attorneys spend 20-30% of their working time on client communication — status update emails, explaining developments in the matter, requesting documents or information from the client, relaying opposing counsel's positions, and answering questions that require some research before responding. Most of this communication is substantively similar from matter to matter (here's where we are, here's what happened, here's what you need to do, here's what we're doing next) but requires personalization to the specific client relationship and matter context. Writing a good client status email from scratch takes 8-15 minutes; an attorney billing at $350/hour loses $50-90 in revenue time on each one, or accepts that the email will be rushed and possibly unclear.

## What Already Exists
General-purpose LLMs write professional emails effectively. Clio has introduced some AI email drafting features. Legal document drafting tools (Spellbook, Harvey) focus on legal documents rather than client communications. The gap is a tool that understands the specific matter context — knows what stage the litigation is at, what the last action was, what the next deadline is, and what the specific question was — and generates a communication that feels like it was written by the specific attorney for this specific client.

## The Customisation Gap
Client communications in a legal context require: (1) calibration to professional responsibility rules (the attorney cannot share certain privileged strategy with clients in certain contexts; communications with represented parties have specific rules); (2) reflection of the matter's specific current state from the case management system; (3) the attorney's individual voice and relationship style (formal with institutional clients, more conversational with individuals); (4) appropriate caveats and next-steps that reflect legal standards, not just pleasantries. These customizations require matter-context integration and legal-domain constraints that generic communication tools don't provide.

## Impact If Solved
Reduces client communication drafting time by 60-70%. For an attorney who sends 15-20 client communications per day across all active matters, recovering 5-8 minutes per communication saves 75-160 minutes daily — 1-2.5 additional billable hours that were previously consumed by non-billable administrative writing.
