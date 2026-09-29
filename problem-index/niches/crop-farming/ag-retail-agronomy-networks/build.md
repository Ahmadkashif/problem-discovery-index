# A Prescription Is a Prediction and the Harvest Grades It Every Autumn

**Niche:** [[niches/crop-farming/ag-retail-agronomy-networks/profile|Agricultural Retail Agronomy Networks]]
**Industry:** [[industries/crop-farming|Crop Farming]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Thousands of agronomists write field-level prescriptions every spring, every field reports its yield every autumn, and no retailer scores one against the other.
**Tags:** #gradient-boosting #causal-inference #evaluation-metrics #confidence-intervals #time-series-forecasting

## The Problem
An agronomist walks a field, reads the soil test and the stand, and writes a prescription: this rate, this product, this timing, on these acres. The grower applies it. Six months later a combine with a yield monitor drives across the same field and records, at sub-acre resolution, exactly what came out of it.

That is a prediction and a graded answer, generated on millions of acres a year, by an organisation that employs more crop advisers than anyone else in the country.

Nobody joins them. The prescription lives in the retailer's agronomy system as a work order. The yield map lives in the grower's farm management software, or on a memory card, or in the cab. The agronomist's next-season recommendation is informed by memory of how the field looked, not by a measured comparison of what was prescribed against what was produced.

The consequence is that the largest agronomic advisory workforce in the country runs on a feedback loop of personal recollection. Nobody can say which recommendations paid, which agronomists are consistently right, or how much of the yield variation attributed to a product was actually weather, soil, or the grower's own execution. The retailer's own trial network — genuinely proprietary, run over many years — is used to support product positioning rather than to calibrate the advice.

There is a structural reason this matters more than it looks. The agronomy is given away to sell inputs, which means every recommendation carries an unstated conflict: the adviser recommending a rate is employed by the party selling the product. The only thing that can settle whether the advice is good is outcome measurement, and outcome measurement is the one thing nobody does.

## Why Nobody Has Built This
Yield data belongs to the grower, and growers are — reasonably — cautious about handing it to the company selling them fertiliser. Data-sharing arrangements exist and are patchy, and the trust deficit is the real obstacle rather than the technical one.

Attribution is also genuinely hard. A field's yield reflects weather, hybrid, soil, drainage, planting date, pest pressure and a dozen management decisions the agronomist did not make. Isolating the effect of one prescription is a causal problem, not a correlation, and doing it badly would produce confident nonsense that a grower would catch immediately.

And the commercial model does not ask for it. The agronomist's performance is measured in product volume moved, not in yield delivered, so nothing in the incentive structure funds the join.

## What to Build
Prescription-to-outcome measurement, treated as the retailer's own research asset.

**Assemble the paired record.** Prescription as written, application as executed, field attributes, and yield at sub-acre resolution. The retailer already holds the first two and has the relationship to negotiate the third — with the grower's own benefit as the consideration, because the grower gets the analysis back.

**Model the counterfactual, not the yield.** The question is not what this field produced but what it would have produced under a different prescription. Within-field variation is the lever: strip trials, rate ramps and unintentional application variation occur constantly and turn ordinary commercial fields into a very large observational experiment.

**Use the trial network as the anchor.** The proprietary trial plots are randomised where the commercial fields are not. Fitting on trials and correcting the observational fields against them is the standard structure, and it is exactly what a network with both should do.

**Score agronomists, privately and carefully.** Consistency and calibration by adviser, by crop, by region. This is delicate — it is a workforce measured on volume — and it is the only route to transferring what the best advisers know.

**Report uncertainty to the grower.** A prescription delivered with an expected response and an honest interval is a materially different product from one delivered as a number, and it is the version a sceptical grower will trust from a party that also sells the product.

## Target Customer
VP of Agronomy or Director of Agronomic Research at a national agricultural retailer. The commercial argument is that agronomy is the only defence against a cheaper input channel, and it is currently defended by assertion.

## Impact If Built
US growers spend tens of billions on crop inputs annually against recommendations from advisers whose accuracy has never been measured, sold by the party supplying the product. Closing the prescription-to-yield loop makes the advice testable, gives the retailer the one claim a discount channel cannot answer, and turns millions of acre-years of commercial application into the largest agronomic evidence base in the country.
