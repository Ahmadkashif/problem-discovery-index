# Buy: Freelance Financial Tools Adapted to Session-Based Teaching

**Niche:** [[niches/online-tutoring-platforms/the-tutor/profile|The Tutor]]
**Industry:** [[industries/online-tutoring-platforms|Online Tutoring Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Freelancer accounting tools record invoiced hours; a tutor's economics are dominated by the hours between sessions that nobody invoices.
**Tags:** #descriptive-statistics #time-series-forecasting #confidence-intervals #data-integration #evaluation-metrics #exponential-smoothing #worker-facing #automation
**Contested on:** Whether tools built around billable hours can account for a practice where the unbilled hours determine the margin.

## The Problem

Freelancer financial tooling is well developed: invoicing, time tracking, expense capture, tax estimation and client management, with good products at low prices. Tutors working independently use them, and tutors working on platforms occasionally do.

Every one of them is organised around billable time. The tutor's economic problem is the opposite — the billable hour is fixed by the platform and known, and everything that determines whether the work pays happens in the hours that are not billed. A tool that tracks invoiced sessions tells a tutor something they already know.

## What Already Exists

FreshBooks, Wave, Bonsai, Harvest, QuickBooks Self-Employed and the freelancer tooling market. Time trackers with project tagging. Tax estimation. Client management. Payment platform integrations. Calendar tools. Nothing here needs rebuilding.

## The Customization Gap

**Unbilled time has to be first-class and nearly free to log.** These tools support non-billable time as a category and assume someone will record it. A tutor between two sessions will not open an app. Capture has to be one tap from a notification, inferred from message and document activity, or estimated from a short calibration period — a capture design problem the existing products have not faced because their users bill their time.

**Platform payouts hide the structure.** Earnings arrive as a periodic deposit from the platform, which a bank feed categorises as income and loses entirely: which students, how many sessions, what commission, which subject. Ingesting platform statements with the session detail intact is the integration nobody has built and the one everything else depends on.

**Seasonality is extreme and regular.** Freelancer tools extrapolate trends. Tutoring income drops sharply in summer and peaks before exams, on a schedule that repeats annually and is entirely forecastable. Modelling it as a strong seasonal component rather than a trend is necessary and is not what these tools do.

**Per-student profitability is the decision unit.** The freelancer tools report by client and by project, which maps reasonably. What is missing is the preparation and admin allocation that turns it into a real per-student margin, which is the analysis that changes a tutor's roster.

**Multi-platform working is normal.** Serious tutors work on two or three platforms plus private clients, and comparing realised rate across them is the most valuable output. That requires ingesting several statement formats, which is durable engineering rather than a feature.

## Target Customer

The freelancer tooling vendors, for whom tutors are a visible sub-segment with a distinct and unserved economic shape. Also tutor-focused product builders, where the unbilled-time capture is the wedge and the accounting is the retention.

## Impact If Solved

The accounting, tax and invoicing machinery gets reused, and the unbilled capture, platform statement ingestion, seasonal forecasting and per-student margin get built. Concretely: a tutor sees their realised rate per hour worked, which student is costing them money, and what July will look like — three answers the category's existing products cannot give.
