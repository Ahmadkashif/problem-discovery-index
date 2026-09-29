# Lineage: MLOps Platforms

**Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Wave:** [[series/eras/wave-07-big-data|7 — Big Data]]
**The tool:** the feature store in Uber's Michelangelo platform — a shared repository of named features computed once, kept offline in Hive for training and online in Cassandra for serving, with a feature DSL whose expressions run identically at training time and at prediction time
**Builder:** Uber
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A model is trained on one computation of a feature and served on another.

The data scientist builds "average delivery time over the last hour" in a notebook, against a warehouse table, in batch. An engineer rebuilds it in the production service, against a live stream, in a different language. The two are meant to agree. Nobody checks, because there is no single place both computations live. When they drift, the model does not fail. It returns confident numbers computed on inputs it never saw in training.

Google's 2015 NIPS paper *Hidden Technical Debt in Machine Learning Systems* named the category of cost: data dependencies, entanglement, configuration debt, "system-level anti-patterns." Uber's own description of where it stood before its platform is concrete. Data scientists used R, scikit-learn and custom algorithms; engineering teams built one-off serving containers per project; there was no standard pipeline for training or prediction data; models were limited to what fit on a desktop; there was no central record of experiments and no established path to production.

## What Got Built

Michelangelo, Uber's internal machine-learning platform, which the company says it began building in mid-2015 and described publicly on 5 September 2017. The piece that became an industry category is its **feature store**.

A team defining a feature registered it once, in a shared repository. The platform computed it two ways from the same definition: a **batch precompute** into Hive for historical training data, and a **near-real-time compute** through Kafka and Samza into Cassandra for low-latency serving. By 2017 Uber reported about 10,000 features stored and refreshed daily.

On top sat a Scala-based DSL for selecting and transforming features. The design constraint is stated outright: "the same expressions are applied at training time and at prediction time." For a new online feature with no history, a backfill tool generated training data "by running a batch job against historical logs."

**The feature store is a consistency guarantee packaged as a database.** One definition, two materialisations, and the claim that they cannot disagree.

## Who Built It, And Why Them

Uber, and the reason is the product it sold.

A ride-hailing marketplace predicts in real time, per trip, on inputs that go stale in minutes — how busy an area is now, how long a driver has been waiting. A company that only needed batch scoring could live with skew; its errors surface in a monthly report. Uber's surfaced on a rider's phone. It also had many teams building models on the same underlying entities, so recomputing "driver's recent cancellation rate" separately per team was pure waste.

The authors were Mike Del Balso, a product manager, and Jeremy Hermann, an engineering manager. The idea escaped by publication rather than product. In January 2019 Gojek and Google Cloud released **Feast**, an open-source feature store, listing the same problems — features re-engineered team by team, inconsistent definitions, and training-serving skew. Feast's announcement does not cite Michelangelo, so the lineage is shared shape, not documented descent.

## What It Cost

**The guarantee only covers features defined inside the store.** Everything else — a normalisation done in the model code, a join in a notebook, a feature computed by the serving team before the store existed — sits outside it, and skew lives there.

The store also made features a shared dependency. A definition used by twenty models cannot be changed without changing twenty models, which is exactly the entanglement the Google paper warned about, moved one layer down.

## What You Still Touch

Any vendor selling "online/offline consistency" is selling Michelangelo's split: a warehouse table for training, a key-value store for serving, one definition between them.

- [[problems/mlops-platforms/high-impact|🔴 Training-Serving Skew and Silent Degradation]] — the failure the store was built to prevent, outside its boundary
- [[problems/mlops-platforms/low-impact-2|🟡 Feature Store Consistency Guarantees]] — the guarantee's coverage gap
- [[niches/mlops-platforms/training-serving-consistency/profile|Training–Serving Consistency]]
- [[niches/mlops-platforms/feature-coverage-and-lineage/profile|Feature Coverage & Lineage]]

**Sources:** WebSearch was unavailable this session (session cap reached); research was by direct fetch. Mike Del Balso and Jeremy Hermann, "Meet Michelangelo: Uber's Machine Learning Platform," Uber Engineering blog, 5 Sept 2017 (mid-2015 start; pre-platform problems; Hive/Cassandra; Kafka/Samza; ~10,000 features; Scala DSL and the "same expressions" quotation; backfill) — Uber's own account, not independent; D. Sculley et al., "Hidden Technical Debt in Machine Learning Systems," NIPS 28 (2015), abstract read at papers.nips.cc; Tim Sell, Willem Pienaar and Peter Richens, "Introducing Feast: an open source feature store for machine learning," Google Cloud blog, 19 Jan 2019 (checked directly: no mention of Michelangelo). ⚠️ **Not established:** whether anyone used the term "feature store" before Uber's 2017 post — I found no earlier use but could not search for one, so priority is not claimed. The widely repeated link between Michelangelo's authors and the later vendor Tecton could not be confirmed (tecton.ai about page returned 404) and is not asserted. The examples of per-trip, minute-fresh inputs above are illustrative, not quoted; the post gave no per-trip prediction count.
