# ESP Failure Root Cause Analysis Data Gap

**Niche:** [[niches/oil-gas-field-services/esp-workover-specialists/profile|ESP Workover Specialists]]
**Industry:** [[industries/oil-gas-field-services|Oil & Gas Field Services]]
**Type:** Fix (Pain Point)
**One-liner:** ESP teardown reports documenting what actually failed are handwritten, unstructured, and rarely linked to pre-failure telemetry — destroying the ground truth data needed for predictive models.
**Tags:** #bert #text-classification #nlp #data-integration #tacit-knowledge-ml

## The Problem
After an ESP is pulled from a well, a teardown analysis is performed to determine what failed: motor burnout (insulation breakdown), pump stage erosion (sand or scale), shaft failure (fatigue, corrosion), cable breakdown (hot spot, mechanical damage), or gas lock (well conditions, not equipment). This teardown is the ground truth label that, combined with pre-failure telemetry, could train predictive models. But teardown reports are handwritten on paper forms or dictated into unstructured text fields: "Motor showed signs of insulation breakdown, likely due to overheating. Pump stages 3-7 showed erosion consistent with sand production. Cable intact." This narrative lives in a filing cabinet at the service company and is never linked to the telemetry data stored in the monitoring system. The two datasets — pre-failure telemetry and post-failure diagnosis — exist in separate systems owned by different companies and are never joined.

## Why It's Still Broken
ESP monitoring is done by the operator or the ESP OEM (Baker Hughes, Schlumberger). Teardown analysis is done by the service company that pulled and inspected the equipment. These are often different organizations with no data-sharing infrastructure. Within a single operator, the production engineering team (who monitors telemetry) and the workover team (who manages teardowns) use different systems and often do not communicate failure details. Teardown reports have no standard format — each service company uses its own template with different terminology for the same failure modes.

## What a Fix Looks Like
A structured ESP failure database that: (1) digitizes teardown reports using NLP to extract structured failure mode, root cause, and component condition data from narrative text, (2) links each teardown record to the well's pre-failure telemetry data using well ID and date matching, (3) standardizes failure terminology across service companies using an industry taxonomy (API standards for artificial lift failures), and (4) creates the labeled dataset needed for predictive model training. The system accepts teardown data from multiple service companies and telemetry data from multiple monitoring systems, normalizing both into a common schema.

## Who Feels the Pain
Artificial lift engineers who know that telemetry + teardown data could prevent failures but cannot access joined datasets, ESP OEMs whose predictive analytics products are limited by the absence of labeled failure data, and operators who pay for the same preventable failures repeatedly because root cause data is not systematically captured.

## Impact If Fixed
Creates the labeled dataset foundation for ESP failure prediction models. For operators with 100+ ESP wells, linking just 50 historical teardowns to telemetry data could enable a baseline predictive model that prevents 10-20% of future emergency failures — saving $1-3M annually per operator.
