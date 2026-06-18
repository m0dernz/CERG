#!/usr/bin/env python3
"""
cerg-query.py — Query the CERG machine-readable index.

Usage:
    cerg-query.py --pillar risk --type procedure
    cerg-query.py --control AC-6 --evidence-tier E2
    cerg-query.py --status Approved --owner "Governance Pillar Leader"
    cerg-query.py --list-pillars
    cerg-query.py --list-types
    cerg-query.py --help
"""
import json
import os
import sys
import argparse

INDEX_PATH = os.path.join(os.path.dirname(__file__), "..", "machine-readable", "cerg-llm-index.json")


def load_index(path):
    with open(path) as f:
        return json.load(f)


def build_doc_index(data):
    """Build a searchable list of documents with denormalized metadata."""
    docs = []
    for doc in data.get("documents", []):
        entry = {
            "id": doc.get("id", ""),
            "title": doc.get("title", ""),
            "type": doc.get("type", ""),
            "pillar": doc.get("pillar", ""),
            "status": doc.get("status", ""),
            "owner": doc.get("owner", ""),
            "version": doc.get("version", ""),
            "path": doc.get("repo_relative_path", doc.get("path", "")),
            "summary": doc.get("summary", "")[:200],
        }
        docs.append(entry)
    return docs


def format_table(entries, columns):
    """Pretty-print a table."""
    if not entries:
        print("No matching documents found.")
        return

    col_widths = {}
    for col in columns:
        values = [str(e.get(col, "")) for e in entries] + [col]
        col_widths[col] = max(len(v) for v in values)

    header = " | ".join(col.ljust(col_widths[col]) for col in columns)
    sep = "-+-".join("-" * col_widths[col] for col in columns)
    print(header)
    print(sep)
    for e in entries:
        row = " | ".join(str(e.get(col, "")).ljust(col_widths[col]) for col in columns)
        print(row)


def format_json(entries):
    print(json.dumps(entries, indent=2))


def format_csv(entries, columns):
    import csv
    import io
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(columns)
    for e in entries:
        w.writerow([str(e.get(c, "")) for c in columns])
    print(buf.getvalue().strip())


def main():
    ap = argparse.ArgumentParser(description="Query the CERG machine-readable index.")
    ap.add_argument("--pillar", help="Filter by pillar (governance, engineering, risk, workforce)")
    ap.add_argument("--type", dest="doc_type", help="Filter by document type (policy, standard, procedure, plan, template, job-family, job-description, governance-instrument, guideline)")
    ap.add_argument("--status", help="Filter by status (Approved, Draft, For Review, Retired)")
    ap.add_argument("--owner", help="Filter by owner (partial match)")
    ap.add_argument("--scope", help="Filter by scope/environment keyword (ot, cui, sox, cloud, ai)")
    ap.add_argument("--control", help="Filter by control ID reference")
    ap.add_argument("--evidence-tier", help="Filter by evidence tier (E1, E2, E3)")
    ap.add_argument("--list-pillars", action="store_true", help="List all unique pillars")
    ap.add_argument("--list-types", action="store_true", help="List all unique document types")
    ap.add_argument("--list-statuses", action="store_true", help="List all unique statuses")
    ap.add_argument("--format", choices=["table", "json", "csv"], default="table", help="Output format")
    ap.add_argument("--index", default=INDEX_PATH, help="Path to cerg-llm-index.json")

    args = ap.parse_args()

    if not os.path.isfile(args.index):
        sys.exit(f"ERROR: Index file not found: {args.index}")

    data = load_index(args.index)

    if args.list_pillars:
        values = sorted(set(d.get("pillar", "") for d in data.get("documents", []) if d.get("pillar")))
        for v in values:
            print(v)
        return

    if args.list_types:
        values = sorted(set(d.get("type", "") for d in data.get("documents", []) if d.get("type")))
        for v in values:
            print(v)
        return

    if args.list_statuses:
        values = sorted(set(d.get("status", "") for d in data.get("documents", []) if d.get("status")))
        for v in values:
            print(v)
        return

    docs = build_doc_index(data)

    # Apply filters
    if args.pillar:
        docs = [d for d in docs if args.pillar.lower() in d["pillar"].lower()]
    if args.doc_type:
        docs = [d for d in docs if args.doc_type.lower() in d["type"].lower()]
    if args.status:
        docs = [d for d in docs if args.status.lower() in d["status"].lower()]
    if args.owner:
        docs = [d for d in docs if args.owner.lower() in d["owner"].lower()]

    columns = ["id", "title", "type", "pillar", "status", "owner"]
    if args.format == "json":
        format_json(docs)
    elif args.format == "csv":
        format_csv(docs, columns)
    else:
        format_table(docs, columns)


if __name__ == "__main__":
    main()
