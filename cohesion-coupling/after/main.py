from dataclasses import dataclass
import string
import random


@dataclass
class VechileInfo:
    brand: str
    catalog_price: int
    electric: bool

    def compute_tax(self) -> float:
        tax_percentage = 0.05
        if self.electric:
            tax_percentage = 0.02
        return tax_percentage * self.catalog_price

    def print(self):
        print(f"Brand: {self.brand}")
        print(f"Payable tax: {self.compute_tax():,.2f}")

@dataclass
class Vehicle:
    id: str
    license_plate: str
    info: VechileInfo

    def print(self):
        print(f"ID: {self.id}")
        print(f"License plate: {self.license_plate}")
        self.info.print()


class VehicleRegistry:

    vehicle_info_lookup = {}

    def add_vehicle_info(self, brand: str, electric: bool, catalog_price: int):
        self.vehicle_info_lookup[brand] = VechileInfo(
            brand, catalog_price, electric)

    def __init__(self):
        self.add_vehicle_info("Tesla Model 3", True, 60_000)
        self.add_vehicle_info("Ford F-150", False, 75_000)
        self.add_vehicle_info("BMW 5", False, 45_000)
        self.add_vehicle_info("Volkswagen ID3", True, 35_000)
        self.add_vehicle_info("Tesla Model Y", True, 75_000)

    def generate_vehicle_id(self, length) -> str:
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id) -> str:
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def create_vehicle(self, brand) -> Vehicle:
        vehicle_id = self.generate_vehicle_id(12)
        license_plate = self.generate_vehicle_license(vehicle_id)
        vehicle_info = self.vehicle_info_lookup[brand]
        return Vehicle(id=vehicle_id, license_plate=license_plate, info=vehicle_info)


class Application:

    def register_vehicle(self, brand: str):
        registry = VehicleRegistry()
        return registry.create_vehicle(brand)


app = Application()
vehicle = app.register_vehicle("Ford F-150")
vehicle.print()