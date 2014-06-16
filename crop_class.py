class Crop:
    '''A generic food crop'''

    #constructor
    def __init__(self, growth_rate, light_need, water_need):
        #set the attributes with an initial value

        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = 'Seed'
        self._type = 'Generic'

        #the aboce attributes are prefixed with an underscore to indicate
        #that they should no be accessed directly from outwith the class

    def needs(self):
        #return a dictionary containing the light and water needs
        return {'light need':self._light_need, 'water need': self._water_needs}

    #method to report the provided information about the state of the
    #current crop
    def report(self):
        #return a dictionary containing the type,status, growth and days growing
        return {'type':self._type,'status':self._status,'growth':self.
        


def main():
    #instaniate the class
    new_crop = Crop(1,4,3)
    #test to see if it works
    print(new_crop._status)
    print(new_crop._light_need)
    print(new_crop._water_need)
    new_crop2 = Crop(2,5,7)
    print(new_crop2._status)
    print(new_crop2._light_need)
    print(new_crop2._water_need)

if __name__ == "__main__":
    main()
