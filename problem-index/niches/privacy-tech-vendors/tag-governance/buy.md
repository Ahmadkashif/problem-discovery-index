# Buy: Synthetic Monitoring for the Privacy Question

**Niche:** Cookie & Tag Governance
**Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Synthetic monitoring already walks authenticated user journeys continuously and records every network request, for performance, and nobody reads the same recordings for who received the data.
**Tags:** #evaluation-metrics #change-point-detection #confidence-intervals #graph-theory #data-integration #automation #compliance
**Contested on:** Whether the tags on the site are the ones that were approved, or whatever has accumulated in the tag manager since anyone last looked.

## The Problem

Walking a website's real user journeys continuously, from many locations, in a real browser, recording every network request with timing and headers, is a solved and widely deployed capability. Synthetic monitoring does exactly this, for performance and availability, at most organisations of any size — including the authenticated journeys, with maintained test accounts, because checkout availability is a revenue concern.

Those recordings contain the complete answer to the privacy question: every third-party request, on every journey, including the ones behind login, continuously, with change over time.

They are read for latency. The privacy team runs a separate monthly crawler over the public pages and gets a worse answer to a related question, because the two capabilities live in different teams with different vendors and nobody has connected them.

## What Already Exists

Synthetic monitoring: Datadog Synthetics, Catchpoint, Dynatrace, New Relic, Checkly and the monitoring suites generally — scripted browser journeys including authentication, executed continuously from multiple locations, with full request capture.

Real user monitoring: the same vendors capturing actual user sessions with full resource timing, which observes what real users' browsers actually load rather than what a test account does.

Session replay: products recording user sessions in detail, with their own privacy considerations, and complete visibility of third-party requests.

Cookie scanning: the privacy-specific crawlers run by consent platforms and dedicated scanners, covering public pages periodically.

Tag management: the deployment layer, with audit logs recording who deployed what and when.

## The Customization Gap

**The recordings are analysed for the wrong thing.** Synthetic and real user monitoring capture every request and surface latency. Extracting the third-party privacy view — who received data, what identifiers were sent, which cookies were set — is a different analysis over data already collected.

**No vendor attribution.** Monitoring reports domains. Privacy needs the company, its jurisdiction and its register status, which is the attribution registry problem again.

**Cookie and identifier detail is not retained.** Monitoring records requests and does not generally analyse cookies set or identifiers in query strings, which is where the privacy substance sits.

**Consent state is not a test dimension.** A privacy check needs journeys executed under accept, reject and no-decision states, and compared. Synthetic monitoring has no concept of consent variants.

**Real user monitoring sees what synthetics cannot.** Actual users experience geographic and personalised tag variations that a test account does not. It is the better data source and is used exclusively for performance.

**The buyer is engineering.** Monitoring is bought by engineering for reliability. The privacy analysis would need to be surfaced to a different function, which is why the connection has not been made.

## Target Customer

The monitoring vendors — Datadog, Dynatrace, Catchpoint — for whom a privacy view over data they already collect is a new buyer inside existing accounts and requires no new instrumentation.

The consent platforms, who should be consuming monitoring data rather than running their own inferior crawlers.

Web operations as the internal bridge, since they typically own both the monitoring and the tag manager and are the only people positioned to notice that one answers the other's question.

## Impact If Solved

The authenticated coverage problem disappears. Synthetic monitoring already walks logged-in journeys with maintained credentials, which is the exact capability privacy scanning lacks and finds hardest to build.

Real user monitoring would give a far better picture than any crawler, because it observes what actual users' browsers load rather than what a test account in one location does.

And continuous observation replaces the monthly scan with data already being collected, which makes this one of the cheapest large improvements available in the category.
