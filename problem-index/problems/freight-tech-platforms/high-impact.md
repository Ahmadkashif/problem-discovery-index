# Carrier Identity and Double Brokering Fraud

**Industry:** [[freight-tech-platforms|Freight Tech Platforms]]
**Type:** High Impact
**One-liner:** Establish who is actually hauling a load before it moves, by treating carrier identity as a network problem rather than a document check — because the fraud is visible in the relationships between parties and invisible in any single carrier's paperwork.
**Tags:** #graph-neural-networks #gradient-boosting #dbscan #feature-engineering #evaluation-metrics #confidence-intervals #change-point-detection #compliance #revenue-impact

## The Problem
A broker books a load with a carrier. The carrier's authority is active, its insurance certificate is current, its safety rating is acceptable. The load is then re-brokered to a second carrier the shipper never approved, at a lower rate, with the difference pocketed. Sometimes the second carrier is legitimate and the freight arrives; the broker discovers the arrangement only when two invoices appear or when the carrier of record does not get paid. Sometimes the freight is stolen outright.

Beneath that sits a worse version: the carrier the broker vetted does not exist in the form presented. A dormant authority with a clean history is taken over — its phone number, email and remittance details quietly changed — and used to book freight under a reputation somebody else earned. Every document checks out because the documents belong to a real carrier.

Losses across the industry run into the hundreds of millions annually and have risen sharply. The vetting infrastructure was designed for a world where an MC number, a certificate of insurance and a phone call to a listed number were sufficient. All three are now trivially spoofable.

The information that would catch it exists, and it is relational. The same phone number appearing across four unrelated authorities. A remittance detail changing three days before a high-value booking. A dormant authority suddenly booking freight in a lane it never served, at a rate below market. A cluster of carriers sharing an address, a certificate issuer and a booking pattern. None of that is visible in any one carrier's record and all of it is visible in the graph.

## Why It's Unsolved
Vetting is performed per carrier as a document check, which is a shape the fraud has adapted to. Each broker sees only its own interactions, so a carrier that has defrauded eleven other brokers presents to the twelfth as new.

Data sharing between brokers is the obvious answer and is genuinely hard. Brokers compete on carrier relationships and treat their carrier lists as commercial assets. There are also real defamation and antitrust concerns in circulating negative assessments of named businesses, which has made everyone cautious about exactly the sharing that would work.

The public data is thin and slow. Federal authority and insurance records are the foundation of vetting and they update on their own schedule, do not reflect operational control, and say nothing about who is answering the phone today.

And the fraud adapts quickly. It is committed by organised operators who test defences continuously, which means any static rule set is a temporary measure and a learned, relational approach is the only thing that keeps pace.

## What a Solution Looks Like
Carrier identity modelled as a graph: authorities, people, phone numbers, email domains, addresses, remittance accounts, insurance certificates, equipment and booking behaviour, connected by observed co-occurrence across the platform's whole broker base. Fraud shows up as structure — shared attributes across supposedly unrelated carriers, sudden changes in the attributes attached to an established identity, and booking patterns inconsistent with a carrier's own history.

Change detection on established identities is the sharpest single signal. A carrier's contact and payment details are stable for years; a change immediately preceding an unusual booking is the pattern behind most authority takeover, and it is trivially observable to whoever holds the record.

The output must be a risk assessment routed to a human with the specific evidence attached, not a blocklist. The consequences of being wrong fall on a small business that may be entirely legitimate, and the legal exposure of an automated denial is real.

## Impact If Solved
Freight fraud is the industry's most acute current problem and the reason shippers are pulling freight back from brokers toward asset carriers. A vetting layer that works on relationships rather than documents protects cargo, protects the legitimate carriers whose identities are being stolen, and is the only defensible product in a category where everyone else is reselling the same public records.
