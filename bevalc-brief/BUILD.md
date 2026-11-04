# Building the Bev-Alc Morning Brief

The scheduled task "Bev-Alc Brief daily edition" (trig_01AwxcYsC8s3maNddjwSSfrJ) runs these steps. It fires into the original Claude session, which has repo push access, in two cases:

- **Daily update:** every day at 7:06am Central, so the page is ready around 7:30. The page always shows the **last 7 days** of news. Each morning the run adds the new headlines (marked NEW TODAY), re-ranks the Top 5 for the week, and removes anything more than 7 days old.
- **Update:** when the owner selects **Check for new headlines** on the page (the appended text starts with "Update request"). It adds only new headlines published since `meta/lastUpdate.at` to the current edition. The page allows this at most once an hour after the last update.

Key locations:

- Brief page (published): https://claude.ai/artifact/A3w74NNW8EQ4LeH9PgTzy3
- Page source: `bevalc-brief/brief.html`
- Source rules: `bevalc-brief/sources.yaml` and the "Bev-Alc Morning Brief" section of `CLAUDE.md`
- Edition archive: `bevalc-brief/editions/YYYY-MM-DD.md`
- Repo: `ryphi90/claude`, branch `claude/add-marketing-skills-zB8Kh`. Pull before starting.

## Steps

1. **Mark the run.** Set `meta/lastUpdate` in the page database (ArtifactData, `url` above) to `status: "running"` and `requestedAt` set to now, keeping its other fields.
2. **Apply page blocks.** Read `blockRequests`. For each doc with `status: "pending"`, move that source to `block` in `sources.yaml` and update the doc to `status: "applied"`.
3. **Research.** A daily run looks for news since the previous run, normally the last 24 hours. An update covers the time since `meta/lastUpdate.at`. Find US three-tier beverage alcohol news in that window and follow `sources.yaml` and the CLAUDE.md rules: allow and block lists, English-language only, include awards and rankings, exclude juice and soft drinks, include non-alc only for beer, wine and spirits, keep hemp-THC to a minority. Copy figures exactly from the source.
   - **Use the coverage guide.** Check the recurring data releases and the topics in `bevalc-brief/COVERAGE.md` every run. That includes the Retail & on-premise section, placed after Beer & RTD.
   - **Use web search only.** Don't use Bigdata.com or any other news database, not even as an intermediary.
   - **Carry forward running deadlines.** If a date in "Coming up" is within 14 days and directly affects what retailers or distributors can sell (a state or federal ban, a tariff, a law expiring), keep it in the related item with a link to the primary source, such as the agency bulletin or the statute, even when there's no new coverage that day.
   - **Verify every item and link the original.** Each item must link the original publisher's article or the issuer's own release, found and checked through web search. Never use a database or syndication copy (Bigdata.com, AOL, Yahoo, MSN). If the original can't be found, or a figure can't be confirmed by a search result, cut the item or the figure. Where sources disagree, use the primary document (for example an SEC filing over a news summary).
4. **Write the page.** The page holds a rolling 7-day window. Keep its structure, styles and scripts.
   - **Every item** carries `data-date` (publication date, YYYY-MM-DD), `data-added` (the day it first appeared on the page) and `data-src` (source keys). Rows in "The numbers" carry `data-date`.
   - **Daily:** remove items and number rows whose `data-date` is more than 6 days before today. Add the new items with `data-added` set to today, in the right sections. Merge follow-up coverage into an existing item instead of duplicating it; when you do, update its text and set its `data-added` to today. Re-rank the Top 5 across the whole week. Update the "Updated" date in the header, the numbers table and "Coming up".
   - **Update:** add new items the same way, with `data-added` set to today. If nothing new turned up, leave the page unchanged.
   - **Both:**
     - Leave out any section with no items, and remove its section button.
     - Keep the `SOURCES` array matched to the sources the page cites, marking new ones `l:0`.
     - The page also drops expired items, marks NEW TODAY (where `data-added` is the viewer's today) and hides empty sections in the browser, as a safeguard.
5. **Save the edition.** Run `python3 -I bevalc-brief/to_markdown.py bevalc-brief/brief.html bevalc-brief/editions/<today>.md`. This saves the full 7-day page as it stood that day, with today's additions marked **NEW TODAY**. An update overwrites that day's file.
6. **Publish.** Publish `bevalc-brief/brief.html` to the `url` above, reading it first if this session hasn't. Omit `capabilities` so the page keeps them.
7. **Commit and push** `brief.html`, `sources.yaml` and the edition file.
8. **Record the update.** Set `meta/lastUpdate` to `{at: <now>, status: "done", kind: "daily"|"update", added: <new item count>}`. On failure, set `status: "failed"` with a one-line `error` a viewer can act on, and keep the previous `at`.
