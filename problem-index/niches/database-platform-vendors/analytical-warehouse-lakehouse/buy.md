# Physical Design Advisors for Columnar Layouts

**Niche:** [[niches/database-platform-vendors/analytical-warehouse-lakehouse/profile|Analytical Warehouse & Lakehouse]]
**Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Automated physical design — choosing indexes, partitions and materialised views from a workload — is a mature database research area, and lakehouse layout is chosen by a data engineer's judgement.
**Tags:** #optimization-fundamentals #dynamic-programming #convex-optimization #gradient-boosting #evaluation-metrics #confidence-intervals #automation #graph-theory
**Contested on:** Every serious competitor here is fighting to make a large query cheap and a hundred concurrent users fast without locking the customer's data into a format they cannot leave — and whoever does that takes the data platform account, because cost at scale and openness are the two things that decide it.

## The Problem
Choosing the physical design of a database from an observed workload — which indexes, which partitions, which materialised views, subject to a storage budget — is automated physical design, studied for decades with advisor tools shipped in several commercial engines. The analytical equivalent is partitioning, clustering, file sizing, compaction and materialisation, which determines query cost enormously and is decided by a data engineer's judgement and adjusted when something becomes slow.

## What Already Exists
Index and view selection algorithms with formal treatment; materialised view selection and query rewriting; workload-driven partitioning research; the what-if optimiser interfaces several engines expose for evaluating hypothetical designs; and the compaction and layout optimisation literature emerging around open table formats.

## The Customization Gap
The adaptation is to columnar storage on object storage with open formats. It requires: (1) a cost model reflecting object storage economics, where the dominant term is bytes scanned and file count rather than random access, which changes the design objective substantially from the classical formulations; (2) clustering and sort order as the main levers rather than secondary indexes, since data skipping depends on how well the layout correlates with the filters and this is where most of the available saving is; (3) file sizing and compaction as first-class decisions, because too many small files and too few large ones both degrade performance badly and the trade-off depends on the query mix; (4) format-neutral recommendations, since the customer's strategic requirement is openness and a design that only works on a proprietary path undermines the thing they are buying; and (5) continuous rather than one-off design, because analytical workloads shift as dashboards and models change, and a layout tuned once decays exactly as an index set does.

## Target Customer
Warehouse and lakehouse vendors, the open table format projects, data platform teams, and the query acceleration vendors.

## Impact If Solved
A mature physical design discipline maps onto a layout problem currently solved by judgement, in a setting where the cost consequence is directly monetary. Object storage economics and clustering-as-the-main-lever are the two adaptations, and format neutrality is what keeps the recommendation aligned with why the customer chose a lakehouse.
