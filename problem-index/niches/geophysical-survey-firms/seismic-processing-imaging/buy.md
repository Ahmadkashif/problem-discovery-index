# HPC Job Orchestration With Parameter Lineage

**Niche:** [[niches/geophysical-survey-firms/seismic-processing-imaging/profile|Seismic Processing & Imaging]]
**Industry:** [[industries/geophysical-survey-firms|Geophysical Survey Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Processing houses schedule thousands of compute jobs with general HPC tools that know nodes and queues, not which flow version, parameter set and input volume produced the image the client is looking at.
**Tags:** #optimization-fundamentals #descriptive-statistics #data-integration #workflow-orchestration #automation
**Contested on:** Every serious competitor in this sub-niche is fighting to deliver a depth image whose velocity model ties the wells and that the client's interpreters trust, before the lease sale or drilling decision, and whoever gets there with the fewest re-runs takes the reprocessing work.

## The Problem
A reprocessing project runs hundreds of tests and thousands of production jobs across clusters or cloud. When the client asks why one test panel looked better than another, or a re-run produces a different result, the answer is buried in job logs and processors' notes.

## What Already Exists
Slurm and PBS schedulers, AWS ParallelCluster and Azure CycleCloud for cloud bursting, and experiment trackers such as MLflow built for machine learning.

## The Customization Gap
The seismic adaptation needs: lineage from every output volume back to the flow version, parameter values, input data vintage and velocity model used; test-panel comparison linked to that lineage; cost tracking per project and per test against the processing budget; and storage tiering for multi-terabyte prestack data with client ownership tags so data is never mixed across clients.

## Target Customer
Processing managers and IT leads at imaging houses moving from owned clusters to cloud.

## Impact If Solved
Reproducible images, fewer accidental re-runs and visible compute cost per project, on workloads where compute is a major share of delivery cost (estimate).
