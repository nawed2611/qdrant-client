from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

class neural_searcher:
    def __init__(self, collection_name, model_name):
        self.collection_name = "startups"
        self.model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens', device='cpu')
        self.qdrant_client = QdrantClient(host='localhost', port=6333)

    def search(self, text:str):
        vector = self.model.encode(text).tolist()

        # Search for nearest vectors
        result = self.qdrant_client.search(
            collection_name=self.collection_name,
            query_vector=vector,
        )
        payloads = [r.payload for r in result]

        return payloads
