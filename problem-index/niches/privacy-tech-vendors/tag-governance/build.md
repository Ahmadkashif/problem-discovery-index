# Build: Continuous Reconciliation of What Actually Fires

**Niche:** Cookie & Tag Governance
**Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Continuous observation of every third-party request across the real site — authenticated paths included — reconciled against the approved list, the consent declaration and the processor register.
**Tags:** #graph-theory #gradient-boosting #evaluation-metrics #change-point-detection #confidence-intervals #compliance #automation #data-integration
**Contested on:** Whether the tags on the site are the ones that were approved, or whatever has accumulated in the tag manager since anyone last looked.

## The Problem

A cookie scan runs monthly. It crawls the public pages, enumerates cookies and third-party requests, and produces a report. The report is compared informally against the consent banner's vendor list and filed.

Three things are wrong with this. The crawl covers the pages a crawler can reach, which excludes everything behind authentication — the account pages, the checkout, the support flow — and those are where personal data actually moves. The categorisation relies on a database of known tags, which misses new vendors and cannot follow a redirect chain to the party at the end. And the comparison against what was approved is done by a person reading two lists, occasionally.

Meanwhile tags change weekly. A marketing team adds a pixel for a campaign. A product team enables a session recording trial. An agency adds a partner script. Each is a new third party receiving data, each requires consent gating and a register entry, and none of them waits for the monthly scan.

The result is a site whose third-party population is continuously drifting from every artefact that claims to describe it — the consent banner, the processor register and the privacy notice.

## Why Nobody Has Built This

**Authenticated coverage requires test accounts and journey scripting.** Crawling public pages is easy; walking a checkout flow as a logged-in user requires maintained test credentials and scripted journeys that break when the site changes.

**Categorisation is a maintenance business.** Keeping a database of tag vendors current, including new ones and redirect chains, is continuous unglamorous work and is the actual asset.

**Server-side tagging is invisible to browser observation.** The route that is growing fastest is the one browser scanning cannot see, which means any product built purely on browser observation covers a shrinking fraction.

**The finding embarrasses marketing.** Continuous reconciliation produces a list of tags added without approval, which is a list of colleagues' actions, and the privacy team must then raise it.

**Tag governance is bought by web operations.** Their priority is site performance and tag functionality, not the privacy register, so the product is shaped by a buyer with different concerns.

**Nobody reconciles across the three artefacts.** The approved list, the consent banner and the processor register are maintained in different places by different people, so the comparison that would catch everything is nobody's task.

## What to Build

**Observe continuously, not on a schedule.** Real user monitoring or frequent synthetic checks, so a new tag is detected within hours of deployment rather than at the next monthly scan. Change detection is the product; the inventory is the by-product.

**Cover the authenticated and transactional journeys.** Scripted journeys through login, account management, checkout and support, with maintained test accounts. This is where sensitive data moves and where public crawling never reaches, and it is the coverage difference that matters most.

**Follow the chain to the end recipient.** Execute the page and record the full request chain, including tags loaded by other tags, so the report names the party that actually received data rather than the one the organisation deployed.

**Reconcile against all three artefacts.** What fires, against the approved tag list, against the vendors named in the consent banner, and against the processor register. Any discrepancy is a finding, and the three-way comparison catches things no single comparison would.

**Verify gating by behaving like a user who declined.** Decline consent and observe what still fires. This is the enforcement test from [[niches/privacy-tech-vendors/consent-management/profile|🔵 Consent Management]] and it belongs here operationally, because this is where the tags are.

**Detect tags deployed outside the tag manager.** Compare what fires against what the tag manager contains. Directly-injected tags are the most common governance bypass and are trivially detectable this way.

**Extend to server-side.** Observe the server-side tagging configuration and the destinations it forwards to, because the browser view covers less of the picture every year.

**Alert with an owner.** A new tag detected should reach whoever deployed it, from the tag manager's own audit log, rather than arriving as an anonymous finding the privacy team must investigate.

## Target Customer

Privacy counsel and web operations jointly — the finding matters to the first and the remediation is performed by the second, and the product only works if both are in it.

Organisations with large marketing technology estates and frequent campaigns, where drift is fastest and the register is furthest from reality.

The consent platforms, for whom continuous reconciliation is the natural extension of the scanning they already do monthly.

## Impact If Built

Drift is detected in hours rather than at the next scan, which is the difference between governance and periodic archaeology.

Covering authenticated and checkout journeys addresses the coverage gap that matters most, since the pages a crawler cannot reach are the pages where personal data actually moves.

And the three-way reconciliation against the approved list, the banner and the register is the check that would keep all three artefacts honest — which is currently done by nobody because it belongs to three different people.
