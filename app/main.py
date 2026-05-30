import sys
import os
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFontDatabase
from app.window import MainWindow


def load_font():
    # Build the path to the font file relative to this script
    font_path = os.path.join(os.path.dirname(__file__), "assets", "fonts", "VT323-Regular.ttf")

    # Load the font into Qt's font database so widgets can use it by name
    font_id = QFontDatabase.addApplicationFont(font_path)

    if font_id == -1:
        print("Warning: VT323 font could not be loaded. Using system default.")
    else:
        print("VT323 font loaded successfully.")


def main():
    # Create the Qt application instance
    app = QApplication(sys.argv)

    # Load the retro font before creating any windows
    load_font()

    # Create and show the main window
    window = MainWindow()
    window.show()

    # Start the Qt event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main()


