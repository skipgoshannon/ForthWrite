# Core colors
BACKGROUND       = "#000000"
TERMINAL_BG      = "#001100"
PRIMARY_GREEN    = "#00ff00"
DARK_GREEN       = "#003300"
GLOW_GREEN       = "rgba(0, 255, 0, 0.5)"
DIM_GREEN        = "#006600"
TEXT_COLOR       = "#00ff00"
BLACK            = "#000000"

# Font
FONT_FAMILY      = "VT323"
FONT_SIZE_LARGE  = 24
FONT_SIZE_MEDIUM = 20
FONT_SIZE_SMALL  = 18

# Main window style
WINDOW_STYLE = f"""
    QMainWindow {{
        background-color: {BACKGROUND};
    }}
    QWidget#central {{
        background-color: {BACKGROUND};
    }}
"""

# Terminal container style
TERMINAL_STYLE = f"""
    QWidget#terminal {{
        background-color: {TERMINAL_BG};
        border: 4px solid {PRIMARY_GREEN};
    }}
"""

# Editor margins for normal and fullscreen modes
EDITOR_MARGINS_NORMAL     = (20, 20, 20, 20)
EDITOR_MARGINS_FULLSCREEN = (250, 40, 250, 40)

# Line spacing for the editor (as a proportion, 1.0 is normal, 1.5 is 50% more)
EDITOR_LINE_SPACING = 2.0


# Header bar style
HEADER_STYLE = f"""
    QWidget#header {{
        background-color: {PRIMARY_GREEN};
        border-bottom: 4px solid {PRIMARY_GREEN};
    }}
    QLabel#title {{
        color: {BLACK};
        font-family: {FONT_FAMILY};
        font-size: {FONT_SIZE_LARGE}px;
        letter-spacing: 2px;
    }}
    QPushButton#format_btn {{
        color: {BLACK};
        background-color: {PRIMARY_GREEN};
        font-family: {FONT_FAMILY};
        font-size: {FONT_SIZE_MEDIUM}px;
        border: 2px solid {BLACK};
        padding: 2px 6px;
        letter-spacing: 1px;
    }}
    QPushButton#format_btn:hover {{
        background-color: {BLACK};
        color: {PRIMARY_GREEN};
    }}
"""

# Format button style
FORMAT_BTN_STYLE = f"""
    QPushButton {{
        color: {BLACK};
        background-color: {PRIMARY_GREEN};
        font-family: {FONT_FAMILY};
        font-size: {FONT_SIZE_MEDIUM}px;
        border: 2px solid {BLACK};
        padding: 2px 6px;
        letter-spacing: 1px;
    }}
    QPushButton:hover {{
        background-color: {BLACK};
        color: {PRIMARY_GREEN};
    }}
"""

# Filename bar style
FILENAME_STYLE = f"""
    QWidget#filename_bar {{
        background-color: {DARK_GREEN};
        border-bottom: 2px solid {PRIMARY_GREEN};
    }}
    QLabel#file_label {{
        color: {PRIMARY_GREEN};
        font-family: {FONT_FAMILY};
        font-size: {FONT_SIZE_MEDIUM}px;
    }}
    QLineEdit#filename_input {{
        color: {PRIMARY_GREEN};
        background-color: transparent;
        font-family: {FONT_FAMILY};
        font-size: {FONT_SIZE_MEDIUM}px;
        border: none;
        letter-spacing: 2px;
    }}
"""

# Editor area style
EDITOR_STYLE = f"""
    QPlainTextEdit#editor {{
        color: {PRIMARY_GREEN};
        background-color: {TERMINAL_BG};
        font-family: {FONT_FAMILY};
        font-size: {FONT_SIZE_LARGE}px;
        border: none;
        padding: 8px;
        selection-background-color: {PRIMARY_GREEN};
        selection-color: {BLACK};
    }}
"""


# Scrollbar style to match the terminal aesthetic
SCROLLBAR_STYLE = f"""
    QScrollBar:vertical {{
        background-color: {TERMINAL_BG};
        width: 12px;
        border: 1px solid {PRIMARY_GREEN};
    }}
    QScrollBar::handle:vertical {{
        background-color: {PRIMARY_GREEN};
        min-height: 20px;
    }}
    QScrollBar::add-line:vertical,
    QScrollBar::sub-line:vertical {{
        height: 0px;
    }}
    QScrollBar::add-page:vertical,
    QScrollBar::sub-page:vertical {{
        background: none;
    }}
"""


# Status bar style
STATUS_STYLE = f"""
    QWidget#status_bar {{
        background-color: {DARK_GREEN};
        border-top: 2px solid {PRIMARY_GREEN};
    }}
    QLabel#status_label {{
        color: {PRIMARY_GREEN};
        font-family: {FONT_FAMILY};
        font-size: {FONT_SIZE_MEDIUM}px;
    }}
"""

# Pause button style
PAUSE_BTN_STYLE = f"""
    QPushButton {{
        color: {PRIMARY_GREEN};
        background-color: {DARK_GREEN};
        font-family: {FONT_FAMILY};
        font-size: {FONT_SIZE_MEDIUM}px;
        border: 2px solid {PRIMARY_GREEN};
        padding: 2px 6px;
        letter-spacing: 1px;
    }}
    QPushButton:hover {{
        background-color: {PRIMARY_GREEN};
        color: {BLACK};
    }}
"""


# Help dialog style
HELP_DIALOG_STYLE = f"""
    QDialog {{
        background-color: {TERMINAL_BG};
        border: 4px solid {PRIMARY_GREEN};
    }}
    QPlainTextEdit {{
        background-color: {TERMINAL_BG};
        color: {PRIMARY_GREEN};
        font-family: {FONT_FAMILY};
        font-size: {FONT_SIZE_SMALL}px;
        border: none;
        padding: 10px;
    }}
    QPushButton {{
        background-color: {PRIMARY_GREEN};
        color: {BLACK};
        font-family: {FONT_FAMILY};
        font-size: {FONT_SIZE_SMALL}px;
        border: 2px solid {PRIMARY_GREEN};
        padding: 4px 12px;
    }}
    QPushButton:hover {{
        background-color: {DARK_GREEN};
        color: {PRIMARY_GREEN};
    }}
"""


# Help bar style
HELP_STYLE = f"""
    QWidget#help_bar {{
        background-color: {PRIMARY_GREEN};
        border-top: 4px solid {PRIMARY_GREEN};
    }}
    QLabel#help_label {{
        color: {BLACK};
        font-family: {FONT_FAMILY};
        font-size: {FONT_SIZE_SMALL}px;
    }}
"""