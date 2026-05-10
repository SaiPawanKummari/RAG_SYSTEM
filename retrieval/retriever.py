import numpy as np

class Retriever:

    def retrieve(self,
                 query,
                 embedder,
                 index,
                 texts,
                 top_k=3):

        query_embedding = np.array(
            list(embedder.model.embed([query])),
            dtype='float32'
        )

        distances, indices = index.search(
            query_embedding,
            top_k
        )

        results = [texts[i] for i in indices[0]]

        return results