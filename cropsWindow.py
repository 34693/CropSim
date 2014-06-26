import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class CropWindow(QMainWindow):
    '''this class creates a main window to observe the growth of a simulation'''

    #constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crop Simulator")

def main():
    crop_simulation = QApplication(sys.argv)
    crop_window = CropWindow()
    crop_window.show()
    crop_window.raise_()
    crop_simulation.exec_()

if __name__ == "__main__":
    main()