# The Envelope That Looks Exactly Like Phishing

**Niche:** [[niches/esignature-document-workflow/signer-side-experience/profile|The Signer Side]]
**Industry:** [[industries/esignature-document-workflow|E-Signature & Document Workflow]]
**Type:** Fix (Pain Point)
**One-liner:** Every organisation trains its staff to distrust unexpected emails asking them to click a link and enter details, and that is a precise description of a signature request.
**Tags:** #descriptive-statistics #hypothesis-testing #evaluation-metrics #confidence-intervals #logistic-regression #compliance #quick-win #automation
**Contested on:** Every serious competitor that takes the counterparty seriously is fighting to make the person receiving an agreement able to understand it, trust it and ask about it without leaving the envelope — and whoever does that raises completion, which is the only number the sender buys on.

## The Problem
A signature request arrives from a third-party domain the recipient has never seen, with a generic subject line, asking them to click a link to view a document and provide information. Security awareness training, correctly, has taught them that this is what an attack looks like. Some delete it. Some report it to their security team, which blocks the domain, which means nobody at that company can receive an envelope from that platform again. Some forward it to a colleague to ask if it is real. The genuinely dangerous outcome is the opposite one: because these emails are normal, real phishing that imitates them succeeds, and the category has trained an entire population to click links in exactly this shape of message.

## Why It's Still Broken
The delivery pattern was set when the category was new and nobody had been trained to distrust it, and it has not been revisited. Platforms measure open rates rather than non-opens attributable to suspicion, so the cost is invisible in their own data. Verification would require the sender to do something in advance — a domain arrangement, an out-of-band notice — which adds friction to the sender's flow, and the sender is the customer. And the security-awareness contradiction sits between two industries that do not talk to each other.

## What a Fix Looks Like
Make the request verifiable without clicking. Put the specific, checkable facts in the message body — sender organisation, named individual, the agreement's subject, the reference the signer already has — so a recipient can confirm it against something they know rather than against a logo. Support proper sender domain authentication and encourage sending from the sender's own domain where the platform supports it, which removes the unfamiliar-domain problem at its source. Provide an independent verification route: a page where a recipient can enter a code from the message and confirm the request exists, which is the pattern banks use and which costs nothing. Give senders a pre-notification path so the recipient is expecting it, which is the single most effective intervention and is currently an informal habit rather than a feature. Handle the security-team case explicitly, with documentation and allowlisting guidance, since a blocked domain is a silent and total failure for every future envelope to that organisation. And measure it — non-open rates by recipient domain, and the correlation with domains that have security filtering — which would show platforms a cost they currently cannot see.

## Who Feels the Pain
Recipients trained to distrust exactly this message; senders whose envelopes fail for reasons that never appear in any report; security teams fielding reports about legitimate mail; and everyone affected by attackers imitating a pattern the category normalised.

## Impact If Fixed
Verifiable content, sender-domain authentication and pre-notification are all straightforward and address the largest silent failure mode in the funnel. The security-awareness contradiction is the more serious issue, because the category has spent two decades teaching people to click links in unexpected emails.
