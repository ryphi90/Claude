"""Save the current brief page as a Markdown edition.

Usage: python3 -I bevalc-brief/to_markdown.py bevalc-brief/brief.html bevalc-brief/editions/YYYY-MM-DD.md
"""
import html
import re
import sys


def text(fragment):
    """Turn an HTML fragment into Markdown inline text, keeping links."""
    fragment = re.sub(r'<a href="([^"]+)">(.*?)</a>', lambda m: f"[{text(m.group(2))}]({m.group(1)})", fragment, flags=re.S)
    fragment = re.sub(r"</?b>", "**", fragment)
    fragment = re.sub(r"<[^>]+>", "", fragment)
    return re.sub(r"\s+", " ", html.unescape(fragment)).strip()


def main(src, dst):
    page = open(src, encoding="utf-8").read()
    title = text(re.search(r"<h1>(.*?)</h1>", page, re.S).group(1))
    eyebrow = text(re.search(r'<div class="eyebrow">(.*?)</div>', page, re.S).group(1))
    out = [f"# {title}", "", f"_{eyebrow}_", ""]

    for sec in re.finditer(r'<section id="([^"]+)">(.*?)</section>', page, re.S):
        sid, body = sec.groups()
        if sid == "sources":
            continue  # the interactive list; sources are cited on each item
        if not re.search(r'<article class="item"|<tbody>\s*<tr|<li><time>', body):
            continue  # empty sections are left out, as on the page
        heading = text(re.sub(r"<small>.*?</small>", "", re.search(r"<h2>(.*?)</h2>", body, re.S).group(1)))
        out += [f"## {heading}", ""]
        note = re.search(r'<p class="secnote">(.*?)</p>', body, re.S)
        if note:
            out += [f"_{text(note.group(1))}_", ""]

        for item in re.finditer(r'<article class="item"[^>]*>(.*?)</article>', body, re.S):
            a = item.group(1)
            out.append(f"### {text(re.search(r'<h3>(.*?)</h3>', a, re.S).group(1))}")
            meta = re.search(r'<div class="meta">(.*?)</div>', a, re.S)
            if meta:
                parts = [text(s) for s in re.findall(r"<span[^>]*>(.*?)</span>", meta.group(1), re.S)]
                out.append(f"_{' · '.join(p for p in parts if p)}_")
            out.append("")
            for para in re.findall(r"<p>(.*?)</p>", a, re.S):
                out += [text(para), ""]
            why = re.search(r'<div class="why">(.*?)</div>', a, re.S)
            if why:
                out += [f"> {text(why.group(1))}", ""]
            srcs = re.search(r'<div class="src">(.*?)</div>', a, re.S)
            if srcs:
                out += [f"Sources: {text(srcs.group(1))}", ""]

        table = re.search(r"<table[^>]*>(.*?)</table>", body, re.S)
        if table:
            heads = [text(h) for h in re.findall(r"<th>(.*?)</th>", table.group(1), re.S)]
            out += ["| " + " | ".join(heads) + " |", "|" + "---|" * len(heads)]
            for row in re.findall(r"<tr[^>]*>((?:(?!</tr>).)*<td.*?)</tr>", table.group(1), re.S):
                cells = [text(c).replace("|", "/") for c in re.findall(r"<td[^>]*>(.*?)</td>", row, re.S)]
                out.append("| " + " | ".join(cells) + " |")
            out.append("")

        cal = re.findall(r"<li><time>(.*?)</time><span>(.*?)</span></li>", body, re.S)
        for when, what in cal:
            out.append(f"- **{text(when)}** {text(what)}")
        if cal:
            out.append("")

    open(dst, "w", encoding="utf-8").write("\n".join(out).rstrip() + "\n")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
