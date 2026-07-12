import json
import uuid
from pathlib import Path

from langchain_text_splitters import RecursiveCharacterTextSplitter

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "processed" / "documents.jsonl"
OUTPUT_DIR = BASE_DIR / "data" / "chunks"
OUTPUT_FILE = OUTPUT_DIR / "chunks.jsonl"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Chunk Configuration

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150,
    separators=[
        "\n\n",
        "\n",
        ". ",
        "? ",
        "! ",
        " ",
        ""
    ]
)

# Chunk Documents

with open(INPUT_FILE, "r", encoding="utf-8") as infile, \
     open(OUTPUT_FILE, "w", encoding="utf-8") as outfile:

    for line in infile:

        document = json.loads(line)

        content = document.get("content", "").strip()

        if not content:
            continue

        chunks = text_splitter.split_text(content)

        for index, chunk in enumerate(chunks):

            chunk_doc = {
                "chunk_id": str(uuid.uuid4()),
                "chunk_index": index,

                "url": document.get("url"),
                "canonical_url": document.get("canonical_url"),

                "title": document.get("title"),
                "page_type": document.get("page_type"),

                "meta_description": document.get("meta_description"),

                "content": chunk,

                "source": "namasteindiatrip"
            }

            outfile.write(
                json.dumps(chunk_doc, ensure_ascii=False) + "\n"
            )

print(f"Chunks saved to: {OUTPUT_FILE}")