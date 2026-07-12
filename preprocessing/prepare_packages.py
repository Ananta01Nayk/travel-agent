import json
import uuid
from pathlib import Path

INPUT_FILE = Path("data/processed/documents.jsonl")
OUTPUT_FILE = Path("data/processed/package_documents.jsonl")


def clean(value):
    if not value:
        return ""

    return " ".join(str(value).split()).strip()


def build_embedding_text(package):

    text = f"""
Package Name: {package.get("title","")}

Price: {package.get("price","")}

Duration: {package.get("duration","")}

Starting & Ending:
{package.get("start_end","")}

Destinations:
{package.get("destinations","")}

Includes:
{", ".join(package.get("includes", []))}

Tour Type:
{package.get("tour_type","")}

Description:
{package.get("raw_text","")}
"""

    return clean(text)


def main():

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    seen_urls = set()

    total_packages = 0

    with open(INPUT_FILE, "r", encoding="utf-8") as infile, \
         open(OUTPUT_FILE, "w", encoding="utf-8") as outfile:

        for line in infile:

            page = json.loads(line)

            page_title = page.get("title", "")
            page_url = page.get("url", "")

            for package in page.get("packages", []):

                detail_url = package.get("detail_url", "")

                if detail_url in seen_urls:
                    continue

                seen_urls.add(detail_url)

                document = {
                    "id": str(uuid.uuid4()),

                    "page_title": page_title,

                    "page_url": page_url,

                    "title": clean(package.get("title")),

                    "price": clean(package.get("price")),

                    "duration": clean(package.get("duration")),

                    "start_end": clean(package.get("start_end")),

                    "destinations": clean(package.get("destinations")),

                    "includes": package.get("includes", []),

                    "tour_type": clean(package.get("tour_type")),

                    "image": package.get("image"),

                    "detail_url": detail_url,

                    "category": package.get("category"),

                    "raw_text": clean(package.get("raw_text")),

                    "embedding_text": build_embedding_text(package),
                }

                outfile.write(
                    json.dumps(
                        document,
                        ensure_ascii=False
                    ) + "\n"
                )

                total_packages += 1

    print("=" * 60)
    print(f"Total Packages : {total_packages}")
    print(f"Saved File     : {OUTPUT_FILE}")
    print("=" * 60)


if __name__ == "__main__":
    main()