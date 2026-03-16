# Machine Learning Opportunities — Moving Companies

**Industry:** [[moving-companies|Moving Companies]]
**Derived from:** [[problems/moving-companies/high-impact|High Impact]], [[problems/moving-companies/low-impact-1|Low Impact 1]], [[problems/moving-companies/low-impact-2|Low Impact 2]], [[problems/moving-companies/worker-life-1|Worker Life 1]], [[problems/moving-companies/worker-life-2|Worker Life 2]]

---

## 1. Move Scope Estimation from Walkthrough Video
#gradient-boosting #regression #computer-vision #tabular-ml #tacit-knowledge-ml

**Problem statement:** An experienced estimator walks a home and intuitively predicts cubic footage, crew size, truck allocation, and labor hours within 10% accuracy — a skill that takes 2-3 years to develop and cannot be explicitly articulated. The goal is to replicate this tacit pattern recognition by extracting visual and spatial features from a walkthrough video and combining them with structured move metadata to predict move scope.

**ML task:** Multi-output Regression (cubic footage, labor hours, crew size, truck count)
**Input data:** Walkthrough video frames (smartphone camera, 1-5 minutes per room), structured metadata (origin/destination floor level, staircase type, elevator availability, drive distance, season, day of week). Training data sourced from move companies that already use virtual survey tools like Yembo or MoveSnap, augmented with post-move actuals from dispatch records.
**Target:** Four continuous outputs: total cubic footage (100-2500 cu ft), labor hours (2-16 hrs), crew size (2-6), truck count (1-3). Each with a calibrated confidence interval.
**Evaluation metric:** Mean Absolute Percentage Error (MAPE) on each output, weighted by revenue impact. Primary target: MAPE < 8% on cubic footage (vs. 15-20% for junior estimators). Secondary: labor hours MAPE < 12%.
**Scope:** Phase 1 (3-4 months, 2-3 engineers): object detection and room segmentation from video frames using a fine-tuned YOLO or Faster R-CNN model to identify furniture items, boxes, and access obstacles. Phase 2 (2-3 months): gradient-boosted regression model combining extracted visual features with structured inputs. Requires 5,000+ completed moves with both walkthrough video and actual post-move measurements for training. Deployment as a mobile SDK integrated into the estimator's survey app.
**Data availability:** Hard to assemble. Virtual survey companies (Yembo, MoveSnap) have walkthrough videos but not post-move actuals. Moving companies have post-move actuals but rarely retain survey video. A data partnership or purpose-built collection campaign across 10-20 mid-size movers over 6-12 months would be required. Labeling requires experienced estimators to annotate items in video frames and validate scope predictions — and two estimators may disagree on the "correct" cubic footage for edge cases.

---

## 2. Crew Size and Move Duration Prediction
#gradient-boosting #regression #tabular-ml #quick-win

**Problem statement:** Dispatchers manually assign crew sizes and estimate move durations based on gut feel and the estimator's cube sheet, frequently under-staffing complex moves (leading to overtime and customer dissatisfaction) or over-staffing simple ones (wasting labor). A tabular model trained on historical move outcomes can predict optimal crew allocation and expected duration from structured move attributes.

**ML task:** Multi-output Regression (labor hours, optimal crew size)
**Input data:** Structured move records: cubic footage, item count by category (heavy furniture, fragile, boxes), origin and destination characteristics (floor level, stairs vs. elevator, walk distance from truck to door), drive distance, season, day of week, crew experience ratings. Sourced from dispatch and invoicing systems of moving companies using SmartMoving, MoveitPro, or equivalent.
**Target:** Predicted labor hours (continuous, 2-20 hours) and recommended crew size (integer, 2-8). Optional: probability of overtime flag.
**Evaluation metric:** MAPE on labor hours (target < 10%), crew size accuracy within +/-1 person on 90%+ of moves.
**Scope:** 2-3 months, 1-2 engineers. This is a structured tabular problem with well-defined features. Requires 3,000+ completed moves with actual labor hours recorded. GBM (XGBoost/LightGBM) is the natural starting point. Low deployment complexity — outputs feed into dispatch scheduling.
**Data availability:** Moderate. Any company using digital dispatch tracks actual crew assignments and clock-in/clock-out times. The challenge is standardizing feature definitions across companies (what counts as "heavy furniture" varies). A single mid-size mover with 3-5 years of history likely has enough data.

---

## 3. Customer Churn and Rebooking Prediction
#gradient-boosting #binary-classification #tabular-ml #revenue-impact

**Problem statement:** Moving companies lose 30-50% of qualified leads between initial inquiry and booking, and a significant portion of booked customers cancel or rebook with competitors after receiving the quote. Predicting which leads are likely to convert and which booked customers are at risk of cancellation allows targeted follow-up and pricing adjustments.

**ML task:** Binary Classification (will-book / won't-book; will-cancel / won't-cancel)
**Input data:** Lead attributes (move size, distance, date flexibility, how they found the company, response time to inquiry), quote details (price relative to market average, binding vs. non-binding, valuation tier selected), behavioral signals (email open/click rates, number of follow-up calls, time between quote receipt and response). Sourced from CRM and communication logs.
**Target:** Binary label: booked vs. not-booked (for leads), cancelled vs. completed (for booked moves).
**Evaluation metric:** AUC-ROC as primary; precision at 80% recall for the cancellation model (sales team can only follow up on so many accounts). Revenue lift measured as incremental bookings from targeted intervention.
**Scope:** 2 months, 1 engineer. Standard classification problem. Requires 10,000+ lead records with outcome labels across 1-2 years. Feature engineering around timing signals (how fast the customer responded, which competitors they mentioned) is likely the highest-leverage work.
**Data availability:** Good for companies using any CRM. Lead outcome data (booked vs. lost) is naturally tracked. Cancellation data requires linking CRM records to dispatch records to confirm whether the move actually happened. The main gap is competitive intelligence — knowing whether the customer booked with someone else and at what price.

---

## 4. Multi-Stop Route and Load Optimization for Moving Fleets
#reinforcement-learning #regression #tabular-ml #automation

**Problem statement:** Dispatchers manually plan daily routes for 5-20 trucks, each potentially handling multiple moves (especially for local/short-distance operations). They balance drive time, loading sequence (items for the last delivery go in first), crew availability windows, customer time preferences, and truck capacity constraints. The combinatorial complexity means dispatchers use simple heuristics that leave 15-25% of efficiency on the table.

**ML task:** Constrained Optimization / Reinforcement Learning (route sequencing and truck assignment)
**Input data:** Daily move manifest (origins, destinations, estimated cubic footage, estimated load/unload times, customer time windows), fleet inventory (truck capacities, current locations, maintenance schedules), crew roster (availability, CDL status, skill ratings). Real-time inputs: traffic data, actual load/unload completion times.
**Target:** Optimized assignment of moves to trucks and crews, with sequenced routes that minimize total drive time while respecting all constraints (truck capacity, crew hours, customer windows, loading order).
**Evaluation metric:** Total fleet drive-miles (minimize), percentage of moves delivered within customer window (maximize, target >95%), average truck utilization by volume (maximize, target >75%).
**Scope:** 4-6 months, 2-3 engineers including one with OR/optimization background. Start with a constraint-programming baseline (Google OR-Tools), then layer an RL agent for dynamic re-routing when actual times deviate from estimates. Requires integration with dispatch systems for real-time constraint updates. The hardest part is modeling the loading-order constraint: items for the last stop must be loaded first, which couples the route sequence to the loading plan.
**Data availability:** Moderate. Dispatch records contain move assignments and timing, but most companies don't record actual routes taken or truck utilization by volume. GPS tracking data from fleet management systems (Samsara, Verizon Connect) can fill the route gap. A 6-month pilot with a single fleet of 10+ trucks would generate sufficient training data for the RL component.
