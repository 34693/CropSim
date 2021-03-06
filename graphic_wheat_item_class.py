from graphic_crop_item_class import *
from wheat_class import *

import field_resources

class WheatGraphicsPixmapItem(CropGraphicsPixmapItem):
    '''this class provides a graphical representation of a wheat crop'''

    def __init__(self):
        self.avaliable_graphics = [":/wheat_seed.png", ":/wheat_seedling.png",
                                   ":/wheat_young.png", ":/wheat_mature.png",
                                   ":/wheat_old.png"]
        super().__init__(self.avaliable_graphics)

        self.crop = Wheat()
