# Fix: Nobody Will Say What Happened to Them

**Niche:** Outcome Linkage
**Industry:** [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Every organisation holds detailed records of the incidents it contained, and disclosing any of it creates legal and reputational risk with no offsetting benefit.
**Tags:** #compliance #evaluation-metrics #confidence-intervals #hypothesis-testing #data-integration #revenue-impact
**Contested on:** Whether what actually happened to organisations can be joined to their control state at all.

## The Problem

An organisation detects an intrusion attempt, contains it, investigates, and writes it up internally. The write-up says what the attacker tried, where they got, what stopped them, and what was changed afterwards. It is precisely the information the field needs and it never leaves the building.

The reasons are not secrecy for its own sake. Disclosing an incident, even a contained one, creates legal exposure — the document becomes discoverable, and a contained incident described in detail can be characterised later as evidence of a known weakness. It attracts regulatory attention. It worries customers, who do not distinguish well between a contained attempt and a breach. It may trigger contractual notification obligations. And it offers the organisation nothing in return.

So every organisation rationally withholds, and collectively the field has no data. The only incidents that become public are the ones that legally must be, which are the largest and least representative, and the resulting picture of what actually happens to organisations is drawn entirely from catastrophes.

This is a coordination failure with a well-understood shape. Other fields with the same structure solved it, and security has not.

## Why It's Still Broken

**The incentive is entirely one-directional.** Contribution is costly and risky for the contributor and beneficial only to everyone else. Nothing in the current arrangement offsets that.

**Legal privilege is the operative constraint.** Incident investigations are frequently conducted under privilege precisely to protect them from discovery, and sharing waives it. Counsel advising against contribution is giving correct advice under current law.

**Existing voluntary schemes have thin uptake for exactly this reason.** Several information-sharing organisations exist and receive far less than they would if participation were safe. Their experience is the evidence that goodwill alone does not solve it.

**No taxonomy, so no comparability.** Organisations describe incidents differently and there is no shared vocabulary for what happened, what stopped it and what control was involved.

**Near-misses are not recorded consistently.** Many organisations do not formally document attempts that were blocked, so even willing contributors often have nothing structured to give.

**The parties who would benefit most cannot convene.** Researchers have no leverage, insurers have a commercial interest, and vendors have a conflict. The natural convenor is a regulator, and regulators have generally focused on mandatory breach notification rather than on voluntary near-miss reporting.

## What a Fix Looks Like

**Create legal protection for good-faith contribution.** Statutory shielding making contributed incident data non-discoverable and inadmissible, as aviation and healthcare safety reporting have. This is the fix — everything else is implementation, and without it counsel will continue to advise against participation and be right to.

**Collect near-misses, not breaches.** Far more numerous, far less sensitive, and far more informative about which controls actually stopped something. The aviation precedent is exact: the safety transformation came from near-miss reporting, not from accident investigation.

**Give contributors something back.** Benchmarking against the aggregate, early warning about attack patterns appearing in similar organisations, and — where insurers participate — a premium reduction. Contribution has to be worth something to the contributor or it will not happen.

**Standardise the taxonomy.** A shared vocabulary for incident type, entry vector, what stopped it and which control was involved. Existing attack taxonomies provide most of the vocabulary and none of the defender-side structure.

**Make reporting a by-product of incident closure.** Integrated into the incident response tooling organisations already use, structured, short, submitted at closure. Any scheme requiring separate effort will be used by the few organisations that need it least.

**Convene through a regulator or agency.** The natural host is a body with standing, no commercial interest and the ability to create the legal protection. Several national security agencies are well positioned and have not taken this particular step.

**Start sector by sector.** Organisations share more readily with peers facing the same threats than with the world. Sector-based schemes have better uptake and can federate later.

## Who Feels the Pain

The field, which has no denominator and therefore no ability to say what works — every claim about control effectiveness in security rests on plausibility because this data does not exist.

Smaller organisations most of all, who have the least ability to learn from their own experience and would benefit most from aggregate findings.

Security teams, arguing for control investment with no evidence beyond framework citation, against budget holders who reasonably ask what the evidence is.

And every organisation that suffers an incident of a type others had already contained and learned from privately.

## Impact If Fixed

Legal protection for good-faith contribution is the single change that unlocks everything else, and the precedents in aviation and healthcare are strong, well studied and directly transferable.

Near-miss collection would give the field an order of magnitude more data than breach disclosure ever will, and it is the less sensitive half — which makes it both more useful and easier to obtain.

And benchmarking returned to contributors would convert a public-goods problem into a mutual-benefit one, which is the only structure under which voluntary reporting has ever achieved real uptake.
