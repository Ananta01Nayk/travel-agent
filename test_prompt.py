from rag.retriever import Retriever
from rag.prompt import build_prompt

retriever = Retriever()

docs = retriever.retrieve(
    "Best Vietnam family tour package"
)

prompt = build_prompt(
    "Best Vietnam family tour package",
    docs
)

print(prompt)