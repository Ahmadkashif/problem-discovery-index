# Cross-Tool Dependency Graph

**Parent Industry:** [[industries/work-collaboration-tools|Work Collaboration Tools]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in integration is fighting to turn pairwise field syncing into a single graph of what blocks what across the whole tool estate — and whoever holds that graph owns the question every executive asks and no integration answers.

## Profile
**Market Size:** ~$1.4B US integration platform and connector spend attributable to work-tool interoperability
**Share of Parent Industry:** ~7% of collaboration software revenue
**Digital Adoption:** High for connectors, near zero for cross-tool dependency
**Target Buyer:** Operations, IT and programme management at companies with a multi-tool estate
**Automation Potential:** Very High — the dependency information exists as text and structure in the tools already

## What Makes This a Distinct Niche
Integration marketplaces are enormous and every connector does the same thing: it syncs fields between two named tools when a trigger fires. A company with nine tools therefore has up to thirty-six brittle pairwise links, each maintained by whoever set it up, each breaking silently when a field is renamed — and after all that, still cannot answer whether the design decision recorded in the design tool is blocking the engineering ticket that is blocking the launch tracked in the programme plan. That question needs a graph, not a set of edges maintained bilaterally. The distinction matters because the two are sold as the same thing: integration vendors describe themselves as connecting a company's stack when what they connect is pairs of records, and the difference only becomes apparent when someone asks what is actually blocking the launch.

## Current Tools & Gaps
Integration platforms with large connector libraries; native integrations between major work tools; enterprise service buses and iPaaS at the larger end; and a small number of dependency-mapping features inside single platforms. The gaps: everything is pairwise, so dependency is never transitive and a chain through three tools is invisible; dependency is expressed in prose — "waiting on the API work" — which no connector reads; sync failures are silent, so the graph degrades without notice; and no product presents a critical path across tools, which is the output the whole arrangement exists to produce.

## Problems
- [[niches/work-collaboration-tools/cross-tool-dependency-graph/build|🔨 Build: Thirty-Six Pairwise Links and No Graph]]
- [[niches/work-collaboration-tools/cross-tool-dependency-graph/buy|🛒 Buy: Entity Resolution and Critical Path, Applied Across Tools]]
- [[niches/work-collaboration-tools/cross-tool-dependency-graph/fix|🔧 Fix: Integrations Fail Silently and Nobody Is Watching]]
