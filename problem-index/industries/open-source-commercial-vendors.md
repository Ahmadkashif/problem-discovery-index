# Open Source Commercial Vendors

## Profile
**Category:** Developer Tools & Infrastructure
**Market Size:** ~$30B US revenue attributable to commercially backed open-source software
**Tech Maturity:** Technically excellent, commercially precarious — HashiCorp, Elastic, MongoDB, Redis, Grafana Labs, Databricks and hundreds of smaller companies build genuinely important software in the open and struggle to convert its use into revenue. Several have changed licences under exactly this pressure.
**Workforce:** Core maintainers, community managers, developer relations, support engineers, product managers for commercial editions, licence and compliance staff

## Key Pain Themes
The category's defining problem is that adoption is invisible and conversion is unmeasurable. Downloads and stars measure attention rather than use, and the companies deriving the most value from the software are frequently the ones the vendor has never heard of. Every commercial decision — where to invest, what to put behind a licence, who to reach out to, whether the open-source strategy is working at all — is made without knowing who is actually running the software or how. Around that sit two chronic burdens: the maintainer queue, where a small team triages issues and contributions from a community much larger than itself; and the open-core boundary, redrawn repeatedly because nobody can measure which features actually drive purchase. Support engineers carry the additional weight of serving both paying customers and a community whose problems are identical, and maintainers burn out at rates the industry acknowledges and does not address.

## Current Tech Landscape
The commercial models are open core, hosted service, and support subscription, frequently in combination. Licence changes — to Business Source, SSPL or Elastic-style licences — have become common enough to be a recognised phase, usually triggered by a hyperscaler offering the software as a service. Foundations provide governance neutrality for some projects. Package registries and container registries provide download telemetry of very limited fidelity. Product analytics in open-source software is contentious and often disabled by default. Community platforms are fragmented across issue trackers, forums, chat and social media.

## Problems
- [[problems/open-source-commercial-vendors/high-impact|🔴 High Impact: Adoption That Cannot Be Seen]]
- [[problems/open-source-commercial-vendors/low-impact-1|🟡 Low Impact: The Maintainer Triage Queue]]
- [[problems/open-source-commercial-vendors/low-impact-2|🟡 Low Impact: Drawing the Open-Core Boundary]]
- [[problems/open-source-commercial-vendors/worker-life-1|🟢 Worker Life: Maintainer Burnout]]
- [[problems/open-source-commercial-vendors/worker-life-2|🟢 Worker Life: Support Across the Paid and Free Boundary]]
- [[problems/open-source-commercial-vendors/ml-opportunity|🧠 ML Opportunities]]
- [[problems/open-source-commercial-vendors/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
Open-source vendors are the only software companies with a structurally invisible customer base. A proprietary vendor knows every installation; an open-source vendor knows downloads, which conflate a build cache with a production deployment. The public signals that do exist — issues, discussions, public code, conference talks, job postings, container manifests — are abundant, textual and scattered, and reconstructing adoption from them is the analytical problem underneath every commercial decision the category makes.
