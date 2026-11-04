# Building the Bev-Alc Morning Brief

These are the steps a session follows to update the brief. It runs in two cases:
when a viewer picks a timeframe on the brief page, and on the daily schedule.

- Brief page (published): https://claude.ai/artifact/A3w74NNW8EQ4LeH9PgTzy3
- Page source: `bevalc-brief/brief.html` (the copy to edit and publish)
- Source rules: `bevalc-brief/sources.yaml` and the "Bev-Alc Morning Brief" section of `CLAUDE.md`
- Repo: `ryphi90/claude`, branch `claude/add-marketing-skills-zB8Kh`. If the repo isn't checked out, clone that branch first.

## Inputs

The run request is JSON, for example:
`{"timeframe":"7d","label":"Last 7 days","start":"2026-10-29","end":"2026-11-04","runId":"7d-2026-11-04"}`.
The daily run uses `{"timeframe":"today", ...}` for the current date. Dates are inclusive and in US Eastern time.

## Steps

1. **Mark the run started.** In the page's database (ArtifactData, `url` above), update `runs/<runId>` to `status: "running"` and `startedAt` set to now. If the doc doesn't exist, create it.
2. **Apply page blocks.** Read the `blockRequests` collection. For each doc with `status: "pending"`, move that source to `block` in `sources.yaml` and update the doc to `status: "applied"`.
3. **Find what's missing.** Read `meta/coverage` (`{ranges:[{start,end,builtAt}]}`). Only research the days in `start..end` that no range covers yet. Today counts as covered only if its range was built in the last 3 hours. Re-check it for new stories, and if the request says force, rebuild the whole window.
4. **Research those days.** Use web search and Bigdata.com news search to find US three-tier beverage alcohol news published in that window. Follow `sources.yaml` and the CLAUDE.md rules: allow and block lists, English-language only, include awards and rankings, exclude juice and soft drinks, include non-alc only for beer, wine and spirits, keep hemp-THC to a minority. Copy figures exactly from the source.
5. **Add the items to `brief.html`.** Keep the existing items. Add new ones to the right sections in the same markup, with `data-date` (the publication date) and `data-src` (source keys). Never duplicate a story already on the page: merge new coverage into the existing item instead. Add new data points to "The numbers" with `data-date`. Add any new source to the `SOURCES` array in the Sources script, marked `l:0` (new). Update the "Coming up" dates so they are still in the future.
6. **Publish.** Read the artifact first (`Artifact` `action: "read"`, `url` above), then publish `bevalc-brief/brief.html` to that `url`. Omit `capabilities` so the page keeps them. Commit and push `brief.html` and `sources.yaml`.
7. **Record coverage.** Add `{start,end,builtAt}` to `meta/coverage`, merging overlapping ranges. Update `runs/<runId>` to `status: "done"`, with `finishedAt` and `itemsAdded`.
8. **On failure,** update `runs/<runId>` to `status: "failed"` with a one-line `error` that a viewer can act on.
