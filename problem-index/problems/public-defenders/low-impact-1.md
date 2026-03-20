# Client Communication Across Incarcerated and Non-Incarcerated Populations

**Industry:** [[public-defenders|Public Defenders]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic legal communication tools assume clients have email and phone access, but 60% of public defender clients are incarcerated with access limited to $0.25-per-message kiosks, monitored phone calls, and postal mail — creating a communication blackout at the moment when informed consent matters most.
**Tags:** #large-language-models #transformers #attention-mechanisms #transfer-learning #evaluation-metrics #entropy-cross-entropy-kl-divergence #data-integration #worker-facing

## The Problem

Public defenders must communicate with clients about case developments, plea offers, hearing dates, and legal strategy. For clients who are out on bail or released on recognizance, this happens via phone, text, or in-person office visits — imperfect but functional. For the approximately 470,000 people held in pretrial detention at any given time, communication is severely constrained: jail visits require travel and scheduling (often 30-60 minutes each way, available only during business hours), phone calls are monitored by the prosecution (destroying privilege unless on a pre-approved legal line), and electronic messaging through JPay or Securus costs money the client's family can barely afford.

The result is that incarcerated clients make critical decisions — accepting or rejecting plea offers that determine years of their lives — with minimal attorney contact. A defender may convey a plea offer via a 10-minute jail visit squeezed between court appearances, leaving no time for the client to ask questions or for the attorney to explain sentencing implications, collateral consequences (immigration, employment, housing), or alternative strategies.

## What Already Exists

Clio, MyCase, and other legal practice management tools offer client portals with secure messaging. JPay and Securus provide electronic messaging within correctional facilities. Zoom and Microsoft Teams are used for remote hearings. None of these systems bridge the communication gap between the attorney's workflow and the incarcerated client's constrained access. The attorney must manually switch between their case management system, the jail's visitation scheduling system, and the facility's messaging platform — each with different login credentials, different interfaces, and different availability windows.

## The Customisation Gap

The missing layer is a unified client communication platform that adapts to the client's custodial status and facility-specific access constraints. For non-incarcerated clients: secure text messaging, appointment reminders, and document sharing through a mobile-optimized portal. For incarcerated clients: integration with facility messaging systems (GTL, Securus, JPay APIs where available), automated scheduling of legal calls on privileged lines, plain-language case update summaries formatted for kiosk-sized screens, and preparation of documents for postal mail delivery when electronic access is unavailable.

The system needs to understand the legal communication context: that privilege must be maintained (no discoverable content in non-privileged channels), that clients may have limited literacy (requiring simplified language at a 6th-grade reading level), and that family members often serve as communication intermediaries (requiring consent-managed information sharing).

## Impact If Solved

Increases client contact frequency from 1-2 interactions per month to 4-6 for incarcerated clients, enabling genuinely informed decision-making on plea offers and case strategy. Saves defenders 3-5 hours/week currently spent on jail visit logistics and phone scheduling. Reduces the 15-20% of cases where clients accept plea deals without understanding collateral consequences — each informed rejection of a bad plea deal can prevent years of unnecessary incarceration and its cascading effects on families and communities.
