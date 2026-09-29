# Service Catalogue Metadata Decay

**Industry:** [[internal-developer-platforms|Internal Developer Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** The service catalogue is the foundation everything else depends on, and it is populated by asking teams to fill in metadata files that are accurate on the day they are written and never again.
**Tags:** #graph-neural-networks #bert #word-embeddings #gradient-boosting #k-nearest-neighbors #evaluation-metrics #data-integration

## The Problem
Every internal platform rests on a catalogue: what services exist, who owns them, what they depend on, where they run, what tier they are, how to reach the on-call.

It is populated by asking teams to write a metadata file and keep it current. They write it once, during onboarding, and then reality moves. Ownership transfers in a reorganisation. A dependency is added. A service is deprecated but not removed. The on-call rotation changes. The team named in the file no longer exists.

Within a year a meaningful share of entries are wrong, and the failure surfaces at the worst time: during an incident, when someone needs to know who owns a failing service and the catalogue names a team that was dissolved.

Everything built on the catalogue inherits the decay. Scorecards score stale entries. Dependency views are incomplete. Cost allocation misattributes. Access reviews cover the wrong owners.

The information is mostly derivable. Who commits, who deploys, who is paged, what a service actually calls at runtime, and which repository it lives in are all observable, and none of it requires anyone to update a file.

## What Already Exists
Backstage and its commercial equivalents define catalogue schemas and ingest metadata files from repositories. Some ingest from cloud provider APIs and Kubernetes. Dependency discovery from tracing exists in observability tools. Ownership can be partly derived from code owners files. Scorecards enforce completeness by nagging.

## The Customisation Gap
Derivation is preferred to declaration and almost nobody does it. Ownership inferred from commit and deployment activity is more current than any file, because it reflects who is actually working on the service today rather than who was assigned it two reorganisations ago.

Dependency discovery from runtime tracing is available in observability tooling and is rarely joined to the catalogue, which means the catalogue's dependency graph is a hand-drawn approximation of one that already exists in another system.

Staleness scoring is the practical middle ground: rather than demanding everything be current, flag the entries whose declared state contradicts observed behaviour, which turns an unbounded maintenance obligation into a short list.

Lifecycle detection closes the loop at the other end. A service with no deployments, no traffic and no commits for six months is dead, and identifying it is how a catalogue stops growing monotonically — which is the same disease that afflicts dashboards, APIs and every other inventory in this vault.

## Impact If Solved
The catalogue is the foundation of the platform and it is maintained by a declaration that decays from the day it is written. Deriving ownership and dependencies from observable behaviour makes it current by construction, and the failure it prevents — not knowing who owns a failing service during an incident — is the one everyone has experienced.
