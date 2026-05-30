from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QFileDialog, QMessageBox
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QKeySequence, QShortcut
from app.toolbar import Toolbar
from app.editor import Editor
from app.statusbar import StatusBar
from app.styles import WINDOW_STYLE, TERMINAL_STYLE


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Set the window title and minimum size
        self.setWindowTitle("ForthWrite")
        self.setMinimumSize(800, 600)

        # Apply the main window stylesheet
        self.setStyleSheet(WINDOW_STYLE)

        # Track elapsed session time in seconds
        self.elapsed_seconds = 0

        # Build the UI and connect everything together
        self._build_ui()
        self._setup_shortcuts()
        self._setup_timers()


def _build_ui(self):
        # Create the central widget that holds everything
        central = QWidget()
        central.setObjectName("central")
        self.setCentralWidget(central)

        # Create the terminal container widget with the green border
        self.terminal = QWidget()
        self.terminal.setObjectName("terminal")
        self.terminal.setStyleSheet(TERMINAL_STYLE)

        # Create the three main sections of the app
        self.toolbar    = Toolbar()
        self.editor     = Editor()
        self.statusbar  = StatusBar()

        # Connect the format buttons in the toolbar to the editor
        self.toolbar.bold_btn.clicked.connect(self.format_bold)
        self.toolbar.italic_btn.clicked.connect(self.format_italic)
        self.toolbar.h1_btn.clicked.connect(self.format_h1)
        self.toolbar.h2_btn.clicked.connect(self.format_h2)
        self.toolbar.bullet_btn.clicked.connect(self.format_bullet)

        # Update the status bar whenever the text changes
        self.editor.textChanged.connect(self.on_text_changed)

        # Stack toolbar, editor, and statusbar vertically inside the terminal
        terminal_layout = QVBoxLayout(self.terminal)
        terminal_layout.setContentsMargins(0, 0, 0, 0)
        terminal_layout.setSpacing(0)
        terminal_layout.addWidget(self.toolbar)
        terminal_layout.addWidget(self.editor)
        terminal_layout.addWidget(self.statusbar)

        # Center the terminal container inside the central widget
        central_layout = QVBoxLayout(central)
        central_layout.addWidget(self.terminal)


def _setup_shortcuts(self):
        # Ctrl+S — save the current document
        QShortcut(QKeySequence("Ctrl+S"), self).activated.connect(self.save_file)

        # Ctrl+B — wrap selected text in bold markdown
        QShortcut(QKeySequence("Ctrl+B"), self).activated.connect(self.format_bold)

        # Ctrl+I — wrap selected text in italic markdown
        QShortcut(QKeySequence("Ctrl+I"), self).activated.connect(self.format_italic)

        # Ctrl+M — toggle the format menu in the toolbar
        QShortcut(QKeySequence("Ctrl+M"), self).activated.connect(self.toolbar.toggle_format_menu)

        # Ctrl+Shift+N — start a new document
        QShortcut(QKeySequence("Ctrl+Shift+N"), self).activated.connect(self.new_document)

        # Ctrl+E — exit the application
        QShortcut(QKeySequence("Ctrl+E"), self).activated.connect(self.exit_app)


def _setup_timers(self):
        # Timer to update the clock in the toolbar every second
        self.clock_timer = QTimer()
        self.clock_timer.timeout.connect(self.toolbar.update_date)
        self.clock_timer.start(1000)  # Fire every 1000 milliseconds (1 second)

        # Timer to update the session elapsed time every second
        self.session_timer = QTimer()
        self.session_timer.timeout.connect(self.tick_session)
        self.session_timer.start(1000)

        # Update the clock immediately so it shows on launch
        self.toolbar.update_date()


def tick_session(self):
        # Increment the elapsed time by one second and update the status bar
        self.elapsed_seconds += 1
        self.statusbar.update_timer(self.elapsed_seconds)


def on_text_changed(self):
        # Get the current text from the editor and update the status bar stats
        text = self.editor.toPlainText()
        self.statusbar.update_stats(text)


def format_bold(self):
        # Wrap the selected text in markdown bold markers
        cursor = self.editor.textCursor()
        selected = cursor.selectedText()
        cursor.insertText(f"**{selected}**")

    def format_italic(self):
        # Wrap the selected text in markdown italic markers
        cursor = self.editor.textCursor()
        selected = cursor.selectedText()
        cursor.insertText(f"*{selected}*")

    def format_h1(self):
        # Add a markdown H1 marker at the start of the current line
        cursor = self.editor.textCursor()
        cursor.movePosition(cursor.MoveOperation.StartOfLine)
        cursor.insertText("# ")

    def format_h2(self):
        # Add a markdown H2 marker at the start of the current line
        cursor = self.editor.textCursor()
        cursor.movePosition(cursor.MoveOperation.StartOfLine)
        cursor.insertText("## ")

    def format_bullet(self):
        # Add a bullet point marker at the start of the current line
        cursor = self.editor.textCursor()
        cursor.movePosition(cursor.MoveOperation.StartOfLine)
        cursor.insertText("• ")


def save_file(self):
        # Get the filename from the toolbar input
        filename = self.toolbar.filename_input.text()

        # Open a save dialog starting with the current filename
        path, _ = QFileDialog.getSaveFileName(
            self, "Save File", filename, "Text Files (*.txt);;All Files (*)"
        )

        # If the user didn't cancel, write the editor contents to the file
        if path:
            with open(path, "w") as f:
                f.write(self.editor.toPlainText())

            # Update the filename bar to show the saved filename
            self.toolbar.filename_input.setText(path.split("/")[-1].upper())

    def new_document(self):
        # Ask the user to confirm before clearing the editor
        reply = QMessageBox.question(
            self, "New Document",
            "Start a new document? Unsaved changes will be lost.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            # Clear the editor, reset the filename, and reset the session timer
            self.editor.clear()
            self.toolbar.filename_input.setText("UNTITLED.TXT")
            self.elapsed_seconds = 0

    def exit_app(self):
        # Ask the user to confirm before closing the application
        reply = QMessageBox.question(
            self, "Exit ForthWrite",
            "Exit ForthWrite? Unsaved changes will be lost.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.close()


