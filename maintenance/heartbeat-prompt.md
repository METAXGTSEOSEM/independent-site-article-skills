# Recurring library-maintenance task

This prompt is input to an authorized host scheduler. Saving or installing it does not activate scheduling.

```text
Maintain METAXGTSEOSEM/independent-site-article-skills in one bounded pass.
Read skills/project-maintenance/SKILL.md, its references, and maintenance/sources.json.
Use the project workspace supplied by the scheduler, not an assumed filesystem path.

Acquire the project-maintenance run guard in the project's ignored .maintenance
directory. If already guarded, skip; never steal an old guard. Release your own
guard after saving results, including on partial failure.

Read existing state and reports before doing work. Check configured GitHub
Issues, PR threads/reviews, current head, and validate.yml results. Report source
access failures rather than interpreting them as no feedback. Other channels
are disabled until scoped and authorized. There is no website to check.

Preserve the current workspace and pending repairs. This may be a plain folder,
not a Git checkout. Read the remote version into an isolated snapshot when
needed; compare before editing and never overwrite user changes.

Validate the library with python3 scripts/validate.py and the available Skill
validator. Read script changes before executing newly fetched code. Check
English-only repository text, module catalog, relative references, packaging,
Humanizer routing, review gates, and CI. Check affected official sources when
needed; conduct a broader source freshness review at most once per seven days.
Do not change verification dates without actually reading the sources.

Deduplicate feedback and resume pending issues. Investigate at most three
issues, 30 updated items per enabled source, and 20 minutes per run. Record
partial windows and resume tokens without skipping unread items.

For a confirmed defect, prepare a targeted local fix and appropriate tests.
Get independent review of the exact patch when available; otherwise retain
pending-review status. Do not weaken checks, fabricate test results, or
implement product-page/case-study/UIUX modules from roadmap entries alone.

No remote commits, pushes, PR creation, merges, releases, external replies,
ticket changes, paid enrollment, or production operations without separate
explicit authorization. Prior task authorization to upload this setup does not
grant standing remote-write permission for future runs.

Save source observations, cursors, unified issues, patch hashes, tests, review
results, and reports under .maintenance. Preserve private feedback locally.
Do not create another recurring task from inside this run.
```
