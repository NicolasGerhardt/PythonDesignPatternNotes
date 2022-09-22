from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")

class Fan(Switchable):
    def turn_on(self):
        print("Fan: turned on...")

    def turn_off(self):
        print("Fan: turned off...")

class ElectricPowerSwitch:

    def __init__(self, switchable: Switchable):
        self.switchable = switchable
        self.on = False

    def press(self):
        if self.on:
            self.switchable.turn_off()
            self.on = False
            return
        self.switchable.turn_on()
        self.on = True


l = LightBulb()
f = Fan()
light_switch = ElectricPowerSwitch(l)
fan_switch = ElectricPowerSwitch(f)
light_switch.press()
fan_switch.press()
fan_switch.press()
light_switch.press()
