from PyQt6.QtWidgets import QPlainTextEdit
from PyQt6.QtGui import QFont, QPainter, QColor, QTextBlockFormat, QTextCursor
from PyQt6.QtCore import Qt
from app.styles import EDITOR_STYLE, FONT_FAMILY_EDITOR, FONT_SIZE_LARGE, TERMINAL_BG, EDITOR_MARGINS_NORMAL, EDITOR_LINE_SPACING, SCROLLBAR_STYLE

class Editor(QPlainTextEdit):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Set the object name so the stylesheet can target this widget
        self.setObjectName("editor")

        # Apply the green-on-black terminal stylesheet
        self.setStyleSheet(EDITOR_STYLE)

        # Apply the scrollbar style
        self.verticalScrollBar().setStyleSheet(SCROLLBAR_STYLE)

        # Set margins so text is not flush against the edges
        self.setViewportMargins(*EDITOR_MARGINS_NORMAL)

        # Track current font size so we can increase and decrease it
        self.current_font_size = FONT_SIZE_LARGE

        # Load the VT323 retro font at the correct size
        font = QFont(FONT_FAMILY_EDITOR, self.current_font_size)
        self.setFont(font)

        # Show placeholder text when the editor is empty
        self.setPlaceholderText("START TYPING...")

        # Wrap lines at the widget boundary so text doesn't scroll off screen
        self.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)

        # Apply line spacing to the document
        self._apply_line_spacing()

        # Reapply line spacing whenever the document changes
        self.document().contentsChanged.connect(self._apply_line_spacing)

    def _apply_line_spacing(self):
        # Temporarily disconnect to avoid recursive calls
        try:
            self.document().contentsChanged.disconnect(self._apply_line_spacing)
        except TypeError:
            pass

        # Apply the block format with line spacing to all text
        block_format = QTextBlockFormat()
        block_format.setLineHeight(
            EDITOR_LINE_SPACING * 100,
            QTextBlockFormat.LineHeightTypes.ProportionalHeight.value
        )
        cursor = QTextCursor(self.document())
        cursor.select(QTextCursor.SelectionType.Document)
        cursor.mergeBlockFormat(block_format)

        # Reconnect after applying
        self.document().contentsChanged.connect(self._apply_line_spacing)

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