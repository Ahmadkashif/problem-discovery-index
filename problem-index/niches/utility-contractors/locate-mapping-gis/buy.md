# ESRI GIS with Field Detection Integration

**Niche:** [[niches/utility-contractors/locate-mapping-gis/profile|Locate, Mapping & GIS]]
**Industry:** [[industries/utility-contractors|Utility Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Utility locators detect underground utilities in the field and mark them with paint on the surface, but these field-detected positions are rarely captured digitally — creating a gap where the most accurate utility location data (measured in the field) never makes it back to the GIS database that future excavators rely on.
**Tags:** #data-integration #automation #compliance #quick-win

## The Problem
Every day, thousands of utility locators walk job sites with electromagnetic locators and GPR, detecting and marking underground utilities with surface paint and flags. Each locate produces the most accurate utility position data available — measured in the field at the actual location, not estimated from decades-old as-built drawings. But this field data is ephemeral: the paint fades in 2-4 weeks, the flags are removed during construction, and the measured positions are never transferred to the utility's GIS database. The GIS still shows the original (inaccurate) as-built position. The next excavation at the same location will request a new locate, and the locator will re-detect the same utilities — the same work done again because the previous field data was never captured.

## What Already Exists
ESRI ArcGIS stores utility asset locations and supports field data collection through ArcGIS Collector and ArcGIS Field Maps. Utility locating equipment (Radiodetection, Vivax-Metrotech) produces position data with GPS coordinates. The pieces exist but aren't connected: locators don't use ArcGIS Collector during locates, and their equipment doesn't export detected positions to GIS format.

## The Customization Gap
A field-to-GIS integration layer that: (1) captures the locator's field-detected utility positions during routine 811 locates — each mark is GPS-captured (using the locating equipment's GPS or the locator's phone) with utility type, estimated depth, and detection method; (2) uploads these field positions to the utility's GIS as "field-verified" data points, maintaining both the original as-built position and the field-detected position; (3) identifies discrepancies between GIS records and field detections — flagging locations where the field-detected position differs from the GIS record by more than 2 feet; and (4) over time, builds a continuously improving underground utility database where every 811 locate contributes positional accuracy improvements to the GIS.

## Target Customer
Utility companies wanting to improve their GIS accuracy using field data they're already collecting. 811 locate service providers (USIC, Utility Locating Services) performing thousands of locates daily. ESRI seeking to add utility locate integration to ArcGIS.

## Impact If Solved
Continuously improves GIS accuracy using field data that currently evaporates when the paint fades. Reduces repeat locate effort by 15-25% as GIS accuracy improves in frequently-excavated areas. Identifies the highest-priority GIS corrections (where as-built positions are most wrong) from the field data, enabling targeted record updates. Creates a data asset that improves with every 811 locate performed.
