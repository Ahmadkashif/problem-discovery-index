# As-Built Documentation Accuracy

**Niche:** [[niches/utility-contractors/water-sewer-infrastructure/profile|Water & Sewer Infrastructure]]
**Industry:** [[industries/utility-contractors|Utility Contractors]]
**Type:** Fix (Pain Point)
**One-liner:** As-built drawings for buried water and sewer utilities are inaccurate 30-40% of the time — pipes are not where the records say they are — causing 500,000+ utility strikes per year during excavation, at an estimated industry cost of $30B annually in damage, delays, and injuries.
**Tags:** #object-detection #data-integration #compliance #worker-facing #cnns

## The Problem
When a contractor buries a water main or sewer line, they are required to submit an as-built drawing showing the final installed location, depth, and material. This as-built becomes the permanent record. The problem: as-builts are produced by the construction crew, often sketched on the original design plan with hand-written annotations, then digitized by a GIS technician who interprets the sketches. At each step, accuracy degrades — the construction crew estimates offset distances from surface features, the sketches are imprecise, and the GIS technician makes interpretive decisions about ambiguous annotations. Studies by the Common Ground Alliance (CGA) show that 30-40% of utility as-built locations are inaccurate by more than 2 feet horizontally and/or 1 foot vertically. This inaccuracy causes utility strikes: when a future excavation project requests a utility locate, the locator marks the surface based on records that are wrong. The excavator digs where the locate mark says it's safe and hits a pipe that's 3 feet from where the records indicate.

## Why It's Still Broken
As-built production has remained essentially unchanged for decades: paper markup, manual measurement, hand digitization. GPS-enabled as-built collection exists (Trimble, Leica) but requires survey-grade equipment ($15K-30K) and trained operators. Most utility contractors don't invest in GPS as-built collection because the cost isn't justified by their contract terms — utilities don't typically require GPS-grade as-builts or pay a premium for them. The problem is externalized: the cost of inaccurate as-builts is borne by future excavators (who strike utilities), not by the original contractor (who submitted the inaccurate as-built).

## What a Fix Looks Like
A mobile as-built collection system that achieves sub-foot accuracy using consumer-grade technology: (1) the construction crew photographs the installed pipe in the open trench using a smartphone with GPS and augmented reality positioning, capturing the pipe's 3D location relative to surrounding surface features; (2) the system uses visual odometry and landmark matching to achieve sub-foot positional accuracy without survey-grade GPS (by referencing visible surface features — curbs, utility poles, building corners — with known coordinates from aerial imagery); (3) as-built data is automatically uploaded to the utility's GIS as a verified record, eliminating the sketch-to-digitize interpretation step; and (4) over time, the system builds a high-accuracy underground utility database that reduces strike risk for all future excavation in the area.

## Who Feels the Pain
Excavation contractors who strike utilities because the locate marks based on inaccurate records are wrong — each strike costs $2,000-50,000 in repair, delay, and potential injury. Utility locators who can't find utilities because the records are wrong, spending 30-60 minutes per locate request searching with electromagnetic detection equipment. Municipalities that face liability for utility strikes caused by their inaccurate records.

## Impact If Fixed
Reduces utility strike frequency by 30-50% by improving the underlying as-built accuracy that locators depend on. Saves $9-15B annually in strike-related costs across the US utility industry. Reduces excavation project delays caused by inaccurate locates, saving $500-2,000 per excavation project in avoided re-work. Creates a continuously improving underground utility database that gains value with every new as-built submission.
