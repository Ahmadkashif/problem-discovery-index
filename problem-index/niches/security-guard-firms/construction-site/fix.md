# Theft Discovery Delay

**Niche:** [[niches/security-guard-firms/construction-site/profile|Construction Site Security]]
**Industry:** [[industries/security-guard-firms|Security Guard Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Construction site thefts are often discovered 12-48 hours after they occur because no one inventories the site daily — the guard didn't know the copper wire was supposed to be there.
**Tags:** #computer-vision #object-detection #anomaly-detection

## The Problem
Construction site guards patrol for intruders but don't inventory materials and equipment. When 200 linear feet of copper wire disappears overnight, the theft isn't discovered until the electrician arrives the next morning and reports it missing. By then, the material is gone, the security footage (if it exists) must be reviewed for an unknown time window, and the guard who was on duty can't recall anything unusual. The guard had no way of knowing what was supposed to be on-site.

## Why It's Still Broken
Construction sites change daily — materials arrive, get installed, and move between areas. A static inventory is obsolete within hours. Guards are hired for patrol and deterrence, not inventory management. They don't have training or tools to track what materials should be in which locations. The GC knows what's on-site (they ordered it), but this information doesn't flow to the security team.

## What a Fix Looks Like
A simplified inventory awareness system: the GC flags high-value deliveries (copper wire delivery to building B, generator parked at lot C) in a shared platform. The guard's patrol app shows expected high-value items at each patrol checkpoint with photos. If something is missing during patrol, the guard reports it immediately rather than discovering it 12-48 hours later. For ongoing monitoring, fixed cameras with basic change detection can flag significant visual changes in material staging areas between patrol rounds.

## Who Feels the Pain
GCs who lose $10,000-$100,000 per theft incident and blame the security firm for not detecting it, and security firms who lose contracts after major theft events they couldn't have prevented without inventory awareness.

## Impact If Fixed
Reduces theft discovery time from 12-48 hours to 1-4 hours, improving recovery rates (police response is far more effective when theft is discovered quickly) and protecting the security firm's reputation and contract.
