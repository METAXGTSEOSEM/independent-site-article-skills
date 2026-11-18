# Changelog

## 1.2.0 - 2026-11-18

- Add the self-contained `project-maintenance` Skill alongside the article module.
- Integrate multi-channel feedback intake, deduplication, revision-bound review, and repository checks.
- Configure GitHub Issues, PR feedback, and CI for this library; leave other channels disabled until scoped and authorized.
- Exclude website feedback and website monitoring because there is no website to maintain.
- Add a local run guard, state templates, a recurring-run prompt, and maintenance documentation.
- Keep remote changes and external replies separate from the default local-repair authorization.
- Add a daily validation schedule in GitHub Actions; this is a structural check, not an autonomous repair agent.

## 1.1.0 - 2026-11-17

### Library

- Present the repository as Independent Site SOPs, a modular workflow library.
- Add a machine-readable catalog and extension architecture.
- Reserve product-page, case-study, and UI/UX modules as planned work.
- Add contribution instructions and repository validation.
- Redesign the README with a local SVG cover, navigation, module status, and workflow diagram.

### Article module

- Translate all instructions, templates, references, and interface metadata into English.
- Default output to English while retaining explicitly requested Chinese editing through `humanizer-zh`.
- Preserve the Skill identifier and repository URL for existing installations.
- Retain factual verification, specified Humanizer routing, version-bound independent review, and separate publishing authorization.

## 1.0.0 - 2026-11-17

- Publish the first article-production Skill.
- Include research, writing, fact-checking, search review, language editing, independent review, and optional CMS QA.
- Include source, claim, brief, and delivery templates.
