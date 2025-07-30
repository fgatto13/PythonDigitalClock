import sys
from PyQt5.QtWidgets import QApplication
from digitalClock import DigitalClock
from logConfig import setupLogging

def main():
    setupLogging()
    app = QApplication(sys.argv)
    ex = DigitalClock()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()