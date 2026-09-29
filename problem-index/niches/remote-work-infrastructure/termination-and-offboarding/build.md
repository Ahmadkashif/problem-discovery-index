# Build: Termination as an Enforced Jurisdictional Process

**Niche:** [[niches/remote-work-infrastructure/termination-and-offboarding/profile|Termination & Offboarding]]
**Industry:** [[industries/remote-work-infrastructure|Remote Work Infrastructure]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Model each jurisdiction's termination process as required steps with dependencies and waiting periods, and refuse to advance until each is complete.
**Tags:** #compliance #workflow-orchestration #evaluation-metrics #confidence-intervals #data-integration #descriptive-statistics #automation #worker-facing
**Contested on:** Whether a platform will hold a termination that its client has instructed.

## The Problem

A termination in a jurisdiction with meaningful employment protection is a process, not an event. There are required grounds, documented and communicated in a specified way. There may be a required warning sequence, a consultation, a notice period that cannot be shortened, a protected category check, a works council notification, a specified final pay calculation and a statutory severance amount.

The platform holds the guidance describing all of this. The execution is a person following it under pressure from a client who wants a date, with steps that are guided rather than enforced.

So steps get compressed or skipped. Notice is paid in lieu where the jurisdiction does not permit it. A documented reason is assembled retrospectively. A consultation is abbreviated. Each of these is the ground on which a tribunal later finds the termination unlawful, and the liability lands on the employer of record and through it on the client.

## Why Nobody Has Built This

Enforcement means telling the customer no. A platform that holds a termination because a required consultation has not occurred is obstructing the thing the client asked for, at the moment the client is least patient.

The processes are also genuinely intricate and jurisdiction-specific, so modelling them properly is the same large unglamorous rule-structuring exercise as everywhere else in this industry.

And terminations are individually urgent and collectively infrequent enough that the tooling has never been prioritised — each one is handled as an exception by a person, which is exactly how the errors happen.

## What to Build

The process as a modelled workflow with hard gates.

**Model each jurisdiction's termination path.** Grounds and their evidentiary requirements, required steps in order, waiting periods, notification obligations, protected category checks, notice calculation, severance calculation and final pay components. As a structured process definition with dependencies, not as a guidance page.

**Gate on the required steps.** A termination cannot advance past a step until that step is recorded complete with its evidence. Notice cannot be served before the consultation is documented; the final date cannot precede the notice period's end. This is what converts guidance into compliance and it is the whole build.

**Compute the dates from the process, not from the request.** The client asks for a date; the system returns the earliest lawful date given the jurisdiction's requirements and the worker's tenure. Presenting that at the start reframes the conversation before anyone is committed.

**Check protected categories automatically.** Pregnancy, parental leave, sick leave, disability, trade union role, recent protected complaint — categories that in many jurisdictions block or complicate a termination. A check against the platform's own records at initiation, with the finding stated, prevents the most serious errors.

**Calculate final pay and severance from the rules.** Accrued leave, notice pay, statutory severance, pro-rated bonuses and thirteenth-month amounts, per the jurisdiction. This is arithmetic and is frequently wrong.

**Tell the worker what is happening and what they are entitled to.** Notice period, severance, final pay composition, their rights to contest, and the applicable timeframes. The worker is the least informed party in the most consequential event of the relationship, and informing them is both required in many jurisdictions and right.

**Record everything as evidence.** Steps, dates, documents, communications — assembled as the file that will be examined if this is challenged, produced as a by-product rather than reconstructed afterwards.

## Target Customer

Platform legal and operations leadership, for whom an unlawful termination is the highest-severity outcome they produce. Also clients' legal functions, who carry the residual exposure and would rather be told the earliest lawful date than discover a tribunal claim.

## Impact If Built

The termination process gets enforced rather than guided, so the steps that make it lawful cannot be skipped under pressure. The earliest lawful date is computed at the start rather than discovered. The worker is told what they are entitled to. And the evidence file exists because it was produced as the process ran.
