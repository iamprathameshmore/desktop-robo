from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from voice import listen, speak
from bot import generate_response

class VoiceBotApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Voice Bot")
        self.setGeometry(100, 100, 400, 200)

        self.layout = QVBoxLayout()
        self.label = QLabel("Press 'Speak' to interact with the bot.")
        self.layout.addWidget(self.label)

        self.speak_button = QPushButton("Speak")
        self.speak_button.clicked.connect(self.on_speak)
        self.layout.addWidget(self.speak_button)

        self.setLayout(self.layout)

    def on_speak(self):
        command = listen()
        if command:
            response = generate_response(command)
            self.label.setText(f"Bot: {response}")
            speak(response)
