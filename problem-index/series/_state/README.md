# Phase 3 state

Durable helpers for the history layer. Nothing here is generated at runtime — it is the
source data H1 produced and later stages consume.

| File | What it is |
|---|---|
| `wave-assignment.txt` | `slug\|primary-wave\|secondary-wave` for all 250 industries. The authoritative assignment; `series/_eras.md` is rendered from it. |
| `kids.sh` | `./kids.sh <wave> <primary\|secondary>` — emits the wikilink list of a wave's child industries. |

Regenerate a wave's children:

```bash
series/_state/kids.sh 6 primary
```

Verify the assignment still covers exactly the 250 industries:

```bash
comm -3 <(cut -d'|' -f1 series/_state/wave-assignment.txt | sort) \
        <(ls industries | sed 's/\.md$//' | sort)   # must print nothing
```
