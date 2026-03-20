# Group Booking & Manifest Management

**Industry:** [[charter-bus-operators|Charter Bus Operators]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Event ticketing and group travel platforms exist everywhere — but none handle the specific chaos of charter bus manifests where passenger counts change daily, pickup locations multiply, and the operator needs a real-time headcount to assign the right bus.
**Tags:** #large-language-models #bert #transformers #attention-mechanisms #word-embeddings #transfer-learning #workflow-orchestration

## The Problem
A typical charter booking starts as a single contact (wedding planner, school administrator, corporate event coordinator) who provides an estimated headcount. Between booking and departure, that headcount changes 3-8 times as individual passengers confirm, cancel, or request different pickup points. The operator needs an accurate manifest for DOT compliance (passenger lists are required for interstate travel), for assigning the correctly-sized bus, and for planning multi-stop pickups. Today this information flows through email chains, text messages, and phone calls — the dispatcher manually updates a spreadsheet that is outdated within hours of being created.

## What Already Exists
Eventbrite, SignUpGenius, and Google Forms handle group RSVPs. CRM tools like HubSpot manage customer contacts. Charter-specific platforms like BusHive offer basic trip management. Group travel tools like Travefy and TripIt organize itineraries for travel agencies.

## The Customisation Gap
None of these tools connect the RSVP/manifest workflow to the operational decisions it drives. When a wedding planner adds 8 passengers, the system should automatically flag that the 36-seat bus is no longer sufficient and a 56-seater needs to be assigned — triggering a re-quote and a driver reassignment. When a school trip coordinator submits a roster, the system should extract student names, guardian contacts, and medical/allergy notes into a DOT-compliant manifest format and a driver briefing sheet. The NER layer needs to parse unstructured emails ("Hi, we're adding the Johnson family — that's 4 adults and 2 kids under 5, they'll need car seats") into structured passenger records with age categories and equipment requirements.

## Impact If Solved
Dispatchers currently spend 30-60 minutes per booking managing manifest changes across multiple communication channels. A self-service portal where group coordinators update their own manifests — with automatic operational triggers — eliminates 70-80% of that back-and-forth while reducing day-of-departure surprises (wrong bus size, missing passengers, incorrect pickup sequence) that cost $500-$2,000 per incident in emergency reconfigurations.
