import graphic_animal_item_class import *
from cow_class import *

import field_resources

class CowGraphicsPixmapItem(AnimalgraphicsPixmapItem):
    '''this class provides a graphical represenation of a cow'''

    def __init__(self):
        self.avaliable_graphics = [";/cow_baby.png",":/cow_poor.png",
                                   ":/cow_fine.png", ":/cow_prime.png"]
