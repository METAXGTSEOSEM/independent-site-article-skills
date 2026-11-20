# Compatibility and requirements

## What the Skill needs

- A host that can load a folder containing `SKILL.md`, `references/`, `assets/`
  and `agents/`.
- Permission to read the supplied brief and write output files in the workspace.
- The `humanizer` Skill for English language editing, or `humanizer-zh` when
  Chinese output is explicitly requested.
- Optional web research access for current sources.
- Optional subagent or delegation support for an independent final review.

No specific model, paid research provider or CMS connection is required.

## Tested and untested hosts

| Host type | Status | Notes |
| --- | --- | --- |
| Codex-style multi-file Skill environment | Tested | Used for the development and review workflow in this repository. |
| Other folder-based Skill hosts | Expected but not verified | Confirm that the host loads supporting files and can write outputs. |
| Chat-only interfaces | Not supported without adaptation | They generally cannot load the folder or preserve the review artifacts. |

Do not treat "compatible" as a guarantee. Check the host's current Skill
documentation and run one small article before relying on it for production.

## Invocation

Use the host's explicit Skill invocation where available, for example
`$independent-site-article`. If the host only supports automatic selection,
include the Skill name and the full brief in the request.

## Review without subagents

If the host cannot delegate, the coordinator can still produce a draft and a
self-review report. The independent final review must then be marked as pending.
Do not label self-review as independent.

## Research access

Without web access, the workflow can still organize supplied evidence and draft
from it. It must mark current facts, regulations and competitor claims as
unverified. Do not invent search volumes, rankings, citations or product data
to compensate for missing access.
