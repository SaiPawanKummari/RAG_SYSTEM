import os

from langchain_community.document_loaders import PyPDFLoader

class DocumentLoader:

    def load_pdfs(self, folder_path):

        all_docs = []

        for file_name in os.listdir(folder_path):

            if file_name.endswith(".pdf"):

                full_path = os.path.join(
                    folder_path,
                    file_name
                )

                print(f"Loading: {file_name}")

                loader = PyPDFLoader(full_path)

                docs = loader.load()

                for doc in docs:
                    doc.metadata["source_file"] = file_name

                all_docs.extend(docs)

        return all_docs