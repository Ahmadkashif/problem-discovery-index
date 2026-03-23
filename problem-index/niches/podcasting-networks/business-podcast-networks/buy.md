# Guest Booking CRM with Audience-Fit Scoring

**Niche:** [[niches/podcasting-networks/business-podcast-networks/profile|Business Podcast Networks]]
**Industry:** [[industries/podcasting-networks|Podcasting Networks]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Hubspot CRM tracks contacts and Calendly handles scheduling, but neither scores potential guests by audience fit, prevents duplicate bookings across shows in a network, or manages the pre-interview prep workflow.
**Tags:** #gradient-boosting #ranking #tabular-ml #automation #revenue-impact

## The Problem
A business podcast network with 5 shows books 300–500 guests per year. Guest sourcing comes from inbound pitches (200+ per week from PR agencies), host networks, listener suggestions, and active outreach. The booking coordinator must: (1) evaluate each pitch for relevance to the right show, (2) research the guest's expertise, audience, and social following, (3) check that the guest hasn't appeared on another show in the network recently, (4) schedule the recording, (5) send prep materials (show format, talking points, tech requirements), (6) confirm 48 hours before, and (7) manage rescheduling when guests cancel (20–30% cancellation rate). This is done via email, a shared Google Sheet, and Calendly — with no visibility into whether a guest is a good audience fit or just a good self-promoter.

## What Already Exists
HubSpot and Salesforce manage contacts and pipeline stages. Calendly and SavvyCal handle scheduling. PodMatch and MatchMaker.fm connect guests with hosts. But these tools don't integrate: the guest CRM doesn't talk to the scheduling tool, neither connects to the episode tracking system, and nobody checks guest overlap across shows. PodMatch matches by topic category, not by audience fit — a guest who's perfect for a startup-focused show might be wrong for an enterprise leadership show, even though both are "business" podcasts.

## The Customization Gap
A podcast guest CRM needs to: (1) score inbound pitches by audience fit using the show's listener demographics, past guest performance (download numbers for episodes featuring similar guests), and the guest's own audience reach, (2) deduplicate across shows in the network (Guest X appeared on Show A 3 months ago — don't book on Show B until Month 6), (3) manage the full booking pipeline with automated prep email sequences, tech check reminders, and day-before confirmations, (4) track guest episode performance post-publication (did this guest's episode perform above or below average?) to inform future booking decisions, and (5) maintain a "guest alumni" database for rebooking high-performers.

## Target Customer
Booking coordinators and content directors at business podcast networks managing 3+ shows with 50+ guests per show per year.

## Impact If Solved
Audience-fit scoring increases average episode downloads by 15–25% by booking guests whose expertise and reach align with listener interests. Automated pipeline management reduces booking coordinator time from 30 hours/week to 10 hours/week. Network-wide deduplication prevents the awkward situation where the same guest tells the same story on two different shows 2 weeks apart — an estimated 5–8% occurrence rate without coordination.
