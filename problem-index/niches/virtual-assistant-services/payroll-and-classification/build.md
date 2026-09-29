# Build: Jurisdiction-Aware Classification and Landed-Pay Transparency

**Niche:** [[niches/virtual-assistant-services/payroll-and-classification/profile|Payroll, Classification & Cross-Border Pay]]
**Industry:** [[industries/virtual-assistant-services|Virtual Assistant Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Assess each placement's classification against the assistant's own jurisdiction, and show the assistant what actually lands in their account and why.
**Tags:** #compliance #descriptive-statistics #confidence-intervals #evaluation-metrics #data-integration #workflow-orchestration #worker-facing #revenue-impact
**Contested on:** Whether an agency will examine a classification position it currently asserts.

## The Problem

Two problems sit in this layer, one legal and one plain.

The legal one is classification. The industry's standard arrangement has features that classification tests in several jurisdictions treat as indicative of employment: set hours in the client's timezone, exclusivity to one client, day-to-day direction, use of the client's systems, and duration measured in years. The default position is contractor, applied uniformly, generally without jurisdiction-specific analysis. Several of the relevant markets have tightened their tests, and the exposure — back social contributions, mandatory benefits, termination entitlements — falls on the agency and potentially on the client.

The plain one is that an assistant earning a modest wage loses several percent of it to FX spread and transfer fees they were never shown. A rate quoted in dollars arrives in local currency at a rate nobody explained, and the difference between a good and a bad payout path over a year is real money to the recipient.

## Why Nobody Has Built This

Classification analysis costs money, produces an answer that may require restructuring, and creates a written record of a risk the agency currently does not have documented. Not analysing is the position of least immediate cost, and the industry has taken it collectively, which makes it feel safer than it is.

Pay transparency erodes nothing for the agency if the payout path is good and is embarrassing if it is not, which is why it is absent where it matters most — the agencies using the cheapest rails are the ones least likely to show the arithmetic.

And the assistant has no standing to raise either. Contractors in another jurisdiction do not challenge their classification or their FX rate.

## What to Build

An assessment capability and a transparent payout.

**Assess classification per placement and per jurisdiction.** The features that matter — hours control, exclusivity, direction, equipment, duration, substitution rights, integration into the client's organisation — captured as structured facts about each placement, evaluated against the tests in the assistant's own jurisdiction. This is a rules-and-content problem: the tests are published, the facts are knowable, and the analysis is repeatable once built.

**Score the exposure and act on it.** Placements with several employment indicators in a jurisdiction with a strict test are the ones to restructure — through an employer-of-record arrangement, through genuine changes to the working arrangement, or both. Ranking the book by exposure lets an agency fix the worst tenth rather than restructuring everything.

**Use employer-of-record where the analysis says so.** EOR providers cover most relevant markets and turn an uncertain contractor position into a compliant employment one, with local benefits and termination handled. It costs more per placement and it is the answer for the placements that need it.

**Show the landed amount.** Gross, agency deductions if any, FX rate against mid-market, transfer fee, and the local-currency amount that arrives. Per payment. This is arithmetic and it converts an opaque number into a checkable one.

**Optimise the payout path.** Compare rails by corridor on landed amount rather than headline fee, and route accordingly. The differences are several percent and the agency is the only party positioned to negotiate them.

**Document the local obligations.** Mandatory contributions, benefits and termination requirements in each market, and who is responsible for them. Most agencies operate in five or six markets and could not state this for any of them.

## Target Customer

Agency leadership and counsel, driven by exposure rather than enthusiasm — which is the honest account of why this gets built. Also the larger clients, whose own procurement and legal functions increasingly ask how offshore contractors are engaged, and for whom an agency with a documented position is a materially easier supplier to approve.

## Impact If Built

The classification position stops being an assumption applied uniformly and becomes an assessment made per jurisdiction, with the worst exposures fixed. Assistants see what arrives and why, and the payout path gets chosen on landed amount. And the agency acquires a documented answer to a question its clients are starting to ask.
