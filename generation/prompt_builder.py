class PromptBuilder:

    def build_prompt(self,
                     query,
                     retrieved_chunks):

        context = "\n\n".join(retrieved_chunks)

        prompt = f"""
You are a helpful assistant.

Answer the question using the context below.

If the answer is not in the context, say:
"I could not find the answer in the document."

Context:
{context}

Question:
{query}

Helpful Answer:
"""

        return prompt