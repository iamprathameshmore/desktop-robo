from PyQt6.QtWidgets import QApplication
from gui import VoiceBotApp

if __name__ == "__main__":
    app = QApplication([])
    window = VoiceBotApp()
    window.show()
    app.exec()
