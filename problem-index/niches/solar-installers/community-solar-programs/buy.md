# CRM Adapted for Subscriber Lifecycle

**Niche:** [[niches/solar-installers/community-solar-programs/profile|Community Solar Programs]]
**Industry:** [[industries/solar-installers|Solar Installers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Community solar developers use Salesforce or HubSpot for subscriber management but these CRMs treat subscribers as sales contacts — they don't model subscription shares, credit allocation, utility enrollment, or the regulatory lifecycle that makes community solar subscriber management fundamentally different from standard CRM.
**Tags:** #data-integration #workflow-orchestration #automation #compliance #quick-win

## The Problem
A subscriber in a community solar project is not a traditional CRM contact. They have a subscription size (measured in kW or percentage of array capacity), an associated utility account number, a credit allocation schedule, a contract term with renewal provisions, and regulatory status (enrolled/pending/waitlisted/cancelled) that affects the project's compliance reporting. Salesforce can store all of this as custom fields, but the workflow automation required — calculating monthly credit allocations, triggering utility enrollment paperwork, processing churn replacements from the waitlist, and generating regulatory compliance reports — requires extensive Salesforce customization that costs $50K-100K to implement and ongoing admin support to maintain.

## What Already Exists
Salesforce and HubSpot handle contact management, pipeline tracking, and email communication. Several community solar developers have built custom Salesforce implementations with community-solar-specific objects and workflows. These custom implementations work but are expensive to build, fragile to maintain, and not transferable between developers.

## The Customization Gap
A Salesforce managed package (or standalone lightweight CRM) purpose-built for community solar that: (1) includes community-solar-specific objects — Subscriber (with subscription kW, utility account, contract term, enrollment status), Project (with total capacity, subscribed capacity, available capacity, waitlist depth), and Allocation (monthly credit calculation per subscriber); (2) automates the subscriber lifecycle — when a new subscriber is enrolled, the system generates utility enrollment paperwork, updates project available capacity, and adjusts the waitlist; when a subscriber cancels, it triggers the churn replacement workflow; (3) calculates monthly credit allocations from production data and subscription percentages, generating subscriber credit statements; and (4) produces state-specific compliance reports from the subscriber data without manual data compilation.

## Target Customer
Community solar developers currently using customized Salesforce instances who spend $10K-30K/year on CRM admin and maintenance. New community solar developers who need subscriber management but can't justify the $50K-100K custom Salesforce build.

## Impact If Solved
Reduces CRM implementation cost from $50K-100K custom build to $500-2,000/month managed package. Standardizes subscriber management workflows across the community solar industry. Eliminates 5-10 hours per month of manual compliance report generation. Enables smaller developers to enter the community solar market without enterprise CRM investment.
