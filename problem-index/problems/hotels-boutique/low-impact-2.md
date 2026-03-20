# Guest Communication & Pre-Arrival Personalization

**Industry:** [[hotels-boutique|Boutique Hotels]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic CRM and messaging tools exist but can't replicate the boutique hotel's signature touch — personalized, context-aware guest communication that drives upsells and loyalty without sounding automated.
**Tags:** #large-language-models #transfer-learning #attention-mechanisms #transformers #entropy-cross-entropy-kl-divergence #automation

## The Problem
Boutique hotels differentiate on personal service, yet guest communication is fragmented across 4-5 channels: OTA messaging (Booking.com and Expedia each have their own portals), email, SMS, WhatsApp, and sometimes Instagram DMs. A guest who books through Booking.com asks about parking via the OTA app, then emails about a dinner reservation, then texts on arrival day about early check-in. No single thread exists, so the front desk agent pieces together context from memory or by searching multiple systems. Pre-arrival upsell opportunities (room upgrades, airport transfers, spa packages, restaurant reservations) are handled inconsistently — some guests get a templated email, others get nothing, and the personalization that boutique guests expect is absent.

## What Already Exists
Guest messaging platforms (Akia, Whistle by Cloudbeds, Duve) unify channels and offer template-based automation. CRM tools (Revinate, Guestfolio) store guest preferences and trigger email campaigns. These tools treat all hotels identically — a 200-room airport Hilton and a 25-room design hotel in Asheville get the same templates and segmentation logic. The tone, timing, and content of boutique guest communication requires a fundamentally different approach: fewer guests, deeper personalization, and a voice that reflects the property's specific character.

## The Customisation Gap
A boutique-specific communication layer needs to ingest the property's brand voice (from its website copy, past guest interactions, and owner guidance), guest history (previous stays, stated preferences, booking notes), and real-time context (weather at destination, local events during stay dates, restaurant availability) to generate pre-arrival messages that feel handcrafted. The LLM must be fine-tuned or prompted to match the specific property's tone — a surf lodge in Montauk communicates differently than a historic inn in Charleston. It must also respect OTA messaging policies (Booking.com restricts promotional content in their channel) and route responses to the correct platform. The gap is not "can an LLM write a hotel email" — it's "can it write as *this* hotel, to *this* guest, about *this* stay."

## Impact If Solved
Properties using personalized pre-arrival communication see 15-30% upsell conversion rates on ancillary services (vs. 3-5% for generic templates), adding $8K-$25K annually in ancillary revenue while reducing front desk time spent on repetitive guest inquiries by 5-8 hours per week.
