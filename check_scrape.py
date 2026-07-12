import json

count = 0

with open("data/processed/documents.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        doc = json.loads(line)

        packages = doc.get("packages", [])

        if packages:
            print("=" * 100)
            print("PAGE:", doc["title"])
            print("URL :", doc["url"])
            print("TOTAL PACKAGES:", len(packages))
            print("=" * 100)

            print(json.dumps(packages[0], indent=2, ensure_ascii=False))

            count += 1

            if count == 3:
                break