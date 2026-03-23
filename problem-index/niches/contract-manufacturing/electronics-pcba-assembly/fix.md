# Siloed Inspection Data Across SPI, AOI, and Functional Test

**Niche:** [[niches/contract-manufacturing/electronics-pcba-assembly/profile|Electronics PCBA Assembly]]
**Industry:** [[industries/contract-manufacturing|Contract Manufacturing]]
**Type:** Fix (Pain Point)
**One-liner:** SPI data lives in the Koh Young dashboard, AOI data lives in the Mirtec database, and functional test results live in the test engineering system — three data silos that prevent process engineers from seeing the full quality picture for any given board without manual data pulling across three different applications.
**Tags:** #data-integration #automation #worker-facing

## The Problem
A process engineer investigating a yield problem on a specific PCB assembly must manually query three separate systems to understand what happened: the SPI system (was paste volume within spec?), the AOI system (what defects were detected and where?), and the functional test system (what test failures occurred and are they correlated to specific component locations?). Each system has its own interface, its own data export format, and its own identifiers for the same board. Correlating a functional test failure to a specific AOI finding to a specific SPI measurement for the same component on the same board requires manual data manipulation that takes 1-3 hours per investigation.

## Why It's Still Broken
Inspection system vendors compete with each other and have no incentive to build data integration with competitors' products. The IPC-CFX (Connected Factory Exchange) standard was designed to solve this problem, but adoption is partial — many installed AOI and SPI systems predate CFX support. EMS companies lack the internal software engineering capacity to build custom data integration layers across vendor systems. The result: the data exists to perform cross-process quality analysis, but it's trapped in vendor-specific silos.

## What a Fix Looks Like
A middleware data integration layer that pulls inspection data from SPI, AOI, and functional test systems into a unified database with board-level and component-level identifiers. For each board serial number, all inspection results from all process stages are linked and queryable from a single interface. Process engineers can search by board, component, defect type, or time period and see the complete inspection history without switching between applications. Correlation views automatically highlight relationships — "boards with SPI paste volume below 80% on pads 12-15 have a 3x higher functional test failure rate on U7."

## Who Feels the Pain
Process engineers who spend 1-3 hours per investigation on data gathering across siloed systems, and quality managers who cannot generate cross-process yield reports without custom spreadsheet manipulation.

## Impact If Fixed
Reduces yield investigation data gathering from 1-3 hours to 10-15 minutes. Enables continuous cross-process yield monitoring that currently requires dedicated data engineering effort. For an EMS company running 10 SMT lines with 2-3 yield investigations per week per line, recovering 20-90 engineering hours weekly for process optimization rather than data gathering.
