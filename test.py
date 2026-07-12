import json

with open("data/processed/documents.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        doc = json.loads(line)

        if "Vietnam Tour Packages" in doc.get("title", ""):
            print("=" * 100)
            print(doc["title"])
            print("=" * 100)
            print(doc["content"][:8000])
            break