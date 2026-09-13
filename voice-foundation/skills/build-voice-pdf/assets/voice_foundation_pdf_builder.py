# -*- coding: utf-8 -*-
"""
Creative Authority - Voice Foundation PDF builder (generic).

Usage:
    python3 voice_foundation_pdf_builder.py content.json output.pdf [logo.png]

content.json shape:
{
  "biz": "Business Name",
  "date": "Month Year",
  "note": "one-line honesty note",
  "identity": [["Name","..."], ["Title","..."], ...],
  "mission": [["Question","Answer (use \\n\\n for paragraphs)"], ...],
  "voice":   [["Question","Answer"], ...],
  "voice_anchors": [["Label","Quote text"], ...],
  "prompt": "the full operating prompt as plain text"
}
Every text field must come from the agent's own material. Do not invent content here.
"""
import base64, html, os, sys, json

INK = "#283040"; CERULEAN = "#34789E"; CLAY = "#B26A47"
EGGSHELL = "#F6F2E9"; PAPER = "#FBF9F3"; LINE = "#D9D2C4"

def esc(s): return html.escape(s or "")
def para(t): return "".join(f"<p>{esc(p.strip())}</p>" for p in (t or "").split("\n\n") if p.strip())
def qa_block(items):
    out = []
    for q, a in items:
        out.append(f'<div class="qa"><div class="q">{esc(q)}</div><div class="a">{para(a)}</div></div>')
    return "".join(out)
def quote_block(label, text):
    return f'<div class="anchor"><div class="anchor-label">{esc(label)}</div>{para(text)}</div>'

def css():
    return f"""
@page {{ size: Letter; margin: 26mm 20mm 22mm 20mm;
  @bottom-left {{ content: "Creative Authority"; font-family: Poppins, 'Helvetica Neue', Arial, sans-serif; font-size: 7.5pt; letter-spacing: 1.5px; text-transform: uppercase; color: {CERULEAN}; }}
  @bottom-right {{ content: counter(page); font-family: Poppins, 'Helvetica Neue', Arial, sans-serif; font-size: 8pt; color: {INK}; }} }}
@page cover {{ margin: 0; @bottom-left {{ content: none; }} @bottom-right {{ content: none; }} }}
* {{ box-sizing: border-box; }}
html {{ font-family: Poppins, 'Helvetica Neue', Arial, sans-serif; color: {INK}; font-size: 10.5pt; line-height: 1.5; }}
p {{ margin: 0 0 7pt 0; }}
.cover {{ page: cover; height: 100vh; background: {EGGSHELL}; padding: 34mm 24mm; position: relative; }}
.cover img {{ width: 74mm; }}
.cover .rule {{ height: 2px; background: {CERULEAN}; width: 46mm; margin: 26mm 0 9mm 0; }}
.cover h1 {{ font-family: Lora, Georgia, 'Times New Roman', serif; font-weight: 600; font-size: 40pt; line-height: 1.04; margin: 0; color: {INK}; }}
.cover .sub {{ font-family: Poppins, 'Helvetica Neue', Arial, sans-serif; font-size: 12pt; margin-top: 10mm; max-width: 120mm; line-height: 1.55; }}
.cover .biz {{ font-family: Lora, Georgia, 'Times New Roman', serif; font-style: italic; font-size: 17pt; color: {CLAY}; margin-top: 20mm; }}
.cover .meta {{ position: absolute; bottom: 26mm; left: 24mm; font-family: Poppins, 'Helvetica Neue', Arial, sans-serif; font-size: 8.5pt; letter-spacing: 1px; text-transform: uppercase; }}
.section-label {{ font-family: Poppins, 'Helvetica Neue', Arial, sans-serif; font-weight: 600; font-size: 8pt; letter-spacing: 2.4px; text-transform: uppercase; color: {CERULEAN}; border-bottom: 1.5px solid {CERULEAN}; padding-bottom: 4pt; margin: 0 0 3pt 0; }}
h2 {{ font-family: Lora, Georgia, 'Times New Roman', serif; font-weight: 600; font-size: 21pt; margin: 4pt 0 3pt 0; }}
.lead {{ font-family: Lora, Georgia, 'Times New Roman', serif; font-style: italic; font-size: 11.5pt; color: #4a5364; margin: 0 0 12pt 0; }}
.newpage {{ break-before: page; }}
.qa {{ margin: 0 0 13pt 0; }}
.q {{ font-family: Lora, Georgia, 'Times New Roman', serif; font-weight: 600; font-size: 11.5pt; margin-bottom: 4pt; }}
.a {{ padding-left: 10pt; border-left: 2px solid {LINE}; }}
.a p {{ margin: 0 0 5pt 0; }}
.idgrid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 3pt 24pt; margin: 6pt 0 4pt 0; }}
.idrow {{ font-size: 9.5pt; border-bottom: 1px solid {LINE}; padding: 4pt 0; }}
.idrow b {{ font-family: Poppins, 'Helvetica Neue', Arial, sans-serif; font-weight: 600; color: {CERULEAN}; font-size: 7.5pt; letter-spacing: 1px; text-transform: uppercase; display: block; margin-bottom: 1pt; }}
.anchor {{ background: {PAPER}; border: 1px solid {LINE}; border-left: 3px solid {CLAY}; padding: 10pt 12pt; margin: 8pt 0 12pt 0; }}
.anchor-label {{ font-family: Poppins, 'Helvetica Neue', Arial, sans-serif; font-weight: 600; font-size: 7.5pt; letter-spacing: 1.6px; text-transform: uppercase; color: {CLAY}; margin-bottom: 5pt; }}
.anchor p {{ font-family: Lora, Georgia, 'Times New Roman', serif; font-size: 10pt; line-height: 1.55; color: #3a4250; }}
.prompt {{ background: {INK}; color: {EGGSHELL}; border-radius: 3pt; padding: 12pt 14pt; margin-top: 8pt; break-inside: avoid; }}
.prompt .plabel {{ font-family: Poppins, 'Helvetica Neue', Arial, sans-serif; font-weight: 600; font-size: 7.5pt; letter-spacing: 2px; text-transform: uppercase; color: {CERULEAN}; margin-bottom: 7pt; }}
.prompt pre {{ font-family: "DejaVu Sans Mono", monospace; font-size: 7.3pt; line-height: 1.45; color: {EGGSHELL}; white-space: pre-wrap; margin: 0; }}
.note {{ font-size: 8.5pt; color: #6b7280; font-style: italic; margin-top: 6pt; }}
.intro {{ font-size: 10.5pt; margin-bottom: 6pt; }}
.printbar {{ position: fixed; top: 0; left: 0; right: 0; z-index: 99; background: {CERULEAN}; color: #fff; font-family: Poppins, 'Helvetica Neue', Arial, sans-serif; font-size: 11pt; padding: 10px 16px; text-align: center; }}
@media print {{ .printbar {{ display: none !important; }} }}
"""

def build_html(d, logo_b64, printbar=False):
    id_rows = "".join(f'<div class="idrow"><b>{esc(k)}</b>{esc(v)}</div>' for k, v in d.get("identity", []))
    anchors = "".join(quote_block(l, t) for l, t in d.get("voice_anchors", []))
    bar = ('<div class="printbar">To save this as a PDF: press Command-P (or Control-P), '
           'then choose Save as PDF. This bar will not appear in the saved file.</div>') if printbar else ""
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>Voice Foundation</title><style>{css()}</style></head><body>
{bar}
<section class="cover">
  <img src="data:image/png;base64,{logo_b64}">
  <div class="rule"></div>
  <h1>Voice<br>Foundation.</h1>
  <div class="sub">How you think, decide, and communicate with your clients. Your mission, your decision rules, and your voice, captured in your own words.</div>
  <div class="biz">{esc(d.get("biz",""))}</div>
  <div class="meta">Prepared by Creative Authority &nbsp;&middot;&nbsp; {esc(d.get("date",""))}</div>
</section>
<section>
  <div class="section-label">The Basics</div><h2>Your details</h2>
  <p class="intro">The facts your system runs on: signatures, market, and how you show up on everything it helps you make.</p>
  <div class="idgrid">{id_rows}</div>
</section>
<section class="newpage">
  <div class="section-label">Part One</div><h2>Mission &amp; Decision Rules</h2>
  <p class="lead">How you think, what you prioritize, and the lines you will not cross.</p>
  {qa_block(d.get("mission", []))}
</section>
<section class="newpage">
  <div class="section-label">Part Two</div><h2>Canonical Voice</h2>
  <p class="lead">How you sound in writing and out loud, with the examples that prove it.</p>
  {qa_block(d.get("voice", []))}{anchors}
</section>
<section class="newpage">
  <div class="section-label">Part Three</div><h2>Your Operating Prompt</h2>
  <p class="intro">Paste this into any AI, ChatGPT, Claude, Gemini, or a new project, when you want it to work and write the way you do. It travels with you, inside the Creative Authority System or anywhere else.</p>
  <p class="note">{esc(d.get("note",""))}</p>
  <div class="prompt"><div class="plabel">Operating Prompt &middot; copy and paste</div><pre>{esc(d.get("prompt",""))}</pre></div>
</section>
</body></html>"""

def main():
    if len(sys.argv) < 3:
        print("usage: voice_foundation_pdf_builder.py content.json output.pdf [logo.png]"); sys.exit(1)
    content_path, out_path = sys.argv[1], sys.argv[2]
    logo = sys.argv[3] if len(sys.argv) > 3 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "creative_authority_logo.png")
    with open(content_path, encoding="utf-8") as f:
        data = json.load(f)
    # normalize [ [k,v], ... ] pairs
    for key in ("identity", "mission", "voice", "voice_anchors"):
        data[key] = [list(x) for x in data.get(key, [])]
    with open(logo, "rb") as f:
        logo_b64 = base64.b64encode(f.read()).decode()

    force_html = "--html" in sys.argv
    if not force_html:
        try:
            from weasyprint import HTML
            HTML(string=build_html(data, logo_b64)).write_pdf(out_path)
            print("WROTE", out_path, os.path.getsize(out_path), "bytes")
            return
        except Exception as e:
            print("PDF engine unavailable (%s). Falling back to HTML." % type(e).__name__)

    html_path = os.path.splitext(out_path)[0] + ".html"
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(build_html(data, logo_b64, printbar=True))
    print("WROTE_HTML", html_path, os.path.getsize(html_path), "bytes")
    print("Open it in a browser and use Print, then Save as PDF.")

if __name__ == "__main__":
    main()
