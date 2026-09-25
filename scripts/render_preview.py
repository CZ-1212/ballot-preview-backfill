#!/usr/bin/env python3
"""Render per-county ballot-preview HTML widgets from the backfill workbook.

Usage:
    python3 scripts/render_preview.py <workbook.xlsx> [--county "Alameda County"] [--out html/] [--theme blue]

Each output file is a self-contained CMS embed: scoped <style>, the
.lnm-results-widget markup, and the search <script>. No live-election
fields (turnout, votes, percentages, bars) are emitted -- this is a preview.
"""
import argparse, collections, html, os, re, sys
import openpyxl

ELECTION_TITLE = "November 3, 2026 General Election"

# Color themes: primary (banners, headers) and accent (election title).
# "default" is the navy/green newsroom; "blue" is the blue/orange newsroom.
THEMES = {
    "default": {"primary": "#1a3668", "accent": "#accf00"},
    "blue":    {"primary": "#1e7ec4", "accent": "#ff8c1a"},
}

def theme_css(theme):
    t = THEMES[theme]
    h = t["primary"].lstrip("#")
    rgb = ",".join(str(int(h[i:i+2], 16)) for i in (0, 2, 4))
    return CSS.format(primary=t["primary"], accent=t["accent"], primary_rgb=rgb)

CSS = """<style>
    /* Scoped widget CSS -- this entire block is extracted verbatim for CMS embeds. */

    .lnm-results-widget, .lnm-results-widget * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    .lnm-results-widget {{ font-family: Arial, sans-serif; }}

    /* County banner */
    .lnm-results-widget .lnm-county-banner {{
      background-color: {primary};
      color: white;
      padding: 14px 18px;
      border-radius: 5px;
      margin-bottom: 12px;
      text-align: center;
    }}
    .lnm-results-widget .lnm-county-name {{
      font-size: 22px;
      font-weight: 700;
      line-height: 1.2;
    }}
    .lnm-results-widget .lnm-election-title {{
      font-size: 13px;
      font-weight: 400;
      color: {accent};
      text-transform: uppercase;
      letter-spacing: 0.06em;
      margin-top: 4px;
    }}


    /* Race box */
    .lnm-results-widget .race-box {{
      background-color: white;
      border: 1px solid #ddd;
      border-radius: 5px;
      margin-bottom: 20px;
      overflow: hidden;
    }}
    .lnm-results-widget .race-title {{
      background-color: {primary};
      color: white;
      padding: 10px 14px;
      font-weight: bold;
      font-size: 1em;
    }}

    /* Ballot measure */
    .lnm-results-widget .measure-block {{
      padding: 16px;
    }}
    .lnm-results-widget .measure-name {{
      font-size: 1.15em;
      font-weight: 700;
      color: {primary};
      margin-bottom: 6px;
    }}
    .lnm-results-widget .measure-desc {{
      font-size: 0.88em;
      color: #555;
      line-height: 1.55;
    }}

    /* Candidate table header */
    .lnm-results-widget .candidate-table-head {{
      padding: 6px 14px;
      border-top: 1px solid #ddd;
      background: #fafafa;
    }}
    .lnm-results-widget .candidate-table-head span {{
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: #999;
    }}

    /* Candidate row */
    .lnm-results-widget .candidate-row {{
      border-top: 1px solid #eee;
      padding: 10px 14px;
    }}
    .lnm-results-widget .candidate-name-cell {{
      display: flex;
      align-items: center;
      gap: 8px;
      min-width: 0;
    }}
    .lnm-results-widget .candidate-party {{
      width: 30px; height: 30px;
      border-radius: 50%;
      display: flex; align-items: center; justify-content: center;
      font-size: 11px;
      font-weight: 700;
      flex-shrink: 0;
      position: relative;
      cursor: default;
    }}
    .lnm-results-widget .candidate-party::after {{
      content: attr(data-party);
      position: absolute;
      bottom: calc(100% + 5px);
      left: 0;
      background: rgba({primary_rgb},0.92);
      color: white;
      font-size: 11px;
      font-weight: 400;
      white-space: nowrap;
      padding: 4px 9px;
      border-radius: 4px;
      pointer-events: none;
      opacity: 0;
      transition: opacity 0.15s ease;
      z-index: 20;
    }}
    .lnm-results-widget .candidate-party:hover::after {{ opacity: 1; }}
    .lnm-results-widget .party-n {{ background: #e8e8e8; color: #555; }}
    .lnm-results-widget .candidate-name-text {{
      display: flex;
      flex-direction: column;
      min-width: 0;
      flex: 1;
    }}
    .lnm-results-widget .candidate-name {{
      font-weight: 700;
      font-size: 0.92em;
      color: #333;
      word-wrap: break-word;
      overflow-wrap: break-word;
    }}
    .lnm-results-widget .candidate-profession {{
      font-size: 0.78em;
      color: #666;
      margin-top: 2px;
      word-wrap: break-word;
      overflow-wrap: break-word;
    }}

    /* Search */
    .lnm-results-widget .search-wrap {{
      margin-bottom: 16px;
      position: relative;
    }}
    .lnm-results-widget .search-input {{
      width: 100%;
      padding: 10px 16px;
      font-size: 15px;
      border: 1px solid #ccc;
      border-radius: 6px;
      background: white;
      outline: none;
      box-shadow: 0 1px 3px rgba(0,0,0,0.08);
    }}
    .lnm-results-widget .search-input:focus {{
      border-color: {primary};
      box-shadow: 0 0 0 2px rgba({primary_rgb},0.15);
    }}
    .lnm-results-widget .no-results {{
      display: none;
      text-align: center;
      color: #888;
      font-size: 14px;
      padding: 24px 0;
    }}
  </style>
"""

SCRIPT = """<script>
  (function() {
    var input = document.getElementById('electionSearch');
    var noResults = document.getElementById('noResults');
    if (!input) return;
    input.addEventListener('input', function() {
      var q = this.value.trim().toLowerCase();
      var container = input.closest('.lnm-results-widget') || document;
      var boxes = container.querySelectorAll('.race-box');
      var visible = 0;
      boxes.forEach(function(box) {
        var show = !q || box.textContent.toLowerCase().indexOf(q) !== -1;
        box.style.display = show ? '' : 'none';
        if (show) visible++;
      });
      noResults.style.display = (q && visible === 0) ? 'block' : 'none';
    });
  })();
</script>
"""

# Known encoding damage in the source workbook (a mangled em dash).
MOJIBAKE = {"Ã¢??": "\u2014"}

def esc(s):
    s = "" if s is None else str(s).strip()
    for bad, good in MOJIBAKE.items():
        s = s.replace(bad, good)
    return html.escape(s, quote=True)

def slug(county):
    return re.sub(r"[^a-z0-9]+", "-", county.lower()).strip("-")

def load(path):
    wb = openpyxl.load_workbook(path, read_only=True)
    def rows(sheet):
        it = wb[sheet].iter_rows(values_only=True)
        header = [str(h).strip() if h else "" for h in next(it)]
        out = []
        for r in it:
            if not any(c is not None for c in r):
                continue
            d = dict(zip(header, r))
            # A URL stranded in an unlabeled far-right column is still the source.
            if not d.get("Source URL"):
                stray = [c for c in r[len(header):] if isinstance(c, str) and c.startswith("http")]
                if stray:
                    d["Source URL"] = stray[0]
            out.append(d)
        return out
    return rows("Measures"), rows("Candidates")

def render_measure(m):
    return (
        '<div class="race-box">\n'
        f'<div class="race-title">{esc(m.get("Measure Juristiction") or m.get("Measure Jurisdiction") or "")}</div>\n'
        '<div class="measure-block">\n'
        f'<div class="measure-name">{esc(m.get("Measure Name"))}</div>\n'
        f'<div class="measure-desc">{esc(m.get("Measure Description"))}</div>\n'
        '</div>\n</div>\n'
    )

def render_race(race, cands):
    parts = ['<div class="race-box">\n',
             f'<div class="race-title">{esc(race)}</div>\n',
             '<div class="candidate-table-head">\n<span>Candidate</span>\n</div>\n']
    for c in cands:
        prof = esc(c.get("Candidate Profession"))
        prof_html = f'\n<div class="candidate-profession">{prof}</div>' if prof else ""
        parts.append(
            '<div class="candidate-row">\n'
            '<div class="candidate-name-cell">\n'
            '<div class="candidate-party party-n" data-party="Non-Partisan">N</div>\n'
            '<div class="candidate-name-text">\n'
            f'<div class="candidate-name">{esc(c.get("Candidate Name"))}</div>{prof_html}\n'
            '</div>\n</div>\n</div>\n'
        )
    parts.append('</div>\n')
    return "".join(parts)

def render_county(county, measures, candidates, theme="default"):
    races = collections.OrderedDict()
    for c in candidates:
        races.setdefault((c.get("Race") or "").strip(), []).append(c)
    body = [theme_css(theme),
            '<div class="lnm-results-widget">\n',
            '<div class="lnm-county-banner">\n',
            f'<div class="lnm-county-name">{esc(county)}</div>\n',
            f'<div class="lnm-election-title">{esc(ELECTION_TITLE)}</div>\n',
            '</div>\n',
            '<div class="search-wrap">\n',
            '<input class="search-input" id="electionSearch" placeholder="Search for measures, candidates, contests…" type="text">\n',
            '</div>\n',
            '<div class="no-results" id="noResults">No results found.</div>\n']
    body += [render_measure(m) for m in measures]
    body += [render_race(r, cs) for r, cs in races.items()]
    body.append('</div>\n')
    body.append(SCRIPT)
    return "".join(body)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("workbook")
    ap.add_argument("--county", action="append", help="render only this county (repeatable)")
    ap.add_argument("--out", default="html")
    ap.add_argument("--theme", default="default", choices=sorted(THEMES),
                    help="color theme; non-default themes get a '-<theme>' filename suffix")
    a = ap.parse_args()
    measures, candidates = load(a.workbook)
    counties = list(dict.fromkeys([m["County"] for m in measures] + [c["County"] for c in candidates]))
    if a.county:
        counties = [c for c in counties if c in a.county]
    os.makedirs(a.out, exist_ok=True)
    for county in counties:
        ms = [m for m in measures if m["County"] == county]
        cs = [c for c in candidates if c["County"] == county]
        suffix = "" if a.theme == "default" else f"-{a.theme}"
        path = os.path.join(a.out, f"{slug(county)}{suffix}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(render_county(county, ms, cs, a.theme))
        races = len({c["Race"] for c in cs})
        print(f"{path}: {len(ms)} measures, {races} races, {len(cs)} candidates")

if __name__ == "__main__":
    main()
