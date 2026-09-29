# Fix: Nobody in the Chain Knows the Conditions

**Niche:** The Annotation Workforce
**Industry:** [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The platform buys a classifier, the vendor buys labelled data, the supplier employs the people, and nobody at the top of the chain could say anything about how the bottom of it works.
**Tags:** #compliance #evaluation-metrics #confidence-intervals #worker-facing #data-integration #descriptive-statistics
**Contested on:** Whether the people who look at harmful material so a classifier can learn from it are visible to anyone.

## The Problem

A platform procures a content classifier. The vendor's materials describe the model's architecture, its language coverage and its accuracy. They do not describe how the training data was labelled, by whom, where, or under what conditions.

The vendor contracts a labelling supplier. The supplier may subcontract further. Somewhere at the end of that chain, people work through concentrated streams of the worst material online so that the model can learn to detect it.

The platform's procurement process asks about security, about data handling, about uptime and about accuracy. It does not ask who produced the training data or how they were treated, because the question is not on any standard vendor assessment and nobody has thought to add it.

So an organisation with a supply chain labour policy, a modern slavery statement and a vendor code of conduct buys a product whose production involves a workforce it has never asked about, doing work it has never characterised, under conditions nobody in the chain has described.

This is not concealment. It is that the question has not been asked, by anyone, at any point in the chain.

## Why It's Still Broken

**The question is not in any assessment.** Vendor security questionnaires and procurement processes have no section on training data production conditions.

**Each link only sees the next one.** The platform sees the vendor, the vendor sees the supplier, and visibility ends there — which is the standard supply chain problem and it has a standard answer nobody has applied here.

**The workforce is not named.** They do not appear in vendor materials, in supply chain reporting or in any public account, which means there is no group for a policy to attach to.

**Moderation attention did not extend.** The journalism and litigation that made moderation conditions visible did not reach this layer, so no external pressure has been applied.

**Buyers do not know it exists.** Many platform procurement teams have not considered that training a content classifier requires people to view the content.

**Cost pressure runs down the chain.** Each link prices the next, and conditions are where the pressure lands, which is exactly why the visibility matters.

## What a Fix Looks Like

**Add the question to procurement.** How is training data labelled, by whom, where, under what conditions, with what exposure management. Four questions on a vendor assessment that nobody currently asks.

**Ask vendors to describe the chain.** Which suppliers, in which locations, with what subcontracting. This is standard supply chain disclosure applied to a supply chain nobody has mapped.

**Require exposure management as a contractual term.** The platform requires it of the vendor, the vendor of the supplier. This is how moderation conditions were specified and it is the mechanism that reaches through.

**Name the workforce in supply chain reporting.** A platform that reports on its moderation supply chain should report on its annotation supply chain, and most do not know they have one.

**Ask vendors what they know about their own chain.** Some vendors will not be able to answer, which is itself the finding and is what would prompt them to find out.

**Include it in responsible AI statements.** Vendors publishing responsible development commitments should cover the conditions under which their training data was produced, which is a conspicuous absence in most of them.

**Publish something.** The first vendor to describe its annotation supply chain and its exposure practices would be making a claim no competitor makes and would establish an expectation.

## Who Feels the Pain

The annotation workforce, working under conditions nobody at the top of the chain has asked about, in a role nobody has named.

The platform, whose supply chain labour commitments do not reach a workforce it did not know it had.

The vendor, who may genuinely not know how their supplier's supplier operates and has never been asked.

And the industry's credibility on responsible development, which addresses model behaviour extensively and the conditions of the people who made the model possible not at all.

## Impact If Fixed

Four questions added to a vendor assessment is the entire first step, and it would prompt vendors to find out what they currently do not know about their own chain.

Naming the annotation workforce in supply chain reporting is what makes them a group to whom policies can attach, and most platforms do not currently know they have this supply chain.

And a contractual exposure management requirement is the mechanism that reached through the chain for content moderation, is well understood, and has simply never been pointed one layer further down.
