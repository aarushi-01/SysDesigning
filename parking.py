'''{
    'parkinglot design':['entry-exit','multilevel','slots- available'],
    'vehichle types':[],
    'bill_generation':['vehichle type','slot availability']

}'''

class ParkingLot():

    def __init__(self, levels: int, floor_limit:int, availability: bool):

        assert levels>0, f"Levels of parking {levels} is less than zero"

        self.levels= levels
        self.floor_limit= floor_limit
        self.__availability= availability

    @property
    def availability(self):
        return self.__availability
    
    def entry_exit(self):
        self.entry= "spot 0"
        self.exit= f"spot {self.floor_limit+1}"

        return f" Enter from {self.entry} and exit from {self.exit}"

    def max_limit(self):
        return self.levels*self.floor_limit
    

'''print(p1.max_limit())
print(p1.entry_exit())'''





