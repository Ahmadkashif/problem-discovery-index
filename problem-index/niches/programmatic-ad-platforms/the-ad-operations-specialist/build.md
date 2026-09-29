# Three Numbers, Same Impressions

**Niche:** [[niches/programmatic-ad-platforms/the-ad-operations-specialist/profile|The Ad Operations Specialist]]
**Industry:** [[industries/programmatic-ad-platforms|Programmatic Ad Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Three systems count the same impressions and report three different numbers, and an ad operations specialist spends the month explaining a gap that has the same six causes every time.
**Tags:** #worker-facing #data-integration #descriptive-statistics #evaluation-metrics #workflow-orchestration #automation #quick-win #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to explain the discrepancy between three systems automatically instead of having a person derive it every month — and whoever does that removes the most repeated unproductive task in the category.

## The Problem
The platform says eleven million impressions. The verification vendor says ten point four. The publisher's own server says ten point nine. Somebody has to explain the difference to a client who wants to know which number to pay against. The specialist pulls three exports, aligns time zones, checks counting methodology, looks for a tag that fired late, finds a geography filter applied in one system and not another, and produces an explanation. Next month, same campaign, same exercise. The causes are the same six every time, they are diagnosable from data the systems already emit, and a skilled person derives them by hand indefinitely.

## Why Nobody Has Built This
Each vendor reports its own numbers correctly by its own definition and has no incentive to build a tool that highlights disagreement with others. Discrepancy is contractually tolerated up to a threshold, which converts a solvable problem into an accepted condition — this normalisation is why nothing changes. The work is invisible, performed by people with no product budget. And the institutional knowledge lives in the heads of specialists who are not asked to write it down.

## What to Build
Diagnose the discrepancy automatically. Ingest the counts from every system and align them on definitions, time zones, counting points and filters, which is the mechanical majority of the work and is the whole of what a specialist does by hand. Attribute the remaining gap to specific causes with evidence — late-firing tags, client-side versus server-side counting, viewability filtering, geography and invalid-traffic exclusions, time zone offsets, deduplication differences — since these are enumerable and each leaves a distinguishable signature. Produce the explanation as a document the specialist can send, which is the deliverable and is what turns three days into ten minutes. Alert on discrepancies as they emerge rather than at month end, which is when they can still be fixed. Prevent at trafficking time by checking tag placement, counting configuration and definition alignment before the campaign runs, since most recurring discrepancies originate in setup and are cheapest to fix there. Track cause frequency by partner and campaign type, which turns a monthly annoyance into an addressable pattern and is the fix note's subject. Maintain a definition registry across vendors, because the underlying problem is that nobody has written down what each system counts. Flag the discrepancies that indicate a real problem rather than a definitional one, as they look identical and only one of them matters. Support the commercial conversation with evidence, since these gaps become invoice disputes. And measure the hours returned, because that is the case for the tool and for the profession.

## Target Customer
Ad operations teams at agencies, publishers and advertisers, the specialists themselves, and the platforms whose support queues carry the same question repeatedly.

## Impact If Built
The six causes are known, enumerable and diagnosable from data the systems already emit, and a skilled person derives them by hand every month. Automated attribution with evidence turns three days into ten minutes, and trafficking-time checks prevent most of them entirely.
