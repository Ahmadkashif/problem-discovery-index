# Leachate Loads Without a Guaranteed Outlet

**Industry:** [[landfill-operators|Landfill Operators]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Tank telemetry, wastewater SCADA and truck dispatch tools already exist; what no tool does is plan a landfill's leachate against rain forecasts, tank space and a shrinking list of treatment plants that each set their own PFAS, volume and surcharge rules.
**Tags:** #time-series-forecasting #optimization-fundamentals #large-language-models #data-integration #workflow-orchestration #compliance

## The Problem
Rain that falls on open cells and seeps through the waste collects on the liner as leachate. Federal rules require the collection system to keep less than 30 cm of leachate over the liner, so it is pumped to sumps and tanks and then piped to a sewer, treated on site, recirculated where the permit allows, or trucked to a municipal treatment plant. A wet month can multiply volumes, and a large landfill may ship tens of thousands of gallons a day (estimate). The environmental manager juggles tank levels, sump pumps, haulers, plant receiving hours and the conditions in each plant's industrial user permit.

Those conditions are tightening. Plants have begun capping volumes, demanding PFAS pretreatment or refusing leachate altogether; Montpelier, Vermont is described as that state's last plant accepting it, and requires ~80% PFAS removal first (search summary). EPA has finished its study of the landfill effluent guideline and plans to revise it for PFAS. Republic reported that its 2025 landfill operating costs rose mainly because of monitoring and maintenance on gas and leachate extraction systems. When an outlet closes or a storm fills the tanks, the manager phones haulers and plants, pays emergency rates, and watches the head on the liner climb.

## What Already Exists
Tank and sump level telemetry from SCADA and IoT vendors; on-site treatment systems from vendors such as Heartland Water Technology, Veolia and the newer PFAS destruction firms; haulers' own dispatch software; wastewater utilities' pretreatment programme software that tracks industrial users from the plant's side; and the weather forecasts everyone already reads. Spreadsheets hold the haul log and the monthly volumes reported to the state.

## The Customisation Gap
The landfill-specific layer is a leachate generation forecast built from rainfall forecasts, open and capped area, recent cell construction and the site's own history, joined to tank and sump capacity and the 30 cm head limit. On top sits an outlet book: each plant's permitted volume, PFAS and other limits, sampling frequency, surcharges, receiving hours and travel time, with the landfill's own sample results checked against them before a truck leaves. The output is a week-ahead plan of loads by outlet, an alert when forecast volume exceeds the secured outlets, and the monthly discharge and haul reports assembled from the same record. Generic dispatch and telemetry tools have none of the permit logic, and plants' pretreatment software sees only its own end.

## Impact If Solved
For a landfill trucking ~10M gallons a year (estimate), shifting 20% of loads from emergency to planned hauling at ~$0.05 a gallon saved (estimate) is ~$100K a year, and the forecast gives the manager the weeks of warning needed to secure a second outlet before a plant's PFAS limit takes effect.
