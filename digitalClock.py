import logging
import os
import sys

from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, Qt, QTime
# to add a custom font:
from PyQt5.QtGui import QFont, QFontDatabase

# our main class will be a digital clock, which inherits from the QWidget class
class DigitalClock(QWidget):
    # let's define the constructor first
    def __init__(self):
        super().__init__()
        # we want to create a time label and then a timer
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        # now we can call the UI initializer
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(1100, 300, 500, 300)

        # let's create a vbox layout
        vbox = QVBoxLayout()

        # add our label to the widget
        vbox.addWidget(self.time_label)
        # and set the layout inside our clock widget
        self.setLayout(vbox)

        # now we want to center our label
        self.time_label.setAlignment(Qt.AlignCenter)
        # and style it a bit:
        self.time_label.setStyleSheet("font-size: 150px;"
                                      "color: hsl(111, 100%, 50%);")

        self.load_font()

        # now we need to connect our timer to the update time function
        self.timer.timeout.connect(self.update_time)
        # and we use the start function to update it every second (1000 ms)
        self.timer.start(1000)

    # now we want to define a function to update the time
    def update_time(self):
        current_time = QTime.currentTime()
        self.time_label.setText(current_time.toString("hh:mm:ss AP"))
        # light mode from 6:00 AM to 7:00 PM
        start_day = QTime(6, 0, 0)
        end_day = QTime(19, 0, 0)
        # let's add a light/dark mode based on the current time:
        if start_day < current_time < end_day:
            self.setStyleSheet("background-color: #f9f9f9;")  # light background
        else:
            self.setStyleSheet("background-color: black;")  # dark background

    def load_font(self):
        try:
            if hasattr(sys, '_MEIPASS'):
                # For PyInstaller, not py2app, but kept for portability
                base_path = sys._MEIPASS
            elif getattr(sys, 'frozen', False):
                # Running inside a macOS .app bundle
                base_path = os.path.join(os.path.dirname(sys.executable), "..", "Resources")
            else:
                # Normal execution
                base_path = os.path.dirname(__file__)
            font_path = os.path.abspath(os.path.join(base_path, "fonts", "ds_digital", "DS-DIGIT.TTF"))

            # to add a downloaded font, we use the QFontDatabase:
            # - it is a class for managing and querying fonts available to the application
            # - the addApplicationFont(path) allows us to add a font to the QFont db
            font_id = QFontDatabase.addApplicationFont(font_path)

            # we want to check if the font has been loaded:
            if font_id == -1:
                # if not, it raises an exception
                raise RuntimeError("Failed to load custom font")

            # we then retrieve the family from the db
            families = QFontDatabase.applicationFontFamilies(font_id)
            # and check that the list is not empty
            if not families:
                # if so, we raise an exception
                raise IndexError("No font families returned")
            # otherwise, we set up the font
            my_font = QFont(families[0], 150)
        except (FileNotFoundError, IndexError, RuntimeError, OSError) as e:
            logging.error("Font loading error", exc_info=True)
            # go back to system font
            my_font = QFont()
            my_font.setPointSize(150)
        self.time_label.setFont(my_font)

