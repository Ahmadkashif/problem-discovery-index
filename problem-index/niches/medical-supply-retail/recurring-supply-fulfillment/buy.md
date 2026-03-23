# Multi-Channel Patient Engagement for Resupply

**Niche:** [[niches/medical-supply-retail/recurring-supply-fulfillment/profile|Recurring Supply Fulfillment]]
**Industry:** [[industries/medical-supply-retail|Medical Supply Retail]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Patient communication platforms exist in healthcare, but none are designed for DME resupply outreach — where the goal is order conversion (not appointment booking), the content is supply-specific, and regulatory constraints (TCPA, HIPAA) apply to every message.
**Tags:** #automation #workflow-orchestration #compliance #revenue-impact

## The Problem
DME resupply outreach is overwhelmingly phone-based: reps call patients, often 3-5 times before reaching them. But patients increasingly prefer text and email — a 65-year-old CPAP user may not answer unknown numbers but reads every text. The supplier wants to add text and email channels but faces regulatory barriers: TCPA requires explicit opt-in for automated text messages, HIPAA requires secure messaging for health-related content, and state telemarketing laws apply to sales-oriented outreach (which resupply calls are). Most suppliers avoid multi-channel outreach because the compliance requirements are unclear and the penalties for violations ($500-1,500 per unsolicited text under TCPA) are severe.

## What Already Exists
Healthcare patient engagement platforms (Luma Health, Klara, Relatient) handle appointment reminders and secure messaging but are designed for clinical practices, not DME suppliers. SMS marketing platforms (Twilio, Podium) handle text messaging but don't include HIPAA compliance or TCPA consent management. IVR systems handle automated phone outreach but have declining effectiveness as patients screen calls.

## The Customization Gap
The missing capability is a DME-specific multi-channel engagement platform that: manages TCPA consent at the patient level (tracking opt-in status per channel), sends HIPAA-compliant messages (encrypted, with proper consent), provides resupply-specific message templates ("Your CPAP mask replacement is eligible. Reply YES to order your ResMed AirFit F20, size Medium"), handles order confirmation via text (patient replies "YES" and the order is placed without a phone call), and tracks channel performance by patient segment. The platform must handle the legal complexity transparently — the supplier shouldn't need to think about TCPA/HIPAA compliance for each message.

## Target Customer
DME suppliers with 500+ recurring patients who rely primarily on phone outreach and want to add text and email channels without assuming regulatory risk.

## Impact If Solved
Adds text and email channels that convert 10-15% of previously unreachable patients (those who don't answer phone calls). Reduces cost-per-contact from $2-3 (phone call with rep time) to $0.05-0.10 (automated text). On 5,000 monthly outreach attempts, shifting 30% to text saves $3K-4K/month in labor while maintaining or increasing order volume.
