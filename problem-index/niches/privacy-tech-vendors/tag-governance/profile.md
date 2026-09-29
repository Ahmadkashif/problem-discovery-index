# Cookie & Tag Governance

**Parent Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Category:** Highly Automatable
**Contested on:** Whether the tags on the site are the ones that were approved, or whatever has accumulated in the tag manager since anyone last looked.

## Profile

**Market Size:** ~$420M
**Share of Parent Industry:** ~6%
**Digital Adoption:** Moderate — scanning and blocking
**Target Buyer:** Web and marketing operations, privacy counsel
**Automation Potential:** Very high — scanning, categorising and gating are mechanical

## What Makes This a Distinct Niche

The website loads third-party scripts. Each one may set cookies, read identifiers, and send data to a company the organisation may or may not have approved. Governing them — scanning the site, categorising what is found, gating each tag behind the relevant consent, and keeping the register current — is mechanical work with well-understood tooling.

The contest is drift. Tags accumulate. A campaign adds a pixel, a trial adds a session recorder, a partner integration adds a script, and each is added through the tag manager by someone with access and a deadline. Some are removed when the campaign ends and most are not. Redirect chains load further parties nobody chose at all.

So the site's actual third-party population diverges continuously from the approved list, the consent banner names a set of vendors that no longer matches what fires, and the privacy team's picture is a scan from whenever the last one ran. It is the most automatable niche in the industry and the one where the automation is most obviously not keeping up with the rate of change.

## Current Tools & Gaps

Cookie scanners crawling the site and enumerating cookies and third-party requests. Consent platforms gating tags through the tag manager. Tag management systems with version control and approval workflow. Some continuous monitoring offerings. Categorisation databases mapping known tags to purposes and vendors.

The gaps are about coverage and enforcement. Scans crawl a sample of pages and miss authenticated areas, checkout flows and conditional paths, which is where the most sensitive data moves. Categorisation databases lag new vendors and miss redirect chains entirely. Server-side tagging is outside the scanner's view and is growing precisely because of browser restrictions. Gating depends on tags being deployed through the tag manager, so anything added directly bypasses it. And nothing reconciles what actually fires against what the consent banner declares, which is the check that would matter most.

## Problems

- [[niches/privacy-tech-vendors/tag-governance/build|🔨 Build: Continuous Reconciliation of What Actually Fires]]
- [[niches/privacy-tech-vendors/tag-governance/buy|🛒 Buy: Synthetic Monitoring for the Privacy Question]]
- [[niches/privacy-tech-vendors/tag-governance/fix|🔧 Fix: The Scan Crawled the Homepage]]
