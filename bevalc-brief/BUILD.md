# Building the Bev-Alc Morning Brief

These are the daily steps for building one edition. Each edition covers the last 24 hours and replaces the one before it on the page.

- Brief page (published): https://claude.ai/artifact/A3w74NNW8EQ4LeH9PgTzy3
- Page source: `bevalc-brief/brief.html`
- Source rules: `bevalc-brief/sources.yaml` and the "Bev-Alc Morning Brief" section of `CLAUDE.md`
- Edition archive: `bevalc-brief/editions/YYYY-MM-DD.md`
- Repo: `ryphi90/claude`, branch `claude/add-marketing-skills-zB8Kh`. If the repo isn't checked out, clone that branch first.

## Steps

1. **Apply page blocks.** Read the page database's `blockRequests` collection (ArtifactData, `url` above). For each doc with `status: "pending"`, move that source to `block` in `sources.yaml` and update the doc to `status: "applied"`.
2. **Research the last 24 hours.** Find US three-tier beverage alcohol news published since the previous edition. Follow `sources.yaml` and the CLAUDE.md rules: allow and block lists, English-language only, include awards and rankings, exclude juice and soft drinks, include non-alc only for beer, wine and spirits, keep hemp-THC to a minority. Copy figures exactly from the source.
3. **Rewrite `brief.html` for the new edition.** Keep the page's structure, styles and scripts. Replace the date line, the items in each section, "The numbers" rows and "Coming up". Give each item `data-src` (space-separated source keys). Rebuild the `SOURCES` array in the Sources script so it lists exactly the sources this edition cites, marking new ones `l:0`. Remove the sample banner after the first edition.
4. **Save the edition.** Run `python3 -I bevalc-brief/to_markdown.py bevalc-brief/brief.html bevalc-brief/editions/<date>.md`.
5. **Publish.** Read the artifact first (`Artifact` `action: "read"`, `url` above), then publish `bevalc-brief/brief.html` to that `url`. Omit `capabilities` so the page keeps them.
6. **Commit and push** `brief.html`, `sources.yaml` and the new edition file.
