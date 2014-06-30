import sys
import random

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from radio_button_widget_class import *

from cow_class import *
from sheep_class import *

class AnimalWindow(QMainWindow):
    '''this class creates a main window to observe the growth of a simulation'''

    #constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crop Simulator")
        self.create_select_animal_layout()

        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.select_animal_widget)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)

    def create_select_animal_layout(self):

        self.animal_radio_buttons = RadioButtonWidget("Animal Simulation", "Please select a animal", ("Cow", "Sheep"))
        self.instantiate_button = QPushButton("Create Crop")

        self.initial_layout = QVBoxLayout()
        self.initial_layout.addWidget(self.animal_radio_buttons)
        self.initial_layout.addWidget(self.instantiate_button)

        self.select_animal_widget = QWidget()
        self.select_animal_widget.setLayout(self.initial_layout)

    def create_view_animal_layout(self,animal_type):

        self.growth_label = QLabel("Growth")
        self.days_label = QLabel("Days Growing")
        self.status_label = QLabel("Crop Status")

        self.growth_line_edit = QLineEdit()
        self.days_line_edit = QLineEdit()
        self.status_line_edit = QLineEdit()

        if crop_type == 1:
            self.crop_view = WheatView()
        elif crop_type == 2:
            self.crop_view = PotatoView()

        self.crop_view.setHorizontalScrollBarPolicy(1)
        self.crop_view.setVerticalScrollBarPolicy(1)
        self.crop_view.setFixedHeight(182)
        self.crop_view.setFixedWidth(242)

        self.manual_grow_button = QPushButton("Manually Grow")
        self.automatic_grow_button = QPushButton("Automatically gorw")

        self.grow_grid = QGridLayout()
        self.status_grid = QGridLayout()

        self.status_grid.addWidget(self.growth_label,0,0)
        self.status_grid.addWidget(self.days_label,1,0)
        self.status_grid.addWidget(self.status_label,2,0)

        self.status_grid.addWidget(self.growth_line_edit,0,1)
        self.status_grid.addWidget(self.days_line_edit,1,1)
        self.status_grid.addWidget(self.status_line_edit,2,1)
        
        self.grow_grid.addWidget(self.crop_view,0,0)
        self.grow_grid.addLayout(self.status_grid,0,1)
        self.grow_grid.addWidget(self.manual_grow_button,1,0)
        self.grow_grid.addWidget(self.automatic_grow_button,1,1)

        self.view_crop_widget = QWidget()
        self.view_crop_widget.setLayout(self.grow_grid)

        self.automatic_grow_button.clicked.connect(self.automatically_grow_crop)
        self.manual_grow_button.clicked.connect(self.manually_grow_crop)

        
        self.instantiate_button.clicked.connect(self.instantiate_animal)

    def instantiate_animal(self):
        animal_type = self.animal_radio_buttons.selected_button()
        if animal_type == 1:
            self.simulated_crop = Cow()
        elif animal_type == 2:
            self.simulated_crop = Sheep()


def main():
    animal_simulation = QApplication(sys.argv)
    animal_window = AnimalWindow()
    animal_window.show()
    animal_window.raise_()
    animal_simulation.exec_()

if __name__ == "__main__":
    main()
