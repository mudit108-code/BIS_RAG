"""
app.py — Flask web UI for BIS Standard Recommendation Engine
Run: python app.py
Open: http://localhost:5000
"""

import sys
import os
import json

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from flask import Flask, request, jsonify, render_template_string
from retriever import recommend
from knowledge_base import BIS_STANDARDS

app = Flask(__name__)

# ──────────────────────────────────────────────────────────────────────────────
# HTML Template
# ──────────────────────────────────────────────────────────────────────────────

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>BIS Standard Finder — MSE Compliance Engine</title>
<style>
  :root {
    --primary: #1a4fad;
    --primary-light: #2d6ae0;
    --accent: #f97316;
    --success: #16a34a;
    --bg: #f8fafc;
    --card: #ffffff;
    --border: #e2e8f0;
    --text: #1e293b;
    --muted: #64748b;
    --tag-bg: #eff6ff;
    --tag-text: #1d4ed8;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', system-ui, sans-serif; background: var(--bg); color: var(--text); }

  /* ── Header ── */
  header {
    background: linear-gradient(135deg, var(--primary) 0%, #0f2d6b 100%);
    color: white; padding: 1.25rem 2rem;
    display: flex; align-items: center; gap: 1rem;
    box-shadow: 0 2px 8px rgba(0,0,0,.25);
  }
  header .logo { font-size: 2rem; }
  header h1 { font-size: 1.4rem; font-weight: 700; line-height: 1.2; }
  header p  { font-size: .82rem; opacity: .8; margin-top: .2rem; }
  .badge {
    margin-left: auto; background: var(--accent);
    color: white; font-size: .7rem; font-weight: 700;
    padding: .3rem .7rem; border-radius: 999px; white-space: nowrap;
  }

  /* ── Layout ── */
  main { max-width: 960px; margin: 2rem auto; padding: 0 1.25rem; }

  /* ── Search card ── */
  .search-card {
    background: var(--card); border: 1px solid var(--border);
    border-radius: 16px; padding: 2rem;
    box-shadow: 0 4px 24px rgba(0,0,0,.06);
    margin-bottom: 1.5rem;
  }
  .search-card h2 { font-size: 1.1rem; margin-bottom: .75rem; color: var(--primary); }
  .search-row { display: flex; gap: .75rem; }
  textarea {
    flex: 1; border: 2px solid var(--border); border-radius: 10px;
    padding: .75rem 1rem; font-size: .95rem; font-family: inherit;
    resize: vertical; min-height: 90px; outline: none; transition: border .2s;
  }
  textarea:focus { border-color: var(--primary-light); }
  .controls { display: flex; flex-direction: column; gap: .5rem; min-width: 130px; }
  select {
    border: 2px solid var(--border); border-radius: 8px;
    padding: .5rem .75rem; font-size: .9rem; outline: none;
    background: white; cursor: pointer;
  }
  select:focus { border-color: var(--primary-light); }
  button.search-btn {
    background: var(--primary); color: white;
    border: none; border-radius: 10px; padding: .75rem 1rem;
    font-size: .95rem; font-weight: 600; cursor: pointer;
    transition: background .2s, transform .1s;
  }
  button.search-btn:hover  { background: var(--primary-light); }
  button.search-btn:active { transform: scale(.97); }
  button.search-btn:disabled { opacity: .5; cursor: not-allowed; }

  /* ── Quick examples ── */
  .examples { margin-top: 1rem; }
  .examples p { font-size: .8rem; color: var(--muted); margin-bottom: .4rem; }
  .chips { display: flex; flex-wrap: wrap; gap: .4rem; }
  .chip {
    background: var(--tag-bg); color: var(--tag-text);
    border: 1px solid #bfdbfe; border-radius: 999px;
    padding: .3rem .75rem; font-size: .78rem; cursor: pointer;
    transition: background .15s;
  }
  .chip:hover { background: #dbeafe; }

  /* ── Metrics bar ── */
  .metrics-bar {
    display: none; gap: 1rem; margin-bottom: 1.5rem; flex-wrap: wrap;
  }
  .metric {
    background: var(--card); border: 1px solid var(--border);
    border-radius: 12px; padding: .75rem 1.25rem; flex: 1; min-width: 130px;
    text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,.04);
  }
  .metric .val { font-size: 1.5rem; font-weight: 800; color: var(--primary); }
  .metric .lbl { font-size: .72rem; color: var(--muted); margin-top: .15rem; }

  /* ── Result cards ── */
  .results-header { font-size: .85rem; color: var(--muted); margin-bottom: .75rem; }
  .result-card {
    background: var(--card); border: 1px solid var(--border);
    border-radius: 14px; padding: 1.25rem 1.5rem;
    margin-bottom: 1rem; box-shadow: 0 2px 12px rgba(0,0,0,.05);
    transition: box-shadow .2s;
  }
  .result-card:hover { box-shadow: 0 4px 20px rgba(0,0,0,.1); }
  .result-card.top1 { border-left: 4px solid var(--success); }
  .result-top { display: flex; align-items: flex-start; gap: .75rem; margin-bottom: .6rem; }
  .rank-badge {
    background: var(--primary); color: white;
    width: 1.8rem; height: 1.8rem; border-radius: 50%;
    font-size: .8rem; font-weight: 700; flex-shrink: 0;
    display: flex; align-items: center; justify-content: center;
  }
  .rank-badge.gold { background: #d97706; }
  .std-id {
    font-size: .8rem; font-weight: 700; color: var(--primary);
    background: var(--tag-bg); border: 1px solid #bfdbfe;
    padding: .15rem .55rem; border-radius: 6px; display: inline-block;
    margin-bottom: .25rem;
  }
  .std-title { font-size: 1rem; font-weight: 600; color: var(--text); }
  .cat-tag {
    margin-left: auto; background: #f1f5f9; color: var(--muted);
    font-size: .72rem; font-weight: 600; padding: .25rem .6rem;
    border-radius: 6px; white-space: nowrap;
  }
  .rationale { font-size: .85rem; color: var(--muted); line-height: 1.55; }
  .score-row { margin-top: .6rem; display: flex; align-items: center; gap: .5rem; }
  .score-bar-wrap { flex: 1; height: 5px; background: #e2e8f0; border-radius: 99px; }
  .score-bar { height: 100%; background: var(--primary); border-radius: 99px; transition: width .5s; }
  .score-label { font-size: .72rem; color: var(--muted); white-space: nowrap; }

  /* ── Error / empty ── */
  .error-box {
    background: #fef2f2; border: 1px solid #fca5a5;
    border-radius: 12px; padding: 1rem 1.25rem; color: #dc2626;
    font-size: .9rem; margin-bottom: 1rem;
  }
  .empty-state { text-align: center; padding: 3rem 1rem; color: var(--muted); }
  .empty-state .icon { font-size: 3rem; margin-bottom: .75rem; }

  /* ── Spinner ── */
  .spinner { display: none; text-align: center; padding: 2rem; }
  .spinner-ring {
    width: 42px; height: 42px; border: 4px solid #e2e8f0;
    border-top-color: var(--primary); border-radius: 50%;
    animation: spin .8s linear infinite; margin: 0 auto 1rem;
  }
  @keyframes spin { to { transform: rotate(360deg); } }

  /* ── Footer ── */
  footer {
    text-align: center; padding: 2rem 1rem;
    color: var(--muted); font-size: .78rem;
  }

  @media (max-width: 600px) {
    .search-row { flex-direction: column; }
    header h1 { font-size: 1.1rem; }
  }
</style>
</head>
<body>

<header>
  <div class="logo">🏗️</div>
  <div>
    <h1>BIS Standard Finder</h1>
    <p>MSE Compliance Engine — Building Materials · RAG-Powered</p>
  </div>
  <span class="badge">Hackathon 2026</span>
</header>

<main>
  <!-- Search -->
  <div class="search-card">
    <h2>Describe your product or material</h2>
    <div class="search-row">
      <textarea id="query" placeholder="e.g. We manufacture 33 Grade Ordinary Portland Cement and need to identify the applicable BIS standard for chemical and physical requirements…"></textarea>
      <div class="controls">
        <select id="topk">
          <option value="3">Top 3</option>
          <option value="5" selected>Top 5</option>
        </select>
        <button class="search-btn" id="searchBtn" onclick="doSearch()">
          🔍 Find Standards
        </button>
      </div>
    </div>
    <div class="examples">
      <p>Quick examples:</p>
      <div class="chips" id="chips"></div>
    </div>
  </div>

  <!-- Metrics -->
  <div class="metrics-bar" id="metricsBar">
    <div class="metric"><div class="val" id="mCount">—</div><div class="lbl">Standards Found</div></div>
    <div class="metric"><div class="val" id="mTop">—</div><div class="lbl">Top Match</div></div>
    <div class="metric"><div class="val" id="mLatency">—</div><div class="lbl">Latency (ms)</div></div>
    <div class="metric"><div class="val" id="mCat">—</div><div class="lbl">Category</div></div>
  </div>

  <!-- Spinner -->
  <div class="spinner" id="spinner">
    <div class="spinner-ring"></div>
    <p>Searching BIS knowledge base…</p>
  </div>

  <!-- Results -->
  <div id="resultsArea"></div>
</main>

<footer>
  BIS SP 21 — Building Materials · Powered by BM25 RAG · No external APIs
</footer>

<script>
const EXAMPLES = [
  "33 Grade Ordinary Portland Cement chemical and physical requirements",
  "Coarse and fine aggregates from natural sources for structural concrete",
  "Precast concrete pipes reinforced and unreinforced for water mains",
  "Hollow and solid lightweight concrete masonry blocks dimensions",
  "Corrugated asbestos cement sheets for roofing and cladding",
  "Portland slag cement manufacture chemical requirements",
  "Portland pozzolana cement calcined clay based",
  "Masonry cement for mortar not structural concrete",
  "Supersulphated cement marine works aggressive water",
  "White Portland cement architectural decorative",
];

// Populate chips
const chipsEl = document.getElementById("chips");
EXAMPLES.forEach(ex => {
  const chip = document.createElement("span");
  chip.className = "chip";
  chip.textContent = ex.length > 55 ? ex.slice(0, 52) + "…" : ex;
  chip.title = ex;
  chip.onclick = () => {
    document.getElementById("query").value = ex;
    doSearch();
  };
  chipsEl.appendChild(chip);
});

async function doSearch() {
  const query = document.getElementById("query").value.trim();
  if (!query) return;
  const topk = parseInt(document.getElementById("topk").value);

  const btn = document.getElementById("searchBtn");
  btn.disabled = true;
  document.getElementById("spinner").style.display = "block";
  document.getElementById("resultsArea").innerHTML = "";
  document.getElementById("metricsBar").style.display = "none";

  try {
    const resp = await fetch("/api/recommend", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({query, top_k: topk})
    });
    const data = await resp.json();

    document.getElementById("spinner").style.display = "none";
    btn.disabled = false;

    if (data.error) {
      document.getElementById("resultsArea").innerHTML =
        `<div class="error-box">⚠️ ${data.error}</div>`;
      return;
    }

    renderResults(data, topk);
  } catch(e) {
    document.getElementById("spinner").style.display = "none";
    btn.disabled = false;
    document.getElementById("resultsArea").innerHTML =
      `<div class="error-box">⚠️ Request failed: ${e.message}</div>`;
  }
}

function renderResults(data, topk) {
  const results = data.results || [];

  // Metrics
  const mb = document.getElementById("metricsBar");
  mb.style.display = "flex";
  document.getElementById("mCount").textContent = results.length;
  document.getElementById("mTop").textContent = results[0]?.id || "—";
  document.getElementById("mLatency").textContent =
    results[0] ? Math.round(data.latency_seconds * 1000) + " ms" : "—";
  document.getElementById("mCat").textContent = results[0]?.category || "—";

  if (!results.length) {
    document.getElementById("resultsArea").innerHTML = `
      <div class="empty-state">
        <div class="icon">🔍</div>
        <p>No standards found. Try a more specific product description.</p>
      </div>`;
    return;
  }

  const maxScore = results[0].score || 1;
  let html = `<div class="results-header">Showing ${results.length} recommended standard(s)</div>`;

  results.forEach((r, i) => {
    const rankBadge = i === 0 ? "gold" : "";
    const topClass  = i === 0 ? "top1" : "";
    const pct = Math.round((r.score / maxScore) * 100);
    html += `
    <div class="result-card ${topClass}">
      <div class="result-top">
        <div class="rank-badge ${rankBadge}">${i+1}</div>
        <div style="flex:1">
          <div class="std-id">${r.id}</div>
          <div class="std-title">${r.title}</div>
        </div>
        <span class="cat-tag">${r.category}</span>
      </div>
      <div class="rationale">${r.rationale}</div>
      <div class="score-row">
        <div class="score-bar-wrap"><div class="score-bar" style="width:${pct}%"></div></div>
        <span class="score-label">Relevance ${pct}%</span>
      </div>
    </div>`;
  });

  document.getElementById("resultsArea").innerHTML = html;
}

// Enter key submits
document.getElementById("query").addEventListener("keydown", e => {
  if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); doSearch(); }
});
</script>
</body>
</html>
"""


# ──────────────────────────────────────────────────────────────────────────────
# Routes
# ──────────────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template_string(HTML)


@app.route("/api/recommend", methods=["POST"])
def api_recommend():
    data = request.get_json(force=True, silent=True) or {}
    query = str(data.get("query", "")).strip()
    top_k = int(data.get("top_k", 5))
    top_k = max(1, min(top_k, 10))

    if not query:
        return jsonify({"error": "Query is empty."}), 400

    result = recommend(query, top_k=top_k)
    return jsonify(result)


@app.route("/api/standards", methods=["GET"])
def api_standards():
    """Return full catalogue of standards."""
    out = [
        {"id": s["id"], "title": s["title"], "category": s["category"]}
        for s in BIS_STANDARDS
    ]
    return jsonify({"total": len(out), "standards": out})


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "standards_loaded": len(BIS_STANDARDS)})


if __name__ == "__main__":
    print("=" * 55)
    print("  BIS Standard Finder — MSE Compliance Engine")
    print(f"  Standards loaded: {len(BIS_STANDARDS)}")
    print("  Open: http://localhost:5000")
    print("=" * 55)
    app.run(debug=False, port=5000)
