# AI Vendor Communication Orchestrator

**Niche:** [[niches/event-planning/vendor-coordination/profile|Vendor Coordination Automation]]
**Industry:** [[industries/event-planning|Event Planning]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No system automates the cascading vendor communication sequence that every event requires — sending role-specific details, collecting confirmations, following up on non-responses, and managing change propagation.
**Tags:** #llm #text-generation #nlp #ai-agent #automation

## The Problem
Three weeks before a 300-person corporate gala, the planner must send final details to 20 vendors — but each vendor needs different information. The caterer needs the final head count, dietary restrictions, and service timeline. The florist needs table count, centerpiece specifications, and setup time. The AV company needs the presentation schedule, speaker requirements, and podium setup. The photographer needs the key moments timeline and family groupings. The planner drafts 20 customized emails, manually extracting vendor-relevant details from the master event document. Then they track responses, follow up with non-responders, and repeat when details change.

## Why Nobody Has Built This
Vendor communication appears simple but requires contextual understanding: knowing what information each vendor type needs, how to phrase requests for different vendor relationships (formal for the venue, casual for the familiar DJ), and how to propagate changes (head count increased → notify caterer, venue, and rentals, but not photographer or DJ). This is an LLM-native problem — generating contextualized communications from a master event document.

## What to Build
An AI-powered vendor communication engine: the planner maintains a master event document (details, timeline, specifics). When communication is triggered (final details, change notification, confirmation request), the system generates vendor-specific messages extracting only the relevant details for each vendor's role. The planner reviews and sends with one click. Non-responses trigger automated follow-ups. Changes to the master document automatically identify which vendors are affected and draft change notifications.

## Target Customer
Event planners managing 15+ events per year with 10+ vendors each who spend 8-12 hours per event on vendor email communication.

## Impact If Built
Reduces vendor communication time from 8-12 hours per event to 1-2 hours, ensures no vendor receives incomplete or irrelevant information, and guarantees that changes propagate to all affected vendors — preventing the "nobody told the caterer" disasters.
