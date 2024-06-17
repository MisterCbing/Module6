class Vehicle:
    vehicle_type = 'none'

class Car:
    price = 1000000
    def horse_powers(self):
        return self.horse_powers()

class Nissan(Car, Vehicle):
    vehicle_type = 'bullet'
    price = 1500000

    def horse_powers(self):
        return self.horse_powers()

nissan_skyline = Nissan()
print(nissan_skyline.vehicle_type)
print(nissan_skyline.price)