# Parking Notices Checked Against Each State's Rules

**Industry:** [[parking-operators|Parking Operators]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Collections and compliance software already manages notices, letters and disputes, but none of it knows which states bar plate cameras at public lots, what a parking notice must say, how long the driver must have to pay or when a registered-owner lookup is allowed.
**Tags:** #large-language-models #bert #transformers #evaluation-metrics #compliance #workflow-orchestration #automation

## The Problem
At a gateless lot, a car that leaves without paying becomes a notice. The camera system matches the entry and exit images to a plate, looks up the registered owner from state motor-vehicle records, and a notice processor mails a demand with the date, time, photos and amount. A notice-compliance specialist at the operator or the processor decides, lot by lot, whether a notice can go out at all and what it must say. The rules differ by state and are changing fast. Maine's 2025 chapter 350 requires the fee to be reasonable and posted at every entrance and exit, and the notice to give the date and time, the rule broken, the amount, a due date at least 10 business days out, payment instructions and contact details. It also applies the state statute that bars automated plate recognition at lots open to the public, subject to that statute's exceptions, and gives drivers treble damages for violations. California regulates plate-reader operators under its ALPR statute, and an appeals court has let a suit proceed against a garage operator without proof of actual harm (search summary). Federal DPPA suits challenge the registered-owner lookups themselves: in Crostarosa v. LAZ Parking, a Colorado court's January 2026 order sent the claim against the notice processor to arbitration and kept LAZ and Asura in court.

## What Already Exists
Collections platforms (for example, debt-collection systems built around FDCPA and Regulation F letter rules), general compliance and policy-management tools, document-generation software, and the notice and dispute modules inside parking enforcement suites from T2, Passport and the notice processors. Legal teams track statutes in spreadsheets and outside-counsel memos.

## The Customisation Gap
What the generic tools lack is a parking-specific rule set, applied to each lot before any notice is created. It needs to know whether plate recognition is permitted at this lot in this state, given that state's exceptions, and whether a registered-owner lookup is a permissible use for this purpose. It needs to check that the posted signage shows the fee at every entrance and exit, and that the notice carries every required field and the minimum payment window. It needs to know whether the state caps the fee or bars credit reporting, which notice language reads like an official citation and is banned, and when the session images must be deleted. Then each dispute (paid but misread, plate cloned, signage missing, medical emergency) has to be classified against those rules and answered with the right citation.

## Impact If Solved
A rule engine that blocks non-compliant notices before they are mailed protects the operator from statutory exposure that runs to treble damages in Maine and $2,500 per DPPA violation (search summary). It would also cut the specialist's per-state review from days per new lot to minutes (estimate).
