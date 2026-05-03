"""
RAG Retrieval Engine for BIS Standard Recommendation
Uses TF-IDF + BM25-style scoring — no external ML packages needed.
"""

import math
import re
import time
from collections import Counter
from typing import List, Dict, Tuple

from knowledge_base import BIS_STANDARDS, STANDARDS_BY_ID


# ──────────────────────────────────────────────────────────────────────────────
# Text utilities
# ──────────────────────────────────────────────────────────────────────────────

STOPWORDS = {
    "a", "an", "the", "and", "or", "for", "of", "in", "on", "at", "to",
    "is", "are", "was", "were", "be", "been", "being", "have", "has", "had",
    "do", "does", "did", "will", "would", "could", "should", "may", "might",
    "it", "its", "this", "that", "these", "those", "with", "from", "by",
    "as", "we", "our", "us", "i", "my", "me", "you", "your", "which",
    "what", "who", "where", "when", "how", "not", "no", "nor", "so",
    "both", "but", "if", "then", "than", "such", "also", "more", "very",
    "can", "about", "need", "looking", "applicable", "standard", "standards",
    "specification", "specifications", "indian", "bis", "requirement",
    "requirements", "compliance", "regulation", "regulations", "any",
    "all", "each", "per", "up", "set", "use", "used", "using",
}


def tokenize(text: str) -> List[str]:
    """Lowercase, split on non-alphanumeric, remove stopwords."""
    tokens = re.findall(r"[a-z0-9]+", text.lower())
    return [t for t in tokens if t not in STOPWORDS and len(t) > 1]


def ngrams(tokens: List[str], n: int) -> List[str]:
    """Generate n-gram strings from token list."""
    return [" ".join(tokens[i:i+n]) for i in range(len(tokens) - n + 1)]


def expand_tokens(tokens: List[str]) -> List[str]:
    """Add bigrams and trigrams to token list."""
    out = list(tokens)
    out.extend(ngrams(tokens, 2))
    out.extend(ngrams(tokens, 3))
    return out


# ──────────────────────────────────────────────────────────────────────────────
# Document building
# ──────────────────────────────────────────────────────────────────────────────

def build_doc_text(standard: dict) -> str:
    """Combine all fields of a standard into a single searchable text blob."""
    parts = [
        standard["id"],
        standard["title"],
        standard["category"],
        standard["description"],
        " ".join(standard["keywords"]),
        # Repeat title and keywords for boosting
        standard["title"],
        standard["title"],
        " ".join(standard["keywords"]),
        " ".join(standard["keywords"]),
    ]
    return " ".join(parts)


# ──────────────────────────────────────────────────────────────────────────────
# Index
# ──────────────────────────────────────────────────────────────────────────────

class BM25Index:
    """Lightweight BM25 index over BIS standards corpus."""

    # BM25 hyperparams
    K1 = 1.5
    B = 0.75

    def __init__(self, standards: List[dict]):
        self.standards = standards
        self.n_docs = len(standards)

        # Tokenize each document
        raw_texts = [build_doc_text(s) for s in standards]
        self.doc_tokens: List[List[str]] = [
            expand_tokens(tokenize(t)) for t in raw_texts
        ]
        self.doc_freqs: List[Counter] = [Counter(toks) for toks in self.doc_tokens]
        self.doc_lengths = [len(toks) for toks in self.doc_tokens]
        self.avg_dl = sum(self.doc_lengths) / self.n_docs if self.n_docs else 1

        # Build inverted index: term → list of (doc_idx, freq)
        self.inv_index: Dict[str, List[Tuple[int, int]]] = {}
        for doc_idx, freq_map in enumerate(self.doc_freqs):
            for term, freq in freq_map.items():
                self.inv_index.setdefault(term, []).append((doc_idx, freq))

        # DF per term
        self.df: Dict[str, int] = {
            term: len(postings) for term, postings in self.inv_index.items()
        }

    def idf(self, term: str) -> float:
        df = self.df.get(term, 0)
        if df == 0:
            return 0.0
        return math.log((self.n_docs - df + 0.5) / (df + 0.5) + 1)

    def score_doc(self, query_terms: List[str], doc_idx: int) -> float:
        score = 0.0
        dl = self.doc_lengths[doc_idx]
        freq_map = self.doc_freqs[doc_idx]
        norm = 1 - self.B + self.B * (dl / self.avg_dl)
        for term in query_terms:
            f = freq_map.get(term, 0)
            if f == 0:
                continue
            idf = self.idf(term)
            tf = (f * (self.K1 + 1)) / (f + self.K1 * norm)
            score += idf * tf
        return score

    def retrieve(self, query: str, top_k: int = 5) -> List[Dict]:
        """Return top_k standards with scores and rationale."""
        t0 = time.time()

        q_tokens = expand_tokens(tokenize(query))
        if not q_tokens:
            return []

        # Collect candidate docs (those sharing at least 1 token)
        candidate_idx = set()
        for term in set(q_tokens):
            for doc_idx, _ in self.inv_index.get(term, []):
                candidate_idx.add(doc_idx)

        # If very few candidates, evaluate all docs
        if len(candidate_idx) < top_k:
            candidate_idx = set(range(self.n_docs))

        # Score candidates
        scores = []
        for doc_idx in candidate_idx:
            s = self.score_doc(q_tokens, doc_idx)
            if s > 0:
                scores.append((doc_idx, s))

        scores.sort(key=lambda x: -x[1])
        top = scores[:top_k]

        latency = time.time() - t0

        results = []
        for doc_idx, score in top:
            std = self.standards[doc_idx]
            results.append({
                "id": std["id"],
                "title": std["title"],
                "category": std["category"],
                "score": round(score, 4),
                "rationale": build_rationale(query, std),
                "latency_seconds": round(latency, 4),
            })

        return results


# ──────────────────────────────────────────────────────────────────────────────
# Rationale generation (rule-based, no LLM needed)
# ──────────────────────────────────────────────────────────────────────────────

def build_rationale(query: str, standard: dict) -> str:
    """Generate a brief rationale explaining why this standard matches."""
    q_lower = query.lower()
    desc_sentences = standard["description"].split(". ")

    # Find most relevant sentence from description
    q_tokens = set(tokenize(q_lower))
    best_sent = desc_sentences[0]
    best_overlap = 0
    for sent in desc_sentences:
        overlap = len(q_tokens & set(tokenize(sent)))
        if overlap > best_overlap:
            best_overlap = overlap
            best_sent = sent

    return (
        f"{standard['id']} — {standard['title']}. "
        f"Relevance: {best_sent.strip()}."
    )


# ──────────────────────────────────────────────────────────────────────────────
# Singleton index
# ──────────────────────────────────────────────────────────────────────────────

_INDEX: BM25Index = None


def get_index() -> BM25Index:
    global _INDEX
    if _INDEX is None:
        _INDEX = BM25Index(BIS_STANDARDS)
    return _INDEX


def recommend(query: str, top_k: int = 5) -> Dict:
    """
    Main entry point.
    Returns dict with keys: retrieved_standards (list), results (list of dicts), latency_seconds.
    """
    t0 = time.time()
    index = get_index()
    results = index.retrieve(query, top_k=top_k)
    latency = round(time.time() - t0, 4)

    return {
        "retrieved_standards": [r["id"] for r in results],
        "results": results,
        "latency_seconds": latency,
    }
