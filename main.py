import sys
from PyQt5.QtWidgets import QApplication
from ui.ui_chatbot import ChatBotUI
from models.llama3_ollama_lib import LlamaChatBot

"""
    Examples of models you can use:
        - mistral:7b
        - llama3:8b
        - mixtral
        - Phi4

"""

if __name__ == "__main__":
    app = QApplication(sys.argv)

    model = "mistral:7b"

    ChatBotUIInstance = ChatBotUI(model)
    ChatBotUIInstance.show()  
    sys.exit(app.exec_())   