import sys
import os
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFontDatabase
from app.window import MainWindow


def load_font():
    # Load the VT323 font for UI elements
    vt323_path = os.path.join(os.path.dirname(__file__), "assets", "fonts", "VT323-Regular.ttf")
    vt323_id = QFontDatabase.addApplicationFont(vt323_path)
    if vt323_id == -1:
        print("Warning: VT323 font could not be loaded.")
    else:
        print("VT323 font loaded successfully.")

    # Load the WarGames Terminal DT font for the editor
    wargames_path = os.path.join(os.path.dirname(__file__), "assets", "fonts", "WarGames Terminal D T.ttf")
    wargames_id = QFontDatabase.addApplicationFont(wargames_path)
    if wargames_id == -1:
        print("Warning: WarGames Terminal DT font could not be loaded.")
    else:
        print("WarGames Terminal DT font loaded successfully.")


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


