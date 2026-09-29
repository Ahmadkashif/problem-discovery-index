# MLOps Platforms

## Profile
**Category:** Data & AI Economy
**Market Size:** ~$3B US machine learning operations tooling, fragmenting rather than consolidating
**Tech Maturity:** Excellent at recording, poor at concluding — Weights & Biases, MLflow, Databricks, SageMaker, Vertex AI, Comet and Neptune capture experiments, artefacts, lineage and metrics with real fidelity. Almost none of them answer the question every team actually has, which is whether the model in production is still working and why it stopped.
**Workforce:** Platform engineers, ML infrastructure engineers, developer advocates, solutions architects, support engineers, GPU capacity and scheduling operations

## Key Pain Themes
The category solved experiment tracking and has not solved production. A model is trained, evaluated on a held-out set, deployed, and then degrades — through data drift, upstream schema changes, a feature computed differently at serving time than at training time, or a genuine change in the world — and the first signal is usually a business metric moving weeks later. Training-serving skew in particular is the most common and most expensive failure in applied machine learning and is detected by almost no platform. Around it sit two persistent burdens: instrumentation coverage, where tracking works beautifully for the frameworks the vendor supports and requires bespoke work for anything else; and feature consistency, where feature stores exist and the guarantee they were built to provide is honoured inconsistently. The engineers carrying it are paged for pipeline failures at unsociable hours and spend their days on GPU scheduling arithmetic.

## Current Tech Landscape
Weights & Biases owns experiment tracking mindshare among research teams; MLflow is the open default and is now largely a Databricks asset; the hyperscaler platforms bundle tracking with compute. Feature stores (Feast, Tecton, and the platform-native offerings) address training-serving consistency and are adopted unevenly. Model monitoring is a separate category (Arize, WhyLabs, Fiddler, Evidently) precisely because the training platforms did not extend into it. Orchestration is fragmented across Airflow, Dagster, Prefect, Flyte and Kubeflow. The rise of foundation model applications has shifted attention toward LLM-specific observability, leaving classical ML operations comparatively neglected.

## Problems
- [[problems/mlops-platforms/high-impact|🔴 High Impact: Training-Serving Skew and Silent Degradation]]
- [[problems/mlops-platforms/low-impact-1|🟡 Low Impact: Instrumentation Coverage Across Frameworks]]
- [[problems/mlops-platforms/low-impact-2|🟡 Low Impact: Feature Store Consistency Guarantees]]
- [[problems/mlops-platforms/worker-life-1|🟢 Worker Life: ML Engineer on the Pipeline Page]]
- [[problems/mlops-platforms/worker-life-2|🟢 Worker Life: Platform Engineer Rationing GPUs]]
- [[problems/mlops-platforms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/mlops-platforms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
These platforms hold the most complete record of how machine learning is actually practised: millions of training runs with hyperparameters, datasets, code versions, metrics and outcomes, across thousands of organisations. That is the empirical basis for questions the field answers with folklore — which hyperparameter search strategies actually pay for themselves, how much a given architecture change is typically worth, whether an experiment is worth continuing at epoch three. Every vendor sits on this and ships a chart.
