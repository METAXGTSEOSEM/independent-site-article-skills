# WordPress Content Skills

<p align="center">
  <strong>Turn a content brief into a sourced, reviewed WordPress article.</strong><br>
  Research, drafting, fact-checking, SEO / GEO review, human editing, and a publish-ready package.
</p>

<p align="center">
  <a href="https://github.com/METAXGTSEOSEM/wordpress-content-skills/releases">
    <img src="https://img.shields.io/github/v/release/METAXGTSEOSEM/wordpress-content-skills?display_name=tag&sort=semver" alt="Release">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/github/license/METAXGTSEOSEM/wordpress-content-skills" alt="License: MIT">
  </a>
  <a href="https://github.com/METAXGTSEOSEM/wordpress-content-skills/actions/workflows/validate.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/METAXGTSEOSEM/wordpress-content-skills/validate.yml?branch=main&label=validate" alt="Validate">
  </a>
</p>

<p align="center">
  <a href="#quickstart">Quickstart</a> ·
  <a href="examples/project-management-tool-article/README.md">See a full example</a> ·
  <a href="#workflow-catalog">Workflows</a> ·
  <a href="#installation">Install</a> ·
  <a href="docs/compatibility.md">Compatibility</a> ·
  <a href="docs/faq.md">FAQ</a> ·
  <a href="CONTRIBUTING.md">Contribute</a>
</p>

<p align="center">
  <img src="docs/assets/cover.svg" alt="WordPress Content Skills. Articles available; product pages, case studies, and UI/UX planned." width="1200">
</p>

---
WordPress Content Skills provides evidence-based article writing and review for
WordPress websites. The released article workflow covers research, drafting,
fact-checking, SEO content review, and generative engine optimization (GEO) /
AI search considerations.

Product pages, case studies, and UI/UX improvements are planned as separate
modules with their own briefs, review criteria, and deliverables. They are not
included in the current release.

**Current release:** `1.3.0` · **Available modules:** `1` · **License:** MIT

**Repository:** [METAXGTSEOSEM/wordpress-content-skills](https://github.com/METAXGTSEOSEM/wordpress-content-skills).
The article Skill keeps its existing ID, `independent-site-article`, and version,
`1.1.0`.

The workflow produces a manuscript and WordPress publishing fields. It runs in
a compatible agent host; it is not a WordPress plugin. CMS access and publishing
authorization are separate.

## What you get

- A researched, evidence-based draft in the requested language.
- A visible review decision: `PASS`, `REWORK` or `BLOCKED`.
- Source and claim records, including missing evidence.
- H1, SEO title, meta description, slug, excerpt, image notes and internal-link
  suggestions.
- A WordPress field pack and publishing checklist.
- A separate technical status: `TECH_PASS`, `TECH_REWORK` or `TECH_NOT_CHECKED`.

`PASS` confirms the editorial workflow completed. It does not mean the page has
been published, indexed, ranked or cited by an AI search service.

## Who it is for

- WordPress site owners and editors who publish buying guides or educational content.
- SEO / GEO operators who need a repeatable research and review process.
- B2B teams preparing quote-request or product-education pages.
- B2C teams preparing article-led product content.

It is not an auto-publishing plugin, a ranking guarantee, or a replacement for
legal, regulatory or product-engineering review.

## Quickstart

1. Install the complete `skills/independent-site-article/` folder and the
   required Language Editor listed below.
2. Copy the [example brief](examples/project-management-tool-article/brief.md) or write
   your own.
3. Ask the agent:

```text
Use independent-site-article.

Brief: [paste or link your brief]
Market: [country]
Audience: [reader and knowledge level]
Business model: [B2B or B2C]
Goal: [what the reader should understand or do]
Evidence: [datasheets, first-party material, sources]

Write in English. Research before drafting.
Mark missing product evidence as missing; do not invent it.
Use humanizer for language editing, then an independent final reviewer.
Deliver the article, source and claim records, review report, and WordPress fields.
Do not upload or publish.
```

No specific model, paid research provider or CMS connection is required.
Missing capabilities limit what can be verified.

## See a full example

The [project management tool example](examples/project-management-tool-article/README.md)
shows the complete handoff:

| Stage | File |
| --- | --- |
| Brief | [brief.md](examples/project-management-tool-article/brief.md) |
| Evidence ledger | [sources.csv](examples/project-management-tool-article/sources.csv) |
| Claim checks | [claims.csv](examples/project-management-tool-article/claims.csv) |
| First draft | [draft-v1.md](examples/project-management-tool-article/draft-v1.md) |
| Review decision | [review.md](examples/project-management-tool-article/review.md) |
| Final article | [final.md](examples/project-management-tool-article/final.md) |
| WordPress fields | [wordpress-fields.md](examples/project-management-tool-article/wordpress-fields.md) |

The example is synthetic and clearly labeled. Do not publish its fictional brand,
placeholders or product details as real claims.

## Workflow catalog

| Workflow | Status | Installable Skill | Scope |
| :--- | :--- | :--- | :--- |
| **Articles** | **Available · v1.1.0** | [`independent-site-article`](skills/independent-site-article/SKILL.md) | Blog articles, buying guides, educational content, and existing-article review with research, evidence checks, SEO / GEO review, language editing, and final review. |
| **Product pages** | Planned | Not released | Product specifications, purchase intent, substantiated benefits, comparisons, and conversion review. |
| **Case studies** | Planned | Not released | Customer permission, project evidence, measured outcomes, narrative, and attribution review. |
| **UI/UX improvements** | Planned | Not released | Existing-site audit, page structure, design handoff, responsive behavior, and implementation QA. |

Only **Available** modules can be installed. Planned modules are specifications,
not placeholder Skills. See the [roadmap](docs/roadmap.md) and machine-readable
[catalog](catalog.json).

## Installation

Use your agent host's documented Skill installation method. The source repository is:

```text
https://github.com/METAXGTSEOSEM/wordpress-content-skills
```

1. Download the release ZIP or use a host-supported repository installer.
2. Select only the available article module at `skills/independent-site-article/`.
3. Keep the complete folder, including `SKILL.md`, `references/`, `assets/` and
   `agents/`. Copying only `SKILL.md` leaves required instructions and templates behind.
4. Install the required language editor listed below and make both Skills
   available to the coordinating assistant.
5. Confirm the host can load the Skill and its supporting files before starting
   an article.

For discovery and installation, use only entries marked `available` in
[catalog.json](catalog.json). Planned modules have no installation path.
Installing the article module does not register seven global subagents.

### Language editing dependencies

| Output language | Required Skill | Source |
| :--- | :--- | :--- |
| English, the default | `humanizer` | [blader/humanizer](https://github.com/blader/humanizer) |
| Chinese, only when explicitly requested | `humanizer-zh` | [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh) |

All repository documentation, templates, Skill instructions, and interface
metadata are in English. An explicit article-language request may override the
English output default.

The required editor must actually be available and used. Missing dependencies
are reported; ordinary rewriting is never labeled as a completed Humanizer pass.
Third-party Skill text is not bundled.

## How an article moves through review

```mermaid
flowchart LR
    A[Brief and research] --> B[Draft]
    B --> C[Fact check]
    B --> D[SEO and AI-search review]
    C --> E[Revision]
    D --> E
    E --> F[Humanizer]
    F --> G[Independent final review]
    G -->|Rework| E
    G -->|Pass| H[Delivery]
    H --> I[Authorized CMS QA]
```

| Role | Responsibility |
| :--- | :--- |
| Researcher | Search intent, first-party material, source records, and outline. |
| Writer | Evidence-based drafting and revisions. |
| Fact checker | Claims, figures, specifications, scope, and citations. |
| Search reviewer | Reader intent, SEO, AI-search considerations, and technical unknowns. |
| Language editor | The specified Humanizer, with meaning and sources preserved. |
| Final reviewer | Independent assessment of the exact edited version. |
| Publishing reviewer | CMS and page checks within the authorized scope. |

The coordinator can pass these roles to available general-purpose subagents. A
host without delegation can produce a draft and self-review report, but must mark
independent review as pending.

## WordPress handoff

- [WordPress publishing fields](docs/wordpress-fields.md): H1, SEO title, meta
  description, slug, excerpt, taxonomy, media, schema and B2B/B2C CTA differences.
- [Publishing checklist](docs/publishing-checklist.md): what to verify before,
  during and after publishing.
- [Example field pack](examples/project-management-tool-article/wordpress-fields.md):
  a concrete handoff an editor can review.

The Skill does not write to WordPress by default. A CMS connection, publishing
action or production change requires separate authorization.

## Compatibility and data

- [Compatibility and requirements](docs/compatibility.md): tested and untested
  hosts, optional research, subagent support and review limitations.
- [Data handling and permissions](docs/data-handling.md): what the Skill reads,
  what it writes, and what it does not do by default.
- [FAQ](docs/faq.md): plugin vs Skill, publishing, API keys, languages, SEO
  plugins, missing data and updates.

## Quality boundaries

<details>
<summary><strong>What the workflow will not do</strong></summary>

- Verify current primary sources instead of treating the policy baseline as permanently current.
- Do not invent specifications, testimonials, experience, certifications, statistics, or search data.
- Recheck facts and qualifiers after language editing.
- Do not substitute word-count targets, keyword density, NLP scores, or AI-detector scores for review.
- Keep search-crawler access distinct from model-training permission.
- Require separate authorization for CMS writes, publishing, and production changes.
- Do not promise rankings, indexing, AI citations, or AI-detector results.

</details>

## Project layout

```text
catalog.json                     Available and planned modules
skills/
  independent-site-article/      The installable article workflow
    SKILL.md
    agents/openai.yaml
    references/                  Workflow, roles, and policy sources
    assets/                      Blank production templates
examples/
  project-management-tool-article/  Complete synthetic article package
docs/
  architecture.md                Packaging and compatibility rules
  compatibility.md               Host requirements and limits
  data-handling.md               Reads, writes and permissions
  faq.md                         Common questions
  publishing-checklist.md        WordPress pre/post-publish checks
  roadmap.md                     Planned workflow specifications
  wordpress-fields.md            Field mapping and handoff guidance
scripts/
  validate.py                    Catalog, packaging, language, and link checks
```

To add a workflow, follow [CONTRIBUTING.md](CONTRIBUTING.md). Each installable
module must remain self-contained because a host may copy its folder without the
rest of this repository.

Run the library checks with Python 3.9 or later:

```bash
python3 scripts/validate.py
```

## Community and feedback

- Use the [Bug report](.github/ISSUE_TEMPLATE/bug_report.yml) or
  [Feature request](.github/ISSUE_TEMPLATE/feature_request.yml) template.
- Ask usage questions in [Discussions Q&A](https://github.com/METAXGTSEOSEM/wordpress-content-skills/discussions/categories/q-a).
- Share a redacted output in [Show and tell](https://github.com/METAXGTSEOSEM/wordpress-content-skills/discussions/categories/show-and-tell).

Remove credentials, customer names, private messages and unpublished product
data before posting. An Issue or Discussion is not authorization to publish a
page or change a live site.

## Updates and attribution

Check [CHANGELOG.md](CHANGELOG.md) before updating installed Skills. Preserve
existing Skill identifiers; add new modules rather than expanding the article
workflow into unrelated tasks.

The editorial process draws on evidence-based review and revision practices.
Search guidance is checked against primary documentation, and language editing
uses the specified external projects. See [THIRD_PARTY.md](THIRD_PARTY.md) for
sources and [LICENSE](LICENSE) for the license covering this repository.
