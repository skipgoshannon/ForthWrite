from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QLineEdit, QVBoxLayout
from PyQt6.QtCore import Qt, QDateTime
from app.styles import (
    HEADER_STYLE, FILENAME_STYLE, FORMAT_BTN_STYLE,
    FONT_FAMILY, FONT_SIZE_MEDIUM
)


class Toolbar(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        # Build each section of the toolbar
        self.format_visible = False
        self._build_header()       # Top bar with title and format buttons
        self._build_filename_bar() # Bar below header showing the filename
        self._setup_layout()       # Stack them vertically

    def _build_header(self):
        # Container widget for the top header row
        self.header = QWidget()
        self.header.setObjectName("header")
        self.header.setStyleSheet(HEADER_STYLE)

        # App title on the left
        self.title_label = QLabel("ForthWrite")
        self.title_label.setObjectName("title")

        # Button to toggle the format menu
        self.format_btn = QPushButton("FORMAT")
        self.format_btn.setObjectName("format_btn")
        self.format_btn.clicked.connect(self.toggle_format_menu)

        # Formatting buttons — hidden by default until FORMAT is clicked
        self.bold_btn   = QPushButton("[B]OLD")
        self.italic_btn = QPushButton("[I]TALIC")
        self.h1_btn     = QPushButton("H1")
        self.h2_btn     = QPushButton("H2")
        self.bullet_btn = QPushButton("BULLET")

        # Apply style and hide all format buttons initially
        for btn in [self.bold_btn, self.italic_btn, self.h1_btn,
                    self.h2_btn, self.bullet_btn]:
            btn.setStyleSheet(FORMAT_BTN_STYLE)
            btn.hide()

        # Date and time label on the right
        self.date_label = QLabel()
        self.date_label.setObjectName("title")

        # Arrange everything horizontally in the header
        layout = QHBoxLayout(self.header)
        layout.addWidget(self.title_label)
        layout.addSpacing(10)
        layout.addWidget(self.format_btn)
        layout.addSpacing(10)
        layout.addWidget(self.bold_btn)
        layout.addWidget(self.italic_btn)
        layout.addWidget(self.h1_btn)
        layout.addWidget(self.h2_btn)
        layout.addWidget(self.bullet_btn)
        layout.addStretch()
        layout.addWidget(self.date_label)

    def _build_filename_bar(self):
        # Container widget for the filename row
        self.filename_bar = QWidget()
        self.filename_bar.setObjectName("filename_bar")
        self.filename_bar.setStyleSheet(FILENAME_STYLE)

        # Static "FILE:" label on the left
        self.file_label = QLabel("FILE:")
        self.file_label.setObjectName("file_label")

        # Editable filename field, defaults to UNTITLED.TXT
        self.filename_input = QLineEdit("UNTITLED.TXT")
        self.filename_input.setObjectName("filename_input")

        # Arrange label and input side by side
        layout = QHBoxLayout(self.filename_bar)
        layout.addWidget(self.file_label)
        layout.addWidget(self.filename_input)

    def _setup_layout(self):
        # Stack the header bar and filename bar vertically
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)  # No padding around the toolbar
        layout.setSpacing(0)                    # No gap between header and filename bar
        layout.addWidget(self.header)
        layout.addWidget(self.filename_bar)

    def toggle_format_menu(self):
        # Show or hide the formatting buttons based on current state
        self.format_visible = not self.format_visible

        for btn in [self.bold_btn, self.italic_btn, self.h1_btn,
                    self.h2_btn, self.bullet_btn]:
            if self.format_visible:
                btn.show()
            else:
                btn.hide()

    def update_date(self):
        # Update the date and time label in the top right of the header
        now = QDateTime.currentDateTime()
        self.date_label.setText(now.toString("MM/dd/yyyy HH:mm"))