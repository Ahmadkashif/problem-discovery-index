# Link Monitoring Built for Websites

**Niche:** [[niches/libraries-and-archives/academic-unified-resource-management/profile|Academic Unified Resource Management]]
**Industry:** [[industries/libraries-and-archives|Libraries & Archives]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Uptime and broken-link monitors check whether a page loads; a library needs to know whether a licensed article loads for an authenticated student off campus.
**Tags:** #feature-engineering #evaluation-metrics #data-integration #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to keep one record of what a university library has paid for, is entitled to and can actually deliver across print and every publisher platform, and whoever keeps entitlements, links and access correct for the most publishers with the least staff effort takes the platform renewal.

## The Problem
Broken access is found by patrons who email or give up. Libraries have no routine test of whether the full text behind each discovery link actually opens.

## What Already Exists
Website monitoring and broken-link checkers (Pingdom, Siteimprove, Screaming Frog) and synthetic transaction testing in application performance tools; OCLC's EZproxy logs.

## The Customization Gap
The test has to authenticate as the library — through EZproxy or OpenAthens, from the campus IP range — follow an OpenURL through the link resolver, and decide whether the landing page is full text, an abstract or a paywall, which differs by publisher platform. It has to sample titles weighted by usage and licence value, and write failures back to the knowledge base or a ticket queue. None of that exists in a website monitor.

## Target Customer
Electronic resources librarians and discovery teams at universities with large licensed collections.

## Impact If Solved
A nightly sampled access test catches platform changes and lapsed activations within a day rather than when a dissertation student hits a paywall.
