from rag.vectorstore import FaissVectorStore

class RAGRetriever:
    def __init__(self, vector_store=None):
        self.vector_store = vector_store or FaissVectorStore()

    def add_reference_docs(self, documents):
        """
        documents: list of reference doc texts to add to vector store
        """
        self.vector_store.add_documents(documents)

    def retrieve(self, query, top_k=3):
        """
        Retrieve most relevant documents to the query.
        Returns list of text snippets.
        """
        results = self.vector_store.search(query, top_k=top_k)
        # Return only the texts, sorted by similarity (lowest distance first)
        return [text for text, _ in sorted(results, key=lambda x: x[1])]
