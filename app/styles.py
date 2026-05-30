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