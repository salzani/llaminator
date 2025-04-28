import requests

class LocalOllama:
    def __init__(self, prompt, model):
        self.prompt = prompt
        self.model = model
        
    def query_ollama(self):
        url = "http://localhost:11434/api/generate"
        payload = {
            "model": self.model,
            "prompt": f'{self.prompt}',
            "stream": False,
            "temperature": 0.1
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                output = data.get("response", "No response received")
                return output
            else:
                return f"Error: {response.status_code}, {response.text}"
        except Exception as e:
            return f"error: {e}"