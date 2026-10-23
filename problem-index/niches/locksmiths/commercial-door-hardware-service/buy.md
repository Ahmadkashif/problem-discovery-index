# Facility Work-Order Platforms Extended to the Opening

**Niche:** [[niches/locksmiths/commercial-door-hardware-service/profile|Commercial Door Hardware Service & Code Compliance]]
**Industry:** [[industries/locksmiths|Locksmiths]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Clients already route every door ticket through a facility work-order platform; the platform knows the building and the trade, not the door, its hardware or its fire rating.
**Tags:** #large-language-models #cnns #data-integration #compliance #workflow-orchestration #automation
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor is fighting to be the vendor a facility calls for its openings. But a fire-rated or egress door is won by inspecting it and closing deficiencies before the fire marshal or accreditation surveyor arrives, while an access-controlled door is won by delivering electrified hardware that works with the client's access system and still releases for egress on commissioning day. The buyers, data and clocks differ. Decomposed into contested sub-niches below.

## The Problem
Retail chains, banks and property managers dispatch locksmiths through facility service platforms, and schools and hospitals through a CMMS. The locksmith checks in, attaches a photo, enters a resolution code and closes the ticket. The platform's resolution codes were written for every trade at once ("repaired", "replaced part"), so nothing useful about the opening survives.

## What Already Exists
ServiceChannel, Corrigo and similar facility work-order platforms handle dispatch, check-in, not-to-exceed limits, invoicing and vendor scorecards. CMMS products hold asset registers. Locksmiths' own field-service software (Workiz, ServiceTitan, Jobber) handles the firm's side.

## The Customization Gap
Door work needs the door as an asset. Each record should carry a hardware set with function (BHMA function numbers for locks and exit devices), fire rating and label status, egress and accessibility flags, and electrified components. Resolution codes should be door-specific (closer adjusted, hinge replaced, strike realigned, device latch replaced) and parts lines should map to manufacturer catalogues. Callback detection should tie a new ticket to the opening's last visit, and an NFPA 80 inspection form should create deficiency tickets automatically. A connector that writes these records back from the locksmith's app into the client's platform makes the extension worth having for both sides.

## Target Customer
Facility managers at multi-site clients who already run a work-order platform, and the commercial locksmiths on their vendor lists.

## Impact If Solved
The client sees its door spend and failure patterns inside the system it already uses, and the locksmith's work becomes measurable rather than a closed ticket. That is the basis for being kept on the vendor list.
