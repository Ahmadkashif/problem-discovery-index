# AI-Assisted Preliminary Cost Estimation from Architectural Drawings

**Industry:** [[general-contractors|General Contractors]]
**Type:** High Impact
**One-liner:** An experienced estimator who can eyeball a floor plan and get within 10-15% of final cost before any itemized takeoff — a judgment built from hundreds of projects — gets that capability embedded in a model that any estimator on the team can invoke in 5 minutes instead of 3 days of preparation.
**Tags:** #cnn #regression #computer-vision #multimodal #tacit-knowledge-ml #revenue-impact

## The Problem
Construction estimating has two phases: preliminary (ballpark) estimates used for bid/no-bid decisions and early owner conversations, and detailed estimates (takeoffs) used for formal bids and contracts. The preliminary estimate is where experienced estimators earn their salary — they process an architectural drawing set and apply accumulated cost pattern knowledge (structural system type, mechanical complexity, building envelope, site access, local labor market, current material costs) to produce a reliable order-of-magnitude number in hours rather than weeks. Junior estimators cannot do this without supervision because the cost pattern recognition requires processing hundreds of variables simultaneously — variables that an experienced estimator has internalized as intuition. The result: preliminary estimates can only be produced by the firm's senior estimators, creating a bottleneck that limits bid volume and forces go/no-go decisions based on incomplete data.

## Why It's Unsolved
Construction cost estimation is notoriously hard to automate because the input (architectural drawing sets) is unstructured visual + spatial data, the cost model is highly local (labor rates, material costs, subcontractor availability all vary by geography and time), and the relevant features are architectural concepts that require domain understanding (what is the structural system? is the mechanical system exposed or concealed?) rather than simple measurements. Image recognition can extract dimensions; it cannot yet reliably classify "this is a Type V wood frame with conventional MEP" vs. "this is a Type II structural steel with exposed mechanical" — the distinction that drives 30-50% cost variance. The tacit knowledge problem is that the classification requires the same visual pattern recognition that experienced estimators have developed over hundreds of projects.

## What a Solution Looks Like
A multimodal model that processes the architectural drawing set images alongside extracted text (room labels, dimensions, specification notes) and structured project metadata (location, building type, gross area, number of floors) to: classify the building's primary structural and mechanical system type; estimate cost-per-square-foot ranges for each major division (structural, mechanical, electrical, plumbing, finishes, site work); produce a preliminary total cost estimate with a ±20% range; and identify the 3-5 uncertainty factors that could move the estimate significantly in either direction. The output is a 30-minute estimator review input, not a final estimate.

## Impact If Solved
Compresses preliminary estimate production from 2-3 days (senior estimator) to 30 minutes (any estimator reviewing AI output). Enables GCs to evaluate 3-5x more bid opportunities with the same estimating team. Reduces bid/no-bid decision risk on poorly-fit projects (projects that will be unprofitable at reasonable margins become visible before a detailed estimate investment is made).
