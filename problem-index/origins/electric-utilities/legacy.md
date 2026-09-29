# Legacy: What Electric Utilities Bequeathed

**Origin:** [[origins/electric-utilities/profile|Electric Utilities]]

## The Direct Inheritance: a grid built to be metered, then measured

The dispatch/commitment discipline stayed inside the utility. What left the building was the **metering and telemetry layer** built to feed it — first for billing, then, from the mid-2000s, for continuous visibility into what was happening at the network's edge.

The EIA began tracking **Advanced Metering Infrastructure (AMI)** deployment in **2007**. **ARRA (2009)** funded the **Smart Grid Investment Grant** programme, disbursing **$3.4 billion** toward utility AMI and grid-modernisation projects — the single largest driver of the boom that followed. Smart meter counts roughly **quadrupled between 2007 and 2011**, passing 23% of US customers; growth slowed 2012–2016, then the base roughly doubled again, reaching **~71 million meters — about 47% of US customers — by end of 2016.**

> **Myth to kill:** ARRA is commonly said to have *mandated* smart meter rollout. It did not. ARRA funded and subsidised deployment through competitive grants; the pace remained a utility- and regulator-level choice, and it tracks state regulatory posture more than federal policy.

## What the Metering Layer Actually Bought

Interval metering enabled **time-of-use (TOU) pricing** and **demand response** — charge more when the grid is stressed, less when it is not, letting price do some of the work the reliability margin used to do alone.

**The evidence on whether this works is genuinely mixed, and this file will not pick a comforting number.** Reported peak-demand reductions range from roughly nothing up to **40%**, depending heavily on rate design. Typical residential TOU load shifting sits closer to **1–6%**. Event-based critical-peak pricing alone can cut demand by around **19%** during called events — layered on flat TOU it dilutes to around **5%**. Some rate designs have produced **rebound peaks of up to +32.9%**, snapping back so hard once the cheap period arrives that it **exceeds** the reduction achieved during the expensive one (as low as −5.7%).

TOU pricing behaves better as a long-run elasticity and awareness tool than as a guaranteed peak-shaving mechanism — exactly why utilities still carry N-1 physical reliability margins in [[origins/electric-utilities/the-mechanism|the dispatch and commitment layer]] rather than relying on price signals alone.

## The Children

| Child | What it inherited |
|---|---|
| [[industries/solar-installers|Solar Installers]] | The interconnection queue — a rooftop system cannot go live until the utility's own metering and grid-study process clears it, and this vault's own notes on the industry record customers cancelling during exactly that wait. |
| [[industries/energy-auditors|Energy Auditors]] | The data. Interval AMI readings are what make a calibrated building energy model possible at all — before granular metering, an auditor had a monthly bill and a guess. |
| [[industries/utility-contractors|Utility Contractors]] | The build-out itself. Someone had to trench, string and connect every AMI meter and every piece of grid-hardening infrastructure this file describes — a direct, physical inheritance rather than a data one. |
| [[industries/agtech-platforms|Agtech Platforms]] | The thinnest line in this table, stated honestly rather than stretched: on-farm solar and irrigation-pump load sit inside the same interconnection and net-metering processes described above, but the vault's own agtech-platforms notes do not evidence this as a load-bearing part of the industry's current problem set. An adjacency, not a direct transplant. |

## What an Episode Should Take From This

1. **A subsidy is not a mandate, and conflating the two erases the actual decision-makers.** ARRA money moved because state regulators and utilities chose to apply for it and chose how to deploy it.
2. **More data does not automatically produce a clean answer.** AMI let the industry measure demand response's effect precisely, and the precise answer turned out to be "it depends, sometimes it backfires" — a better lesson than a false certainty.
3. **The reliability margin built into [[origins/electric-utilities/the-mechanism|dispatch and commitment]] exists because price signals alone have never been proven to reliably substitute for it.**

**Sources:** EIA, Advanced Metering Infrastructure and smart meter deployment data (2007–2016); DOE, *Smart Grid Investment Grant Program* final reports; GAO and NREL literature reviews on time-of-use and demand-response programme effectiveness; this vault's `industries/solar-installers.md`, `industries/energy-auditors.md`, `industries/utility-contractors.md`, `industries/agtech-platforms.md`.
