# The Inquiry Corpus as a Demand Signal on Research Coverage

**Niche:** [[niches/cloud-infrastructure-consultants/it-research-advisory-firms/profile|IT Research & Advisory Firms]]
**Industry:** [[industries/cloud-infrastructure-consultants|Cloud Infrastructure Consultants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Clients place hundreds of thousands of inquiry calls a year describing exactly what they are deciding and what the published research failed to answer, and the research agenda is set by analyst judgment instead.
**Tags:** #bert #transformers #large-language-models #word-embeddings #k-means-clustering #contrastive-learning #evaluation-metrics #tacit-knowledge-ml #data-integration #revenue-impact

## The Problem
The inquiry call is the firm's most distinctive asset and its least exploited one. An enterprise client with a live decision calls an analyst and describes the situation in detail: what they are evaluating, what constraints they face, what the published note did not settle. Across a large firm this happens at enormous volume and produces a picture of enterprise technology decision-making that no survey, scrape, or vendor briefing can match. The calls are recorded and logged for service management — analyst, client, topic, duration — and the substance is captured, if at all, in analyst notes written for their own recall. The research agenda is meanwhile set through planning cycles driven by analyst judgment about what matters, which is informed by the calls only through whatever each analyst happens to remember and volunteer.

## Why Nobody Has Built This
Client confidentiality is real and binding — enterprises describe unannounced strategy on these calls, and any system touching that content has to be architected so that individual client situations cannot leak into published research, which is a genuine constraint rather than an excuse. Analyst independence is also a load-bearing part of the value proposition, and there is a legitimate concern that a demand-driven agenda would chase volume rather than importance. And structurally, inquiry sits in service delivery while research agenda-setting sits in the research organization, with no shared instrumentation between them.

## What to Build
An inquiry intelligence layer that extracts pattern without exposing particulars. Calls are transcribed and structured into the decision being made, the technologies under consideration, the constraints cited, and the specific question the published research left open — with client identity and identifying detail stripped at the point of extraction rather than protected downstream, so the aggregate corpus cannot reconstruct any individual situation. What that yields is a demand map: which decisions enterprises are actually facing, at what volume, in what sequence, and where the published corpus is failing them. Three distinguishable failure modes fall out, exactly as they do in every content business — research that exists but is unfindable, research that exists and is insufficient, and questions the firm has never covered. The third is where the agenda should be pointed and currently is not. It also produces a leading indicator the firm can sell in its own right: inquiry volume shifts precede published market movement by months, because clients call while deciding rather than after.

## Target Customer
Chiefs of research and SVPs of research operations at advisory firms running 1,000-4,000 analysts, and the service delivery leaders whose inquiry volume is currently a capacity metric rather than an intelligence source.

## Impact If Built
Points the largest research organization in the technology industry at what its clients are actually asking, which is a coverage improvement no amount of additional analyst headcount produces. The inquiry corpus is also the firm's only genuinely non-replicable asset — competitors can hire analysts and brief with the same vendors, and none of them can observe enterprise decisions in progress at this volume. Structuring it is the difference between holding that asset and merely possessing it.
