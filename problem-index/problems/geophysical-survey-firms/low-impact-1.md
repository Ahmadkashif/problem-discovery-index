# Field QC Against a Quality Plan the Tablet Doesn't Know

**Industry:** [[geophysical-survey-firms|Geophysical Survey Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every geophysical crew already collects on a rugged tablet; none of the field apps checks the data against the project's quality plan — coverage, line spacing, sensor function tests, positioning accuracy — before the crew demobilises.
**Tags:** #change-point-detection #evaluation-metrics #descriptive-statistics #feature-engineering #compliance #automation #quick-win

## The Problem
A geophysical survey is accepted or rejected against written quality objectives. A munitions response survey under a DoD quality assurance project plan specifies along-line sample spacing, across-line coverage, a daily instrument verification strip that the sensor must pass morning and evening, and a positioning accuracy; a DAGCAP-accredited classification survey adds its own measurement quality objectives. A utility designating job under ASCE 38-22 and a state DOT's SUE directive specifies the project limits that must be covered at QL-B and requires documenting where it could not be achieved. A seismic crew's client specifies fold, offsets and noise thresholds.

In practice the crew collects all day and finds out whether it met those objectives when the data is processed — at the hotel that night, or back at the office next week. A coverage gap behind a parked car, a GPS dropout under trees, a sensor that drifted after lunch, a morning function test that was marginal: each is found after the fact. If the crew has left, someone goes back.

## What Already Exists
Field data collection apps — Esri ArcGIS Field Maps and Survey123, Trimble's field software, Fulcrum — handle forms, photos and GPS points well. Instrument makers ship their own loggers that display the live trace and the track. Processing packages such as Oasis montaj and RADAN compute coverage and QC statistics once the data is loaded. Daily reports are written in Word or a form app.

## The Customisation Gap
None of these tools holds the project's quality objectives as rules and tests the incoming stream against them. The geophysics-specific logic is: coverage computed from sensor footprint and positioning, not from the GPS breadcrumb; line-spacing and sample-density checks per method and per sensor configuration; automated pass/fail of instrument verification strip and function-test results against the plan's tolerances; detection of sensor drift, spikes and positioning jumps in the live stream; and a QC log formatted the way the client's QAPP, the DAGCAP assessor or the DOT reviewer expects it. Each firm currently does this with processing-software scripts and a QC geophysicist reading plots the next day.

## Impact If Solved
A field QC layer that flags a failed function test or a coverage hole while the crew is still on site removes most re-mobilisations, which on a remote munitions site or an out-of-state DOT job can cost several thousand dollars and a lost week each (estimate). It also produces the QC record the client audits, as a by-product of collection rather than a report written afterwards.
