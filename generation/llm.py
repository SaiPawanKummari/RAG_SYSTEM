import ollama

class LLM:

    def generate(self, prompt):

        response = ollama.chat(
            model='tinyllama',
            messages=[
                {
                    'role': 'user',
                    'content': prompt
                }
            ]
        )

        return response['message']['content']