import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class FaissVectorStore:
    def __init__(self, embedding_model_name="all-MiniLM-L6-v2", dimension=384):
        self.dimension = dimension
        self.model = SentenceTransformer(embedding_model_name)
        self.index = faiss.IndexFlatL2(dimension)
        self.texts = []

    def add_documents(self, docs):
        """
        docs: list of strings to index
        """
        embeddings = self.model.encode(docs, convert_to_numpy=True)
        self.index.add(embeddings)
        self.texts.extend(docs)

    def search(self, query, top_k=5):
        """
        query: string
        returns: list of (text, score)
        """
        q_emb = self.model.encode([query], convert_to_numpy=True)
        distances, indices = self.index.search(q_emb, top_k)
        results = []
        for dist, idx in zip(distances[0], indices[0]):
            if idx < len(self.texts):
                results.append((self.texts[idx], dist))
        return results
