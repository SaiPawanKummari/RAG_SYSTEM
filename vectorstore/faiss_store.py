import faiss
import numpy as np

class FAISSStore:

    def build_index(self, embeddings):

        vectors = np.array(
            embeddings,
            dtype='float32'
        )

        dimension = vectors.shape[1]

        index = faiss.IndexFlatL2(dimension)

        index.add(vectors)

        return index