from datetime import datetime
import time

vehichle_type={2: "Bike",3: "Rikshaw", 4: "Car"}

class vehichle:

    all= []

    def __init__(self, number_of_wheels: int, vehichle_number:str, entry_time= datetime.now()):

        assert number_of_wheels in [2,3,4], "Vehichle is not identified, select number of wheels from list[ 2, 3, 4]"
        
        self.number_of_wheels= number_of_wheels
        self.vehichle_type= vehichle_type.get(number_of_wheels)
        self.__vehichle_number= vehichle_number
        self.__entry_time= entry_time
    
        vehichle.all.append(self)

    @property
    def vehichle_number(self):
        return self.__vehichle_number
    
    def entry_time(self):
        return self.__entry_time
    
    @classmethod
    def total_vehichles(cls):
        return len(cls.all)
    

'''v1=vehichle(2,"UP-23-2345")
time.sleep(5)
v2=vehichle(2,"UP-48-9456")
time.sleep(2)
v3=vehichle(4,"MP-10-1156")
v4=vehichle(4,"JKP-15-18526")'''

'''print(vehichle.total_vehichles())
print(v2.vehichle_type)'''