import string
import random

class VehicleRegistry:

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

class Application:

    def register_vehicle(self, brand: string):
        # create registry instance
        registry = VehicleRegistry()

        # generate a vehicle id of length 12
        vehicle_id = registry.generate_vehicle_id(12)

        # now generate a license plate for the vehicle
        # using the first two charactes of the vehicle id
        license_plate = registry.generate_vehicle_license(vehicle_id)

        # compute the catalog price
        catalog_price = 0
        if brand == "Tesla Model 3":
            catalog_price = 60_000
        elif brand == "Ford F-150":
            catalog_price = 54_000
        elif brand == "BMW 5":
            catalog_price = 45_000

        # compute the tax percentage  (default 5% of the catalogue price, except for electric cars where it is 2%)
        tax_percentage = 0.05
        if brand == "Tesla Model 3":
            tax_percentage = 0.02

        #compute the payable tax
        payable_tax = tax_percentage * catalog_price

        # print out the vehicle registration information
        print("Registration complete. Vehicle information:")
        print(f"Brand: {brand}")
        print(f"Id: {vehicle_id}")
        print(f"License plate: {license_plate}")
        print(f"Payable tax: {payable_tax:,.2f}")
        
app = Application()
app.register_vehicle("Ford F-150")