# Lineage: Internal Developer Platforms

**Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** the Backstage software catalog and its `catalog-info.yaml` descriptor — a YAML file kept in each repository declaring a component's name, type, lifecycle and required owner, aggregated into one searchable portal
**Builder:** Spotify
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

Nobody could say who owned a service.

Splitting a large application into many small services was supposed to let teams move independently. It worked, and produced a new problem: an inventory nobody kept. A team built a service, the engineer who wrote it changed teams, and the service kept running in production with no one responsible for it. Another team, not knowing it existed, built a second one that did the same thing.

**The cost was not the services. It was asking about them.** Finding the owner, the documentation, the on-call rota or the deploy status of a service meant asking around in chat, one question at a time, and the answer lived in someone's head until that person left.

## What Got Built

A catalogue, and a file that fed it.

Each piece of software gets a descriptor in its own repository, conventionally named `catalog-info.yaml`:

```yaml
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: artist-web
spec:
  type: website
  lifecycle: production
  owner: artist-relations-team
```

Backstage reads these files and assembles them into a single portal: one page per component, linked to its owner, its APIs, its documentation and the infrastructure it runs on. The descriptor defines kinds beyond Component — API, Resource, System, Domain, Group, User, Template — and **`spec.owner` is a required field.** The format will not let a component exist without naming a team.

Templates sit alongside: a scaffolder that generates a new service from a blessed starting point, already registered in the catalogue — the "golden path."

## Who Built It, And Why Them

Spotify — and the reason is its organisational model more than its scale.

Spotify had publicised its engineering culture as small, autonomous squads, each owning its own services end to end. That model maximises the rate at which new services appear and minimises anyone's obligation to tell anyone else about them. By Gergely Orosz's account, the internal catalogue began in **2014 under the name System Z**, in response to service sprawl — "Spotify was spinning up new services weekly, or even more frequently" — duplicated work, fragmentation, and services becoming "unowned" after their creator moved on. Growth in its use led to a **rewrite in 2017** into what became Backstage.

A company that had deliberately removed central coordination needed a way to recover the inventory without reintroducing a gatekeeper. A file in each repo, owned by the team that owns the code, fit the autonomy model; a central registry run by an operations team would not have.

Spotify open-sourced Backstage on **16 March 2020**, in an announcement by Stefan Ålund. By then, it said, over 280 teams used it to manage 2,000+ backend services, 300+ websites, 4,000+ data pipelines and 200+ mobile features. The CNCF accepted it into its Sandbox on 8 September 2020 and moved it to Incubating on 15 March 2022.

## What It Cost

**The catalogue is only as true as the files, and the files are written by hand.**

`catalog-info.yaml` records what a team declared on the day it wrote the file. Teams reorganise, services change hands, lifecycles move from production to deprecated, and nothing updates the YAML unless someone remembers. The required `owner` field guarantees a name is present; it does not guarantee the name is still right.

Templates carry the same trade. A scaffolded service matches the golden path on the day it is generated and drifts from it every day after, because generation is one-way.

And Backstage is a framework, not a product. Adopters inherit a React and Node codebase to assemble and maintain, which is why a portal can be installed and then sit mostly unused.

## What You Still Touch

If your repository has a `catalog-info.yaml` at its root with an `owner:` line naming a team that was renamed last year, you are looking at the artefact and its cost together.

- [[problems/internal-developer-platforms/low-impact-1|🟡 Service Catalogue Metadata Decay]] — the hand-written descriptor, ageing
- [[problems/internal-developer-platforms/low-impact-2|🟡 Golden Path Drift After Generation]] — one-way templates
- [[niches/internal-developer-platforms/service-catalogue-accuracy/profile|Service Catalogue Accuracy]]
- [[niches/internal-developer-platforms/golden-path-drift/profile|Golden Path Drift]]

**Sources:** Backstage documentation, *Descriptor Format of Catalog Entities* (the Component example, `spec.owner` "This field is required", entity kinds); Stefan Ålund, "Announcing Backstage", backstage.io blog, 16 March 2020 (usage figures); Gergely Orosz, "Backstage: an Open-Source Developer Portal", *The Pragmatic Engineer* newsletter (System Z, 2014; the four problems quoted; 2017 rewrite); CNCF project page and Backstage blog, 23 September 2020 (Sandbox acceptance 8 September 2020; Incubating 15 March 2022). ⚠️ **Not established:** whether System Z used a per-repository YAML descriptor or a central registry — the `catalog-info.yaml` format is documented only for the open-source project, and I found no source dating its design. The names of System Z's original builders were not found and are not given. The reading that the squad model *caused* the sprawl is this note's inference; the Orosz account lists the sprawl but does not attribute it to the squad model. The "installed then unused" adoption pattern is widely discussed but no measured figure was checked.
