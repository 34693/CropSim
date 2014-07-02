from graphic_field_item_class import *

class CropGraphicsPixmapItem(FieldItemGraphicsPixmapItem):
    '''this class provides a pixmap item with a preset image for the crop'''

    def __init__(self,graphics_list):
        super().__init__(graphics_list)

        self.crop = None

    def update_status(self):
        if self.crop._status == "Seed":
            self.setPixmap(QPixmap(self.avaliable_graphics[0]).scaleToWidth(25,1)
        if self.crop._status == "Seedling":
            self.setPixmap(QPixmap(self.avaliable_graphics[1]).scaleToWidth(25,1)
        if self.crop._status == "Young":
            self.setPixmap(QPixmap(self.avaliable_graphics[2]).scaleToWidth(25,1)
        if self.crop._status == "Mature":
            self.setPixmap(QPixmap(self.avaliable_graphics[3]).scaleToWidth(25,1)
        if self.crop._status == "Old":
            self.setPixmap(QPixmap(self.avaliable_graphics[4]).scaleToWidth(25,1)
