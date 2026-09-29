# Third-Party & Processor Register

**Parent Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Category:** Low Digitized
**Contested on:** Whether the list of parties receiving personal data is derived from what actually leaves the organisation, or from what somebody remembered to register.

## Profile

**Market Size:** ~$700M
**Share of Parent Industry:** ~10%
**Digital Adoption:** Very low — a spreadsheet of registered vendors
**Target Buyer:** Privacy counsel, vendor management, procurement
**Automation Potential:** High — the recipients are observable

## What Makes This a Distinct Niche

The processor register is the list of every party processing personal data on the organisation's behalf, with the contract, the transfer mechanism and the subprocessors behind each. It is a regulatory requirement, it is the basis for transfer assessments, and it is where a deletion request must be forwarded.

It lists the vendors somebody remembered to register. Procurement catches the ones that went through procurement. Privacy review catches the ones someone raised. And the tags on the website send data to companies nobody in the organisation has heard of, added by a marketing team through a tag manager, firing redirect chains to parties several steps removed from anyone's approval.

The gap is structural rather than careless. Registration depends on someone recognising that a tool processes personal data and initiating a process. A designer signing up for a free analytics trial, a marketer adding a pixel for a campaign, an engineer enabling a third-party integration — each is a processor relationship and none goes through a register.

Every competitor is fighting over the same question: whether the register can be built from observation instead of memory. The answer is largely yes, using the data flow observation the category has not adopted, and the finding it would produce is a list of unregistered parties receiving personal data.

## Current Tools & Gaps

Vendor registers maintained in privacy platforms, populated by intake forms and procurement integration. Data processing agreement repositories. Transfer impact assessment workflow. Subprocessor lists collected from vendors, usually as a link to their published page. Cookie scanners identifying browser-side third parties.

The gaps are consistent with the rest of this category. Registration is manual and initiated by a person, so it misses everything nobody thought to register. Cookie scanners find browser-side parties and nothing finds server-side ones, which is where data increasingly goes. Subprocessor lists are collected once and not monitored, though vendors change them continuously. Transfer mechanisms are recorded from the vendor's own statement rather than verified against where processing actually occurs. And nothing reconciles the register against observed recipients, which is the check that would make it meaningful.

## Problems

- [[niches/privacy-tech-vendors/processor-register/build|🔨 Build: The Register Built From Observation]]
- [[niches/privacy-tech-vendors/processor-register/buy|🛒 Buy: SaaS Discovery, Read as a Processor Inventory]]
- [[niches/privacy-tech-vendors/processor-register/fix|🔧 Fix: The Subprocessor List Was Checked Once]]
