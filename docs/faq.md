# FAQ

## Is this a WordPress plugin?

No. It is a set of agent instructions and templates. It produces a manuscript
and publishing fields; it does not install into WordPress.

## Does it publish automatically?

No. Publishing, scheduling, CMS writes and live-site changes require separate
authorization and a human review.

## Does it need an API key?

No specific paid API is required. Optional research tools and the external
Humanizer Skill have their own setup and terms.

## Does it guarantee rankings, traffic or AI citations?

No. It supports research, structure, evidence checks and review. It cannot
guarantee indexing, rankings, traffic, conversions or citation by an AI search
service.

## Can it write Chinese?

Yes, when Chinese output is explicitly requested. The workflow then uses
`humanizer-zh` for language editing. English is the default.

## Which SEO plugin does it support?

The output is plugin-agnostic. Map the fields to Yoast SEO, Rank Math or the
site's existing setup. Plugin labels and behavior vary by version.

## What happens when product data is missing?

The workflow marks it as missing or asks for it. It must not invent load
ratings, dimensions, certifications, prices, lead times, warranties or test
results.

## Can I use it for Shopify?

The article workflow can produce general content, but the field pack is
WordPress-oriented. A Shopify implementation needs its own field mapping and
theme checks.

## How do I update an installed Skill?

Read the changelog, replace the complete Skill folder, and keep the same Skill
identifier. Do not copy only `SKILL.md`; the references and templates are part
of the workflow.

## Who owns the generated content?

The repository license covers the Skill material. The output is subject to your
own agreements, the rights of any sources or images you use, and the terms of
the tools you run. This is not legal advice.
