# Lineage: Solar Installers

**Industry:** [[industries/solar-installers|Solar Installers]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** PVWATTS — the free web calculator that turns a location, a system size, a tilt and an azimuth into a month-by-month kWh and savings estimate for a grid-connected PV system
**Builder:** National Renewable Energy Laboratory
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A rooftop system is sold on a number that does not exist yet.

A homeowner putting thousands of dollars into panels is buying future kilowatt-hours. How many depends on where the house is, which way the roof faces, how steep it is, and the weather over years. Working that out properly took hourly solar-radiation data and a simulation model. Both belonged to researchers.

So an installer had two poor choices. It could hire an engineer to model every small job, which the margin on a residential job could not cover. Or it could quote a rule of thumb, which the customer had no reason to trust. There was no shared yardstick.

## What Got Built

A form with four answers and a table.

**PVWATTS — "A Performance Calculator for Grid-Connected PV Systems"** was live on NREL's Renewable Resource Data Center site by **2000**. The earliest archived capture of its home page is from August 2000, and redirects to it were captured in January 2000. The user clicked a state on a US map and chose a weather station, identified by its WBAN number. Then they entered:

- system size as an AC rating, defaulting to **4 kW**, or about 45 m² of array;
- fixed, one-axis or two-axis tracking;
- tilt, defaulting to the site's latitude, with a table converting roof pitch to degrees (a 6/12 roof is 26.6°);
- azimuth, defaulting to south;
- the electricity price, defaulting to the state's average residential rate.

It returned monthly and annual energy and the dollar value of that energy. It used weather "typical or representative of long-term averages during the 1961-1990 time frame."

## Who Built It, And Why Them

A federal laboratory, because it already owned the expensive half.

The lab opened in **1977** as the Solar Energy Research Institute. It was designated a national laboratory in **September 1991** and renamed the National Renewable Energy Laboratory. That is the name it built PVWATTS under, and the name used as the key here. The Department of Energy renamed it the National Laboratory of the Rockies on **1 December 2025**.

The hard part of an estimate was never the arithmetic. It was the decades of measured and modelled solar radiation behind it, and NREL published that dataset. A calculator was the cheapest way to put that asset in the hands of people who would never read a radiation data manual. The page says so: NREL researchers "developed PVWATTS to permit non-experts to quickly obtain performance estimates." It linked out to DOE's Million Solar Roofs programme. A lab with no system to sell could offer a neutral number, which no installer or manufacturer could credibly do.

I could not find the names of the individual researchers or a release date earlier than the 2000 archive captures.

## What It Cost

**It assumed a clear sky.** The original results page said the figures "assume that the PV array has an unobstructed view of the sky. If trees, buildings, mountains, or other obstacles block the sun, the values in the table should be reduced." It did not say by how much. Shade, the main site-specific variable on a real roof, was left to the installer.

It also gave averages as though they were promises. NREL's own page said individual months could miss by as much as 40% and individual years by up to 20%. The savings figure assumed net metering, and the page said so.

## What You Still Touch

Every residential proposal still shows a first-year kWh figure built on the PVWATTS approach: location, orientation, typical-year weather. Two things a 2000 web form set aside are now whole problems of their own: the shade it told you to subtract yourself, and the gap between the estimate and what the meter shows.

- [[problems/solar-installers/high-impact|🔴 Automated Shade Analysis and System Performance Modeling from Aerial Imagery]]: the "values should be reduced" left to the installer
- [[problems/solar-installers/worker-life-2|🟢 System Performance Anomaly Detection and Proactive Customer Communication]]: the customer comparing the meter to the estimate
- [[niches/solar-installers/design-proposal-generation/profile|Design & Proposal Generation]]
- [[niches/solar-installers/solar-resource-independent-engineering/profile|Solar Resource Assessment & Independent Engineering]]

**Sources:** Internet Archive captures of rredc.nrel.gov/solar/codes_algs/PVWATTS/ (home page 15 August 2000; redirects 25 January 2000), with the /system.html and /interp.html subpages and a station page (Birmingham, WBAN 13876), for the title, the "non-experts" sentence, the defaults, the roof-pitch table, the 1961–1990 weather basis, the unobstructed-sky caveat, the error ranges and the net-metering assumption; Wikipedia, *National Renewable Energy Laboratory* (now titled *National Laboratory of the Rockies*), for 1977, September 1991 and 1 December 2025. WebSearch was unavailable (session cap reached). pvwatts.nrel.gov did not resolve and OSTI refused connections, so the later version manuals (V5 onward) were not consulted. ⚠️ **Not established:** the first release date (earlier than 2000 is possible but unconfirmed); the developers' names; and how widely installers used PVWATTS in its first years compared with commercial tools.
