from rag.rag_pipeline import TravelRAG

rag = TravelRAG()

response = rag.ask(
    "Best Vietnam honeymoon package under 30000"
)

print("=" * 80)
print("ANSWER")
print("=" * 80)

print(response["answer"])

print("\nSOURCES")
print("=" * 80)

for source in response["sources"]:

    print(source["title"])
    print(source["price"])
    print(source["duration"])
    print(source["detail_url"])
    print("-" * 80)