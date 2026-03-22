# Maintenance Request Triage

**Niche:** [[niches/property-management/multifamily-apartment/profile|Multifamily Apartment]]
**Industry:** [[industries/property-management|Property Management]]
**Type:** Fix (Pain Point)
**One-liner:** A 300-unit apartment community receives 80-150 maintenance requests per month ranging from genuine emergencies to cosmetic annoyances — but the PM platform assigns them all equal priority, forcing the property manager to manually read every request and triage by urgency, missing true emergencies buried among routine requests.
**Tags:** #bert #automation #worker-facing #quick-win #cnns

## The Problem
Maintenance requests arrive through AppFolio or Yardi's tenant portal as text descriptions (with optional photos): "Water is coming through my ceiling," "My closet door is off track," "The dishwasher smells bad," "There's a weird noise from the unit above me at night." The property manager or maintenance coordinator reads each request, classifies it by urgency (emergency/urgent/routine/cosmetic), identifies the trade needed (plumbing, electrical, appliance, general), and dispatches the appropriate vendor. For a 300-unit community, this triage takes 30-60 minutes daily. Critical requests ("water through ceiling" = active leak potentially causing structural damage to the unit below) must be identified and responded to within minutes, but they arrive mixed with dozens of routine requests in a flat list with no priority differentiation. During after-hours, the emergency on-call person receives all requests regardless of urgency — being woken at 2 AM for a closet door issue is a major quality-of-life problem for maintenance staff.

## Why It's Still Broken
PM platforms display maintenance requests chronologically, not by priority. The tenant selects a category (plumbing, electrical, other) but not a severity. Some platforms allow the tenant to mark "emergency," but tenants over-use the emergency flag (everything feels urgent when it's your home). No platform analyzes the text description and photo to classify actual urgency. Text classification for maintenance requests is a relatively straightforward NLP problem — the training data (millions of maintenance requests with the property manager's assigned priority) exists within PM platforms but hasn't been used.

## What a Fix Looks Like
An AI triage layer that processes each incoming maintenance request: (1) analyzes the text description using a text classification model to identify keywords and patterns associated with each urgency level — "water," "leak," "flooding," "smoke," "no heat" (in winter) = emergency; "running toilet," "dripping faucet" = urgent; "closet door," "touch-up paint" = routine; (2) if a photo is included, analyzes it for visual urgency indicators — visible water pooling, smoke/fire damage, structural damage, mold; (3) assigns an AI-recommended priority (emergency/urgent/routine/cosmetic) with confidence score; (4) routes emergencies to the on-call person immediately while queuing routine requests for next-business-day review; and (5) de-duplicates — if 3 tenants report "elevator not working," the system creates one work order with 3 reporter references.

## Who Feels the Pain
Property managers who spend 30-60 minutes daily reading and triaging maintenance requests. On-call maintenance staff woken at 2 AM for non-emergency requests because the tenant marked it "urgent." Tenants with genuine emergencies (active leak, no heat in January) whose requests wait in the queue behind routine items because no prioritization exists.

## Impact If Fixed
Reduces daily triage time from 30-60 minutes to 5-10 minutes of reviewing AI-classified priorities. Ensures emergency requests are identified and routed within minutes regardless of request volume. Reduces false emergency after-hours calls by 50-70% through accurate urgency classification. Improves tenant satisfaction for emergency reporters by reducing response time from hours to minutes.
