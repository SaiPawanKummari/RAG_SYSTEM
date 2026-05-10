from langchain_community.document_loaders import PyPDFLoader

class DocumentLoader:

    def load_pdf(self, path):
        loader = PyPDFLoader(path)
        docs = loader.load()
        return docs