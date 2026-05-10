from langchain_text_splitters import RecursiveCharacterTextSplitter
class Chunker:

    def split_documents(self, docs):

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )

        chunks = splitter.split_documents(docs)

        return chunks