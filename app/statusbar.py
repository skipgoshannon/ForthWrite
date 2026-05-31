from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt
from app.styles import STATUS_STYLE, HELP_STYLE, PAUSE_BTN_STYLE


class StatusBar(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        # Build each section of the status area
        self._build_status_bar()  # Character count, word count, timer
        self._build_help_bar()    # Keyboard shortcut hints
        self._setup_layout()      # Stack them vertically

    def _build_status_bar(self):
        # Container widget for the stats row
        self.status_bar = QWidget()
        self.status_bar.setObjectName("status_bar")
        self.status_bar.setStyleSheet(STATUS_STYLE)

        # Label showing character count
        self.char_label = QLabel("CH: 0")
        self.char_label.setObjectName("status_label")

        # Label showing word count
        self.word_label = QLabel("WD: 0")
        self.word_label.setObjectName("status_label")

        # Label showing elapsed session time
        self.time_label = QLabel("TIME: 00:00:00")
        self.time_label.setObjectName("status_label")

        # Button to pause and resume the session timer
        self.pause_btn = QPushButton("PAUSE")
        self.pause_btn.setStyleSheet(PAUSE_BTN_STYLE)

        # Button to open the writing prompt menu
        self.prompt_btn = QPushButton("PROMPT")
        self.prompt_btn.setStyleSheet(PAUSE_BTN_STYLE)
        
        # Button to increase font size
        self.font_up_btn = QPushButton("A+")
        self.font_up_btn.setStyleSheet(PAUSE_BTN_STYLE)

        # Button to decrease font size
        self.font_down_btn = QPushButton("A-")
        self.font_down_btn.setStyleSheet(PAUSE_BTN_STYLE)

        # Arrange labels and buttons horizontally
        layout = QHBoxLayout(self.status_bar)
        layout.addWidget(self.char_label)
        layout.addSpacing(20)
        layout.addWidget(self.word_label)
        layout.addStretch()
        layout.addWidget(self.prompt_btn)
        layout.addSpacing(10)
        layout.addWidget(self.font_down_btn)
        layout.addSpacing(5)
        layout.addWidget(self.font_up_btn)
        layout.addSpacing(10)
        layout.addWidget(self.pause_btn)
        layout.addSpacing(10)
        layout.addWidget(self.time_label)

    def _build_help_bar(self):
        # Container widget for the keyboard shortcut hints
        self.help_bar = QWidget()
        self.help_bar.setObjectName("help_bar")
        self.help_bar.setStyleSheet(HELP_STYLE)

        # Single label showing all available keyboard shortcuts
        self.help_label = QLabel(
            "CTRL+N=NEW  CTRL+O=OPEN  CTRL+S=SAVE  CTRL+M=MENU  "
            "CTRL+E=EXIT  CTRL+F=FULLSCREEN"
        )

        self.help_label.setObjectName("help_label")

        # Center the help text horizontally
        layout = QHBoxLayout(self.help_bar)
        layout.addWidget(self.help_label, alignment=Qt.AlignmentFlag.AlignCenter)

    def _setup_layout(self):
        # Stack the status bar and help bar vertically
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)  # No padding around the status area
        layout.setSpacing(0)                    # No gap between the two bars
        layout.addWidget(self.status_bar)
        layout.addWidget(self.help_bar)

    def update_stats(self, text):
        # Count total characters in the editor
        char_count = len(text)

        # Count words by splitting on whitespace, returns 0 if text is empty
        word_count = len(text.split()) if text.strip() else 0

        # Update the labels with the new counts
        self.char_label.setText(f"CH: {char_count}")
        self.word_label.setText(f"WD: {word_count}")

    def update_timer(self, seconds):
        # Convert total seconds into hours, minutes, and seconds
        hours   = seconds // 3600
        minutes = (seconds % 3600) // 60
        secs    = seconds % 60

        # Format as HH:MM:SS and update the timer label
        self.time_label.setText(
            f"TIME: {hours:02d}:{minutes:02d}:{secs:02d}"
        )