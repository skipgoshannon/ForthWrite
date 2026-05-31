from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPlainTextEdit, QPushButton
from PyQt6.QtGui import QFont
from app.styles import FONT_FAMILY, FONT_SIZE_SMALL, HELP_DIALOG_STYLE

HELP_TEXT = """FORTHWRITE KEYBOARD SHORTCUTS

FILE
  Ctrl+N          New document
  Ctrl+O          Open file
  Ctrl+S          Save
  Ctrl+E          Exit

FORMATTING
  Ctrl+B          Bold
  Ctrl+I          Italic
  Ctrl+1          H1 heading
  Ctrl+2          H2 heading
  Ctrl+8          Bullet point
  Ctrl+M          Toggle format menu

VIEW
  Ctrl+F          Toggle fullscreen
  Ctrl+9          Increase font size
  Ctrl+0          Decrease font size

PROMPTS
  Ctrl+W          Random story prompt
  Ctrl+J          Random journal prompt

TIMER
  Ctrl+P          Pause / resume timer

HELP
  Ctrl+H          Show this screen
"""


class HelpDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Set the dialog title and size
        self.setWindowTitle("ForthWrite Help")
        self.setMinimumSize(600, 500)

        # Apply the terminal styled stylesheet
        self.setStyleSheet(HELP_DIALOG_STYLE)

        # Text area showing the help content — read only
        self.text = QPlainTextEdit()
        self.text.setPlainText(HELP_TEXT)
        self.text.setReadOnly(True)
        self.text.setFont(QFont(FONT_FAMILY, FONT_SIZE_SMALL))

        # Close button at the bottom
        self.close_btn = QPushButton("CLOSE")
        self.close_btn.clicked.connect(self.close)

        # Stack text and button vertically
        layout = QVBoxLayout(self)
        layout.addWidget(self.text)
        layout.addWidget(self.close_btn)