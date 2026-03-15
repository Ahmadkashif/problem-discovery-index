# Test Coverage Gap Analysis for ICT/FCT Fixtures

**Industry:** [[electronics-contract-mfg|Electronics Contract Manufacturing]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Test engineering teams develop ICT (In-Circuit Test) and FCT (Functional Test) programs for each new PCBA, but no tool systematically analyzes whether the test program actually covers all critical circuit nodes and failure modes — test coverage gaps are discovered only when field failures occur on nodes that were never tested, generating warranty costs and customer trust damage.
**Tags:** #bayesian-network #binary-classification #tabular-ml #compliance

## The Problem
Every PCBA program requires a test strategy: which components and circuit nodes are tested by ICT (probing individual components and connections), which functional behaviors are verified by FCT (powering the board and testing system-level functions), and which areas are covered only by AOI/visual inspection. Developing this test strategy requires a test engineer to analyze the schematic, identify critical nodes, and determine which nodes are accessible to ICT probe points given the board layout. For complex boards (1,000+ components), this analysis takes 2-4 weeks and relies heavily on the test engineer's judgment about which nodes are high-risk. The consequence of gaps: components that pass visual inspection but have electrical defects (wrong value, incorrect orientation, solder joint that looks good but has high resistance) escape to the field.

## What Already Exists
ICT fixture design tools (Keysight, Teradyne) generate probe point layouts from board CAD data. FCT test platforms (NI LabVIEW, custom test frameworks) provide the execution environment. EDA tools (Altium, Cadence) contain the schematic and layout data that defines the circuit. No tool performs the analytical layer: given this schematic, this board layout, and this ICT fixture design, which circuit nodes and failure modes are NOT covered by the test program? The test coverage analysis is performed manually by the test engineer based on experience.

## The Customisation Gap
A test coverage analysis tool needs: (1) schematic-level circuit understanding — parsing the netlist to identify all circuit nodes, component connections, and signal paths; (2) testability analysis — determining which nodes are accessible to ICT probes given the board layout and fixture design, and which nodes can only be verified by functional test; (3) failure mode mapping — for each component type and circuit function, identifying the failure modes that are detectable by ICT vs. FCT vs. not detectable by either; (4) coverage gap reporting — listing untested failure modes ranked by probability and consequence, enabling the test engineer to add test points or FCT cases where the gap is unacceptable. This schematic-level reasoning combined with component failure mode knowledge is the domain-specific capability that generic test platforms lack.

## Impact If Solved
Identifies test coverage gaps during NPI rather than after field failures. Reduces field failure rates attributable to untested nodes by 30-50%. For an ECM producing 50,000 units/year on a program with 0.5% field failure rate and $200 average warranty cost, reducing field failures by 40% saves $40,000 per program annually — compounded across 20+ active programs.
