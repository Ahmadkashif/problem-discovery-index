# Device Matrix Testing From Mobile Quality Assurance

**Niche:** [[niches/digital-accessibility-firms/at-testing-at-scale/profile|Assistive Technology Testing at Scale]]
**Industry:** [[industries/digital-accessibility-firms|Digital Accessibility Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Mobile testing solved the device and version matrix with cloud device farms, and assistive technology testing runs on the tester's own laptop.
**Tags:** #automation #workflow-orchestration #evaluation-metrics #data-integration #descriptive-statistics #compliance #confidence-intervals #optimization-fundamentals
**Contested on:** Every serious competitor in this niche is fighting to test whether flows complete across the screen reader, browser and operating system combinations users actually have, at a cost that permits doing it repeatedly — and whoever does takes the account.

## The Problem
Mobile quality assurance faced an identical combinatorial explosion — devices, operating system versions, screen sizes, manufacturers — and solved it with cloud device farms, parallel execution, and coverage prioritised by the real device distribution of a product's users. Testing across dozens of configurations became routine and cheap. Assistive technology testing faces a smaller matrix and runs on individual testers' machines, one configuration at a time.

## What Already Exists
Cloud device and configuration farms; parallel test execution across a matrix; coverage prioritised by real user distribution; reusable test definitions across configurations; and result comparison across the matrix.

## The Customization Gap
The adaptation is to a test whose outcome depends on what a person hears and judges. It requires: (1) the assistive technology's spoken or braille output being the thing under test, which requires capture and interpretation rather than assertion against a document object model — this is the substantive difference and is why the device farm model has not transferred; (2) screen readers that are desktop applications with licensing and automation constraints; (3) judgement about whether an announcement is comprehensible, which is expert rather than assertable; (4) flows that require authentication and real data rather than a test harness; and (5) a test population of expert users rather than a script.

## Target Customer
Accessibility firms, in-house accessibility teams, testing tool and device farm vendors, and assistive technology vendors.

## Impact If Solved
Mobile testing made a larger matrix routine and cheap with device farms and parallel execution. Output that is spoken and must be judged, rather than asserted against markup, is why the same model has not crossed over.
