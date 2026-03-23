# Wiki-Link Patterns

**Every link you write MUST match the patterns below. A broken link breaks the vault. Verify every link resolves to an actual file before writing it.**

---

## Industry Profile → Problem Cards

From `problem-index/industries/{id}.md`:

```
- [[problems/{id}/high-impact|🔴 High Impact: {short title}]]
- [[problems/{id}/low-impact-1|🟡 Low Impact: {short title}]]
- [[problems/{id}/low-impact-2|🟡 Low Impact: {short title}]]
- [[problems/{id}/worker-life-1|🟢 Worker Life: {short title}]]
- [[problems/{id}/worker-life-2|🟢 Worker Life: {short title}]]
- [[problems/{id}/ml-opportunity|🔵 ML Opportunities]]
- [[problems/{id}/ai-agents-platforms|🤖 AI Agents & Platforms]]
```

## Problem Card → Industry Profile

From any `problem-index/problems/{id}/*.md`:

```
**Industry:** [[{id}|{Industry Name}]]
```

## ML Opportunity → Problem Cards

From `problem-index/problems/{id}/ml-opportunity.md`:

```
**Derived from:** [[problems/{id}/high-impact|High Impact]], [[problems/{id}/low-impact-1|Low Impact 1]], [[problems/{id}/low-impact-2|Low Impact 2]], [[problems/{id}/worker-life-1|Worker Life 1]], [[problems/{id}/worker-life-2|Worker Life 2]]
```

## Niche Overview → Niche Profiles

From `problem-index/niches/{industry-id}/_overview.md`:

```
- [[niches/{industry-id}/{niche-id}/profile|{emoji} {Niche Name}]]
```

Emoji codes: 🔵 = High Market Share, 🟠 = Low Digitized, 🟣 = Underserved Audience, ⚡ = Highly Automatable

## Niche Profile → Problem Files

From `problem-index/niches/{industry-id}/{niche-id}/profile.md`:

```
**Parent Industry:** [[industries/{industry-id}|{Industry Name}]]

- [[niches/{industry-id}/{niche-id}/build|🔨 Build: {title}]]
- [[niches/{industry-id}/{niche-id}/buy|🛒 Buy: {title}]]
- [[niches/{industry-id}/{niche-id}/fix|🔧 Fix: {title}]]
```

## Niche Problem Files → Profile & Industry

From `problem-index/niches/{industry-id}/{niche-id}/{build|buy|fix}.md`:

```
**Niche:** [[niches/{industry-id}/{niche-id}/profile|{Niche Name}]]
**Industry:** [[industries/{industry-id}|{Industry Name}]]
```

## Learning Plan → Vault Problems

From `problem-index/plans/{tag-id}/project-{N}.md`:

```
**Source Problem:** [[problems/{industry-id}/ml-opportunity|{Industry} ML Opportunities]]
```

## Bookmark Files

Both `_bookmark.md` files use simple industry links:

```
- [[behavioral-health-clinics]]
```

---

## Rules

1. All wiki-links MUST match actual file paths in the vault (minus the `.md` extension)
2. Use the `[[path|Display Text]]` format for human-readable labels
3. Paths are relative to the vault root (`problem-index/`)
4. NEVER link to `.obsidian/` configuration files
