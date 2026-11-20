# WordPress publishing fields

The article workflow produces a manuscript and a field pack. The field pack is
not a replacement for editorial review, and it does not publish anything.

## Recommended fields

| Field | What to provide | Practical guidance |
| --- | --- | --- |
| H1 | One clear page title | Match the article's promise; avoid stuffing keywords. |
| SEO title | Search-facing title | Often around 50-60 characters, but check the actual SERP and plugin preview. |
| Meta description | Short summary with a reason to click | Often around 140-160 characters; write for the reader, not a fixed keyword density. |
| Slug | Short, readable URL path | Use lowercase words and hyphens; avoid dates unless the article is date-specific. |
| Excerpt | Editorial summary | Useful for archives, newsletters and internal previews. |
| Categories | One or two primary categories | Use the site's existing taxonomy instead of creating near-duplicates. |
| Tags | Specific entities or topics | Keep the set small and consistent with the site's tagging rules. |
| Featured image | Licensed or client-supplied image | Record the source and permission. |
| Image alt text | Description of the image | Describe what is visible and relevant; do not repeat the keyword mechanically. |
| Internal links | Related pages on the same site | Verify the destination exists and is published. |
| CTA | The next step for the reader | Match the business model: B2B inquiry, B2C purchase or further reading. |

Field-length guidance is practical, not a ranking rule. Search engines may
rewrite titles and descriptions.

## SEO plugin mapping

Labels vary by plugin and version. In Yoast SEO and Rank Math, map the output to
the equivalent title, description, slug, canonical, social image and schema
controls. Do not assume that identical labels behave identically across
versions.

If the plugin already outputs `Article` schema, do not add a second competing
block. Check the rendered page and the plugin's schema settings before adding
FAQ, Product, HowTo or Breadcrumb markup.

## Canonical and indexability

- Set the canonical to the intended public URL.
- Keep the page indexable unless there is a documented reason to noindex it.
- Do not index staging URLs, duplicate variants or thin category pages.
- Check hreflang and multilingual settings separately when the site uses them.

## B2B and B2C differences

| Decision | B2B inquiry page | B2C product content |
| --- | --- | --- |
| Primary action | Request a quote, sample or consultation | Add to cart or buy |
| Evidence | Specifications, compatibility, documentation, service terms | Product details, delivery, returns, reviews with permission |
| Qualification | Task, volume, destination, timeline | Variant, price, shipping and return expectations |
| Success signal | Qualified inquiry, not just a form click | Order and margin, not just add-to-cart |

Do not use the same CTA or success metric for both without a deliberate reason.

## Verification before publishing

1. Every specification has a source or is marked as missing.
2. The H1, SEO title and meta description describe the same page.
3. Internal links resolve.
4. Images and quotes have permission.
5. Schema matches visible content.
6. The CTA is appropriate for the business model.
7. A human has approved the final version.

See [the publishing checklist](publishing-checklist.md) for the operational
sequence.
