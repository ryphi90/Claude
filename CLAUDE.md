# Lightroom presets

- Every `.xmp` preset created in this repo must set its `crs:Group` to `01_AI Replication`, so all presets import into one Lightroom folder.

# Bev-Alc Morning Brief

- `bevalc-brief/sources.yaml` is the single source of truth for which sources the brief may use (allow / block / pending / syndicators). Read it before building any brief.
- When building a brief: use allowed sources freely; drop blocked sources (count them under "Left out"); for a source on neither list, include the item only if it meets the content rules, flag it as **New source**, and add it to `pending` with a suggested verdict; credit syndicators (AOL, Yahoo, MSN, Google News) to the original publisher.
- When the user gives feedback on a source ("block X", "allow Y", "Y is tier 2"): move the entry to the right list (remove it from any other list), set `added` to today, quote the feedback in `note`, then commit and push the change so it persists. Confirm the change in one line.
- When the user approves or rejects pending sources in bulk ("approve all suggestions", "block the rest"), apply each one the same way.
- Standing rule (user, 2026-11-04): English-language sources only. Exclude any article not published in English, and add a non-English outlet straight to `block` without asking. Official bodies abroad (Comité Champagne, BNIC, OIV) stay allowed, but only their English pages are used.
- Standing rule (user, 2026-11-04): include awards and rankings coverage (competitions, critic lists such as Wine Spectator Top 100, brand rankings) in an "Awards & rankings" section. Same source rules apply; awards are not counted under "Left out".
