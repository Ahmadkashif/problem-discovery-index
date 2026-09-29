# The Interactive Process as a Tracked Case

**Niche:** [[niches/hr-tech-platforms/leave-and-accommodation/profile|Leave & Accommodation]]
**Industry:** [[industries/hr-tech-platforms|HR Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An accommodation request starts a process the employer is legally obliged to engage in and document, and it is conducted as an email thread between a manager, an HR generalist and an employee who is unwell.
**Tags:** #workflow-orchestration #survival-analysis #evaluation-metrics #confidence-intervals #compliance #automation #worker-facing #descriptive-statistics
**Contested on:** Every serious competitor in leave and accommodation software is fighting to run an individual's case as an entitlement with a statutory clock rather than as an email thread — and whoever makes the interactive process trackable takes the account.

## The Problem
An employee requests an adjustment to their working arrangements for a medical reason. What follows is an obligation to engage: consider the request, seek information where needed, explore alternatives, and reach a determination, documented. What actually happens is an email to a manager, who forwards it to HR, who asks for medical certification, which arrives, and then a period during which the employee hears nothing while three people discuss it in a thread. Weeks pass. The employee, who is unwell and waiting, does not know whether their request is being considered or has been forgotten. If the matter later becomes a complaint, the employer's evidence that it engaged properly is an email thread that will not read well.

## Why Nobody Has Built This
Accommodation volume per employer is modest, so it has never been a large enough line item to attract product investment, and it is handled by generalists as part of a broader role. The process resists templating because every case is genuinely different, which has been taken as a reason not to structure it at all — when in fact the structure is in the obligations and the clocks rather than in the content. And there is a defensive instinct: creating a detailed record of an interactive process creates discoverable evidence, which counsel sometimes reads as risk rather than as the protection it usually is.

## What to Build
The case as a first-class object with states, obligations and clocks. A request creates a case regardless of which channel it arrived through — manager, HR, occupational health — which is the first fix, since a request made verbally to a manager currently frequently never becomes anything. Statutory and policy clocks run from the correct trigger with escalation before they lapse. Medical certification is requested with the permissible scope stated, tracked to receipt, and stored separately from the general HR record with access restricted, because medical information about employees requires handling that most HR systems do not provide by default. The interactive process is recorded as what it is: options considered, information sought, positions taken, determination and reasoning — which serves the employee, the employer and any later review equally. The employee has their own view: what stage their case is at, what is required of them, and by when, which is the most direct improvement available to a person managing a medical situation and an employment process at the same time. And the standing report is case ageing, because the most common failure is not denial but drift.

## Target Customer
Absence management vendors, HCM platforms, third-party leave administrators, and employers whose accommodation processes are conducted in email.

## Impact If Built
This is the HR process where the individual's stake is highest and the system support is lowest. Making the case trackable protects the employee from drift, gives the employer the documentation the obligation actually requires, and — through case ageing — surfaces the failure mode that dominates, which is requests that are never determined at all.
