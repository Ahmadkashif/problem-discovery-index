# Rate Filing to Configuration Translation

**Industry:** [[insurtech-platforms|Insurtech Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Rating engines are mature and configurable, and turning a filed rate manual into working configuration across fifty states is a specialised, error-prone job that every carrier staffs and no vendor has automated.
**Tags:** #large-language-models #bert #transformers #word-embeddings #transfer-learning #evaluation-metrics #compliance

## The Problem
A carrier cannot change a rate without filing it. Rate and rule filings go to each state's department of insurance, are reviewed, and take effect on approval — separately per state, with each state having its own requirements, objections and timelines.

Once approved, the filed rate has to become working software. Somebody reads the rate manual — factor tables, territory definitions, classification rules, rating algorithms, minimum premiums, rounding conventions — and configures it in the rating engine. For a multi-state carrier this is the same product implemented fifty times with variations, and the variations are frequently subtle: a different territory definition, one state's mandated minimum, a prohibited rating factor.

Errors here are expensive in an unusual way. A misconfigured factor produces premiums that do not match the filed rate, which is a regulatory problem as well as a financial one, and it is typically discovered in a market conduct examination long after thousands of policies have been written on it.

## What Already Exists
Rating engines from Guidewire, Duck Creek, Earnix and others are capable and configurable. SERFF handles the filing submission workflow. Bureau content from ISO and NCCI supplies loss costs and standard classifications that many carriers adopt with a deviation. Rate comparison and testing tools exist. Document extraction from structured tables is reliable.

## The Customisation Gap
Nothing bridges the filed document and the configuration. The rate manual is prose and tables; the rating engine wants a structured algorithm. The translation is human, specialised and slow, and it is the reason a rate change takes months to reach the market after approval.

Extracting factor tables from filed rate manuals is a well-shaped document task with unusually clean structure. Extracting the rating algorithm — the order of operations, the caps, the rounding, the interaction rules — is harder and is where the errors concentrate, and it is exactly the part that would benefit from a machine reading the document rather than a person skimming it.

Verification is the more valuable half and is entirely absent. Once configured, the engine should be tested against the filed manual automatically: generate rating scenarios across the parameter space, compute the premium under both the configuration and the filed algorithm, and report divergence. That is straightforwardly buildable and would catch the errors that market conduct examinations currently find years later.

Cross-state comparison is the third gap. A carrier operating in forty states has forty variants of one product and no view of how they differ, which makes every subsequent change forty investigations.

## Impact If Solved
Time from filing approval to market is a direct competitive constraint on how responsively a carrier can price, and configuration error is a regulatory exposure discovered years late. Both are addressable from documents the carrier already filed and already stores.
