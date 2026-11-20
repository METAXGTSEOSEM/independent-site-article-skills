# Worked example: fixed scissor lift buying guide

This folder is a synthetic demonstration of the article workflow. The company,
product details and example copy are illustrative. Do not publish the sample as
a real product page or treat its placeholders as verified specifications.

It shows the handoff from a short brief to a reviewed, publish-ready package:

| File | Purpose |
| --- | --- |
| `brief.md` | Input brief with audience, goal and evidence limits. |
| `sources.csv` | Source ledger, including deliberately missing evidence. |
| `claims.csv` | Claim-level checks and the evidence each claim needs. |
| `draft-v1.md` | First draft with reviewable weaknesses. |
| `review.md` | Version-specific `REWORK` decision and required changes. |
| `final.md` | Revised article after the findings were addressed. |
| `wordpress-fields.md` | Publishing fields and handoff notes. |

## What the example demonstrates

- The draft is not accepted just because it reads well.
- Unsupported product or safety claims are removed or qualified.
- Missing manufacturer data stays visibly missing instead of being invented.
- SEO and AI-search guidance does not override factual accuracy.
- The final package includes fields a WordPress editor can use directly.

## Run the same workflow

```text
Use independent-site-article.

Use the example brief at:
examples/fixed-scissor-lift-article/brief.md

Produce a new article package. Keep missing product evidence marked as missing.
Do not invent load ratings, certifications, prices, lead times or test results.
Before drafting, show the research plan and the questions that require the
manufacturer or site owner to answer.
```

The sample is intentionally generic. A real project must use the current
manufacturer datasheet, site conditions, destination-market requirements and
approved company claims.
