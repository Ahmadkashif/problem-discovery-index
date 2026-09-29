# A Worker-Owned Record Employers Will Accept

**Niche:** [[niches/construction-tech-platforms/craft-workforce-platforms/profile|Craft Workforce Platforms]]
**Industry:** [[industries/construction-tech-platforms|Construction Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A skilled tradesperson's hours, certifications, safety record and demonstrated skills are scattered across every employer they have ever had, and the worker — the only party present for all of it — is the one party who holds none of it.
**Tags:** #graph-theory #evaluation-metrics #confidence-intervals #compliance #data-integration #workflow-orchestration #worker-facing #automation
**Contested on:** Every serious competitor in craft workforce software is fighting to give a worker a portable, verified record of their own hours, certifications, skills and safety history that follows them between employers — and whoever makes that record trusted by employers takes the market.

## The Problem
A journeyman electrician has worked for six contractors in eight years. Each holds a fragment: hours worked, the certifications on file at the time, the site orientations completed, the equipment they were signed off on, and a foreman's recollection of what they were good at. When the electrician applies to a seventh contractor, none of it transfers. They are asked to produce cards, re-verify credentials, complete orientations they have completed before, and describe their experience verbally. Advancement toward higher classification depends on documented hours held by a training fund that a worker moving between union and non-union work may have gaps with. The worker's career record is a thing other people own pieces of.

## Why Nobody Has Built This
The payer problem is the whole obstacle. Every product in this space is sold to employers, and an employer's interest in a worker's portable record is at best neutral — portability makes the worker more mobile. Training funds and apprenticeship programmes have a genuine interest but operate regionally with their own systems and limited technology budgets. And the hard part is not storage but acceptance: a record is worthless unless the next employer trusts it, which requires the issuing parties to attest in a verifiable way and requires enough employers to accept the format that it is worth a worker maintaining. That is a network problem, and network problems do not get built by a vendor selling seats.

## What to Build
A worker-held credential record where every entry is an attestation from an identifiable issuer — hours attested by the employer who paid them, certifications by the issuing body, orientations by the site, skill sign-offs by a named supervisor — cryptographically verifiable and checkable without contacting the issuer. The worker controls disclosure and shares a scoped view with a prospective employer. Employer-side verification must be trivially fast, because the adoption path runs through hiring managers who will not add a step. Entry costs the employer nothing beyond what they already record, which means the product has to consume existing payroll and workforce systems rather than ask for new input. The realistic route to critical mass runs through parties whose interest aligns with the worker's: union training funds, apprenticeship programmes, workforce boards and the large owners who impose site credential requirements and would rather verify once.

## Target Customer
Union training funds and apprenticeship programmes, state workforce agencies, large owners with site credentialing requirements, and staffing platforms in the trades — with the worker as the beneficiary and someone else as the payer, which the product design has to face rather than obscure.

## Impact If Built
For the worker, portability means faster hiring, no lost credit toward advancement, and evidence of capability that does not depend on being remembered — which in a career spanning many employers is a material economic difference. For the industry, verified credentials cut hiring friction and reduce the duplicate training that every contractor currently pays for. This is the clearest worker-facing opportunity in construction technology and the one the category's business model has consistently pointed away from.
