# Fix: The Scan Crawled the Homepage

**Niche:** Cookie & Tag Governance
**Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The cookie scan covers the pages a crawler can reach, and the pages where personal data actually moves are behind a login.
**Tags:** #evaluation-metrics #confidence-intervals #compliance #automation #worker-facing #change-point-detection
**Contested on:** Whether the tags on the site are the ones that were approved, or whatever has accumulated in the tag manager since anyone last looked.

## The Problem

The scanner crawls the site. It follows links from the homepage, covers the marketing pages, the blog, the pricing page and the public documentation, and produces an inventory of cookies and third-party requests.

It does not log in. So it never sees the account page, the order history, the support conversation, the checkout flow or the settings screen. Those pages load their own tags — frequently more of them, because personalisation, analytics and support widgets cluster where users are identified — and they carry personal data in a way the marketing pages do not.

The inventory is therefore a description of the least sensitive part of the site, presented as a description of the site. The consent banner's vendor list is built from it. The processor register inherits it. The privacy notice describes it.

Nobody is misleading anyone. The scanner does what scanners do, the limitation is known to the people running it, and the output is used downstream by people who do not know. The gap persists because logging a scanner in requires maintained test credentials, scripted journeys and someone to keep them working — which is a small ongoing engineering commitment that no one has made.

## Why It's Still Broken

**Authenticated scanning needs maintenance.** Test accounts expire, flows change, multi-factor authentication interferes. It is a small, continuous engineering cost with no owner.

**Public crawling produces a plausible result.** The scan returns a substantial list of cookies and tags, which looks like coverage, so nobody asks what it missed.

**Nobody measures coverage.** The scan reports what it found and not what fraction of the site it visited. Without that number the limitation is invisible.

**The checkout is the most sensitive and the most protected.** Nobody wants a scanner walking a payment flow, which is understandable and means the highest-risk page is the least examined.

**Conditional tags are missed anyway.** Some tags fire only on certain user segments, geographies or behaviours. A single scanner in one location sees one variant.

**The privacy team cannot fix it.** They do not own the site, the test accounts or the scanning schedule, and the people who do have other priorities.

## What a Fix Looks Like

**Script the authenticated journeys.** Login, account, settings, checkout, support. Maintained test credentials and a handful of scripted paths covering where real users spend their time. This is the fix and it is a day of engineering plus small ongoing maintenance.

**Report coverage with every scan.** Which pages and journeys were visited, and which parts of the site were not. A scan that states its own scope stops being read as a description of the whole site.

**Use real user monitoring where it exists.** If the organisation already captures real sessions for performance, that data covers every journey every real user takes, in every geography, under every condition — which is strictly better than any crawler and is already being collected.

**Scan under all three consent states.** Accept, reject and no decision, compared. The reject case is the one that reveals enforcement failures and the one nobody runs.

**Scan from multiple locations.** Tag behaviour varies by geography, both because vendors differ by market and because consent regimes do. A single-location scan misses this entirely.

**Give it an owner and a cadence.** Someone in web operations responsible for the journey scripts and the schedule, because a scanning programme with no owner degrades to whatever the default crawler does.

## Who Feels the Pain

The privacy team, whose register and consent configuration are built on an inventory of the marketing site.

Users on the authenticated pages, whose data reaches third parties that appear in no artefact the organisation maintains.

The organisation, whose consent banner names a vendor list derived from the least sensitive part of its estate, which is precisely the kind of gap enforcement decisions in this area have concerned.

And whoever eventually investigates, who will find that the checkout flow loaded three tags nobody had ever recorded.

## Impact If Fixed

Scripting the authenticated journeys is a small engineering task that closes the largest coverage gap in tag governance, and it is the single highest-return action available in this niche.

Reporting coverage with every scan converts an artefact that implies completeness into one that declares its scope, which stops the downstream misuse immediately.

And scanning under the reject state would test enforcement rather than inventory, which is the thing the whole consent apparatus is supposed to deliver and the thing nobody currently checks.
