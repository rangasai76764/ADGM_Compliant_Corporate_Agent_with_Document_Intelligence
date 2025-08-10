from rag.retriever import RAGRetriever

# Initialize retriever
retriever = RAGRetriever()

# Add documents (reference texts loaded from PDFs or TXT)
reference_docs = [
    "ADGM company incorporation rules ...",
    "Articles of Association guidelines ...",
    # Add more reference doc texts
]

retriever.add_reference_docs(reference_docs)

# Query the retriever
results = retriever.retrieve("What are the requirements for company incorporation in ADGM?")
for res in results:
    print(res)
