# Lightroom presets

- Every `.xmp` preset created in this repo must set its `crs:Group` to `01_AI Replication`, so all presets import into one Lightroom folder.

# Bev-Alc Morning Brief

- `bevalc-brief/sources.yaml` is the single source of truth for which sources the brief may use (allow / block / pending / syndicators). Read it before building any brief.
- Before building each brief, apply blocks saved from the brief page: read the `blockRequests` collection of the brief artifact (https://claude.ai/artifact/A3w74NNW8EQ4LeH9PgTzy3) with ArtifactData. For each doc with `status: "pending"`, move that source to `block` in `sources.yaml` (note: "Blocked from the brief page on <requestedAt date>"), then update the doc to `status: "applied"`. Commit and push the YAML change.
- When building a brief: use allowed sources freely; drop blocked sources silently; for a source on neither list, include the item only if it meets the content rules, mark it **New source**, and add it to `pending`. A pending source with no block by the next brief moves to `allow`. Credit syndicators (AOL, Yahoo, MSN, Google News) to the original publisher, and cite company releases as the company, never a reposting site.
- Every brief ends with a "Sources" section listing every publisher, organization and company cited, each with a Block button that writes to `blockRequests`. There is no "Left out" section.
- When the user gives feedback on a source ("block X", "allow Y", "Y is tier 2"): move the entry to the right list (remove it from any other list), set `added` to today, quote the feedback in `note`, then commit and push the change so it persists. Confirm the change in one line.
- When the user approves or rejects pending sources in bulk ("approve all suggestions", "block the rest"), apply each one the same way.
- Standing rule (user, 2026-11-04): English-language sources only. Exclude any article not published in English, and add a non-English outlet straight to `block` without asking. Official bodies abroad (Comité Champagne, BNIC, OIV) stay allowed, but only their English pages are used.
- Standing rule (user, 2026-11-04): include awards and rankings coverage (competitions, critic lists such as Wine Spectator Top 100, brand rankings) in an "Awards & rankings" section. Same source rules apply.
- The brief page is cumulative: each morning, add the new items to the existing page rather than replacing it, so the Timeframe menu (Today default, Yesterday, Last 7 days, This month, Last month) can look back. Every item needs `data-date="YYYY-MM-DD"` (publication date; if only approximate, use the earliest plausible day and say so) and `data-src` (space-separated source keys matching the Sources list); numbers-table rows need `data-date` too.
- Updates are built by the scheduled task "Bev-Alc Brief: build timeframe" (trig_01AQhRmjgTjtjGt45rt4HLK3), following `bevalc-brief/BUILD.md`. The brief page starts it when the owner picks a timeframe that hasn't been built. The page source to edit and publish is `bevalc-brief/brief.html`.
