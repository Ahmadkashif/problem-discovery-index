# Email & SMS Marketing Platforms

## Profile
**Category:** Adtech & Martech
**Market Size:** ~$9B US for messaging platforms and the sending infrastructure beneath them; Klaviyo, Braze, Attentive, Iterable, Customer.io, Mailchimp, Postscript and Salesforce Marketing Cloud take most of the branded spend
**Tech Maturity:** High throughput, blind at the decisive moment. These platforms send billions of messages, run sophisticated segmentation and journey tooling, and cannot observe the one thing that determines whether any of it works — whether the message reached the inbox or was filtered by a carrier. The metric the industry organises around, the open rate, was largely destroyed as a signal by Apple's Mail Privacy Protection in 2021 and remains on every dashboard.
**Workforce:** Deliverability specialists, lifecycle and CRM marketers, platform and infrastructure engineers, compliance and consent teams, solutions architects and onboarding consultants

## Key Pain Themes
Delivery is not placement. A message accepted by a mailbox provider may land in the inbox, in promotions, in spam, or be silently dropped; the provider does not say which, and the platform reports "delivered" for all of them. Carriers filter SMS on opaque criteria and return an error code that means several different things. So the entire optimisation apparatus — subject lines, send times, cadence, content — is tuned against signals that no longer measure what they used to, for an outcome nobody can see.

The signal collapse is worse than generally acknowledged. Mail Privacy Protection pre-fetches images for a large share of the email population, which means open rates are inflated by an amount that varies by audience composition and cannot be recovered. Yet opens still drive engagement-based segmentation, sunset policies, send-time models and reported campaign performance across the industry.

The third theme is compliance with real teeth. The 2024 Gmail and Yahoo bulk sender requirements made authentication, one-click unsubscribe and a hard spam-complaint threshold enforceable conditions of delivery. On SMS, TCPA litigation is an active and expensive risk, consent provenance is frequently poor, and A2P 10DLC registration sits between every brand and the carriers. These are not policy questions; they are the difference between a channel working and not.

## Current Tech Landscape
Klaviyo dominates direct-to-consumer ecommerce; Braze and Iterable lead cross-channel lifecycle at enterprise; Attentive and Postscript own SMS in retail; Customer.io and Mailchimp hold the mid-market and long tail. Sending infrastructure runs on SendGrid, Mailgun, Amazon SES and Twilio. Deliverability monitoring is a specialist adjacent market — Validity, Everest, Google Postmaster Tools, seed-list vendors — that exists precisely because the platforms cannot see placement. Consent and preference management is fragmented across OneTrust, platform-native tools and homegrown systems.

## Problems
- [[problems/email-sms-marketing-platforms/high-impact|🔴 High Impact: Nobody Tells You Whether the Message Arrived]]
- [[problems/email-sms-marketing-platforms/low-impact-1|🟡 Low Impact: Send Timing and Frequency Optimisation]]
- [[problems/email-sms-marketing-platforms/low-impact-2|🟡 Low Impact: Lifecycle Flows Built by Hand]]
- [[problems/email-sms-marketing-platforms/worker-life-1|🟢 Worker Life: The Lifecycle Marketer and the Flow That Broke Silently]]
- [[problems/email-sms-marketing-platforms/worker-life-2|🟢 Worker Life: The Deliverability Specialist Arguing With a Postmaster]]
- [[problems/email-sms-marketing-platforms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/email-sms-marketing-platforms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
These platforms hold a rare combination: the message, the recipient, the engagement, and — in the ecommerce case — the resulting order, all in one system. That is a genuinely closed loop and it is used mostly to report revenue attributed on a click within a window. What it is not used for is the two questions that actually govern the channel: whether the message was placed, and what sending it cost in the recipient's long-run willingness to hear from the brand. The first is an inference problem that the cross-brand corpus makes tractable for a platform and impossible for any single sender. The second is a causal problem where the revenue arrives today and the unsubscribe arrives over a year, and the incentive of a platform paid by volume points away from asking it.
