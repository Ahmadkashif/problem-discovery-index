# Scheduling & Booking Platforms

## Profile
**Category:** Horizontal SaaS
**Market Size:** ~$1.5B US appointment scheduling and booking software
**Tech Maturity:** High and commoditised — Calendly, Acuity, Cal.com, Square Appointments, Setmore and the booking modules inside every vertical platform have made self-service booking universal and nearly free. The category solved putting an appointment on a calendar and has never addressed whether the appointment happens.
**Workforce:** Onboarding specialists, integration engineers, support representatives, availability and resource configuration staff, partnerships teams

## Key Pain Themes
For any business that sells time, the no-show is the loss that cannot be recovered — the slot is gone, the practitioner was paid or idle, and the revenue does not come back. Rates run into the double digits in several sectors, and the category's entire response is a reminder sent to everyone identically. Underneath that, availability logic is where the products actually break: a real business has multiple staff with different skills, rooms and equipment that are also constrained, buffers that vary by service, and travel time — and expressing that correctly defeats most configuration interfaces, so businesses simplify their availability and sell less than they could. Reminder sequences are configured once and never measured. The coordinator resolving resource conflicts by hand and the solo practitioner managing their own calendar between clients are both doing work the system could do.

## Current Tech Landscape
Calendly dominates the individual professional use case and has expanded into teams and routing; Acuity and Square Appointments serve appointment-based small businesses; Cal.com competes as the open-source alternative; vertical platforms in health, beauty, fitness and field service bundle scheduling as a module. Calendar integration with Google and Microsoft is mature. Payment collection and deposits at booking are widely available and inconsistently used. Reminder delivery by email and SMS is universal. Round-robin and pooled availability exist and handle simple team cases well.

## Problems
- [[problems/scheduling-booking-platforms/high-impact|🔴 High Impact: No-Shows and the Unrecoverable Slot]]
- [[problems/scheduling-booking-platforms/low-impact-1|🟡 Low Impact: Multi-Resource Availability Logic]]
- [[problems/scheduling-booking-platforms/low-impact-2|🟡 Low Impact: Reminder and Confirmation Sequences]]
- [[problems/scheduling-booking-platforms/worker-life-1|🟢 Worker Life: Coordinator Resolving Resource Conflicts]]
- [[problems/scheduling-booking-platforms/worker-life-2|🟢 Worker Life: Solo Practitioner Calendar Administration]]
- [[problems/scheduling-booking-platforms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/scheduling-booking-platforms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
These platforms observe an enormous number of appointments across every sector that sells time, with the booking, the lead time, the reminders sent, the channel, the customer's history and the eventual attendance all captured. Whether someone shows up is one of the most consequential and most predictable behaviours in small business, and the industry's universal response — a reminder twenty-four hours before, sent to everyone — is applied without ever having been tested against an alternative.
