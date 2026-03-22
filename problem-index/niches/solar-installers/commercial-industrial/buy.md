# Aurora/Helioscope C&I Financial Model Integration

**Niche:** [[niches/solar-installers/commercial-industrial/profile|Commercial & Industrial Solar]]
**Industry:** [[industries/solar-installers|Solar Installers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Aurora Solar and Helioscope produce accurate C&I production models but their financial analysis modules use simplified rate assumptions — integrating real C&I rate structures with demand charge calculations would eliminate the need for the custom Excel model that every C&I developer builds alongside their design tool.
**Tags:** #data-integration #automation #revenue-impact #quick-win #gradient-boosting

## The Problem
Aurora Solar's financial module supports basic rate inputs: energy rate, net metering credit, and annual escalation. This works for residential but is inadequate for C&I where savings depend on demand charge interaction, TOU period matching, and ratchet effects. The result: C&I developers use Aurora for system design (production modeling) and then export the hourly production data to a custom Excel model that contains the utility's full rate structure, performs the demand charge analysis, and calculates the actual financial return. This dual-tool workflow is time-consuming (4-8 hours of Excel work per project), error-prone (copy-paste errors between Aurora export and Excel input), and inconsistent (every developer builds their own Excel model with different assumptions and methodologies).

## What Already Exists
Aurora Solar produces accurate hourly production curves for any system design. Helioscope does the same with a different interface approach. Both support data export. Energy Toolbase models C&I rates but doesn't integrate with design tools. None offer end-to-end design-to-financial-analysis for C&I.

## The Customization Gap
A C&I rate modeling module integrated directly into Aurora (or Helioscope) that: (1) imports the complete C&I rate schedule from a tariff database when the user enters the utility and rate schedule name — including energy charges by TOU period, demand charges by season, demand ratchet provisions, power factor adjustments, and facilities charges; (2) automatically performs the hourly matching of solar production against load and rate, calculating energy savings, demand charge impact, and net billing credits at 15-minute resolution; (3) models the demand ratchet effect — showing that reducing peak demand in July (with solar + battery) reduces minimum billing demand for the following 12 months; and (4) outputs a complete C&I financial analysis within Aurora/Helioscope, eliminating the Excel export workflow entirely.

## Target Customer
Aurora Solar and Helioscope C&I users (approximately 3,000-5,000 users) who currently maintain parallel Excel models for C&I financial analysis. Aurora/Helioscope as platforms seeking to capture more of the C&I workflow.

## Impact If Solved
Eliminates the 4-8 hour custom Excel model per C&I project, saving 40-80 hours per year for a developer doing 10 projects annually. Reduces financial modeling errors caused by data export/import between design tool and spreadsheet. Enables Aurora/Helioscope to justify premium C&I tier pricing ($100-200/month additional). Makes C&I solar proposals accessible to residential-focused installers exploring commercial opportunities.
