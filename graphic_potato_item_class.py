from graphic_crop_item_class import *
from wheat_class import *

import field_resources

class WheatGraphicsPixmapItem(CropGraphicsPixmapItem):
    '''this class provides a graphical representation of a wheat crop'''

    def __init__(self):
        self.avaliable_graphics = [":/potato_seed.png", ":/potato_seedling.png",
                                   ":/potato_young.png", ":/potato_mature.png",
                                   ":/potato_old.png"]
        super().__init__(self.avaliable_graphics)

        self.crop = Wheat()
