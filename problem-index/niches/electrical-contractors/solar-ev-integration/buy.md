# Utility Interconnection Application Automation

**Niche:** [[niches/electrical-contractors/solar-ev-integration/profile|Solar & EV Integration]]
**Industry:** [[industries/electrical-contractors|Electrical Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Each of the 3,000+ US electric utilities has different interconnection application forms, requirements, fees, and timelines for solar installations — electricians and solar companies spend 2-4 hours per project navigating utility-specific paperwork that delays system commissioning by weeks to months.
**Tags:** #large-language-models #automation #compliance #data-integration #workflow-orchestration #evaluation-metrics

## The Problem
Before a residential solar system can be connected to the grid, the electrician or solar installer must submit an interconnection application to the local electric utility. This application includes system specifications (inverter type, rated output, connection type), single-line diagrams, proof of insurance, and sometimes engineering certifications. The problem is that each utility has its own application form, its own required attachments, its own fee structure ($0-500), its own review timeline (1 week to 6 months), and its own technical requirements that may exceed NEC minimums. An electrician installing solar systems across three utility territories must learn three different processes. National solar companies manage this with dedicated interconnection teams, but independent electricians adding solar to their service offerings spend 2-4 hours per project on interconnection paperwork — often more time than the actual electrical installation.

## What Already Exists
Bodhi (now part of Aurora Solar) offers some interconnection application tracking. SolarAPP+ provides instant permit approval in participating jurisdictions but covers permits, not utility interconnection. Utility portals vary from sophisticated online applications (Pacific Gas & Electric) to paper forms submitted by mail (smaller municipal utilities). No tool consolidates the requirements across utilities.

## The Customization Gap
The gap is a comprehensive utility interconnection database and automation layer: (1) a database of interconnection requirements for every US electric utility — required forms, attachments, fees, technical requirements, typical review timelines, and contact information — maintained through a combination of web scraping and community updates; (2) auto-population of utility-specific forms from a single project data entry — enter the system specs once, and the tool generates the correct form for the specific utility with all fields populated; (3) application tracking with automated follow-up — submit the application through the utility's portal (or generate the mailing package for paper-based utilities), track review status, and auto-follow-up when timelines are exceeded; (4) an LLM-powered requirement interpreter that reads utility tariff documents and engineering standards to flag project-specific requirements that exceed standard NEC (e.g., "Duke Energy requires external AC disconnect for systems >25kW" or "Xcel Energy limits backfeed to 100% of bus rating, not 120%").

## Target Customer
Independent electricians and small solar installers operating across multiple utility territories, submitting 5-50 interconnection applications per year. Also solar sales companies that need accurate interconnection timelines for customer communication.

## Impact If Solved
Reduces interconnection application time from 2-4 hours to 15-30 minutes per project by auto-populating utility-specific forms. Eliminates application rejections caused by missing attachments or incorrect form versions (currently 15-25% of initial submissions). Reduces interconnection timeline by 2-4 weeks through proactive tracking and follow-up.
