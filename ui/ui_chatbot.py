from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QTextEdit, QLineEdit, QPushButton, QFrame
)
from PyQt5.QtGui import QFont, QTextBlockFormat
from PyQt5.QtCore import Qt
from models.llama3_ollama_lib import LlamaChatBot
from models.ollama_local import LocalOllama     
from ui.styles import get_style

class ChatBotUI(QWidget):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.setWindowTitle("llaminator 🦙")
        self.setGeometry(100, 100, 400, 500)
        self.setFixedSize(500, 500)
        self.setStyleSheet(get_style())
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        container = QFrame(self)
        container.setObjectName("backgroundContainer")

        container_layout = QVBoxLayout()

        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setFont(QFont("Segoe UI", 10))
        self.chat_display.setObjectName("chatDisplay")
        self.chat_display.setFixedHeight(400)
        self.chat_display.setAcceptRichText(True)
        container_layout.addWidget(self.chat_display)

        input_layout = QHBoxLayout()

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type your message...")
        self.input_field.setFont(QFont("Segoe UI", 10))
        self.input_field.setObjectName("inputField")
        self.input_field.returnPressed.connect(self.send_message)

        self.chat_display.append(f'<p style="margin-bottom: 5px;"><b>ΛI:</b> Welcome! I\'m llaminator.</p>')
        self.chat_display.append(f'<p style="margin-bottom: 5px;"><b>ΛI:</b> How can I help you today? \n</p>')

        send_button = QPushButton("➤")
        send_button.setObjectName("sendButton")
        send_button.clicked.connect(self.send_message)
        send_button.setCursor(Qt.PointingHandCursor)

        input_layout.addWidget(self.input_field)
        input_layout.addWidget(send_button)
        container_layout.addLayout(input_layout)

        container.setLayout(container_layout)

        layout.addWidget(container)
        self.setLayout(layout)
    
    def send_message(self):
        user_msg = self.input_field.text().strip()
        if user_msg:
            cursor = self.chat_display.textCursor()
            cursor.movePosition(cursor.End)

            format_user = QTextBlockFormat()
            format_user.setAlignment(Qt.AlignRight)
            cursor.insertBlock(format_user)
            cursor.insertHtml(f'<span style="border-radius: 10px; padding: 8px; display: inline-block;"><b>You: </b></span>')
            cursor.insertHtml(f'{user_msg}<br>')
            self.chat_display.setTextCursor(cursor)
            
            self.input_field.clear()
            QApplication.processEvents()
            
            #! You can choose between two implementations:
            #? Use get_bot_reply_ollama_lib to use the ollama-python library
            #? Use get_bot_reply_ollama_local to use the local ollama server

            bot_reply = self.get_bot_reply_ollama_local(user_msg)
            
            format_bot = QTextBlockFormat()
            format_bot.setAlignment(Qt.AlignLeft)
            cursor.insertBlock(format_bot)
            cursor.insertHtml(f'<span style="border-radius: 10px; padding: 8px; display: inline-block;"><b>ΛI: <b></span>')
            cursor.insertHtml(f'{bot_reply}<br>')

            self.chat_display.setTextCursor(cursor)
            self.chat_display.ensureCursorVisible()

    def get_bot_reply_ollama_lib(self, message):
        model = LlamaChatBot(message, self.model)
        output = model.model_response()
        return output
    
    def get_bot_reply_ollama_local(self, message):
        local= LocalOllama(message, self.model)
        local_output = local.query_ollama()
        return local_output
