from ollama import chat
from ollama import ChatResponse

class LlamaChatBot():
    def __init__(self, prompt, model):
        self.prompt = prompt
        self.model = model

    def model_response(self):

        response: ChatResponse = chat(self.model, messages=[
            {
                'role': 'user',
               'content': f'{self.prompt}'
            },
            ]
        )
        return response["message"]["content"]



