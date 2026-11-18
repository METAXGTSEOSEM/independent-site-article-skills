# Workflow roadmap

This page defines intended modules. It is not a claim that planned Skills are implemented, installable, or tested.

## Available: articles

**ID:** `independent-site-article`

Research, draft, fact-check, review for search, edit with the specified Humanizer, and independently review the final version. Optional CMS QA stays separate from writing.

## Available: project maintenance

**ID:** `project-maintenance`

Use configured feedback, repository checks and CI to investigate problems, prepare local fixes and obtain review. Runtime scheduling and source credentials are separate. This module maintains the library; it does not expand the writing workflow or implement roadmap items without a request.

## Planned: product pages

**Reserved ID:** `independent-site-product-page`

### Inputs

Actual product identity, specification revision, target buyer, market, available variants, substantiated capabilities, pricing scope, images, and purchase or inquiry path.

### Expected responsibilities

Product research, specification verification, buyer-intent analysis, copywriting, conversion review, language editing, independent final review, and CMS QA.

### Acceptance criteria to develop

- Each number and capability maps to the correct model and source.
- Benefits do not exceed verified features and operating conditions.
- Certification, warranty, delivery, price, and compatibility claims have a defined scope.
- Images, variant tables, metadata, and CTA agree with the product.
- Appropriate structured data does not conflict with visible content or plugin output.
- B2B inquiry and B2C checkout journeys are handled separately.

This module will produce a product-page package, not a renamed blog article.

## Planned: case studies

**Reserved ID:** `independent-site-case-study`

### Inputs

Customer permission, project dates, original problem, actual solution, source material, measured outcomes, approved quotes, and confidentiality limits.

### Expected responsibilities

Interview or source review, permission and evidence checks, narrative writing, outcome verification, language editing, independent final review, and publishing QA.

### Acceptance criteria to develop

- Customer names, photos, quotes, and confidential details have permission.
- Baseline, measurement window, sample, and calculation are explicit.
- Correlation is not presented as proven causation.
- An anonymized case is still traceable internally.
- A hypothetical example cannot be labeled as a real customer result.

## Planned: UI/UX improvements

**Reserved ID:** `independent-site-uiux`

### Inputs

Existing URL or screenshots, platform and editor, brand constraints, reader tasks, analytics where available, implementation access, and staging or rollback arrangements.

### Expected responsibilities

UX audit, information architecture, visual design, platform implementation, accessibility review, performance review, and evidence-based acceptance.

### Acceptance criteria to develop

- Findings cite actual page behavior or observed evidence.
- The design addresses a stated user task.
- Changes fit the real WordPress theme/editor or Shopify implementation.
- Mobile, keyboard, focus, readable contrast, forms, and errors are checked.
- URLs, SEO controls, tracking, and inquiry or checkout paths are preserved or intentionally migrated.
- Production changes and rollback are separately authorized.

Design references are inputs, not instructions to copy another brand's assets or identity.

## Adding other workflows

Propose the user request, required inputs, deliverables, evidence needs, reviewers, and acceptance criteria first. Reuse an existing module for a minor mode; create a separate module when the job has a different contract.

Prioritization and release dates remain open. Planned modules become available only after implementation and validation.
