# Car Parking Designer
from parking import ParkingLot
from vehichle import vehichle

class Billing:
    def __init__(self, vehichle_obj):
        self.vehichle = vehichle_obj
        self.receipt = self.generate_receipt()

    def generate_receipt(self):
        
        receipt = {
            "Vehichle Type": self.vehichle.vehichle_type,
            "Vehichle Number": self.vehichle.vehichle_number,
            "Entry Time": self.vehichle.entry_time(),
        }
        
        if self.vehichle.vehichle_type == "Bike":
            receipt["Amount Payable"] = 20
        elif self.vehichle.vehichle_type == "Car":
            receipt["Amount Payable"] = 40
        else:
            receipt["Amount Payable"] = 30

        return receipt

    def print_receipt(self):
        print("\n----- Receipt -----")
        for key, value in self.receipt.items():
            print(f"{key}: {value}")
        print("-------------------")

p1= ParkingLot(5, 10, True)
if __name__=="__main__":
        
        num= p1.max_limit()

        for i in range(num):
             wheels=int(input("Enter Number of wheels of vehichle: "))
             v_number= input("Enter vehicle number: ")

             V= vehichle(wheels,v_number)
             tot= vehichle.total_vehichles()
             slots_remaining = num-tot

             bill= Billing(V)
             bill.print_receipt()

             print(f"Slots Remaining: {slots_remaining}\n")





         

        