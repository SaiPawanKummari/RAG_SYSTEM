from fastembed import TextEmbedding

class Embedder:

    def __init__(self):
        self.model = TextEmbedding(
            model_name="BAAI/bge-small-en"
        )

    def create_embeddings(self, chunks):

        texts = [chunk.page_content for chunk in chunks]

        embeddings = list(self.model.embed(texts))

        return texts, embeddings