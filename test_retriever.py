from vectorstore.chroma_retriever import ChromaRetriever

retriever = ChromaRetriever()

results = retriever.search(
    "Best Vietnam honeymoon package under 30000",
    top_k=5
)

for i, r in enumerate(results, 1):

    print("=" * 80)

    print("Rank :", i)
    print("Score:", r["score"])
    print("Title:", r["title"])
    print("Price:", r["price"])
    print("Duration:", r["duration"])
    print("URL:", r["detail_url"])
    