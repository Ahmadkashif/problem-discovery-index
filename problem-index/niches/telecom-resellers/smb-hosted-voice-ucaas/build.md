# Call-Flow Discovery From the Old Phone System

**Niche:** [[niches/telecom-resellers/smb-hosted-voice-ucaas/profile|SMB Hosted Voice & UCaaS]]
**Industry:** [[industries/telecom-resellers|Telecom Resellers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every migration starts with an implementation specialist interviewing an office manager about how calls are answered today, because nobody reads the old system's configuration and call records to find out.
**Tags:** #large-language-models #transformers #graph-theory #feature-engineering #automation #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to move a small business's numbers, call flows and handsets onto its platform with no missed calls on cut-over day, and whoever makes the switch invisible wins the seats.

## The Problem
A 30-seat business's phone system has years of history in it: hunt groups nobody remembers creating, an auto-attendant recording with a menu option that rings a former employee, a night mode, a fax line, a paging zone, a door phone, numbers that forward to a mobile phone. The implementation specialist rebuilds this from a kickoff call and a questionnaire. What the office manager forgets surfaces on cut-over day as a missed call.

## Why Nobody Has Built This
Old systems are varied: on-premises PBXs from many makers, competitors' hosted platforms, analogue key systems. Their configuration exports aren't standard. Providers treat migration as a services cost rather than a product, and the knowledge of how to read an old system sits with a few senior installers.

## What to Build
A discovery tool that ingests whatever is available: configuration exports or screenshots of the old system, the losing carrier's CSR, a month of call detail records and the auto-attendant recordings. From these it reconstructs the call-flow graph (which number rings which group, when, and where calls overflow), flags dead ends and unused numbers, transcribes and drafts new greetings, and generates the configuration for the provider's platform for the customer to confirm in a visual walkthrough.

## Target Customer
Implementation and onboarding leaders at UCaaS and hosted-voice providers, and white-label platform hosts serving thousands of resellers.

## Impact If Built
Discovery that took several calls becomes a review of a draft, cut-over defects drop, and implementation capacity, often the bottleneck on growth, stretches further (estimate).
