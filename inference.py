"""
inference.py — Mandatory hackathon entry point.
Usage:
    python inference.py --input public_test_set.json --output results.json
"""

import argparse
import json
import sys
import os
import time

# Allow running from repo root
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from retriever import recommend


def run_inference(input_path: str, output_path: str) -> None:
    # Load input queries
    with open(input_path, "r", encoding="utf-8") as f:
        queries = json.load(f)

    output = []
    for item in queries:
        qid = item["id"]
        query = item["query"]

        t0 = time.time()
        result = recommend(query, top_k=5)
        latency = round(time.time() - t0, 4)

        output.append({
            "id": qid,
            "query": query,
            "expected_standards": item.get("expected_standards", []),
            "retrieved_standards": result["retrieved_standards"],
            "latency_seconds": latency,
        })

    # Save output
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"[inference.py] Processed {len(output)} queries → {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="BIS RAG Inference Script")
    parser.add_argument("--input", required=True, help="Path to input JSON file")
    parser.add_argument("--output", required=True, help="Path to output JSON file")
    args = parser.parse_args()

    run_inference(args.input, args.output)
