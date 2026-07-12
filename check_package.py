import json

with open(
    "data/processed/package_documents.jsonl",
    encoding="utf-8"
) as f:

    first = json.loads(next(f))

print(json.dumps(first, indent=2, ensure_ascii=False))