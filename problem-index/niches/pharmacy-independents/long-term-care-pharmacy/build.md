# Census-Driven Blister Pack Production Scheduling with Demand Forecasting

**Niche:** [[niches/pharmacy-independents/long-term-care-pharmacy/profile|Long-Term Care Pharmacy]]
**Industry:** [[industries/pharmacy-independents|Independent Pharmacies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A production scheduling system that forecasts blister pack demand based on facility census patterns, medication regimen changes, and admission/discharge trends — replacing the whiteboard-and-spreadsheet approach that causes overtime surges and missed delivery windows.
**Tags:** #gradient-boosting #time-series-forecasting #feature-engineering #optimization-fundamentals #evaluation-metrics #automation #tacit-knowledge-ml

## The Problem
LTC pharmacies produce blister cards on a cycle fill schedule — typically each facility gets its cards refilled every 28-30 days. A pharmacy serving 15 facilities with 100 beds each manages ~1,500 resident medication profiles, producing 3,000-6,000 blister cards per cycle. Production managers must sequence facility cycles across the month to level-load their packaging equipment and staff, but census changes constantly disrupt the plan: new admissions require mid-cycle card production, discharges waste partially-produced cards, and medication changes require reprinting. Experienced production managers develop an intuitive sense for which facilities will have high census volatility (memory care units have lower turnover than skilled nursing), which days of the week see more admissions (Monday after weekend hospitalizations), and which medication changes require full card reprints vs. supplemental strips. This tacit scheduling knowledge is lost when the production manager leaves.

## Why Nobody Has Built This
LTC pharmacy production scheduling sits at the intersection of pharmacy management and manufacturing production planning — a combination that neither PMS vendors nor manufacturing MES vendors address. The market is small (~1,500 independent LTC pharmacies in the US) and the workflow complexity is high: each facility has different cycle dates, different packaging preferences (blister card vs. strip packaging vs. unit dose), different delivery windows, and different census volatility profiles. Building an optimizer requires integrating real-time census data from facilities (which often comes via fax or phone call), medication profile changes from prescribers, and packaging equipment capacity constraints. No single data source contains all the inputs.

## What to Build
A production scheduling platform that ingests census data from each facility (via integration with facility EHRs like PointClickCare, or manual entry for facilities without digital census), medication profile data from the LTC PMS, and historical production records to: (1) forecast per-facility blister card demand for the next 2-4 weeks using gradient-boosted time-series models trained on census patterns, seasonal admission trends, and medication change frequency, (2) optimize cycle fill sequencing across facilities to level-load production equipment and staff, (3) predict mid-cycle production needs (new admissions, medication changes) to pre-allocate capacity, and (4) alert the production manager when a facility's census trend suggests the current cycle date should shift. The tacit scheduling intuition of experienced production managers is encoded as model features — facility type, day-of-week admission patterns, seasonal census trends, medication change frequency — creating institutional knowledge that persists through staff turnover.

## Target Customer
Independent LTC pharmacy owners serving 5+ facilities who manage production scheduling manually and experience regular overtime surges (15-25% of labor costs) due to unplanned mid-cycle production and poor cycle sequencing.

## Impact If Built
Reduces production overtime by 30-50% through better demand forecasting and cycle optimization, saving $25,000-60,000 annually for a mid-size LTC pharmacy. Eliminates missed delivery windows that risk facility contract loss. Captures the production scheduling expertise of experienced managers in a model that new staff can rely on immediately.
