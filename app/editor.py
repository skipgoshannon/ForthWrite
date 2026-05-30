from PyQt6.QtWidgets import QPlainTextEdit
from PyQt6.QtGui import QFont, QPainter, QColor
from PyQt6.QtCore import Qt
from app.styles import EDITOR_STYLE, FONT_FAMILY, FONT_SIZE_LARGE, TERMINAL_BG


class Editor(QPlainTextEdit):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Set the object name so the stylesheet can target this widget
        self.setObjectName("editor")

        # Apply the green-on-black terminal stylesheet
        self.setStyleSheet(EDITOR_STYLE)

        # Load the VT323 retro font at the correct size
        font = QFont(FONT_FAMILY, FONT_SIZE_LARGE)
        self.setFont(font)

        # Disable the spell checker — we don't want red squiggles in a retro editor
        self.setDocument(self.document())

        # Show placeholder text when the editor is empty
        self.setPlaceholderText("START TYPING...")

        # Disable line wrap so long lines scroll horizontally like an old terminal
        self.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)


def paintEvent(self, event):
        # First let Qt draw the editor normally
        super().paintEvent(event)

        # Now paint the scanline overlay on top
        painter = QPainter(self.viewport())

        # Draw horizontal lines across the entire editor area
        # to simulate the look of a CRT screen
        painter.setPen(QColor(0, 255, 0, 8))  # Very faint green lines
        for y in range(0, self.height(), 3):
            painter.drawLine(0, y, self.width(), y)

        painter.end()


