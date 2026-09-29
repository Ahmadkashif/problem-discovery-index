# The Field That Says Publisher

**Niche:** [[niches/music-distribution-platforms/metadata-capture-at-upload/profile|Metadata Capture at Upload]]
**Industry:** [[industries/music-distribution-platforms|Music Distribution Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The artist has no publisher, the field is required, and they type their own name.
**Tags:** #quick-win #worker-facing #evaluation-metrics #automation #workflow-orchestration #descriptive-statistics #compliance #large-language-models
**Contested on:** Every serious competitor in this niche is fighting to get correct rights data out of an artist who does not know what a publisher is — and whoever designs that capture well prevents the matching problem instead of repairing it downstream.

## The Problem
The form requires a publisher. The artist is unpublished, does not know what the field means, cannot proceed without filling it, and enters their own name or something arbitrary. That entry is now a claim about rights administration that propagates into registries and statements. The same happens with performing rights organisation fields, identifier fields and role fields — required inputs that many uploaders cannot answer correctly and must answer to continue.

## Why It's Still Broken
The field is required because the downstream specification requires it, so the form enforces completeness rather than correctness — a validation that checks whether something was entered cannot check whether it is true. Nobody measured what gets entered. Support handles the consequences individually. And a blocked upload is a support ticket, so the path of least resistance is to accept anything.

## What a Fix Looks Like
Let people say they do not have one. Offer an explicit "no publisher" option and handle it correctly downstream, which is the fix and removes the most common forced fabrication in the flow. Explain what the field means in one sentence at the point of entry, since a large share of errors are comprehension rather than carelessness. Report what is actually being entered in these fields, as the distribution will show the problem immediately and nobody has looked. Detect obviously invalid entries — the artist's own name as a publisher, placeholder text, repeated characters — and ask again with an explanation. Validate against membership and registry data where it exists, which resolves the answerable cases automatically. Do not require what is not knowable, because forcing an answer guarantees a wrong one. Tell the artist what the consequence of getting it wrong is, since the motivation is entirely absent today. Offer the registration step rather than only the field, as an unregistered writer needs to register and the form is the moment they are thinking about it. Make the correction path work after release, because the current permanence is what makes each error expensive. And measure downstream match rate by entry pattern, which connects capture quality to the money.

## Who Feels the Pain
Artists entering claims they do not understand; writers whose royalties are misdirected by a placeholder; support agents unpicking it later; and registries receiving assertions nobody checked.

## Impact If Fixed
A validation that checks whether something was entered cannot check whether it is true, so a required field guarantees a fabricated answer. An explicit "no publisher" option plus one sentence of explanation removes the most common forced error in the flow.
