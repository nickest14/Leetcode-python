# 1603. Design Parking System

class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.parking = {
            # [total occupied, max_capacity]
            1: [0, big],
            2: [0, medium],
            3: [0, small],
        }

    def addCar(self, carType: int) -> bool:
        new_total = self.parking[carType][0] + 1
        if new_total <= self.parking[carType][1]:
            self.parking[carType][0] = new_total
            return True
        return False


obj = ParkingSystem(1, 1, 0)
param_1 = obj.addCar(1)
param_2 = obj.addCar(2)
param_3 = obj.addCar(3)
param_4 = obj.addCar(1)
print(param_1, param_2, param_3, param_4)
