# Lineage: Customer Data Platforms

**Industry:** [[industries/customer-data-platforms|Customer Data Platforms]]
**Wave:** [[series/eras/wave-07-big-data|7 — Big Data]]
**The tool:** analytics.js — Segment.io's open-source JavaScript library that put one `identify` / `track` API in front of many analytics services and forwarded each call to all of them, shown on Hacker News on 12 December 2012
**Builder:** Segment.io
**Builder in vault:** [[industries/customer-data-platforms|Customer Data Platforms]]
**Verification:** partial — see Sources

## The Problem That Came First

By 2012 a web product did not have one analytics tool; it had several. Google Analytics for traffic, Mixpanel or KISSmetrics for funnels, Customer.io for lifecycle email, something else for support. Each came with its own snippet, its own call syntax and its own idea of what a user and an event were.

So every new tool meant another integration written by an engineer, and every event had to be instrumented once per destination. **The marginal cost of trying a new marketing tool was an engineering ticket**, and the same fact — "this person bought something" — was recorded several times, slightly differently, in systems that never compared notes.

Nobody owned the question of what an event was called. Each vendor's snippet answered it locally.

## What Got Built

A wrapper with two verbs.

analytics.js exposed `analytics.identify(userId, traits)` to say who someone is and `analytics.track(event, properties)` to say what they did — the Show HN example was `analytics.track('Purchased an Item', { price : 39.95, shippingMethod : '2-day' })`. Configure the destinations once, and every call was translated into each service's own format and sent to all of them. The GitHub repository was created on 18 June 2012 and released under the MIT licence; the Hacker News launch, *"Analytics.js – The analytics API you've always wanted,"* was posted by Ian Storm Taylor on 12 December 2012 and drew 326 points.

The translation was imperfect from day one, and the thread says so. Mixpanel accepted arbitrary JSON properties; Google Analytics wanted category and label fields; and Taylor noted that the identify call "never gets sent to GA" because of Google's terms of service. The library chose one vocabulary and mapped it outward as best it could.

## Who Built It, And Why Them

Segment.io, a Y Combinator company from the Summer 2011 batch, based in San Francisco; YC's directory lists Ilya Volodarsky as founder, and the launch thread was run by Taylor.

The launch discussion explains the business case in the builders' own terms: teams kept having to integrate several analytics services into the same product and kept writing a custom wrapper each time. A small team shipping web products hits that tax on every project, and — unlike any single analytics vendor — has no stake in which destination wins. **A neutral router is only credible from someone who sells none of the destinations.** That neutrality is what later let Segment sell the router itself: collect once, send anywhere. YC's directory still describes the company's product as event tracking "through a single API rather than managing separate integrations for each tool"; Twilio bought the company for $3.2 billion in October 2020.

## What It Cost

The router made the event name the unit of truth and then left it unguarded.

`track('Purchased an Item')` accepts any string. Because instrumenting became cheap, every product team could add events, and nothing in the library checked that "Purchased an Item" and "Order Completed" were the same act. The destinations got fed faster; the vocabulary stopped being anyone's job. `identify` inherited the same looseness — whatever userId the caller passed became the person, and joining that id to an anonymous visitor was left for later systems to guess.

## What You Still Touch

The tracking plan spreadsheet nobody updates, and the data engineer who learns about a renamed event after it ships, are the bill for making `track` free. The identity graph a privacy operator has to delete from is what grew on top of `identify`.

- [[problems/customer-data-platforms/low-impact-2|🟡 Event Schema Governance]] — the unguarded event name
- [[problems/customer-data-platforms/worker-life-1|🟢 The Engineer Whose Tracking Plan Nobody Reads]]
- [[problems/customer-data-platforms/high-impact|🔴 Identity Resolution Is a Guess Nobody Measures]]
- [[niches/customer-data-platforms/event-stream-governance/profile|Event Stream Governance]]
- [[niches/customer-data-platforms/packaged-pipeline-and-activation/profile|Packaged Pipeline & Activation]]

**Sources:** GitHub, `segmentio/analytics.js` README and repository metadata via the GitHub API (created 18 June 2012; MIT licence; archived 28 April 2022, superseded by analytics-next); Hacker News item 4912076, *Show HN: Analytics.js*, posted by ianstormtaylor 12 Dec 2012, 326 points (Algolia HN API), including the Mixpanel/GA mapping discussion and the "never gets sent to GA" comment; Y Combinator company directory, *Segment* (founded 2011, Summer 2011 batch, San Francisco, Ilya Volodarsky listed); Wikipedia, *Twilio* (Segment acquisition, October 2020, $3.2B); this vault's `history/customer-data-platforms.md` (vault material, not independent corroboration). WebSearch was unavailable this session (budget exhausted); research was by WebFetch only. ⚠️ **Not established:** the full co-founder list and the company's pre-analytics.js product — commonly told as an MIT classroom tool that pivoted, but Wikipedia had no Segment article reachable and I could not confirm it from a primary source; when "Segment.io" was renamed "Segment"; and whether analytics.js was written first for the team's own product or as a standalone project.
