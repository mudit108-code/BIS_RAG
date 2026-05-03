# BIS Standard Finder — MSE Compliance Engine 🏗️

An AI-powered Retrieval-Augmented Generation (RAG) system that helps Indian Micro and Small Enterprises (MSEs) instantly find applicable Bureau of Indian Standards (BIS) regulations for Building Materials.

## Features
- **BM25 retrieval** — fast, accurate, no external API or ML model needed
- **Covers 40+ BIS standards** — Cement, Aggregates, Concrete, Masonry, Steel, Tiles, Roofing, etc.
- **Sub-10ms latency** — pure Python, in-memory index
- **Flask web UI** — interactive search with relevance scores and rationale
- **Hackathon-compliant** — `inference.py` and `eval_script.py` included

## Project Structure
```
bis_rag/
├── src/
│   ├── knowledge_base.py    # BIS SP 21 standards corpus
│   └── retriever.py         # BM25 index + recommendation engine
├── data/                    # Public test set results
├── app.py                   # Flask web UI
├── inference.py             # Hackathon mandatory entry-point
├── eval_script.py           # Hackathon evaluation script
├── requirements.txt
└── README.md
```

## Quick Start

```bash
pip install -r requirements.txt

# Run web UI
python app.py
# Open http://localhost:5000

# Run inference on test set
python inference.py --input public_test_set.json --output data/results.json

# Evaluate
python eval_script.py --results data/results.json
```

## Evaluation

```bash
python inference.py --input hidden_private_dataset.json --output team_results.json
python eval_script.py --results team_results.json
```

## How It Works

1. **Knowledge Base** (`src/knowledge_base.py`) — hand-curated corpus of 40+ BIS building material standards from SP 21, each with title, category, keywords, and description.

2. **BM25 Index** (`src/retriever.py`) — builds an inverted index at startup with IDF-weighted term frequencies. Expands tokens with bigrams and trigrams for phrase matching.

3. **Retrieval** — query is tokenized and matched against the index. Top-K standards are returned with relevance scores and rationale sentences.

4. **Web UI** (`app.py`) — Flask app with a polished single-page interface. No frontend framework dependencies.

## Retrieval Strategy

- **BM25** with K1=1.5, B=0.75 (tuned for short technical queries)
- **N-gram expansion** (unigrams + bigrams + trigrams) for phrase-level matching
- **Field boosting** — title and keywords repeated 2x in document for higher weight
- **Stopword removal** — domain-specific stopwords including "standard", "specification", "requirement"
- **Rule-based rationale** — most relevant sentence from standard description selected by token overlap

