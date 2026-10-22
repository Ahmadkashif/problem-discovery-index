# Mobile Coverage Filings Built to FCC Parameters

**Industry:** [[wireless-carriers|Wireless Carriers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every carrier already predicts coverage with RF planning tools, but the FCC's twice-yearly coverage filings need maps built to fixed parameters, defended against challenges within 60 days and re-filed within 30 days if verification fails, and the planning tools weren't built for that.
**Tags:** #gaussian-processes #regularization #feature-engineering #evaluation-metrics #hypothesis-testing #compliance #data-integration

## The Problem
Under the FCC's Broadband Data Collection, every mobile carrier files coverage maps twice a year by technology and speed tier: 4G LTE at 5/1 Mbps, 5G-NR at 7/1 and 35/3 Mbps, each modelled at 90% cell-edge probability and at least 50% cell loading. The maps feed the National Broadband Map and subsidy decisions such as the 5G Fund. They are public, challengeable and checked. Governments, other providers and consumers can submit speed-test challenges, and a carrier has 60 days to rebut or concede. The FCC can open a verification inquiry and require on-the-ground tests or full site and antenna data for a sampled area. A carrier that can't verify must file revised maps within 30 days.

The engineering team that builds these maps also plans the network. Each filing cycle pulls them off planning work to rerun propagation at the FCC parameters, reconcile with crowdsourced and drive-test data, and respond to challenges hex by hex.

## What Already Exists
RF planning tools such as Forsk Atoll and Infovista Planet produce coverage predictions from site databases, antenna patterns, terrain and clutter. Drive-test systems from Keysight, Rohde & Schwarz and Infovista measure real performance. Ookla and Opensignal sell crowdsourced measurements. The FCC publishes its specification and challenge data. The fixed-network side of the same filing, location by location against the FCC's Fabric, is analysed under wired broadband providers as [[niches/wired-broadband-providers/bdc-availability-filings/profile|Broadband Data Collection & Availability Filings]]; mobile filings differ because they are propagation maps at fixed speed, probability and loading parameters rather than lists of served locations.

## The Customisation Gap
Planning tools predict signal strength for engineering decisions; the FCC needs a defensible speed claim at a fixed probability and loading, gridded to its hexagons. The missing layer is a filing workflow. It needs propagation models calibrated against the carrier's own drive and crowdsourced tests by clutter type, with the calibration evidence kept as an exhibit. It needs translation from signal to modelled speed under 50% loading, consistent across filings, so maps don't move for no network reason. It needs challenge triage that sorts valid challenges (concede) from tests taken indoors, on the wrong technology or on congested sectors (rebut). And when the FCC samples an area, it needs verification packages assembled from site records and test plans within the deadline. Rural carriers, whose subsidy eligibility rides on these maps, have one or two engineers to do it.

## Impact If Solved
A calibrated, documented filing pipeline turns each cycle from a weeks-long scramble into a rerun, cuts the share of challenges conceded for lack of evidence, and protects subsidy and roaming positions that depend on what the public map shows. For a rural carrier it can be the difference between keeping and losing support for a county.
